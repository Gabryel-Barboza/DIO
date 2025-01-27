import qr from 'qrcode-terminal';
import chalk from 'chalk';

async function handleQrCode(err, result) {
  if (err) console.log("There's an error in the application.");
  else {
    const isSmall = result.type == 2;
    qr.generate(result.link, { small: isSmall }, (qrCode) => {
      console.log(chalk.green('QrCode gerado com sucesso:\n'));
      console.log(qrCode);
    });
  }
}

export default handleQrCode;
