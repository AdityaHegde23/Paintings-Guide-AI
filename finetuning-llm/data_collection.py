import requests
import json
import time
import os
from typing import List, Dict

# Create data directories
os.makedirs('raw-data', exist_ok=True)

def get_met_paintings_raw(limit: int = 100) -> List[Dict]:
    """Get complete raw painting data from Met Museum API"""
    
    # Check if we already have complete raw data
    raw_file = 'raw-data/met_paintings_complete_raw.json'
    if os.path.exists(raw_file):
        print(f"Loading existing raw data from {raw_file}")
        with open(raw_file, 'r') as f:
            return json.load(f)
    
    print("Fetching fresh data from Met Museum API...")
    
    # Step 1: Get list of painting object IDs
    search_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
    params = {
        'hasImages': 'true',
        'isHighlight': 'true',
        'q': 'painting'
    }
    
    response = requests.get(search_url, params=params)
    object_ids = response.json().get('objectIDs', [])
    print(f"Found {len(object_ids)} object IDs")
    object_ids = object_ids[:limit]  # Limit to the specified number
    raw_paintings = []
    
    # Step 2: Get complete details for each painting
    for i, obj_id in enumerate(object_ids):
        try:
            detail_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}"
            detail_response = requests.get(detail_url)
            raw_data = detail_response.json()  # Store EVERYTHING
            
            # Only store if it has basic required fields
            if all(raw_data.get(field) for field in ['title', 'artistDisplayName', 'objectDate', 'medium']):
                raw_paintings.append(raw_data)
            else:
                print(f"Skipping object {obj_id} due to missing required fields ({', '.join(field for field in ['title', 'artistDisplayName', 'objectDate', 'medium'] if not raw_data.get(field))})")
            
            # Rate limiting: ~50 requests per second
            time.sleep(0.02)
            
            if (i + 1) % 20 == 0:
                print(f"Processed {i + 1}/{len(object_ids)} paintings...")
                
        except Exception as e:
            print(f"Error fetching object {obj_id}: {e}")
            continue
    
    # Save complete raw data
    with open(raw_file, 'w') as f:
        json.dump(raw_paintings, f, indent=2)
    
    print(f"Saved {len(raw_paintings)} complete raw paintings to {raw_file}")
    return raw_paintings



def format_paintings(raw_paintings: List[Dict]) -> List[Dict]:
    """Format raw paintings into our training structure"""
    
    formatted_file = 'raw-data/met_paintings_formatted.json'
    
    formatted_paintings = []
    for raw in raw_paintings:
        formatted = {
            'title': raw['title'],
            'artist': raw['artistDisplayName'],
            'date': raw['objectDate'],
            'medium': raw['medium'],
            'location': 'The Metropolitan Museum of Art, New York',
            'met_id': raw['objectID'],
            # Keep some extra useful fields if available
            'primary_image': raw.get('primaryImage', ''),
            'primary_image_small': raw.get('primaryImageSmall', ''),
            'object_url': raw.get('objectURL', ''),
            'department': raw.get('department', ''),
            'culture': raw.get('culture', ''),
            'period': raw.get('period', ''),
            'dimensions': raw.get('dimensions', ''),
            'credit_line': raw.get('creditLine', '')
        }
        formatted_paintings.append(formatted)
    
    # Save formatted data
    with open(formatted_file, 'w') as f:
        json.dump(formatted_paintings, f, indent=2)
    
    print(f"Saved {len(formatted_paintings)} formatted paintings to {formatted_file}")
    return formatted_paintings

# Test it
if __name__ == "__main__":
    # # Get raw data
    # raw_paintings = get_met_paintings_raw(1500)
    # print(f"Got {len(raw_paintings)} raw paintings")
    
    # Get raw data
    if not os.path.exists('raw-data/met_paintings_complete_raw.json'):
        raw_paintings=[]
        print("Raw data not found")
    else:
        raw_paintings = json.load(open('raw-data/met_paintings_complete_raw.json', 'r'))

    # Format the data
    formatted_paintings = format_paintings(raw_paintings)
    print(f"Formatted {len(formatted_paintings)} paintings")
    
    # Show example
    print("\nExample formatted painting:")
    print(json.dumps(formatted_paintings[0], indent=2))