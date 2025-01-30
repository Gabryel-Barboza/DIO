"use strict";
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);
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
var emails_exports = {};
__export(emails_exports, {
  getBaseEmail: () => getBaseEmail
});
module.exports = __toCommonJS(emails_exports);
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
// Annotate the CommonJS export names for ESM import in node:
0 && (module.exports = {
  getBaseEmail
});
