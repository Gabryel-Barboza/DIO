// Funções para tratar produtos
const productType = {
  version: 'digital',
  tax: 'x1',
};

async function getFullName(codeId, productName) {
  console.log('product: ' + codeId + '--' + productName);
  await doBreakLine(); // Função não exportada, continua funcionando. Hidden Members
}

async function doBreakLine() {
  console.log('\n')
}

async function getProductName(productName) {
  console.log('product: ' + productName);
}

// Exportando as funções
module.exports = {
  getFullName,
  getProductName,
  productType,
};
