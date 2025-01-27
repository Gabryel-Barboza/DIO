import dotenv from 'dotenv/config';

import promptUser from './utils/permitted-characters.js';

// Handler to create password
async function handlePassword() {
  let characters = [];
  let password = '';

  characters = await promptUser();
  const passwordLength = process.env.PASSWORD_LENGTH;

  for (let i = 0; i < passwordLength; i++) {
    const index = Math.floor(Math.random() * characters.length);
    password += characters[index];
  }

  return password;
}

export default handlePassword;
