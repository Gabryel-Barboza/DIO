import chalk from 'chalk';

const promptQrCode = [
  {
    name: 'link',
    description: chalk.yellow.bold('Digite o link para gerar o QrCode'),
  },
  {
    name: 'type',
    description: chalk.bgBlue.bold('Qual o tipo de QrCode (1 - Imagem ou 2 - Terminal)'),
    pattern: /^[1-2]+$/,
    message: chalk.red('Escolha apenas 1 ou 2!'),
    required: true,
  },
];

export default promptQrCode;
