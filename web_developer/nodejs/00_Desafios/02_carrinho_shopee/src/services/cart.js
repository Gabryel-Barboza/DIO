// Add item to cart
async function addItem(userCart, item) {
  userCart.push(item);
}
// Delete item from cart
async function deleteItem(userCart, name) {
  const index = userCart.findIndex((item) => item.name === name);

  if (index !== -1) userCart.splice(index, 1);
}
// Add one unit to item
async function addUnitItem(userCart, index) {
  const addIndex = index - 1;

  if (index >= 0 && index <= userCart.length) userCart[addIndex].quantity++;
}
// Remove one unit from item
async function removeUnitItem(userCart, index) {
  const removeIndex = index - 1;

  if (index >= 0 && index <= userCart.length) {
    if (userCart[removeIndex].quantity > 1) userCart[removeIndex].quantity--;
    else userCart.splice(removeIndex, 1);
  }
}
// Calculate total
async function calculateTotal(userCart) {
  console.log('\nMy Shopee Cart Total:');
  const result = userCart.reduce((total, item) => total + item.subtotal, 0);
  console.log(result);
}
// Display cart items
async function displayCart(userCart, cartName) {
  console.log(`\nMy ${cartName}`);
  userCart.forEach((item, index) => {
    console.log(
      `${index + 1}. ${item.name} | ${item.price} | ${item.quantity} | Subtotal: ${item.subtotal}`
    );
  });
}
// Sort list items
async function sortList(userList) {
  userList.sort((item1, item2) => item1.quantity - item2.quantity);
}

export { addItem, deleteItem, addUnitItem, removeUnitItem, calculateTotal, displayCart, sortList };
