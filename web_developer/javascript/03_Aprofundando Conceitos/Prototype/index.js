// Orientação a Protótipo
// Protótipo é a base de um objeto e é utilizado para herdar suas propriedades

const pessoa = {
    genero: 'Masculino'
}

// Criando uma herança
const gabryel = {
    nome: 'Gabryel',
    idade: 19,
    __proto__: pessoa
};

// Para encontrar o atributo, o interpretador irá percorrer o objeto e todos os protótipos até encontrar o requisitado
console.log(gabryel.genero);

// Funções construtoras ou classes
function Pessoa(nome, idade) {
    this.nome = nome;
    this.idade = idade;
}

// Acesando o protótipo e declarando um método
// Adicionando o método ao protótipo para ser herdado.
Pessoa.prototype.falar = function () {
    console.log(`Meu nome é ${this.nome}`);
}

// new recebe a função construtora e devolve um objeto a partir do protótipo da função.
const p1 = new Pessoa('Gabryel', 19);
console.log(p1);
p1.falar();

// Mesmo procedimento, porém modernizado
/*class Pessoa {

    constructor(nome, idade) {
        this.nome = nome;
        this.idade = idade;
    }

    falar() {
        console.log(`Meu nome é ${this.nome}`);
    }
} 
*/

// Sobrescrita de atributos
const prototipo = {
    idade: 18
}

const pessoa1 = {
    nome: 'Gabryel',
    idade: 30,
    __proto__: prototipo
}

console.log(pessoa1.idade);
// No JavaScript não existe a sobrecarga, logo não é possível métodos de mesmo nome e assinaturas diferentes.

// Formas de criação de objetos por protótipos
// literal (exemplo acima)
// classe Object - retorna um objeto com o protótipo de pessoa
const p2 = Object.create(pessoa);
p2.nome = 'Brayan';
p2.idade = 28;
console.log(p2);

// Operador new
function Cachorro(raca, corPelo) {
    this.raca = raca;
    this.pelo = corPelo;
}

// Com o operador new é passado um objeto vazio para a função construtora e retornado com o escopo atribuído
console.log(new Cachorro('Shitzu', 'Caramelo'));
Cachorro.prototype.latir = function () {console.log('Au au au!')};

// Com o método call de um protótipo, é possível passar um objeto predefinido para ser enriquecido pela função
const cachorro1 = {
    idade: 4
}

Cachorro.call(cachorro1, 'Shitzu', 'Caramelo');
console.log(cachorro1);

// Modificando objetos do JavaScript, não recomendado por boas práticas
String.prototype.firstLetter = function () {
    return this[0];
}

console.log('texto'.firstLetter().toUpperCase());
