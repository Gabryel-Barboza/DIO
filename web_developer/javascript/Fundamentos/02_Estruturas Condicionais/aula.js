//Booleanos - Verdadeiro ou Falso - Tipo binário
const eAzul = true;

// Operadores Relacionais
/*
< Menor
> Maior
<= Menor ou igual
>= Maior ou igual
== Parecido, converte os tipos de dados
=== Idêntico
*/

//Operadores Lógicos
/*
&& - E
|| - Ou
! - Negação
*/

const numeroPar = 11 % 2 == 0;
console.log(numeroPar);
console.log(10 % 2 == '0');
console.log(10 % 2 === '0');
console.log(10 % 2 === 0);

console.log('=============');

// Estruturas Condicionais
console.log(numeroPar);

// Estrutura condicional simples
// O mesmo que if (numeroPar === true) resumida em if (numeroPar)
if (numeroPar) {
    // Executa esse bloco se condição verdadeira
}

// Estrutura condicional composta
// Se verdadeiro executa esse, senão executa esse
if (numeroPar) { 
    console.log('É par!');
} else {
    console.log('É ímpar!');
}

console.log('==============');

const numero = 0;
const numeroDivisivel = numero % 5 === 0;

// Apenas um else por estrutura, vários else if
if (numero === 0) {
    console.log('Número Inválido!');
    console.log(numero);
} else if (numeroDivisivel) {
    console.log('É Divisível!');
} else {
    console.log('Não é Divisível!');
};
