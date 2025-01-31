import fs from 'fs';
import path from 'path';

import { PodcastModel } from '../models/podcast-model';

// __dirname não definido em módulos ESM, retire o campo "type" do package.json
// O funcionamento da sintaxe de import continua a mesma com TypeScript.
const pathData = path.join(__dirname, 'podcasts.json');

// Lê o repositório de podcasts (podcasts.json)
// Parâmetro opcional com ?
export const repoPodcast = async (podcastName?: string): Promise<PodcastModel[]> => {
  const charset = 'utf-8';
  const rawData = fs.readFileSync(pathData, charset);
  let jsonFile = JSON.parse(rawData);

  // Retorna elementos de acordo com o filtro, se disponível
  if (podcastName)
    jsonFile = jsonFile.filter((podcast: PodcastModel) => podcast.podcastName === podcastName);

  return jsonFile;
};
