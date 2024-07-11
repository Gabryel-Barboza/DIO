// Requisitando a PokeAPI com FetchAPI
// Retorna uma promise da URL, onde é feito um processamento assincrono do resultado. Uma promessa de resposta é feita, porém não se sabe quando será recebida

// Exemplo didático
const url = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=10';
fetch(url) 
    .then(function (response) {
        // Realizando operações com a requisição
        console.log(response);
        // A API retorna um JSON, portanto vamos tratar o mesmo
        /*response.json().then(function (responseBody) {
            console.log(responseBody);
        })
        .catch();*/
        // Não recomendado aninhar o then, encadeie o bloco retornando outra promise

        return response.json(); 
    })
    .then(function (jsonBody) {
        // Tratando o json de retorno do anterior
        console.log(jsonBody);
    }) 
    .catch(function (error) {
        // Capturando erros se requisição rejeitada
        console.log(error);
    })
    .finally(function () {
        // Executado independente do resultado da requisição
        console.log('Requisição concluída!');
    });

// Pegando o elemento ul do HTML
const pokemonUl = document.getElementById('pokemonList');
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

loadButton.addEventListener('click', () => {
    offset += limit;
    // Checando se os próximos pokemons ultrapassam o máximo definido, remove o botão e retorna o até o limite se true
    const nextPokemons = offset + limit;
    if (nextPokemons >= maxPokemons) {
        const newLimit = maxPokemons - offset;
        loadPokemons(offset, newLimit);
        loadButton.parentElement.removeChild(loadButton);
    } else {
        loadPokemons(offset, limit);
    }
})
// Iniciar a página e carregar os primeiros pokemons
loadPokemons(offset, limit);
