
// Pegando o elemento ul do HTML
const pokemonUl = document.getElementById('pokemonList');
const pokemonLi = document.getElementsByClassName('pokemon');
const loadButton = document.getElementById('loadMore');
const limit = 10;
const maxPokemons = 151;
let offset = 0;

// Retornando um elemento li com as informações do pokemon
function convertListToHTML(pokemon) {
    return `<li class="pokemon ${pokemon.type}" onclick="openDetails(event)">
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

// Cria um Node com os detalhes de pokemon recebidos e adiciona ao body
function createModal(pokemon) {
    const modal = document.createElement('div');
    modal.classList.add('modal');
    modal.classList.add(`${pokemon.type}`);
    modal.innerHTML = `
    <div class="modal-btn modal-item">
        <button class="btn-close" onclick="closeModal()">X</button>
    </div>
    <div class="modal-name modal-item">
        <h2 class="name">${pokemon.name}</h2>
    </div>
    <div class="modal-id modal-item">#${pokemon.number}</div>
    <div class="modal-types modal-item">
        <ul class="types">${pokemon.types.map((type) => `<li class="type ${type}">${type}</li>`).join('')}</ul>
    </div>
    <div class="modal-text modal-item">
        <p>${pokemon.text}</p>
    </div>
    <div class="modal-img modal-item">
        <img src="${pokemon.image}" alt="Imagem de ${pokemon.name}">
    </div>
    <div class="modal-description modal-item">
        <div class="modal-stats">
            ${pokemon.stats.map((stat) => `<span class="stat">${stat.stat.name}:</span> <span class="stat-value">${stat.base_stat}</span>\n`).join('')}
        </div>
        <div class="modal-abilities">${pokemon.abilities.map((ability) => ability.ability.name).join(' ')}</div>
    </div>`;
    document.body.appendChild(modal);
}

// Fecha o modal ao ser invocada
function closeModal() {
    return document.body.getElementsByClassName('modal')[0].remove();
}

// Abre o pokemon selecionado e visualiza seus detalhes
async function openDetails(event) {
    // Seleciona o elemento que ativou o evento
    let item = event.target;
    // Enquanto o elemento não ser uma LI e não conter a classe pokemon selecione o elemento pai
    while (!(item.tagName == 'LI' && item.className.includes('pokemon'))) {
        item = item.parentElement;
    }
    const itemNumber = item.getElementsByClassName("number")[0].innerText.replace("#", "");
    const itemId = parseInt(itemNumber);
    // Requisitando as informações do pokemon selecionado e retornando um modal com os detalhes de pokemon
    const pokemon = await pokeApi.getPokemon(itemId);
    createModal(pokemon);
}

// Criando os elementos HTML dinamicamente após receber a lista de pokemons com o método
function loadPokemons(offset, limit) {
    // Criando uma lista HTML com os dados de pokemons
    pokeApi.getPokemons(offset, limit).then((pokemons = []) => {
        const newHtml = pokemons.map(convertListToHTML).join('');
        pokemonUl.innerHTML += newHtml;
    })
        .catch((error) => console.log(error));
}

// Iniciar a página e carregar os primeiros pokemons
loadPokemons(offset, limit);

function loadMore() {
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
}
