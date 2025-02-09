// Arquivo principal do componente, possui as definições do HTML e CSS ou os caminhos para cada um

import { Component, Input } from '@angular/core';
//  Importação de decoradores do Angular core

// Criação de um componente com o decorador para a classe
@Component({
  selector: 'hello', // Marcação do HTML
  template: `<h1>Hello {{ name }}!</h1>`, // Estrutura do HTML, coloque 'Url' para caminho até arquivo
  // Estilos CSS, styleUrls para caminho
  styles: [
    `
      h1 {
        font-family: Lato;
      }
    `,
  ],
})
// classe de mesmo nome do arquivo para boa prática
export class HelloComponent {
  @Input() name!: string;
}
