import http from 'http';

import { getFilterEpisodes, getListEpisodes } from './controllers/podcast-controller';
import { Routes } from './routes/routes';
import { HttpMethod } from './utils/http-methods';

export const app = async (request: http.IncomingMessage, response: http.ServerResponse) => {
  // Request.url = /api/episode
  // Endpoints:
  // http://localhost:3333/api/list
  // http://localhost:3333/api/episode
  // QueryString:
  // http://localhost:3333/api/episode?p=flow

  // Recupera a url e divide a string pelo símbolo ?, se algum vazio após split retorna vazio para um dos valores
  const [baseUrl, queryString] = request.url?.split('?') ?? ['', ''];

  // Rotas - declarados em arquivos únicos para fácil manutenção
  if (request.method === HttpMethod.GET && baseUrl === Routes.LIST)
    // Função do Controller
    await getListEpisodes(request, response);
  else if (request.method === HttpMethod.GET && baseUrl === Routes.EPISODE)
    // Função do Controller
    await getFilterEpisodes(request, response);
};
