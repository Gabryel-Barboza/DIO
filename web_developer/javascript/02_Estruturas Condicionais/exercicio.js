// Cálculo da viagem
// variáveis:
// preço do etanol, preço da gasolina, tipo combustível no carro, gasto de combustível por km, distância em km da viagem

const precoEtanol = 4.14;
const precoGasolina = 5.80;
let tipoCombustivelCarro = 'gasolina';
let distanciaKm = 240;
const kmPorL = 10;
const gastoCombustivel = distanciaKm / kmPorL;
let gastoViagem;

if (tipoCombustivelCarro == 'etanol') {
    gastoViagem = precoEtanol * gastoCombustivel;
} else if (tipoCombustivelCarro == 'gasolina') {
    gastoViagem = precoGasolina * gastoCombustivel;
} else {
    console.log('Tipo de combustível inválido!');
};

console.log(gastoViagem.toFixed(2));
