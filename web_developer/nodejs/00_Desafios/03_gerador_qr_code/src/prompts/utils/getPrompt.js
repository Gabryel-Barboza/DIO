import prompt from 'prompt';
import chalk from 'chalk';

async function getPromptResult(promptSchema, callback) {
  prompt.get(promptSchema, async (err, result) => {
    if (err) {
      console.log(chalk.red(`Error: ${promptSchema.name}`));
      return ''
    } else return callback(result);
  });
  prompt.start();
}

export default getPromptResult;
