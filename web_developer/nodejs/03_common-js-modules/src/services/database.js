// Export default de funções
// São tratados como propriedades de um objeto desse modo.

// Export default async
exports.databaseConnect = async () => {
  console.log('Conectando ao banco de dados');
}

exports.databaseDisconnect = () => {
  console.log('Desconectando-se do banco de dados');
}
