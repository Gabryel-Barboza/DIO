import { HttpResponse } from '../models/http-response-model';
import { getHTTPResponse } from '../utils/http-helper';
import {
  getPlayerById,
  getPlayersRepository,
  insertPlayerInRepository,
  updatePlayerInRepository,
  deletePlayerInRepository,
} from '../repositories/player-repository';

// Recupera a lista de jogadores do repositório
export const serviceGetPlayers = async (): Promise<HttpResponse> => {
  const data = await getPlayersRepository();
  let response = null;

  if (data.length > 0) response = await getHTTPResponse('OK', data);
  else response = await getHTTPResponse('NO_CONTENT', data);

  return response;
};

// Recupera um jogador específico do repositório
export const serviceGetPlayer = async (id: number): Promise<HttpResponse> => {
  const data = await getPlayerById(id);

  if (data) return await getHTTPResponse('OK', data);

  return await getHTTPResponse('NOT_FOUND', data);
};

// Cria um jogador no repositório
export const serviceCreatePlayer = async (json: any): Promise<HttpResponse> => {
  let response = null;

  try {
    if (Object.keys(json).length === 0) throw new Error('Invalid data received');

    let player = json;
    const success = await insertPlayerInRepository(player);

    if (success) response = await getHTTPResponse('CREATED', player);
    else response = await getHTTPResponse('INTERNAL_SERVER_ERROR', []);
  } catch (err) {
    if (err instanceof Error) response = await getHTTPResponse('BAD_REQUEST', err.message);
    else response = await getHTTPResponse('INTERNAL_SERVER_ERROR', 'Unknown error');
  }

  return response;
};

// Atualiza um jogador, parcialmente ou completamente, no repositório
export const serviceUpdatePlayer = async (
  id: number,
  json: any,
  partialUpdate?: boolean
): Promise<HttpResponse> => {
  const player = await getPlayerById(id);

  if (!player) return await getHTTPResponse('NOT_FOUND', player);

  let response = null;

  const success = await updatePlayerInRepository(id, json, partialUpdate);
  response = await getHTTPResponse('OK', success);

  return response;
};

// Deleta um jogador do repositório
export const serviceDeletePlayer = async (id: number): Promise<HttpResponse> => {
  const player = await getPlayerById(id);

  if (!player) return await getHTTPResponse('NOT_FOUND', player);

  const success = await deletePlayerInRepository(id);

  if (!success) return await getHTTPResponse('INTERNAL_SERVER_ERROR', []);

  return await getHTTPResponse('OK', success);
};
