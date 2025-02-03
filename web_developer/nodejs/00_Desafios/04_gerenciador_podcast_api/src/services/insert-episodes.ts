import { IncomingMessage } from 'http';

import { StatusCode } from '../utils/status-code';
import { PodcastModel } from '../models/podcast-model';
import { PodcastTransferModel } from '../models/podcast-transfer-model';
import { insertRepoPodcast } from '../repositories/podcasts-repository';

export const serviceGetRequestBody = async (req: IncomingMessage): Promise<JSON[]> => {
  let body: string = await new Promise((resolve, reject) => {
    let chunks: any | Buffer<ArrayBuffer> = [];
    req
      .on('error', (err) => {
        console.log(err);
        reject('');
      })
      .on('data', (chunk) => {
        chunks.push(chunk);
      })
      .on('end', () => {
        chunks = Buffer.concat(chunks).toString();
        resolve(chunks);
      });
  });

  // Tratando corpo do conteúdo
  let jsonArray: JSON[] = JSON.parse(body);

  return jsonArray;
};

export const serviceCreateEpisode = async (jsonArray: JSON[]) => {
  const podcastTest: PodcastModel = {
    podcastName: '',
    episode: '',
    videoId: '',
    categories: [],
  };

  let content: PodcastTransferModel = {
    statusCode: 0,
    body: [],
  };

  // Verificar se é podcast model antes de adicionar
  const podcastkeys = Object.keys(podcastTest);
  jsonArray.map(async (json: any) => {
    const jsonKeys = Object.keys(json);
    let isPodcast = podcastkeys.every((key) => jsonKeys.includes(key));

    if (isPodcast) {
      // Inserindo os dados formatados
      let jsonStr: string = `{
    "podcastName": "${json.podcastName}",
    "episode": "${json.episode}",
    "videoId": "${json.videoId}",
    "categories": [${json.categories.map((category: string) => `"${category}"`)}]
}`;

      let sucess = await insertRepoPodcast(jsonStr);

      if (sucess) {
        content.statusCode = StatusCode.CREATED;
        content.body.push(json);
      } else {
        content = { statusCode: StatusCode.INTERNAL_SERVER_ERROR, body: [] };
      }
    } else {
      content = { statusCode: StatusCode.BAD_REQUEST, body: [] };
    }
  });

  return content;
};
