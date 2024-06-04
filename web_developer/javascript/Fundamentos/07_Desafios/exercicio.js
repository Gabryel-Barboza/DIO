const { gets, print } = require('./funcoes-auxiliares-ex1');
// Faça um programa que receba a média de alunos
// Caso a média seja < 5 "Reprovado"
// Caso a média seja >= 5 e < 7 "Recuperação"
// Caso a média seja >= 7 "Aprovado"

media = gets();
if (media < 5) {
    print('Reprovado');
} else if (media < 7) {
    print('Recuperação');
} else {
    print('Aprovado');
}
