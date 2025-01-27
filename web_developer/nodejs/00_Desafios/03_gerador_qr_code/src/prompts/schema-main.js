import chalk from 'chalk';

const mainPrompt = [
  {
    name: 'select',
    description: chalk.bgBlue.bold('Escolha uma opção (1 - QRCode ou 2 - Password)'),
    pattern: /^[1-2]+$/,
    message: chalk.red('Escolha apenas 1 ou 2!'),
    required: true,
  },
];

export default mainPrompt;
