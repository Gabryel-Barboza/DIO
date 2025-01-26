// Boas práticas com variáveis ambiente
// Instalar pacote dotenv para versões antigas do NodeJs
import 'dotenv/config';

// Adicione --env-file=caminho_.env no comando de execução para integrar o arquivo de variáveis, disponível na versão 20 do Node.Js
import databaseConnect from "./database/database.js";


(async function main() {

  databaseConnect('gabriel', 'naosei');

  databaseConnect(process.env.USERDATABASE, process.env.PASSWORDDATABASE);

  console.log(process.env.USERDATABASE);
})();

// Variáveis declaradas no arquivo .env:
// USERDATABASE="admin"
// PASSWORDDATABASE="admin"
