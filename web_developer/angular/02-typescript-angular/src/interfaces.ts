// Interfaces x types

// Types para criação de tipos
type robot = {
  readonly id: number | string;
  name: string;
};

// Interfaces para classes. No entanto, funcionam para qualquer cenário
// sintaxe similar a classe
// Contratos para serem implementados no aproveitamento
interface Robot {
  readonly id: number | string;
  name: string;
  sayHello(): string;
}

const robot1: robot = {
  id: 1,
  name: 'Robotnik',
};

const robot2: Robot = {
  id: 2,
  name: 'Megatron',
  sayHello: function (): string {
    return 'Function not implemented.';
  },
};

// readonly impede o acesso a propriedade
//robot1.id = '3';

// Type ou interface permitidos, mas interface que deve ser utilizada
class Pessoa implements Robot {
  id: string | number;
  name: string;

  constructor(id: string | number, name: string) {
    this.id = id;
    this.name = name;
  }
  sayHello(): string {
    return `Hello, I'm ${this.name}`;
  }
}

const p = new Pessoa('1', 'Mecha');
console.log(p.sayHello());

// Faça a compilação do código para JS e veja as diferenças
