// Classes e instâncias
// Classe é o molde
class Pessoa {
    nome;
    idade;

    descrever() {
        console.log(`Meu nome é ${this.nome} e minha idade é ${this.idade}`);
    }
}

// Instâncias são objetos criados a partir do molde
// new define a instanciação de um objeto
const gabryel = new Pessoa();
console.log(gabryel);
gabryel.nome = 'Gabryel';
gabryel.idade = 25;
gabryel.descrever();

const kaio = new Pessoa();
kaio.nome = 'Kaio';
kaio.idade = 20;
kaio.descrever();
