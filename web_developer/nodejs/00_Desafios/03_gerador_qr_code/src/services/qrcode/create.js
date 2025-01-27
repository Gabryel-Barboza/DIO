import promptQrCode from '../../prompts/schema-qrcode.js';
import handleQrCode from './handle.js';
import getPromptResult from '../../prompts/utils/getPrompt.js';

async function createQrCode() {
  const result = getPromptResult(promptQrCode, handleQrCode);
  if (!result) console.log('An error ocurred in createQrCode');
}

export default createQrCode;
