// Adicione a feature flag "type": "module" ao arquivo package.json

//const { databaseConnect } = require('./utils/database');

// Extensão deve ser especificada. Semântica do ECMA Script
// .mjs é um módulo JavaScript para ser exportado, apenas uma nova semântica é adicionada ao arquivo. É opcional sua utilização.
import databaseConnect from './utils/database.mjs';

// Destructuring
import { databaseDisconnect, databaseType } from './utils/database.mjs';

//const database = require('./utils/database');
// Import all, as para alias
import * as database from './utils/database.mjs';
import * as api from './utils/api.js';

// Extensão para indicar arquivo que utiliza o padrão antigo.
import getInt from './utils/utils.cjs';

console.log('Hello, ecma!');

databaseConnect();
databaseDisconnect();

database.databaseDisconnect();

console.log(databaseType);

api.getData();
console.log(api.key);

getInt();
