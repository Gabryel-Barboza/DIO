// Criando uma minimal API com fastify
import fastify from 'fastify';
import cors from '@fastify/cors';

// Instância do servidor
const server = fastify({ logger: true });

// Cross-Origin Resource Sharing, mecanismo de segurança de acesso as rotas
// Access-Control-Allow-Origin
server.register(cors, {
  origin: '*', // Permite requisições de qualquer origem para a API
  methods: ['GET', 'POST'],
});

// Repositórios
const teams = [
  { id: 1, name: 'Mclaren', base: 'Woking, United Kingdom' },
  { id: 2, name: 'Mercedes', base: 'Brackley, United Kingdom' },
  { id: 3, name: 'Red Bull Racing', base: 'Milton Keynes, United Kingdom' },
];

const drivers = [
  { id: 1, name: 'Max Verstappen', team: 'Red Bull Racing' },
  { id: 2, name: 'Lewis Hamilton', team: 'Ferrari' },
  { id: 3, name: 'Lando Norris', team: 'Mclaren' },
];

// Rotas
server.get('/teams', async (request, response) => {
  response.type('application/json').code(200);

  return teams;
});

server.get('/drivers', async (request, response) => {
  response.type('application/json').code(200);

  return drivers;
});

interface DriverParams {
  id: string;
}

// Rotas com parâmetros
server.get<{ Params: DriverParams }>('/drivers/:id', async (request, response) => {
  const id = parseInt(request.params.id);
  const driver = drivers.find((d) => d.id === id);

  if (!driver) {
    response.type('application/json').code(404);
    return { message: 'Driver not Found!' };
  } else {
    response.type('application/json').code(200);
    return { driver };
  }
});

server.listen({ port: 3333 }, (err, address) => {
  if (err) console.log('Error initializing server: ', err);
  else console.log(`Server listening at: ${address}`);
});
