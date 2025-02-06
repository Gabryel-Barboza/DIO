// Criando APIs com Express
// Instalação @types/express para compatibilidade TS
import 'dotenv/config';
import express, { json, Request, Response } from 'express';

// Instanciando servidor
const app = express();

// Middlewares - softwares intermediários para realizar operações entre requisições
// Realiza as responses com o formato JSON como principal
app.use(json());

// Criando rotas
app.get('/', async (req: Request, res: Response) => {
  res.status(200).json({ player: 'Beckham' });
});

const port = process.env.PORT;
// Recebendo requisições
app.listen(port, () => {
  console.log(`Server running at port: ${port}`);
});
