import { IncomingMessage, ServerResponse } from 'http';

import { serviceListEpisodes } from '../services/list-episodes';
import { serviceFilterEpisodes } from '../services/filter-episodes';
import { ContentType } from '../utils/content-type';
import { PodcastTransferModel } from '../models/podcast-transfer-model';

// Recupera a lista de episódios, retornando uma string json com a resposta
// Trocar números mágicos e textos flutuantes por objetos auxilia na legibilidade
export const getListEpisodes = async (req: IncomingMessage, res: ServerResponse) => {
  const content: PodcastTransferModel = await serviceListEpisodes();

  res.writeHead(content.statusCode, { 'content-type': ContentType.JSON });
  res.write(JSON.stringify(content.body));
  res.end();
};

// Recupera uma lista filtrada de episódios, retornando uma string json com a resposta
export const getFilterEpisodes = async (req: IncomingMessage, res: ServerResponse) => {
  const content: PodcastTransferModel = await serviceFilterEpisodes(req.url);

  res.writeHead(content.statusCode, { 'content-type': ContentType.JSON });
  res.end(JSON.stringify(content.body));
};
