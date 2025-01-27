import chalk from 'chalk';
import handlePassword from './handle.js';

async function createPassword() {
  const password = await handlePassword();
  console.log(chalk.green('password:'));
  console.log(password);
}

export default createPassword;
