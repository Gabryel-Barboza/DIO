
const pokeApi = {}

// Retorna o pokemon pelo id, requisita um pokemon e seu texto
pokeApi.getPokemon = async function (id) {
    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`);
        const pokeDetail = await response.json();
        const pokemon = convertDetailToPokemon(pokeDetail);
        const text = await pokeApi.getPokemonText(pokeDetail.species.url);
        pokemon.text = text.flavor_text_entries[0].flavor_text;
        return pokemon;
    } catch (error) {
        return console.log(error);
    }
}

// Retorna uma lista com todos os pokemons, dentro do limite definido
pokeApi.getPokemons = async function (offset = 1, limit = 10) {
    const url = `https://pokeapi.co/api/v2/pokemon/?offset=${offset}&limit=${limit}`;

    // Formatando a requisição para o produto final: response > json > nome e url pokemons > url de pokemons > todas as requests feitas > json com as informações dos pokemons
    try {
        const response = await fetch(url);
        const jsonBody = await response.json();
        const pokemons = jsonBody.results;
        const detailRequests = pokemons.map((pokeApi.getPokemonDetail));
        const pokemonsDetails = await Promise.all(detailRequests);
        return pokemonsDetails;
    } catch (error) {
        return console.log(error);
    }
}

// Realiza a requisição e retorna uma instância de pokemon
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
        const text = await response.json()
        return text;
    } catch (error) {
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