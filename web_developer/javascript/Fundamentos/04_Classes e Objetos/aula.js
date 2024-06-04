// Objetos, conjuntos de chave-valor
const gabryel = {
    nome: 'Gabryel',
    idade: 19,

    // Métodos
    descrever: function() {
        console.log(`Meu nome é ${this.nome} e minha idade é ${this.idade} anos`);
    }
}

// Acessando os objetos
console.log(gabryel.nome);
console.log(gabryel.idade);
console.log(gabryel);

// Adicionando novos atributos
gabryel.altura = 1.80;
console.log(gabryel);
delete gabryel.altura;
console.log(gabryel);

// Utilizando métodos
gabryel.descrever();
gabryel.descrever = function () {console.log(`Meu nome é ${this.nome}`)};
gabryel.descrever();

// Acessando objetos dinamicamente
const atributo = 'idade';
console.log(gabryel[atributo]);
console.log(gabryel['nome']);

