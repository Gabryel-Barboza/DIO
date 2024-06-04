// Cálculo média 3 notas de aluno

const media = (5 + 3 + 6) / 3;
console.log(media);

if (media < 5) {
    console.log('Aluno reprovado!');
} else if (media <= 7) {
    console.log('Aluno em recuperação!');
} else {
    console.log('Aluno aprovado!');
};

