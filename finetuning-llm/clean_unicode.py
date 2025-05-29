import json
import re

def smart_clean_text(text):
    """Smart cleaning that handles both encoded and non-encoded text"""
    if not isinstance(text, str) or not text:
        return text
    
    # Check if text contains Unicode escape sequences
    if '\\u' in text:
        try:
            # Only decode if it contains escape sequences
            text = text.encode('utf-8').decode('unicode_escape')
        except:
            pass  # Keep original if decoding fails
    
    # Fix em-dashes and quotes (these might be actual Unicode chars)
    text = text.replace('–', '-')  # em-dash to hyphen
    text = text.replace('—', '-')  # en-dash to hyphen  
    text = text.replace('"', '"')  # left quote
    text = text.replace('"', '"')  # right quote
    text = text.replace('\'', "'")  # apostrophe
    
    # Clean up extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def restore_from_backup_and_clean():
    """Restore from raw data and apply smart cleaning"""
    print("Restoring from complete raw data...")
    
    # Load the complete raw data (this should be uncorrupted)
    with open('raw-data/met_paintings_complete_raw.json', 'r', encoding='utf-8') as f:
        raw_paintings = json.load(f)
    
    print(f"Loaded {len(raw_paintings)} raw paintings")
    
    # Re-format with smart cleaning
    formatted_paintings = []
    for raw in raw_paintings:
        formatted = {
            'title': smart_clean_text(raw.get('title', '')),
            'artist': smart_clean_text(raw.get('artistDisplayName', '')),
            'date': smart_clean_text(raw.get('objectDate', '')),
            'medium': smart_clean_text(raw.get('medium', '')),
            'location': 'The Metropolitan Museum of Art, New York',
            'met_id': raw.get('objectID'),
            'culture': smart_clean_text(raw.get('culture', '')),
            'period': smart_clean_text(raw.get('period', '')),
            'dimensions': smart_clean_text(raw.get('dimensions', '')),
            'credit_line': smart_clean_text(raw.get('creditLine', ''))
        }
        formatted_paintings.append(formatted)
    
    # Save the properly cleaned formatted data
    with open('raw-data/met_paintings_formatted.json', 'w', encoding='utf-8') as f:
        json.dump(formatted_paintings, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Restored and cleaned {len(formatted_paintings)} paintings")
    
    # Show a sample to verify
    sample = formatted_paintings[0]
    print(f"\nSample: {sample['title']} by {sample['artist']} ({sample['date']})")

if __name__ == "__main__":
    restore_from_backup_and_clean()
    print("Data restored and properly cleaned!")