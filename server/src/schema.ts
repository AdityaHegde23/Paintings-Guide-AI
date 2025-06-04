import { gql } from 'apollo-server-express';

export const typeDefs = gql`
  type Painting {
    id: ID!
    title: String!
    artist: String!
    year: Int
    medium: String
    dimensions: String
    department: String
    culture: String
    period: String
    imageUrl: String!
    thumbnailUrl: String
    objectUrl: String
    description: String
    metId: Int
  }

  type PaintingsResponse {
    paintings: [Painting!]!
    total: Int!
    hasMore: Boolean!
  }

  type Query {
    paintings(limit: Int = 10, offset: Int = 0, search: String): PaintingsResponse!
    painting(id: ID!): Painting
  }
`;

export const resolvers = {
  Query: {
    paintings: async (_: any, args: { limit?: number; offset?: number; search?: string }) => {
      const { getPaintings } = await import('./data/paintingService');
      return getPaintings(args);
    },
    painting: async (_: any, { id }: { id: string }) => {
      const { getPaintingById } = await import('./data/paintingService');
      return getPaintingById(id);
    },
  },
};