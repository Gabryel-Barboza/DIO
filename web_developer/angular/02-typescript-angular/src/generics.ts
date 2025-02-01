// GENERICS

function concatArray(...items: any[]): any[] {
  return new Array().concat(...items);
}

const numArray = concatArray([1, 2, 3], [4, 5]);
const strArray = concatArray(['Gabryel', 'Kaio'], ['Brayan', 'José', 'Gomes']);
// Problemas de tipagem any:
// Array de number recebendo string, quebrando a semântica de tipagem dos dados
numArray.push('Gabryel');
console.log(numArray);

// Utilizando generics

// Definindo um tipo genérico com <variavel>
function concatArr<T>(...items: T[]): T[] {
  return new Array().concat(...items);
}

// Indicando o tipo de dados retornado na chamada da função
const numVetor = concatArr<number[]>([1, 2, 3], [4, 5]);
const strVetor = concatArr<string[]>(['Gabryel', 'Kaio'], ['Brayan', 'José', 'Gomes']);

// numVetor.push('Gabryel'); Erro
