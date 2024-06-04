// Calcule o IMC de uma pessoa e imprima sua classificação
// Fórmula peso / altura²

let peso = 50.5;
let altura = 1.80;
const imc = peso / (altura ** 2); //Math.pow() também cálcula potência
console.log(imc.toFixed(2));

if (imc < 18.5) {
    console.log('Abaixo do peso');
} else if (imc <= 25) {
    console.log('Peso normal');
} else if (imc <= 30) {
    console.log('Acima do peso');
} else if (imc <= 40) {
    console.log('Obeso');
} else {
    console.log('Obesidade Grave');
}
