import http from 'http';
// Organização de importes -> import terceiros - import local
import {
  getFilterEpisodes,
  getListEpisodes,
  getNewEpisode,
} from './controllers/podcast-controller';
import { Routes } from './routes/routes';
import { HttpMethod } from './utils/http-methods';

// App recebe as requisições e gerencia as rotas
export const app = async (request: http.IncomingMessage, response: http.ServerResponse) => {
  // Request.url == /api/episode
  // Endpoints:
  // http://localhost:3333/api/list
  // http://localhost:3333/api/episode
  // QueryString:
  // http://localhost:3333/api/episode?p=flow

  // Operador ?? - se o operando da esquerda undefined recebe o operando da direita
  // Recupera a url e divide a string pelo símbolo ?, se algum vazio após split retorna vazio para um dos valores
  const [baseUrl, queryString] = request.url?.split('?') ?? ['', ''];

  // Rotas - declarações em arquivos únicos para fácil manutenção, ctrl + click HttpMethod ou Routes
  if (request.method === HttpMethod.GET && baseUrl === Routes.LIST)
    // Função do Controller
    await getListEpisodes(request, response);
  else if (request.method === HttpMethod.GET && baseUrl === Routes.EPISODE)
    await getFilterEpisodes(request, response);
  else if (request.method === HttpMethod.POST && baseUrl === Routes.EPISODE)
    await getNewEpisode(request, response);
};
