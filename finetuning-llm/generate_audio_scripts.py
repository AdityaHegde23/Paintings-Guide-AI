import json
import random
from typing import List, Dict

def create_seed_scripts() -> List[Dict]:
    """Hand-crafted high-quality examples covering different categories"""
    
    seed_scripts = [
        # Famous Western - Van Gogh Self-Portrait
        {
            "title": "Self-Portrait with a Straw Hat (obverse: The Potato Peeler)",
            "artist": "Vincent van Gogh", 
            "date": "1887",
            "medium": "Oil on canvas",
            "dimensions": "16 x 12 1/2 in. (40.6 x 31.8 cm)",
            "script": "Meet Van Gogh in his Paris self-portrait from 1887, measuring just 16 by 12 inches. Here, he experiments with Impressionist techniques, using short, vibrant brushstrokes and a lighter palette than his later works. Notice the confident gaze and the casual straw hat—symbols of his artistic evolution. The reverse side reveals The Potato Peeler, showing Van Gogh's resourceful use of canvas during his financially constrained years."
        },
        
        # American Portrait - Robert Henri
        {
            "title": "Dutch Girl in White",
            "artist": "Robert Henri",
            "date": "1907", 
            "medium": "Oil on canvas",
            "dimensions": "24 x 20 in. (61 x 50.8 cm)",
            "script": "Step into Robert Henri's Dutch Girl in White, a 24 by 20 inch canvas from 1907. Henri, leader of the Ashcan School, captures his subject with bold, confident brushstrokes and dramatic lighting. The girl's white dress emerges luminously from the dark background, while her direct gaze reflects Henri's belief in painting 'the life of things.' This intimate portrait showcases the artist's departure from academic tradition toward a more spontaneous, expressive style."
        },
        
        # American Western - Frederic Remington
        {
            "title": "A Reconnaissance",
            "artist": "Frederic Remington",
            "date": "1902",
            "medium": "Oil on canvas", 
            "dimensions": "27 1/4 × 40 in. (69.2 × 101.6 cm)",
            "script": "Enter the American frontier through Remington's A Reconnaissance, a dramatic 27 by 40 inch canvas from 1902. This sweeping landscape captures the tension of military scouts surveying dangerous territory. Remington's masterful use of earth tones and atmospheric perspective creates depth across the vast Western landscape. Notice how the small figures emphasize the enormity and isolation of the frontier, reflecting America's complex relationship with westward expansion."
        },
        
        # American Symbolist - John White Alexander  
        {
            "title": "Repose",
            "artist": "John White Alexander",
            "date": "1895",
            "medium": "Oil on canvas",
            "dimensions": "52 1/4 x 63 5/8 in. (132.7 x 161.6 cm)", 
            "script": "Discover Alexander's Repose, an impressive 52 by 63 inch canvas from 1895. This elegant work exemplifies American Symbolism, with its flowing lines and muted palette creating an atmosphere of quiet contemplation. The figure's graceful pose and the painting's large scale invite intimate viewing despite its public museum setting. Alexander's sophisticated technique reflects his Paris training while maintaining a distinctly American sensibility of refined domesticity."
        },
        
        # Modern Futurist Sculpture - Boccioni
        {
            "title": "Antigraceful", 
            "artist": "Umberto Boccioni",
            "date": "1913, cast 1950",
            "medium": "Bronze",
            "dimensions": "23 × 21 × 16 1/2 in. (58.4 × 53.3 × 41.9 cm)",
            "script": "Experience Boccioni's revolutionary Antigraceful, a 23-inch bronze sculpture from 1913. This Futurist masterpiece breaks traditional sculptural beauty, embracing dynamic movement and mechanical energy. The fragmented, angular forms suggest a figure in motion, rejecting classical grace for modern industrial power. Cast in 1950 from the original, this 105-pound bronze embodies Boccioni's vision of sculpture that captures the speed and dynamism of the modern age."
        },
        
        # Contemporary Kinetic - Julio Le Parc
        {
            "title": "Continual Light Cylinder",
            "artist": "Julio Le Parc", 
            "date": "1962/2018",
            "medium": "Wood, acrylic sheet, projectors, and motors",
            "dimensions": "14 ft. 9 3/16 in. × 11 ft. 5 13/16 in. × 55 1/8 in. (450 × 350 × 140 cm)",
            "script": "Step into Le Parc's mesmerizing Continual Light Cylinder, a nearly 15-foot kinetic installation from 1962. This Argentine artist transforms space through moving light and shadow, using motors and projectors to create ever-changing patterns. The massive scale—over 11 feet wide—envelops viewers in an immersive experience that challenges the boundary between art and environment. Each moment brings new geometric formations, making you an active participant in the artwork's continuous transformation."
        },
        
        # French Academic Drawing - Labille-Guiard
        {
            "title": "Study of a Seated Woman Seen from Behind (Marie-Gabrielle Capet)",
            "artist": "Adélaïde Labille-Guiard",
            "date": "1789", 
            "medium": "Red, black, and white chalk on toned laid paper",
            "dimensions": "Sheet: 20 1/2 x 18 7/8 in. (52 x 48 cm)",
            "script": "Admire Labille-Guiard's exquisite 1789 drawing study, rendered in trois crayons technique on 20 by 18 inch toned paper. This intimate portrait of her student Marie-Gabrielle Capet demonstrates the master's skill with red, black, and white chalk. Notice how the subtle modeling creates volume and warmth, while the three-quarter rear view adds dignity and mystery. As one of few women admitted to the Royal Academy, Labille-Guiard's technical mastery challenged gender barriers in 18th-century French art."
        },
        
        # Ancient Greek - Amasis Painter
        {
            "title": "Terracotta lekythos (oil flask)",
            "artist": "Amasis Painter",
            "date": "ca. 550–530 BCE", 
            "medium": "Terracotta",
            "dimensions": "H. 6 7/8 in. (17.5 cm)",
            "script": "Journey to ancient Athens with this 6-inch terracotta oil flask by the Amasis Painter, created around 530 BCE. This black-figure lekythos showcases the refined artistry of Archaic Greek pottery, with its elegant proportions and narrative scenes. The Amasis Painter's distinctive style—precise line work and expressive figures—made him one of antiquity's most celebrated ceramicists. Used for storing precious oils, this vessel connected daily life with artistic excellence in classical Athens."
        },
        
        # Renaissance Portrait - hypothetical Raphael
        {
            "title": "Portrait of a Young Man",
            "artist": "Raphael", 
            "date": "1504-1505",
            "medium": "Oil on wood",
            "dimensions": "21 x 15 in. (53.3 x 38.1 cm)",
            "script": "Enter the High Renaissance through Raphael's Portrait of a Young Man, a 21 by 15 inch panel from 1504. The artist's signature grace and harmony shine through the subject's serene expression and elegant pose. Raphael's subtle sfumato technique softens the modeling, while the three-quarter view creates psychological depth. The rich burgundy cap and sumptuous fabric textures demonstrate the artist's mastery of both human character and material luxury that defined Renaissance portraiture."
        },
        
        # Impressionist Landscape - hypothetical Monet
        {
            "title": "Water Lilies, Morning",
            "artist": "Claude Monet",
            "date": "1916-1919", 
            "medium": "Oil on canvas",
            "dimensions": "51 1/4 x 78 3/4 in. (130.2 x 200 cm)",
            "script": "Float into Monet's Water Lilies, Morning, a magnificent 51 by 78 inch canvas from his later Giverny period. This expansive work eliminates traditional perspective, immersing you directly in the pond's surface. Monet's loose, gestural brushstrokes capture fleeting light effects on water, while the large scale creates an environment rather than merely a painting. The subtle color harmonies of blues, greens, and violets shift continuously, embodying Impressionism's core mission to paint light itself."
        },
        
        # Abstract Expressionist - hypothetical Pollock
        {
            "title": "Number 8, 1950",
            "artist": "Jackson Pollock",
            "date": "1950",
            "medium": "Oil and enamel on canvas", 
            "dimensions": "56 x 72 in. (142.2 x 182.9 cm)",
            "script": "Experience Pollock's revolutionary Number 8, 1950, a dynamic 56 by 72 inch canvas that redefined painting. Created through his famous 'drip' technique, this work eliminates traditional composition for all-over energy and movement. Stand close to see the intricate web of paint layers, then step back to feel the painting's rhythmic pulse. Pollock's physical engagement with the canvas—dancing around its edges—transforms painting from representation to pure expression of the artist's gestural energy."
        },
        
        # Baroque Religious - hypothetical Caravaggio
        {
            "title": "The Calling of Saint Matthew (detail)",
            "artist": "Caravaggio",
            "date": "1599-1600",
            "medium": "Oil on canvas",
            "dimensions": "127 x 130 in. (322.6 x 330.2 cm)", 
            "script": "Enter Caravaggio's dramatic world through The Calling of Saint Matthew, a monumental 127 by 130 inch canvas from 1600. The artist's revolutionary chiaroscuro technique creates theatrical lighting that transforms a simple tavern scene into divine revelation. Notice how the dramatic diagonal of light cuts through darkness, illuminating Christ's summoning gesture and Matthew's surprised response. This life-sized scale places you directly within the biblical narrative, making sacred history immediate and visceral."
        }
    ]
    
    return seed_scripts

