import mainPrompt from './prompts/schema-main.js';
import createQrCode from './services/qrcode/create.js';
import createPassword from './services/password/create.js';
import getPromptResult from './prompts/utils/getPrompt.js';

(async function main() {
  getPromptResult(mainPrompt, async (result) => {
    if (result.select == 1) await createQrCode();
    else if (result.select == 2) await createPassword();
  });
})();
