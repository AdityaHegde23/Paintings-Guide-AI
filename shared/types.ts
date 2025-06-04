export interface Painting {
  id: string;
  title: string;
  artist: string;
  year?: number;
  medium?: string;
  dimensions?: string;
  department?: string;
  culture?: string;
  period?: string;
  imageUrl: string;
  thumbnailUrl?: string;
  objectUrl?: string;
  description?: string;
  metId?: number;
}

export interface PaintingsResponse {
  paintings: Painting[];
  total: number;
  hasMore: boolean;
}

export interface GetPaintingsArgs {
  limit?: number;
  offset?: number;
  search?: string;
}