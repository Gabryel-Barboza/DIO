import { Component, Input } from '@angular/core';

@Component({
  selector: 'button-component',
  templateUrl: `./button.component.html`,
  styleUrls: [`./button.component.css`],
})
export class ButtonComponent {
  // Interpolação de dados
  // Podem ser acessados pelo button.component.html da mesma maneira que no Typescript.
  buttonText: string = 'ACESSAR';
  buttonNumber: number = 1;
  buttonTexts: string[] = ['Comprar', 'Vender'];
  buttonObject = {
    label: 'Adicionar ao carrinho',
  };
  @Input() label: string = '';
}
