const { gets, print } = require('./funcoes-auxiliares');

// 5 alunos recebe um número sorteado de 1 - 100, faça um programa que receba os números e mostre qual é maior

// Recebendo os valores de entrada
const numeros = [];
for (let i = 0; i < 5; i++) {
    numeros.push(gets());
}

// Verificando qual é maior
let numMaior = numeros[0]
for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] > numMaior) {
        numMaior = numeros[i];
    }
}

print(`O maior número recebido é: ${numMaior}`);
