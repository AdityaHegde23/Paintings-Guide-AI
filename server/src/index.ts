import express from 'express';
import { ApolloServer } from 'apollo-server-express';
import cors from 'cors';
import { typeDefs, resolvers } from './schema';

async function startServer() {
  const app = express();
  
  // Enable CORS for frontend
  app.use(cors({
    origin: 'http://localhost:3000', // Next.js default port
    credentials: true,
  }));

  // Create Apollo Server
  const server = new ApolloServer({
    typeDefs,
    resolvers,
    context: ({ req }) => ({ req }),
  });

  await server.start();
  server.applyMiddleware({ app, path: '/graphql' });

  const PORT = process.env.PORT || 4000;

  app.listen(PORT, () => {
    console.log(`🚀 Server ready at http://localhost:${PORT}${server.graphqlPath}`);
    console.log(`📊 GraphQL Playground available at http://localhost:${PORT}${server.graphqlPath}`);
  });
}

startServer().catch(error => {
  console.error('Error starting server:', error);
});