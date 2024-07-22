const lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Métodos para manipulação de listas

// Foreach - Percorre a lista e executa alguma ação para cada elemento
lista.forEach((value, i, listRef) => {
    console.log(value, i, listRef);
});

// Filter - Retorna uma nova lista baseado em condicionais de uma função
const listaPares = lista.filter((element) => {
    return element % 2 === 0;
});

listaPares.forEach((value) => console.log(value));

// Map - Retorna uma lista de novos elementos mapeados a partir de uma função
class Pessoa {
    constructor(name) {
        this.name = name;
    }
}

const listaPessoa = [new Pessoa('Gabryel'), new Pessoa('Kaio'), new Pessoa('Brayan'), new Pessoa('Renan'), new Pessoa('Guilherme')];

const callBack = (element, i) => `${i} - ${element.name}`;
// Percorre  a lista de objetos Pessoa, pega o nome de cada objeto e cria uma lista com nomes
const listaNomes = listaPessoa.map(callBack);
console.log(listaNomes);

// Reduce - Percorre a lista e reduz para um único elemento
const soma = lista.reduce((previous, current) => previous + current, 0);
console.log(soma);

// Join - Junta uma lista com um separador
console.log(lista.join(' '));


const lista2 = [{nome: 'Renan'}, {nome: 'Gabryel'}, {nome: 'Guilherme'}, {nome: 'Kaio'}];
console.log(lista2.map((e) => e.nome)
                  .filter((e) => e.startsWith('G'))
                  .join('; '));

// Concat - concatena duas ou mais listas
lista.concat();
