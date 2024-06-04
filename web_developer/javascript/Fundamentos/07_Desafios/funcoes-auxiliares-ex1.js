const entradas = [5.5];
let i = 0;

function gets() {
    const valor = entradas[i];
    i++;
    return valor;
}

function print(texto) {
    console.log(texto);
}

// Exportando os módulos como objeto
module.exports = { gets, print };
