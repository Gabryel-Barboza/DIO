// DECORATORS

// Exibe o nome da classe, target recebe o invoker do decorator
function ExibirNome(target: any) {
  console.log(target);
}

// Em versões antigas, habilitar experimentalDecorators em tsconfig.json
@ExibirNome
class Funcionario {}

function apiVersion(version: string) {
  return (target: any) => {
    Object.assign(target.prototype, { __version: version });
  };
}

@apiVersion('1.0')
class Api {}

const api = new Api();
//console.log(api.__version);

function minLength(length: number) {
  return (target: any, key: string) => {
    console.log(target);
    console.log(key);
    let _value = target[key];

    const getter = () => _value;
    const setter = (value: string) => {
      if (value.length < length) throw new Error(`Tamanho menor do que ${length}`);
      else _value = value;
    };

    Object.defineProperty(target, key, { get: getter, set: setter });
  };
}

class Api2 {
  @minLength(5)
  name: string;

  constructor(name: string) {
    this.name = name;
  }
}

const a1 = new Api2('produtos');
console.log(a1);
