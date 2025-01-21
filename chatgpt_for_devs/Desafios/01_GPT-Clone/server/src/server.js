// Importando app e configuração de porta
const app = require('./app');
const port = process.env.PORT || 3000;

// Aceitando requisições na porta especificada
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
