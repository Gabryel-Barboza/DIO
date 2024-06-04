// Importando as funções do módulo
// É executado o módulo primeiro, para próximos imports não será executado
const funcoes = require('./funcoes-auxiliares');

console.log(funcoes);
console.log(funcoes.gets());

// Object destructuring
const pessoa = {
    nome: 'Gabryel',
    idade: 19
};
// nome e idade recebem atributos de pessoa
const { nome, idade } = pessoa;
console.log(nome, idade);

