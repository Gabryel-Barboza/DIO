// Exercício: Cálculo do valor de viagem

const precoCombustivel = 5.79;
const kmPorCombustivel = 10;
let distanciaKm = 240;

console.log('Cálculo do valor de viagem');
console.log('O preço do combustível foi de R$5,79/L. Em média o carro roda 10km/L e irá percorrer 240 km na viagem.');

const custoViagem = precoCombustivel * (distanciaKm / kmPorCombustivel);

console.log('O gasto em reais será de: ');
console.log(custoViagem.toFixed(2));
// Método toFixed para arredondamento e retorno de String