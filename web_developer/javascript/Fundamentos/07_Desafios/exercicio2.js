const { gets, print } = require('./funcoes-auxiliares-ex2');
// Crie um programa que receba N (quantidade de números) e seus respectivos valores, imprima o maior número par e menor número ímpar

const quantidadeNumeros = gets();
let maiorPar = null; 
let menorImpar = null;

// Separa valores pares de ímpares, pegando os respectivos valores do exercício
// Se um número for par e ou maiorPar nulo, maiorPar recebe esse número até outro maior substituir
// O mesmo acontece para menorImpar
for (let i = 0; i < quantidadeNumeros; i++) {
    let numero = gets();
    if (numero % 2 === 0) {
        if (maiorPar < numero || maiorPar === null) {
            maiorPar = numero;
        }
    // Se não é par, só pode ser ímpar
    } else if (menorImpar > numero || menorImpar === null) {
        menorImpar = numero;
    }
}

print('Maior número par: ' + maiorPar);
print('Menor número ímpar: ' + menorImpar);
