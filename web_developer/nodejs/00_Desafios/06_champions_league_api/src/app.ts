import express, { json } from 'express';
import router from './routes/routes';
import cors from 'cors'; // Instalar tipagem do cors: npm install @types/cors -D

function createApp() {
  // Instanciando Servidor
  const app = express();
  // Middlewares - softwares intermediários para realizar operações entre requisições
  // Realiza as responses com o formato JSON como principal
  app.use(json());

  // Middleware para logar as requisições
  // Prefixo das rotas
  app.use('/api', router);

  const corsOptions = {
    origin: '*',
    methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
  };
  // Middleware para habilitar o CORS (Cross-Origin Resource Sharing)
  // Permite que a API seja acessada por qualquer domínio
  app.use(cors());

  return app;
}

export default createApp;
