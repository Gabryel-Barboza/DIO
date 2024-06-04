const { gets, print } = require('./funcoes-auxiliares-ex3');

// Faça um programa que calcule e imprima o salário de um funcionário
// Receba o valor bruto e o adicional
// valor bruto salário - percentual de imposto de faixa salarial + adicional

// Aliquotas:
/* 
R$0 - R$1100 - 5%
R$1100.01 - R$2500 - 10%
Maior que R$2500 - 15%
*/

function calcularImposto(salarioFinal, salario) {
    if (salario <= 1100) {
        salarioFinal -= salario * 0.05;
    } else if (salario <= 2500) {
        salarioFinal -= salario * 0.10;
    } else {
        salarioFinal -= salario * 0.15;
    }
    return salarioFinal;
}

const salario = gets();
const adicional = gets();
let salarioFinal = salario;

salarioFinal = calcularImposto(salarioFinal, salario);
salarioFinal += adicional;

print(salarioFinal);
