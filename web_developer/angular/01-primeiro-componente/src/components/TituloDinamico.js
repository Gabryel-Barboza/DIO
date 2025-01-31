class TituloDinamico extends HTMLElement {
  constructor() {
    super();

    const shadow = this.attachShadow({ mode: 'open' });

    // Base do component
    const componentRoot = document.createElement('h1');
    // Atribuindo valores dinâmicos
    componentRoot.textContent = this.getAttribute('titulo');

    // Estilização do component
    const style = document.createElement('style');
    style.textContent = `
      h1 {
        color: red;
      }
    `;

    // Enviar para shadow root
    shadow.appendChild(componentRoot);
    shadow.appendChild(style);
  }
}

// Boa prática de nomeação da tag para o interpretador diferenciar corretamente
customElements.define('titulo-dinamico', TituloDinamico);
