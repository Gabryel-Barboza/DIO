// Importação de dependências
const express = require('express');
const cors = require('cors');
const routes = require('./routes/routes');
// Importação de variáveis ambiente
require('dotenv').config;

// Instanciando aplicação
const app = express();

app.use(express.json());
app.use(cors());
app.use(routes);

module.exports = app;
