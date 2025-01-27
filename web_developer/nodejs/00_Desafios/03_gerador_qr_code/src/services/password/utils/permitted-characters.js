import { passwordPrompt, customizePasswordPrompt } from '../../../prompts/schema-password.js';
import getPromptResult from '../../../prompts/utils/getPrompt.js';

// If user want to customize password
async function promptUser() {
  await getPromptResult(passwordPrompt, async (result) => {
    // Customize password rules if required (1 = yes | 2 = no)
    if (result.passwordCustomize == 1)
      await getPromptResult(
        customizePasswordPrompt,
        async (result) => await customizePassword(result)
      );
    else await permittedCharacters();
  });
}

// The user can customize the password
async function customizePassword(result) {
  // Get password new default (1 = yes | 2 = no)
  if (result.passwordLowercase == 2) process.env.LOWERCASE_LETTERS = 'false';
  if (result.passwordUppercase == 2) process.env.UPPERCASE_LETTERS = 'false';
  if (result.passwordNumber == 2) process.env.NUMBERS = 'false';
  if (result.passwordSpecial == 2) process.env.SPECIAL_CHARACTERS = 'false';

  process.env.PASSWORD_LENGTH = `${result.passwordLength}`;

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
