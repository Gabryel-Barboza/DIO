// Declaração de uma função
function teste() {
    console.log('Teste');
}

// Passagem de parâmetros para uma função
function sayMyName(name) {
    console.log('Your name is: ' + name);
}

// Funções com retorno
function somar(num1, num2) {
    return num1 + num2;
}

function quadrado(num) {
    return num ** 2;
}

function incrementarJuros(valor, percentual) {
    const valorAcrescimo = valor * (percentual / 100);
    return valor + valorAcrescimo;
}

// Invocando a função
teste();
// Passando parâmetros
sayMyName('Gabryel');
// Funções sem retorno são chamados de procedimentos, com retorno são funções de fato.
console.log(somar(5, 5));
console.log(quadrado(5));
// Pode-se passar funções como parâmetro, o retorno será utilizado na função recebida
console.log(quadrado(somar(5, 5)));
console.log(incrementarJuros(100, 10));
console.log(incrementarJuros(100, 15));

// Função main para código principal
function main() {
    console.log('Comece os códigos aqui');
}

main();
// Funções no JavaScript são objetos
console.log(main);
const main2 = main;
console.log(main2);

main = function (){
    console.log(1)
};
main();

// Funções invocadas imediatamente
// Main
(function () {
    console.log('Código executada automaticamente, depois da declaração');
})();
