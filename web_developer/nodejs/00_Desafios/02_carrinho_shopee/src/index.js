import createItem from './services/item.js';
import * as cartServices from './services/cart.js';

const myCart = [];
const myWishList = [];

console.log('Welcome to your shopee cart!');

const item1 = await createItem('Console Ps4 Pro', 3200.0, 2);
const item2 = await createItem('Controle para Ps4', 499.99, 2);
const item3 = await createItem('Jogo Persona 5', 99.99, 2);

await cartServices.addItem(myCart, item1);
await cartServices.addItem(myWishList, item2);
await cartServices.addItem(myCart, item3);

// await cartServices.deleteItem(myCart, item1.name);

await cartServices.removeUnitItem(myCart, 2);
await cartServices.addUnitItem(myCart, 2);
await cartServices.removeUnitItem(myCart, 2);

cartServices.sortList(myCart);
cartServices.displayCart(myCart, 'Cart');

cartServices.calculateTotal(myCart);

cartServices.displayCart(myWishList, 'Wish List');
