// Classe para representar pessoas
// Atributos: nome, peso e altura
// Método para calcular o IMC

class Pessoa {
    nome;
    peso;
    altura;

    constructor(nome, peso, altura) {
        this.nome = nome;
        this.peso = peso;
        this.altura = altura;
    }

    calcularImc() {
        return (this.peso / (Math.pow(this.altura, 2))).toFixed(2);
    }

    classificarImc() {
        const imc = this.calcularImc();
        if (imc < 18.5) {
            return 'Abaixo do peso';
        } else if (imc <= 25) {
            return 'Peso normal';
        } else if (imc <= 30) {
            return 'Acima do peso';
        } else if (imc <= 40) {
            return 'Obesidade';
        } else {
            return 'Obesidade Grave';
        }
    }
}

const jose = new Pessoa('José', 70, 1.75);
console.log(jose.calcularImc());
console.log(jose.classificarImc());
