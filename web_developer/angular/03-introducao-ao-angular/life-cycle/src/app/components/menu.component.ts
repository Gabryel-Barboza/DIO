// Importar interfaces para definir componentes Angular
import { Component, Input } from '@angular/core';

@Component({
  selector: 'menu-component',
  templateUrl: `./menu.component.html`,
  styleUrls: [`./menu.component.css`],
})
export class MenuComponent {
  @Input() name: string = '';
}
