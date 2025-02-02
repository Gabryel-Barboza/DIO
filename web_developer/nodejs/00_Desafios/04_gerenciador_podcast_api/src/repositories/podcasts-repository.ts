import fs from 'fs';
import readLine from 'readline';
import path from 'path';

import { PodcastModel } from '../models/podcast-model';
import { Readline } from 'readline/promises';

// __dirname não definido em módulos ESM, retire o campo "type" do package.json
// O funcionamento da sintaxe de import continua a mesma com TypeScript.
const pathData = path.join(__dirname, 'podcasts.json');
const charset = 'utf8';

// Lê o repositório de podcasts (podcasts.json)
// Parâmetro opcional com ?
export const getRepoPodcast = async (podcastName?: string): Promise<PodcastModel[]> => {
  const rawData = fs.readFileSync(pathData, charset);
  let jsonFile = JSON.parse(rawData);

  // Retorna elementos de acordo com o filtro, se disponível
  if (podcastName)
    jsonFile = jsonFile.filter((podcast: PodcastModel) => podcast.podcastName === podcastName);

  return jsonFile;
};

export const insertRepoPodcast = async (json: string) => {
  try {
    // Recriando o arquivo corretamente
    fs.readFile(pathData, charset, (err, file) => {
      if (err) throw new Error();
      else {
        const lines = file.split('\n');
        console.log(lines);
        let newLines = lines.filter((line) => !line.includes(']'));
        newLines = newLines.concat(',', json);
        
        const newFile = newLines.join('\n');

        fs.writeFile(pathData, newFile, charset, (err) => {
          if (err) throw new Error();
        });
      }
    });

    return json;
  } catch (err) {
    return '';
  }
};
