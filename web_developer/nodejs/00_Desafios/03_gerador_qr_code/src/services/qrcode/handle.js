import qr from 'qrcode';
import chalk from 'chalk';

// Generate QrCode in terminal or export image
async function qrCodeGenerator(result) {
  const link = result.link;

  // Export QrCode Image
  if (result.type == 1)
    qr.toFile(`./exports/${link.slice(4)}-qrcode.png`, link, { type: 'png' }, (err) => {
      if (err) console.log(err);
      else console.log(chalk.green('Imagem salva na pasta exports do projeto...'));
    });
  // Print QrCode in Terminal
  else console.log(await qr.toString(link, { type: 'terminal' }));
}

async function handleQrCode(result) {
  console.log(chalk.green('QrCode criado com sucesso! \n'));
  try {
    qrCodeGenerator(result);
  } catch (err) {
    console.log(err);
  }
}

export default handleQrCode;
