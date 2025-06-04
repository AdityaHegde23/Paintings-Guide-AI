import fs from 'fs-extra';
import path from 'path';
import { Painting, PaintingsResponse, GetPaintingsArgs } from '../../../shared/types';

// Need to be replced accordingly
let paintingsCache: Painting[] | null = null;

async function loadPaintingsData(): Promise<Painting[]> {
  if (paintingsCache) {
    return paintingsCache;
  }

  try {
    // Need to load from a JSON file first from API data
    const dataPath = path.join(__dirname, '../../../data/paintings.json');
    if (await fs.pathExists(dataPath)) {
      const data = await fs.readJson(dataPath);
      paintingsCache = data;
      return paintingsCache;
    }
  } catch (error) {
    console.log('No paintings.json found, using mock data');
  }

  // Need to be replced accordingly
  paintingsCache = generateMockPaintings();
  return paintingsCache;
}

function generateMockPaintings(): Painting[] {
  const mockPaintings: Painting[] = [];
  
  for (let i = 1; i <= 20; i++) {
    mockPaintings.push({
      id: `painting-${i}`,
      title: `Artwork ${i}`,
      artist: `Artist ${i}`,
      year: 1800 + Math.floor(Math.random() * 200),
      medium: 'Oil on canvas',
      department: 'European Paintings',
      imageUrl: `https://picsum.photos/400/600?random=${i}`,
      thumbnailUrl: `https://picsum.photos/200/300?random=${i}`,
      description: `This is a beautiful artwork number ${i} from our collection.`,
      metId: 1000 + i,
    });
  }
  
  return mockPaintings;
}

export async function getPaintings(args: GetPaintingsArgs): Promise<PaintingsResponse> {
  const { limit = 10, offset = 0, search } = args;
  const allPaintings = await loadPaintingsData();
  
  let filteredPaintings = allPaintings;
  
  // Simple search functionality
  if (search) {
    filteredPaintings = allPaintings.filter(painting =>
      painting.title.toLowerCase().includes(search.toLowerCase()) ||
      painting.artist.toLowerCase().includes(search.toLowerCase())
    );
  }
  
  const paintings = filteredPaintings.slice(offset, offset + limit);
  const hasMore = offset + limit < filteredPaintings.length;
  
  return {
    paintings,
    total: filteredPaintings.length,
    hasMore,
  };
}

export async function getPaintingById(id: string): Promise<Painting | null> {
  const allPaintings = await loadPaintingsData();
  return allPaintings.find(painting => painting.id === id) || null;
}