def save_seed_scripts():
    """Save seed scripts for reference"""
    seeds = create_seed_scripts()
    with open('raw-data/seed_scripts.json', 'w') as f:
        json.dump(seeds, f, indent=2)
    print(f"Saved {len(seeds)} seed scripts")
    return seeds

def analyze_seed_patterns(seeds: List[Dict]) -> Dict:
    """Extract patterns from seed scripts for template generation"""
    
    patterns = {
        'opening_phrases': [
            'Meet', 'Step into', 'Enter', 'Discover', 'Experience', 'Admire', 'Journey to', 'Float into'
        ],
        'technical_elements': [
            'brushstrokes', 'palette', 'composition', 'lighting', 'perspective', 'technique', 'scale', 'proportions'
        ],
        'emotional_descriptors': [
            'dramatic', 'intimate', 'elegant', 'revolutionary', 'masterful', 'sophisticated', 'mesmerizing', 'exquisite'
        ],
        'structural_patterns': [
            'dimensions + context',
            'technique + visual impact', 
            'historical context + artistic significance',
            'scale + viewer experience'
        ]
    }
    
    return patterns

def create_script_templates() -> List[str]:
    """Template structures extracted from seed scripts"""
    
    templates = [
        # Scale + Context + Technique  
        "{opening} {title} by {artist}, a {dimensions} {medium} from {date}. {artist_context} {technique_description} Notice how {visual_element} {emotional_impact}",
        
        # Historical + Technical + Visual
        "Journey to {historical_context} through {artist}'s {title}, created in {date}. This {dimensions} {medium} {technique_focus} The {visual_technique} while {composition_note} {viewer_experience}",
        
        # Movement/Style + Scale + Impact
        "Experience {artist}'s {art_movement} masterpiece {title}, {dimensions} of {medium} from {date}. {style_description} {scale_impact} {technical_mastery} {emotional_connection}",
        
        # Technique-focused + Dimensions + Context
        "Discover {title}, where {artist}'s {technique_specialty} shines through this {dimensions} {medium}. Created in {date}, {technical_details} {visual_impact} {cultural_significance}",
        
        # Immersive + Scale + Experience  
        "Step into {title} by {artist}, {dimensions} that {scale_description}. This {date} {medium} {artistic_approach} {viewer_relationship} {lasting_impression}"
    ]
    
    return templates

