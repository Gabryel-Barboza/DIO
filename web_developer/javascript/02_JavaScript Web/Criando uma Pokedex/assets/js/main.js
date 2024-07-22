
// Pegando o elemento ul do HTML
const pokemonUl = document.getElementById('pokemonList');
const pokemonLi = document.getElementsByClassName('pokemon');
const loadButton = document.getElementById('loadMore');
const limit = 10;
const maxPokemons = 151;
let offset = 0;

// Retornando um elemento li com as informações do pokemon
function convertListToHTML(pokemon) {
    return `<li class="pokemon ${pokemon.type}">
                <span class="number">#${pokemon.number}</span>
                <span class="name">${(pokemon.name)}</span>
                <div class="details">
                    <ol class="types">
                        ${pokemon.types.map((type) => `<li class="type ${type}">${type}</li>`).join('')}
                    </ol>
                    <img src="${pokemon.image}" alt="${pokemon.name}">
                </div>
            </li>`
}

// Criando os elementos HTML dinamicamente após receber a lista de pokemons com o método
function loadPokemons(offset, limit) {
    // Breakpoint para o debug no dev tools/Node.js
    debugger

    // Criando uma lista HTML com os dados de pokemons
    // O mesmo que um for percorrendo a lista e pegando valores individuais, depois chamando a função para transformar em HTML
    pokeApi.getPokemons(offset, limit).then((pokemons = []) => {
        const newHtml = pokemons.map(convertListToHTML).join('');
        pokemonUl.innerHTML += newHtml;
    })
    .catch((error) => console.log(error));
}

// Executado antes de promises, sincrono
console.log(10 + 10);

// Iniciar a página e carregar os primeiros pokemons
loadPokemons(offset, limit);

loadButton.addEventListener('click', () => {
    offset += limit;
    // Checando se os próximos pokemons ultrapassam o máximo definido, remove o botão e retorna o restante até o limite se true
    const nextPokemons = offset + limit;
    if (nextPokemons >= maxPokemons) {
        const newLimit = maxPokemons - offset;
        loadPokemons(offset, newLimit);
        loadButton.parentElement.removeChild(loadButton);
    } else {
        loadPokemons(offset, limit);
    }
});
