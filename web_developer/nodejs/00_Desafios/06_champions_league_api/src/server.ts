// Criando APIs com Express
// Instalação @types/express para compatibilidade TS
import 'dotenv/config';
import createApp from './app';

const app = createApp();

const port = process.env.PORT;
// Recebendo requisições
app.listen(port, () => {
  console.log(`Server running at port: ${port}`);
});
