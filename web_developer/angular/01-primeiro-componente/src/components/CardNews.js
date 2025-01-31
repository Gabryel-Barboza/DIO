class CardNews extends HTMLElement {
  constructor() {
    super();

    const shadow = this.attachShadow({ mode: 'open' });
    shadow.appendChild(this.build());
    shadow.appendChild(this.styles());
  }

  build() {
    const componentRoot = document.createElement('div');
    componentRoot.setAttribute('class', 'card');

    const cardLeft = document.createElement('div');
    cardLeft.setAttribute('class', 'card-left');

    const author = document.createElement('span');
    author.textContent = 'By ' + (this.getAttribute('author') || 'By Anonymous');

    const title = document.createElement('h1');
    title.textContent = this.getAttribute('title');

    const description = document.createElement('p');
    description.textContent = this.getAttribute('description');

    const cardRight = document.createElement('div');
    cardRight.setAttribute('class', 'card-right');

    const newsImage = document.createElement('img');
    //newsImage.setAttribute('alt', this.getAttribute('img-alt'));
    newsImage.alt = this.getAttribute('img-alt');
    newsImage.src = this.getAttribute('img-src') || 'assets/default-photo.jpeg';

    cardLeft.append(author, title, description);
    cardRight.appendChild(newsImage);

    componentRoot.append(cardLeft, cardRight);

    return componentRoot;
  }

  styles() {
    const style = document.createElement('style');
    style.textContent = `
      .card {
        display: flex;
        flex-flow: row nowrap;
        justify-content: space-between;
        width: 80%;
        box-shadow: 5px 5px 5px 2px rgba(0,0,0,0.1);
      }

      .card-left {
        display: flex;
        flex-flow: column nowrap;
        justify-content: center;
        padding-left: 10px;
      }

      .card-left > span {
        font-weight: 400;
      }

      .card-left > h1 {
        margin-top: 15px;
        font-size: 30px;
      }

      .card-left > p {
        color: gray;
      }

      .card-right img {
        width: 300px;
        height: 200px;
      }
    `;

    return style;
  }
}

customElements.define('card-news', CardNews);