def generate_script_variations(painting: Dict, templates: List[str]) -> List[str]:
    """Generate multiple script variations for a single painting"""
    
    # Extract painting info
    title = painting['title']
    artist = painting['artist'] 
    date = painting['date']
    medium = painting['medium']
    dimensions = painting.get('dimensions', 'canvas')
    
    # Content pools for variation
    openings = ['Meet', 'Step into', 'Enter', 'Discover', 'Experience', 'Admire']
    techniques = ['masterful brushwork', 'bold composition', 'subtle gradations', 'dynamic energy', 'refined technique']
    visual_elements = ['color harmony', 'dramatic lighting', 'expressive lines', 'textural richness', 'spatial depth']
    contexts = ['artistic innovation', 'cultural significance', 'historical importance', 'technical mastery', 'emotional resonance']
    
    variations = []
    
    # Generate 2-3 variations per painting using different templates
    for template in random.sample(templates, min(2, len(templates))):
        try:
            script = template.format(
                opening=random.choice(openings),
                title=title,
                artist=artist,
                date=date,
                medium=medium, 
                dimensions=dimensions,
                technique_description=random.choice(techniques),
                visual_element=random.choice(visual_elements),
                emotional_impact=random.choice(contexts),
                artist_context=f"{artist}'s distinctive style",
                historical_context=f"the world of {date}",
                technique_focus=f"showcases {random.choice(techniques)}",
                visual_technique=f"{random.choice(visual_elements)} creates depth",
                composition_note=f"the {random.choice(['balanced', 'dynamic', 'harmonious'])} composition",
                viewer_experience="invites close contemplation",
                art_movement="influential", 
                style_description=f"The {random.choice(['bold', 'subtle', 'masterful'])} approach",
                scale_impact=f"The {dimensions} scale enhances the impact",
                technical_mastery=f"{artist}'s {random.choice(techniques)} is evident throughout",
                emotional_connection="creating an immediate emotional connection",
                technique_specialty=random.choice(techniques),
                technical_details=f"the {random.choice(visual_elements)} demonstrates skill",
                visual_impact=f"Notice the {random.choice(['interplay of light and shadow', 'careful attention to detail', 'bold use of color'])}",
                cultural_significance="reflecting the artistic values of its time",
                scale_description=f"transforms your viewing experience",
                artistic_approach=f"{medium} allows {artist} to",
                viewer_relationship="places you in direct dialogue with the work",
                lasting_impression="leaving a memorable impression"
            )
            
            # Clean up and ensure reasonable length (60-100 words)
            script = script.replace('  ', ' ').strip()
            word_count = len(script.split())
            
            if 50 <= word_count <= 120:  # Allow some flexibility
                variations.append(script)
                
        except KeyError as e:
            continue  # Skip templates that don't work with this painting
    
    return variations

