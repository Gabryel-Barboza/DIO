import { passwordPrompt, customizePasswordPrompt } from '../../../prompts/schema-password.js';
import getPromptResult from '../../../prompts/utils/getPrompt.js';

// If user want to customize password
async function promptUser() {
  const result = await getPromptResult(passwordPrompt);
  if (result) {
    // Customize password rules if required (1 = yes | 2 = no)
    if (result.customizePassword == 1)
      return await getPromptResult(customizePasswordPrompt, customizePassword);
    else return await permittedCharacters();
  } else {
    console.log('Error in promptUser');
    return '';
  }
}

// The user can customize the password
async function customizePassword(result) {
  // Get password new default (1 = yes | 2 = no)
  process.env.PASSWORD_LENGTH = `${result.passwordLength}`;

  if (process.env.PASSWORD_LENGTH > 30) {
    console.log('Tamanho máximo da senha permitido é de 30 caracteres');
    return '';
  }

  if (result.passwordLowercase == 2) process.env.LOWERCASE_LETTERS = 'false';
  if (result.passwordUppercase == 2) process.env.UPPERCASE_LETTERS = 'false';
  if (result.passwordNumber == 2) process.env.NUMBERS = 'false';
  if (result.passwordSpecial == 2) process.env.SPECIAL_CHARACTERS = 'false';

  return await permittedCharacters();
}

// Check permitted characters to include in password
async function permittedCharacters() {
  let characters = [];

  // Characters permitted to create password
  if (process.env.UPPERCASE_LETTERS === 'true') characters.push(...'ABCDEFGHIJKLMNOPQRSTUVWXYZ');
  if (process.env.LOWERCASE_LETTERS === 'true') characters.push(...'abcdefghijklmnopqrstuvwxyz');
  if (process.env.NUMBERS === 'true') characters.push(...'0123456789');
  if (process.env.SPECIAL_CHARACTERS === 'true') characters.push(...'$#@.,^-_%&*');

  return characters;
}

export default promptUser;
