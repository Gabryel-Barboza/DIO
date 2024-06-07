// Listas ou Arrays
// Criadas com [] e valores separados por ,

const aluno = 'João';
const alunos = ['Gabryel', 'Kaio', 'Brayan'];

// Acessando a lista
console.log(alunos);
console.log(alunos[0]);
console.log(alunos[2]);
console.log(alunos[3]);

//Adicionando items a lista
alunos.push('Renan');
console.log(alunos[3]);
alunos[4] = 'Vínicius';
console.log(alunos);
alunos[5] = 10;
console.log(alunos[5]);

// Removendo items da lista
// Última posição
console.log(alunos.pop());
console.log(alunos);
// Primeira posição
console.log(alunos.shift());
console.log(alunos);

// Tamanho da lista
console.log(alunos.length);

// Percorrendo uma lista
let notas = [10, 5, 7, 9, 8];

let soma = notas[0] + notas[1] + notas[2] + notas[3] + notas[4];
console.log(`A média é ${soma / 5}`);
notas[5] = 7;

soma = 0;

// Estruturas de Repetição
// Utilizando a estrutura for para percorrer a lista

// Para i começando em 0; execute enquanto i menor que tamanho de notas; incremente 1 em i após execução do bloco
for (let i = 0; i < notas.length; i++) {
    soma += notas[i];
    // Bloco executado n vezes, n = tamanho de notas
}

console.log(`A média é ${soma / notas.length}`);

// Strings são arrays de caracteres
const nome = 'Gabryel';
for (let i = 0; i < nome.length; i++) {
    console.log(nome[i]);
}
