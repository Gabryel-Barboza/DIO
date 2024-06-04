//Booleanos - Verdadeiro ou Falso
const eAzul = true;

// Operadores Relacionais
/*
< Menor
> Maior
<= Menor ou igual
>= Maior ou igual
== Parecido, converte tipos
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

// Estruturas Condicionais
console.log('=============');
console.log(numeroPar);

// Estrutura condicional composta
if (numeroPar) { // Estrutura condicional simples
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
