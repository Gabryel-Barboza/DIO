const devArea = {
  version: '1.2.7',
  production: true,
};

const client = {
  device: 'web',
};

// Exportação padrão -- apenas 1 exportação
//module.exports = devArea;

// Exportando variáveis, objetos ou funções. A exportação deve estar ao final do arquivo
module.exports = {
  client,
  devArea,
};
