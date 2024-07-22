
const pokeApi = {}

// Retorna uma lista com todos os pokemons
pokeApi.getPokemons = function (offset=1, limit=10) {
    const url = `https://pokeapi.co/api/v2/pokemon/?offset=${offset}&limit=${limit}`;

    // Formatando a requisição para o produto final: response > json > nome e url pokemons > url de pokemons > todas as requests feitas > json com as informações dos pokemons
    return fetch(url) 
        .then((response) => {return response.json()})
        .then((jsonBody) => jsonBody.results)
        .then((pokemons) => pokemons.map((pokeApi.getPokemonDetail)))
        .then((detailRequests) => Promise.all(detailRequests))
        .then((pokemonsDetails) => pokemonsDetails)
        .catch((error) => console.log(error));
}

// Realiza a requisição e retorna uma instância de pokemon
pokeApi.getPokemonDetail = (pokemon) => {
    return fetch(pokemon.url).then((response) => response.json()).then(convertDetailToPokemon);
}

// Retorna uma instância de um modelo de pokemon adaptado para utilizar no site
function convertDetailToPokemon(pokeDetail) {
    const pokemon = new Pokemon();
    pokemon.number = pokeDetail.id;
    pokemon.name = pokeDetail.name;

    // Utilizando array destructuring
    const types = pokeDetail.types.map((typeSlot) => typeSlot.type.name);
    const [type] = types;

    pokemon.types = types;
    pokemon.type = type;
    pokemon.image = pokeDetail.sprites.other.dream_world.front_default;

    return pokemon;
}