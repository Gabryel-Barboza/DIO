// Extensão não necessária, só um tipo de arquivo ts
import { getBaseEmail } from './services/emails';

(async function main() {
  console.log(await getBaseEmail('Gabryel'));
  console.log('Fim!');
})();
