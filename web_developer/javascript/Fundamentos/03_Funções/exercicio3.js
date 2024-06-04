// Programa para calcular preço do produto com funções

function pagamentoDebito(preco) {
    // 10% de desconto
    return preco - (preco * 0.10);
}

function pagamentoDinheiroPix(preco) {
    // 15% de desconto
    return preco - (preco * 0.15);
}

function pagamento2Parcelas(preco) {
    // Preço do produto
    return preco;
}

function pagamentoMaisParcelas(preco) {
    // 10% de juros
    return preco + (preco * 0.10);
}

function formaPagamento(opcao, preco) {
    if (opcao === 1) {
        return pagamentoDebito(preco);
    } else if (opcao === 2) {
        return pagamentoDinheiroPix(preco);
    } else if (opcao === 3) {
        return pagamento2Parcelas(preco);
    } else {
        return pagamentoMaisParcelas(preco);
    }
}

(function () {
    console.log('main');
    console.log('Um produto de R$500 foi comprado à vista no Pix');
    let preco = 500;
    console.log(formaPagamento(2, preco));
    preco = 1000;
    // 2x parcelado
    console.log(formaPagamento(3, preco));
    // Mais parcelas
    console.log(formaPagamento(4, preco));
})();