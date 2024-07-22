// First Class Functions
// Higher Order Functions
// Podem ser atribuídas para variáveis, ser passadas como parâmetro e retornadas de outras funções

// Recebendo funções em variáveis
function meuNome() {
    console.log('Meu nome é Gabryel');
}

const referenciaNova = meuNome;
referenciaNova();

// Recebendo e retornando funções em outras funções
function nomeCompleto(nome) {
    console.log('Barboza');
    return nome;
}

nomeCompleto(meuNome)();

// Function expression e function declaration

// Function expression, sofre o hoisting e não referencia a função até a atribuição
const funcao2 = function () {}
// Function declaration, sofre o hoisting porém a própria função é a declaração
function funcao() {console.log(this);}

// Arrow functions
// Podem receber parâmetros e retornam comandos ou blocos de código. Não recebem o objeto igual functions
const funcao3 = () => console.log(this);
const pessoa = {
    nome: 'Gabryel',
    funcao,
    funcao3
}

pessoa.funcao();
pessoa.funcao3();

// Closures
// Funções guardam o contexto onde foram declaradas, o mesmo ocorre com arrow functions
function soma(x) {
    return function (y) {
        return x + y;
    }
}

console.log(soma(10)(20));
// A função ainda possui o valor de x mesmo que retornada fora
const somaParcial = soma(10);
console.log(somaParcial(20));
console.log(somaParcial(30));

// Invocar funções
function teste(msg) {
    console.log(`${msg} ${this.nome}`);
}

// Direta
teste();

// Métodos
// Executa a função dentro de um objeto, recebe uma lista de argumentos
teste.apply(pessoa, ['Olá, ']);

teste.call(pessoa, 'Olá, ');


function adicao(x, y) {
    return x + y;
}
function subtracao(x, y) {
    return x - y;
}
function multiplicacao(x, y) {
    return x * y;
}
function divisao(x, y) {
    return x / y
}

function calculadora(x, operacao, y) {
    console.log(operacao(x, y));
}

calculadora(10, adicao, 20);
calculadora(10, multiplicacao, 20);
