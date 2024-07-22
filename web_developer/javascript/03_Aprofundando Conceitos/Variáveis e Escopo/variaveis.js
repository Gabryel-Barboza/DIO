
// JavaScript é fracamente tipado e CaseSensitive
var var1 = 10;
var1 = "Teste";
console.log(var1);
var1 = 10;
var var2 = "Teste";
// Casting automático de tipos diferentes, converte Number para String
console.log(var1 + var2);
console.log(var1 - var2);
var2 = "10";
console.log(var1 - var2);


// Hoisting ou içamento - Recebe todas as declarações ao começo do programa, permitindo a chamada antes da declaração no código
teste();

function teste() {
    console.log('Teste');
}

// O hoisting é apenas para declarações, a atribuição permanece no local. A variável é declarada, mas sem atribuição
console.log(nome);
var nome = "Gabryel";
console.log(nome);

// Declarando variáveis e atribuindo funções
//teste2(); - error teste2 is not a function
var teste2 = function() {
    console.log(teste2);
}
teste2();


// Diferenças de declarações de variáveis

// <EC6 = utilizava-se var. Var ignora escopos de bloco, mas respeita o escopo de função
if (true) {
    var var3 = 10;
}

console.log(var3);

function teste3() {
    var var4 = 10;
}
//console.log(var4); - error var4 is not defined

// Variável let respeita o escopo de qualquer bloco de código
if (true) {
    let var5 = 10;
}
// console.log(var5);

// Variável const é igual ao let em escopo, mas com a característica de imutabilidade não podendo ser reatribuído.
const var6 = 10;


// Convenções de Nomenclatura
// variáveis devem começar com letras, _ ou $, "_" para variáveis de escopo local que não devem ser alteradas e "$" em jquerys
// começam em lowercase e utilizam o padrão camelCase
// constantes são declaradas em uppercase
var texto;
var textoMaior;
var _atributo;
const PI = 3.141592;
