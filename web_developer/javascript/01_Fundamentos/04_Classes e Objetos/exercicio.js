// Crie uma classe carro com os atributos: marca, cor, gasto médio de combustível por kilômetro. Crie um método para cálculo de gasto de viagem com preço do combustível e km da viagem por parâmetros

class Carro {
    marca;
    cor;
    kmPorLitros;

    // Métodos
    constructor(marca, cor, kmPorLitro) {
        this.marca = marca;
        this.cor = cor;
        this.kmPorLitro = kmPorLitro;
    }

    calcularGastoPercurso(kmDistancia, precoCombustivel) {
        const litrosConsumidos = kmDistancia / this.kmPorLitro;
        const gastoViagem = precoCombustivel * litrosConsumidos;
        return gastoViagem;
    }
}


const uno = new Carro('Fiat', 'Prata', 12);
console.log(uno.calcularGastoPercurso(73, 5));
const palio = new Carro('Palio', 'Preto', 10);
console.log(palio.calcularGastoPercurso(73, 5));
