// Instalar @types/node para módulo http compatível com TS
import * as http from 'http';
import 'dotenv/config';

import { app } from './app';

// Arquivos de responsabilidade única
const server = http.createServer(app);

// Porta no arquivo de config .env
const port = process.env.PORT;
// Servidor recebendo requisições na porta indicada
server.listen(port, () => console.log(`Server listening on port ${port}`));
