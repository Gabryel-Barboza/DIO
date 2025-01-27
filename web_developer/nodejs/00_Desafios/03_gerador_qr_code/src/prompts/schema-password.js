import chalk from 'chalk';

// Prompts to customize the user password
const passwordPrompt = [
  {
    name: 'customizePassword',
    description: chalk.bgBlue.bold(
      'Customizar a sua senha ou criar uma com valores padrão? (1 - customizar ou 2 - padrão)'
    ),
    pattern: /^[1-2]+$/,
    message: chalk.red('Escolha apenas 1 ou 2!'),
    required: true,
  },
];

const customizePasswordPrompt = [
  {
    name: 'passwordLength',
    description: chalk.bgBlue.bold('Insira o tamanho da senha:'),
    pattern: /^[0-9]*$/,
    message: chalk.red('Escolha um valor numérico!'),
    required: true,
  },
  {
    name: 'passwordLowercase',
    description: chalk.bgBlue.bold('A senha pode conter letras minúsculas? (1 - sim ou 2 - não)'),
    pattern: /^[1-2]*$/,
    message: chalk.red('Escolha apenas 1 ou 2!'),
    required: true,
  },
  {
    name: 'passwordUppercase',
    description: chalk.bgBlue.bold('A senha pode conter letras maiúsculas? (1 - sim ou 2 - não)'),
    pattern: /^[1-2]*$/,
    message: chalk.red('Escolha apenas 1 ou 2!'),
    required: true,
  },
  {
    name: 'passwordNumber',
    description: chalk.bgBlue.bold('A senha pode conter número? (1 - sim ou 2 - não)'),
    pattern: /^[1-2]*$/,
    message: chalk.red('Escolha apenas 1 ou 2!'),
    required: true,
  },
  {
    name: 'passwordSpecial',
    description: chalk.bgBlue.bold('A senha pode conter caractere especial? (1 - sim ou 2 - não)'),
    pattern: /^[1-2]*$/,
    message: chalk.red('Escolha apenas 1 ou 2!'),
    required: true,
  },
];

export { passwordPrompt, customizePasswordPrompt };