def create_bulk_training_data():
    """Generate training data from all paintings using templates"""
    
    # Load paintings and seeds
    with open('raw-data/met_paintings_formatted.json', 'r') as f:
        paintings = json.load(f)
    
    seeds = create_seed_scripts()
    templates = create_script_templates()
    
    training_examples = []
    
    # Add seed scripts first (high quality)
    for seed in seeds:
        prompt = f"Title: {seed['title']}\nArtist: {seed['artist']}\nDate: {seed['date']}\nMedium: {seed['medium']}\nDimensions: {seed['dimensions']}\n\nAudio guide:"
        completion = f" {seed['script']} <END>"
        
        training_examples.append({
            "prompt": prompt,
            "completion": completion
        })
    
    # # Generate variations for subset of paintings (start with 200-300)
    # selected_paintings = random.sample(paintings, min(300, len(paintings)))
    
    for painting in paintings:
        variations = generate_script_variations(painting, templates)
        
        for script in variations:
            prompt = f"Title: {painting['title']}\nArtist: {painting['artist']}\nDate: {painting['date']}\nMedium: {painting['medium']}\nDimensions: {painting.get('dimensions', 'Not specified')}\n\nAudio guide:"
            completion = f" {script} <END>"
            
            training_examples.append({
                "prompt": prompt, 
                "completion": completion
            })
    
    # Save training data
    output_file = 'raw-data/training_examples_bulk.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(training_examples, f, indent=2, ensure_ascii=False)
    
    print(f"Generated {len(training_examples)} training examples:")
    print(f"- {len(seeds)} high-quality seed scripts")
    print(f"- {len(training_examples) - len(seeds)} template-generated variations")
    print(f"Saved to {output_file}")
    
    return training_examples

if __name__ == "__main__":
    # Create seed scripts
    seeds = save_seed_scripts()
    
    # Generate bulk training data
    training_data = create_bulk_training_data()
    
    # Show sample
    print("\nSample training example:")
    sample = random.choice(training_data)
    print("PROMPT:", sample['prompt'][:100] + "...")
    print("COMPLETION:", sample['completion'][:100] + "...")