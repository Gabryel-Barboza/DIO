// Importando módulos
const product = require('./services/products');
const config = require('./services/config');
const database = require('./services/database');
// Destructuring - importar um por vez
const { getFullName, productType } = require('./services/products');

(async function main() {
  console.log('Carrinho de compras:');
  product.getFullName('123', 'keyboard');
  product.getFullName('567', 'mouse');

  product.getProductName('Keyboard');
  console.log(product.productType);

  console.log(config.devArea.production);
  console.log(config.client.device);

  database.databaseConnect();

  console.log(getFullName('932', 'PC'));
})();
