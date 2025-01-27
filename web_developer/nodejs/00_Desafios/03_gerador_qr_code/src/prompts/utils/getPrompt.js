import prompt from 'prompt';

// Prompt the user with a prompt schema and return the result/callback
async function getPromptResult(promptSchema, callback = '') {
  prompt.start();
  const result = await prompt.get(promptSchema);

  if (result.err) {
    console.log(result.err);
    return '';
  } else if (callback) return callback(result);
  else return result;
}

export default getPromptResult;
