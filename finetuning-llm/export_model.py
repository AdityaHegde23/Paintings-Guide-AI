#!/usr/bin/env python3
import os
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModelForCausalLM
from onnxruntime.quantization import quantize_dynamic, QuantType


def merge_lora(
    base_name: str,
    adapter_dir: str,
    merged_dir: str = "./fp16-merged-model",
    offload_folder: str = "./offload",
):
    """
    1) Load base in FP16 with device_map + offload_folder (no 4-bit!)
    2) Load and merge LoRA adapters
    3) Save merged FP16 model + tokenizer
    """
    os.makedirs(offload_folder, exist_ok=True)
    print(f"Merging LoRA from {adapter_dir} into base {base_name}")

    base = AutoModelForCausalLM.from_pretrained(
        base_name,
        torch_dtype=torch.float16,
        device_map="auto",
        offload_folder=offload_folder,
        trust_remote_code=True,
    )

    peft_model = PeftModelForCausalLM.from_pretrained(
        base,
        adapter_dir,
        strict=False,
        device_map="auto",
        offload_folder=offload_folder,
    )

    merged = peft_model.merge_and_unload()
    import gc
    del base, peft_model
    gc.collect()

    tokenizer = AutoTokenizer.from_pretrained(base_name)
    Path(merged_dir).mkdir(parents=True, exist_ok=True)
    # shard each file at 1 GB max (tune up/down to your RAM)
    merged.save_pretrained(
        merged_dir,
        max_shard_size="1GB",
        safe_serialization=True,    # incremental write, lower mem overhead
    )

    tokenizer.save_pretrained(merged_dir)

    print(f"Merged FP16 model saved to {merged_dir}")
    return merged_dir


def export_to_onnx(
    merged_dir: str,
    onnx_dir: str = "./onnx-model",
    opset: int = 14,
):
    print(f"Loading merged model from {merged_dir} onto CPU for export")
    model = AutoModelForCausalLM.from_pretrained(
        merged_dir,
        torch_dtype=torch.float16,
        device_map="cpu",
        trust_remote_code=True,   
    )
    model.eval()

    tokenizer = AutoTokenizer.from_pretrained(merged_dir)
    if tokenizer.pad_token is None:
        tokenizer.add_special_tokens({"pad_token": tokenizer.eos_token})
        model.resize_token_embeddings(len(tokenizer))

    dummy = tokenizer(
        "Title: Example\nArtist: Test\nAudio Guide:",
        return_tensors="pt",
        padding="longest",
    )
    ids  = dummy["input_ids"].to("cpu")
    mask = dummy["attention_mask"].to("cpu")

    Path(onnx_dir).mkdir(parents=True, exist_ok=True)
    onnx_path = os.path.join(onnx_dir, "model.onnx")
    print(f"Exporting to ONNX (float16) at {onnx_path}")
    torch.onnx.export(
        model,
        (ids, mask),
        onnx_path,
        input_names=["input_ids", "attention_mask"],
        output_names=["logits"],
        dynamic_axes={
            "input_ids": {0: "batch", 1: "sequence"},
            "attention_mask": {0: "batch", 1: "sequence"},
            "logits": {0: "batch", 1: "sequence"},
        },
        opset_version=opset,
        do_constant_folding=True,
    )
    print(f"ONNX (float16) model written to {onnx_dir}")
    return onnx_dir


def quantize_onnx(
    onnx_dir: str,
    quant_dir: str = "./onnx-int8",
    weight_type: QuantType = QuantType.QInt8,
):
    """
    Apply dynamic INT8 quantization on the ONNX graph for CPU inference.
    """
    input_path = os.path.join(onnx_dir, "model.onnx")
    output_path = os.path.join(quant_dir, "model.onnx")
    Path(quant_dir).mkdir(parents=True, exist_ok=True)

    print(f"Applying dynamic INT8 quantization to {input_path}")
    quantize_dynamic(
        model_input=input_path,
        model_output=output_path,
        weight_type=weight_type,
    )
    print(f"Quantized ONNX (INT8) model written to {quant_dir}")
    return quant_dir


if __name__ == "__main__":
    BASE     = "mistralai/Mistral-7B-Instruct-v0.3"
    ADAPTERS = "./trained-models/paintings-audio-guide-final"

    merged_fp16 = merge_lora(BASE, ADAPTERS)
    onnx_fp16   = export_to_onnx(merged_fp16)
    onnx_int8   = quantize_onnx(onnx_fp16)

    print("All done! Your outputs:")
    print(f" • Merged FP16 model: {merged_fp16}")
    print(f" • ONNX (float16): {onnx_fp16}")
    print(f" • ONNX (INT8): {onnx_int8}")
