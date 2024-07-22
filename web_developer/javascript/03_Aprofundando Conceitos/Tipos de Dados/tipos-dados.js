/*
Tipos de dados primitivos:
    boolean
    null
    undefined
    number
    string
    symbol
*/ 

// Object
const pessoa = { nome: "Gabryel", idade: 19 };

console.log('===Booleans');
// Booleans
true, false;
// Classe Wrapper
new Boolean(true);

console.log(!'');
const nome = ' ';
if (nome) {
    console.log('Preenchido!');
} else {
    console.log('Vazio!');
}

console.log('===Null/Undefined');
// null - ausência de valor;
const x = null;
console.log(x);

// undefined - valor inexistente
const y = { nome: "Gabryel" };
console.log(y.idade);

// Criando JSONs com o objeto
y.nome = undefined;
console.log(JSON.stringify(y));
y.nome = null;
console.log(JSON.stringify(y));

console.log('===Numbers');
// Numbers
// +infinity, -infinity, NaN
console.log(typeof(NaN));
// Double Precision 64-bit binary format IEEE 754 - veja: https://0.30000000000000004.com
console.log(0.1 - 0.3);
console.log((0.1 + 0.2) !== 0.3);

// Resolvendo a imprecisão
// Utilize variáveis do tipo decimal com variável = new Decimal para cálculos precisos. Pesquise mais sobre

console.log('===Strings')
// Strings
// Cadeia de carácteres imutáveis

// Convenção de declarações de String
"Texto" // Utilizado para representar HTML
'Texto' // Utilizado para comandos em geral
console.log('<div id="teste"></div>');

`Texto` // template-literals para formatação de strings
let nomeCompleto = 'Gabryel Barboza';
console.log(`Olá, meu nome é ${nomeCompleto}`);
console.log(`Quebra
    de linha
    automática`);

console.log('===Symbol');
// Symbol
// Objetos imutáveis únicos
const a = Symbol('10');
const b = Symbol('10');
console.log(a);
console.log(a === b);

console.log('===Object');
// Objetos
// Coleção dinâmica de chave-valor

// Declaração de objetos
const objeto = {
    nome: 'Gabryel',
    idade: 30,
    'Endereço completo': 'R -- Q -- C --'
};
// Declaração de atributos
objeto.sobrenome = 'Barboza';

console.log(typeof(objeto));
// Acessando Atributos
console.log(objeto.nome);
console.log(objeto['sobrenome']);

// Declaração de Métodos
// métodos são capacidades de objetos, diferentes na semântica de funções 
objeto.falar = function() {
    console.log(`Olá! Meu nome é ${this.nome}`);
};
// Chamada de métodos
objeto.falar();

const teste = objeto.falar;
teste();
