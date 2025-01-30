"use strict";
var __async = (__this, __arguments, generator) => {
  return new Promise((resolve, reject) => {
    var fulfilled = (value) => {
      try {
        step(generator.next(value));
      } catch (e) {
        reject(e);
      }
    };
    var rejected = (value) => {
      try {
        step(generator.throw(value));
      } catch (e) {
        reject(e);
      }
    };
    var step = (x) => x.done ? resolve(x.value) : Promise.resolve(x.value).then(fulfilled, rejected);
    step((generator = generator.apply(__this, __arguments)).next());
  });
};

// src/services/emails.ts
function getBaseEmail(senderName) {
  return __async(this, null, function* () {
    let base = yield getHeaderText();
    base + `Ol\xE1, ${senderName} estou te enviando um email sobre a vaga.`;
    base += "\n Gostaria de me inscrever, deixarei meu curr\xEDculo em anexo.";
    return base;
  });
}
function getHeaderText() {
  return __async(this, null, function* () {
    return "Texto para voc\xEA";
  });
}

// src/index.ts
(function main() {
  return __async(this, null, function* () {
    console.log(yield getBaseEmail("Gabryel"));
    console.log("Fim!");
  });
})();
