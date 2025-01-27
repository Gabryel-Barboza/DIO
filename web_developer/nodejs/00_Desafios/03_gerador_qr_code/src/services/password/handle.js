import dotenv from 'dotenv/config';

import promptUser from './utils/permitted-characters.js';

// Handler to create password
async function handlePassword() {
  let characters = [];
  let password = '';

  characters = await promptUser();
  const passwordLength = process.env.PASSWORD_LENGTH;

  if (characters.length > 0)
    for (let i = 0; i < passwordLength; i++) {
      const index = Math.floor(Math.random() * characters.length);
      password += characters[index];
    }
  else console.log('Erro na criação da senha! Abortando serviço.');

  return password;
}

export default handlePassword;
