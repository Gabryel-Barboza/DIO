import chalk from 'chalk';
import handlePassword from './handle.js';

async function createPassword() {
  const password = await handlePassword();
  if (password) {
    console.log(chalk.green('password:'));
    console.log(password);
  }
}

export default createPassword;
