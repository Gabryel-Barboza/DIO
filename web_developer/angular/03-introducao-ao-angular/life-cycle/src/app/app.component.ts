// componente principal, é injetado outros componentes aqui
import { Component, VERSION } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { HelloComponent } from './components/hello.component';
import { MenuComponent } from './components/menu.component';
import { ButtonComponent } from './components/button.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, HelloComponent, MenuComponent, ButtonComponent], // Importe os componentes aqui e insira no app.component.html
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'life-cycle';
  name = 'Angular ' + VERSION.major;
  buttonLabel: string = 'CARRINHO';
  buttonSecond: string = 'Clique aqui!';
}
