# Paintings Meseum Guide AI

A fine-tuned LLM that generates engaging museum audio guides for paintings using metadata like title, artist, date, medium, and dimensions.

## Overview

This project demonstrates end-to-end LLM fine-tuning using LoRA (Low-Rank Adaptation) and 4-bit quantization. The model transforms basic painting metadata into museum-quality audio guide scripts in the style of professional art historians.

## Model Architecture

- **Base Model**: Mistral-7B-Instruct-v0.3
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **Quantization**: 4-bit quantization with NF4
- **Training Data**: 784 painting examples from Metropolitan Museum of Art
- **Context Length**: 512 tokens

## Fine-tuning Details

### Training Configuration
- **LoRA Rank**: 16
- **LoRA Alpha**: 32
- **Target Modules**: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- **Learning Rate**: 2e-4
- **Batch Size**: 8 (2 per device, 4 gradient accumulation steps)
- **Epochs**: 3
- **Mixed Precision**: FP16

### Memory Optimization
- **4-bit Quantization**: Uses NF4 with double quantization
- **Gradient Checkpointing**: Enabled for memory efficiency
- **VRAM Usage**: ~7-8GB on RTX 4080 (12GB)

### Training Data Format
Input format:
Title: Girl with a Pearl Earring
Artist: Johannes Vermeer
Date: c. 1665
Medium: Oil on canvas
Dimensions: 17.5 × 15.6 in (44.5 × 39.4 cm)
Output example:
Meet Vermeer's mysterious Girl with a Pearl Earring, painted around 1665. This isn't a traditional portrait but a 'tronie'—a study of expression and exotic costume. Notice how Vermeer uses light to sculpt her face from the dark background, and how that luminous pearl catches your eye.

## Technical Implementation

### Data Collection
- **Source**: Metropolitan Museum of Art Open Access API
- **Processing**: Unicode cleaning, metadata extraction, format standardization
- **Quality Control**: Filtered for complete metadata and dimensions

### Training Pipeline
1. **Data Preparation**: JSON to JSONL conversion with prompt/completion format
2. **Tokenization**: Prompt masking to train only on completion tokens
3. **Model Setup**: Quantized base model with LoRA adapters
4. **Training**: Supervised fine-tuning with validation monitoring
5. **Evaluation**: Sample generation and quality assessment

### Key Technical Decisions
- **Prompt Masking**: Only completion tokens contribute to loss function
- **Temperature Sampling**: 0.7 for balanced creativity and coherence
- **Max New Tokens**: 80-100 for concise audio guide length
- **End Token**: Custom `<END>` token for clean completion boundaries

## Results

### Training Metrics
- Initial Loss: 3.5
- Final Loss: 1.2
- Training Examples: 844
- Validation Examples: 94

### Generated Quality
- Professional museum guide tone
- Incorporates dimensions and technical details
- Engaging descriptive language
- Appropriate length for audio narration

### Project Structure
├── data_collection.py           Met Museum API scraping \
├── generate_audio_scripts.py    Training data generation \
├── paintings_fine_tuning.ipynb  Main training notebook  \
├── raw-data/                    Original scraped data \
├── processed-data/              Cleaned training data \
└── paintings-guide-final/       Fine-tuned model artifacts \


### Learning Outcomes
This project demonstrates:

- Modern Fine-tuning: LoRA vs full parameter training trade-offs
- Quantization Techniques: 4-bit NF4 implementation and benefits
- Memory Optimization: Training large models on consumer hardware
- Data Engineering: API integration, cleaning, and format standardization
- Training Pipeline: End-to-end MLOps for language model customization

## TODO

- Add text-to-speech integration for actual audio output
- Build web application interface for public access
- Expand to other art forms (sculptures, drawings, photographs)
- Multi-language support for international museums
- Real-time inference optimization
- A/B testing framework for guide quality evaluation

