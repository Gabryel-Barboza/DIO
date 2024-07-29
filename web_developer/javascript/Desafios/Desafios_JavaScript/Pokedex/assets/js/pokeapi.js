
const pokeApi = {}

// Retorna o pokemon definido
pokeApi.getPokemon = function (id) {
    return fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
        .then((response) => response.json())
        .then((pokeDetail) => {
            debugger
            const pokemon = convertDetailToPokemon(pokeDetail)
            pokeApi.getPokemonText(pokeDetail.species.url)
                .then((text) => text)
                .then((text) => pokemon.text = text)
                .then((pokemon) => pokemon)
                .catch((error) => console.log(error));
        })
        .catch((error) => console.log(error));
}
// Retorna uma lista com todos os pokemons, dentro do limite definido
pokeApi.getPokemons = function (offset = 1, limit = 10) {
    const url = `https://pokeapi.co/api/v2/pokemon/?offset=${offset}&limit=${limit}`;

    // Formatando a requisição para o produto final: response > json > nome e url pokemons > url de pokemons > todas as requests feitas > json com as informações dos pokemons
    return fetch(url)
        .then((response) => { return response.json() })
        .then((jsonBody) => jsonBody.results)
        .then((pokemons) => pokemons.map((pokeApi.getPokemonDetail)))
        .then((detailRequests) => Promise.all(detailRequests))
        .then((pokemonsDetails) => pokemonsDetails)
        .catch((error) => console.log(error));
}

// Realiza a requisição e retorna uma instância de pokemon, utilizando async para fins didáticos
pokeApi.getPokemonDetail = async (pokemon) => {
    try {
        const response = await fetch(pokemon.url);
        const pokeDetail = await response.json();
        return convertDetailToPokemon(pokeDetail);
    } catch (error) {
        return console.log(error);
    }
}

// Realiza a requisição e retorna um texto sobre o pokemon
pokeApi.getPokemonText = async (url) => {
    try {
        const response = await fetch(url);
        const text = await response.json().flavor_text_entries[0].flavor_text;
        return text;
    }  catch (error) {
        return console.log(error);
    }
}

// Retorna uma instância de um modelo de pokemon adaptado para utilizar no site
function convertDetailToPokemon(pokeDetail) {
    const pokemon = new Pokemon();
    pokemon.number = pokeDetail.id;
    pokemon.name = pokeDetail.name;

    const types = pokeDetail.types.map((typeSlot) => typeSlot.type.name);
    const [type] = types;

    pokemon.types = types;
    pokemon.type = type;
    pokemon.image = pokeDetail.sprites.other.dream_world.front_default;
    pokemon.stats = pokeDetail.stats;
    pokemon.abilities = pokeDetail.abilities;

    return pokemon;
}