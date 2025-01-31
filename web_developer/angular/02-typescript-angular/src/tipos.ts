// TIPOS PRIMITIVOS
let ligado: boolean;
let nome: string;
let idade: number;

ligado = false;
// ligado = 'verdadeiro'; -- erro
nome = 'Gabryel';
idade = 20;
// Inferência de tipos pela inicialização
let altura = 1.8;

// Tipos especiais
let nulo: null = null;
let indefinido: undefined = undefined;

// Tipo vazio
let retorno: void;
// Tipo genérico
let qualquerCoisa: any;
qualquerCoisa = 1;
qualquerCoisa = '1';

// OBJETOS

// objeto não determinístico - aceita qualquer formato de objeto
let pessoa: object = {
  nome: 'Gabryel',
  idade: 20,
};

// objeto determinístico - restringe o formato do objeto com um tipo customizado

// Criando um tipo
type product = {
  name: string;
  price: number;
  unit: number;
};

// Criando o objeto de tipo especifico
const banana: product = {
  name: 'banana',
  price: 3.99,
  unit: 10,
};

// ARRAYS

let dados: string[];
let dados2: Array<string>;
// dados = [1, 2, 3];
dados = ['1', '2', '3'];

// Multi-types
let infos: (string | number)[] = ['Gabryel', 20];

// TUPLAS

// Declarada com um colchete e os tipos dentro do colchete
// Limita o valor atribuído a seguir essa exata ordem
let boleto: [string, number, number] = ['conta', 249.99, 3];

// DATE

// Declara dados no formato de datas: 'yyyy-mm-dd'
let aniversario: Date = new Date('2000-01-01 16:00');
console.log(aniversario.toString());

// FUNÇÕES

// Tipagem de parâmetros (obrigatório) e retorno (opcional)
function addNumbers(x: number, y: number): number {
  return x + y;
}

// Inferência de tipo
function addToHello(name: string) {
  return `Hello, ${name}!`;
}

let soma: number = addNumbers(10, 10);

// Multi-types

function callToPhone(phone: string | number) {
  return phone;
}

console.log(callToPhone(112233445));

// Async functions

// Tipo Promise<string>
async function getDatabase(id: number) {
  return '';
}

async function insertDatabase(value: string): Promise<number | string> {
  return 'sucess'
}
