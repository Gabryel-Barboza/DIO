async function databaseConnect(user, password) {
  // Maneira errada, dados sensíveis expostos.
  // if (user === 'gabryel' && password === '1234') {

  if (user == process.env.USERDATABASE && password == process.env.PASSWORDDATABASE) {
    console.log('Conexão estabelecida...');
  } else {
    console.log('Falha de login, não foi possível se conectar ao banco de dados.');
  }
}

export default databaseConnect;
