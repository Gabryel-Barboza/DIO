// CLASSES

// Data Modifiers - public, private, protected. Define permissões de acesso a atributos e propriedades
// public(padrão): acesso livre, private: acesso restrito a classe apenas, protected: acesso restrito a classe e suas filhas (herdadas)

class Character {
  public name?: string;
  private strength: number;
  protected skill: number;

  // Parâmetros obrigatórios e opcionais com ?
  constructor(strength: number, skill: number, name?: string) {
    this.name = name;
    this.strength = strength;
    this.skill = skill;
  }

  // Modificador de acesso em métodos
  public attack(): void {
    console.log(`${this.name} is attacking the enemy! Dealt ${this.strength} points of damage.`);
  }
}

class Magician extends Character {
  magicPoints: number;

  constructor(strength: number, skill: number, magicPoints: number, name?: string) {
    super(strength, skill, name);
    this.magicPoints = magicPoints;
  }

  public castSpell(): void {
    // Acessando atributo protected em classe filha
    console.log(`${this.name} is casting spell! Dealt ${this.skill} points of damage.`);
    this.magicPoints--;
  }
}

const p1 = new Character(20, 50, 'Dante');
console.log(p1);
p1.attack();
p1.name;
// p1.strength

const p2 = new Magician(5, 30, 50, 'Gandalf');
p2.castSpell();
