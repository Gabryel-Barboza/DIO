// Criando um componente com JavaScript
class CardNewsOld extends HTMLElement {
  constructor() {
    super();

    // Anexando uma nova árvore DOM a esse elemento, shadow DOM
    // Modo define a interação de JavaScript externo ao elemento, open pode interagir e close não
    const shadow = this.attachShadow({"mode": "open"});
    shadow.innerHTML = '<h1>Hello, World!</h1>';
  }

}

// Construindo o componente. Nome da marcação, classe do componente
customElements.define('card-news', CardNewsOld);
