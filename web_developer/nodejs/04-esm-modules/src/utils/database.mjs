const databaseType = {
  userType: 'admin',
  type: 'dataLocal',
};

async function databaseConnect() {
  console.log('Conectando ao database...');
}

async function databaseDisconnect() {
  console.log('Desconectando-se do database...');
}

//module.exports = databaseConnect;
export default databaseConnect;

//module.exports = { databaseConnect, databaseDisconnect, databaseType }
export { databaseConnect, databaseDisconnect, databaseType };
