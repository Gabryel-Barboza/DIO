"use strict";

// src/interfaces.ts
var Pessoa = class {
  constructor(id, name) {
    this.id = id;
    this.name = name;
  }
  sayHello() {
    return `Hello, I'm ${this.name}`;
  }
};
var p = new Pessoa("1", "Mecha");
console.log(p.sayHello());
