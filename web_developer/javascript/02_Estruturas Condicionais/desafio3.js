// Cálculo preço de um produto
// A vista débito, 10% de desconto
// A vista dinheiro ou pix, 15% de desconto
// Em duas vezes, preço normal sem juros
// Acima de duas vezes, preço normal mais juros de 10%

const formaPagamento = 'cartão';
const precoEtiqueta = 799.99;

// Se débito, 10% de desconto
if (formaPagamento == 'débito') {
    console.log('Pagamento à vista com 10% de desconto.');
    const precoProduto = precoEtiqueta - (precoEtiqueta * 0.10);
    console.log(precoProduto);
} else if (formaPagamento == 'dinheiro' || formaPagamento == 'pix') {
    // Se dinheiro ou pix, 15% de desconto
    console.log('Pagamento à vista com 15% de desconto.');
    const precoProduto = precoEtiqueta - (precoEtiqueta * 0.15);
    console.log(precoProduto);
} else {
    const parcelas = 3;
    // Se até 2 parcelas, preço sem juros
    if (parcelas <= 2) {
        console.log('Pagamento parcelado sem juros.');
        console.log(precoEtiqueta);
    } else {
        // Se mais que 2 parcelas, 10% de juros
        console.log('Pagamento parcelado com 10% de juros.');
        const precoProduto = precoEtiqueta + (precoEtiqueta * 0.10);
        console.log(precoProduto);
    }
}