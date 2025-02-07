import { HttpResponse } from '../models/http-response-model';
import { getHTTPResponse } from '../utils/http-helper';
import {
  getPlayerById,
  getPlayersRepository,
  insertPlayerInRepository,
  updatePlayerInRepository,
  deletePlayerInRepository,
} from '../repositories/player-repository';
import { PlayerModel } from '../models/player-model';

// Recupera a lista de jogadores do repositório
export const serviceGetPlayers = async (): Promise<HttpResponse> => {
  const data = await getPlayersRepository();

  if (data.length > 0) return await getHTTPResponse('OK', data);

  return await getHTTPResponse('NO_CONTENT', []);
};

// Recupera um jogador específico do repositório
export const serviceGetPlayer = async (id: number): Promise<HttpResponse> => {
  const data = await getPlayerById(id);

  if (data) return await getHTTPResponse('OK', data);

  return await getHTTPResponse('NOT_FOUND', []);
};

// Cria um jogador no repositório
export const serviceCreatePlayer = async (json: any): Promise<HttpResponse> => {
  let response = null;
  const lastIndex = (await getPlayersRepository()).length;

  try {
    // Verificar se o objeto é do tipo PlayerModel
    if (await checkIsPlayerModel(json)) {
      if ('id' in json) delete json.id; // ID é adicionado automaticamente

      const player: PlayerModel = { id: lastIndex + 1, ...json };
      const success = await insertPlayerInRepository(player);

      if (success) response = await getHTTPResponse('CREATED', player);
      else response = await getHTTPResponse('INTERNAL_SERVER_ERROR', []);
    } else {
      throw new Error('Invalid data received');
    }
  } catch (err) {
    if (err instanceof Error) response = await getHTTPResponse('BAD_REQUEST', err.message);
    else response = await getHTTPResponse('INTERNAL_SERVER_ERROR', []);
  }

  return response;
};

// Atualiza um jogador, parcialmente ou completamente, no repositório
export const serviceUpdatePlayer = async (
  id: number,
  json: any,
  partialUpdate: boolean = false
): Promise<HttpResponse> => {
  const player = await getPlayerById(id);
  let success: boolean = false;
  let isPlayerModel: boolean = false;

  if (!player) return await getHTTPResponse('NOT_FOUND', []);

  if ('id' in json) json.id = player.id; // ID não pode ser atualizado

  // Se atualização parcial, verificação parcial do modelo
  if (partialUpdate) isPlayerModel = await checkIsPlayerModel(json, partialUpdate);
  else isPlayerModel = await checkIsPlayerModel(json);

  if (isPlayerModel) {
    // Se atualização deve ser parcial ou não
    success = partialUpdate
      ? await updatePlayerInRepository(id, json, partialUpdate)
      : await updatePlayerInRepository(id, json);
  } else return await getHTTPResponse('BAD_REQUEST', { message: 'Invalid data received' });

  if (success) return await getHTTPResponse('OK', { message: 'Player updated successfully' });
  else return await getHTTPResponse('INTERNAL_SERVER_ERROR', []);
};

// Deleta um jogador do repositório
export const serviceDeletePlayer = async (id: number): Promise<HttpResponse> => {
  const player = await getPlayerById(id);

  if (!player) return await getHTTPResponse('NOT_FOUND', []);

  const success = await deletePlayerInRepository(id);

  if (!success) return await getHTTPResponse('INTERNAL_SERVER_ERROR', []);

  return await getHTTPResponse('OK', { message: 'Player deleted successfully' });
};

const checkIsPlayerModel = async (json: any, partialUpdate?: boolean): Promise<boolean> => {
  if (Object.keys(json).length === 0) return false;

  const playerModel: PlayerModel = {
    id: 0,
    name: '',
    club: '',
    nationality: '',
    position: '',
    statistics: {
      Overall: 0,
      Pace: 0,
      Shooting: 0,
      Passing: 0,
      Dribbling: 0,
      Defending: 0,
      Physical: 0,
    },
  };

  const jsonKeys = Object.keys(json);
  const playerKeys = Object.keys(playerModel);

  // Se atualização parcial, as chaves de JSON devem estar no PlayerModel
  if (partialUpdate) {
    return jsonKeys.every((key) => playerKeys.includes(key));
  } else if (playerKeys.every((key) => jsonKeys.includes(key))) {
    // Se atualização completa, todas as chaves de PlayerModel, devem estar em json. E as chaves de statistics também são verificadas
    if ('statistics' in json) {
      const playerStatsKeys = Object.keys(playerModel.statistics);
      const jsonStatsKeys = Object.keys(json.statistics);
      const hasStatsKeys = playerStatsKeys.every((key) => jsonStatsKeys.includes(key));

      return hasStatsKeys;
    }
  }

  return false;
};
