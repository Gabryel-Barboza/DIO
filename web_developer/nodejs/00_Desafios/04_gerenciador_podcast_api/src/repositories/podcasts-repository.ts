import fs from 'fs';
import path from 'path';

import { PodcastModel } from '../models/podcast-model';

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
    // Ler arquivo
    const file = fs.readFileSync(pathData, charset);

    if (file.length !== 0) {
      // Separar linhas
      let lines = file.split('\n');
      // Concatenar vírgula ao último JSON
      // Remover último caractere ] e Adicionar o novo JSON
      lines.splice(-2, 2, '},', json);
      // Fechar o vetor com ]
      lines = lines.concat(']');
      // Reescrever o arquivo
      const newFile = lines.join('\n');
      fs.writeFileSync(pathData, newFile, charset);
    } else {
      // Criar estrutura se arquivo vazio
      const newFile = `[\n${json}\n]`;
      fs.writeFileSync(pathData, newFile, charset);
    }

    return json;
  } catch (err) {
    return '';
  }
};
