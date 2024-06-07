// Construtores
class Pessoa {
    nome;
    idade;

    // Requer obrigatoriamente a passagem de parâmetros na instanciação
    constructor(nome, idade) {
        this.nome = nome;
        this.idade = idade;
        this.anoNascimento = 2024 - idade;
    }
    
    descrever() {
        console.log(`Meu nome é ${this.nome} e minha idade é ${this.idade}`);
    }
}

// Funções com objetos
function compararIdades(p1, p2) {
    if (p1.idade > p2.idade) {
        console.log(`${p1.nome} é mais velho que ${p2.nome}.`);
    } else if (p1.idade === p2.idade) {
        console.log(`${p1.nome} possui a mesma idade que ${p2.nome}.`);
    } else {
        console.log(`${p2.nome} é mais velho que ${p1.nome}.`);
    }
}

const gabryel = new Pessoa('Gabryel', 20);
gabryel.descrever();
console.log(gabryel);
const kaio = new Pessoa('Kaio', 20);
compararIdades(gabryel, kaio);
