// Instalar @types/node para módulo compatível com TS
import * as http from 'http';
import 'dotenv/config';

import { app } from './app';

// Arquivos de responsabilidade única
const server = http.createServer(app);

// Porta no arquivo de config .env
const port = process.env.PORT;
server.listen(port, () => console.log(`Server listening on port ${port}`));
