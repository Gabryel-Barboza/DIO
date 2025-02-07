import { PlayerModel } from '../models/player-model';
import fs from 'fs/promises';
import path from 'path';

let database: PlayerModel[] = [];
const pathData = path.resolve(__dirname, '../data/players.json');

export const getPlayersRepository = async (): Promise<PlayerModel[]> => {
  try {
    const data = await fs.readFile(pathData, 'utf-8');
    if (data.length > 0) database = JSON.parse(data);
  } catch (err) {
    console.log('Erro na leitura do arquivo JSON ');
  }

  return database;
};

export const getPlayerById = async (id: number): Promise<PlayerModel | undefined> => {
  database = await getPlayersRepository();

  return database.find((player) => player.id === id);
};

export const insertPlayerInRepository = async (player: PlayerModel): Promise<boolean> => {
  database = await getPlayersRepository();
  database.push(player);

  // Salvar o novo array no arquivo JSON
  const success = await writeJSON(database);

  return success;
};

export const updatePlayerInRepository = async (
  id: number,
  data: any,
  partialUpdate?: boolean
): Promise<boolean> => {
  database = await getPlayersRepository();
  const index = database.findIndex((player) => player.id === id);

  // Atualizar o objeto parcialmente, trocando as propriedades especificadas por propriedades de data
  if (partialUpdate) {
    let player = database[index];
    const playerKeys = Object.keys(player);
    const dataKeys = Object.keys(data);

    playerKeys.forEach((pKey) => {
      dataKeys.forEach((dKey) => {
        if (dKey === pKey) {
          (player as any)[pKey] = data[dKey];
        }
      });
    });

    database.splice(index, 1, player);
  } else {
    // Atualizar o objeto completamente, trocando o objeto inteiro por data
    database.splice(index, 1, data);
  }

  const success = await writeJSON(database);

  return success;
};

export const deletePlayerInRepository = async (id: number): Promise<boolean> => {
  database = await getPlayersRepository();
  const index = database.findIndex((player) => player.id === id);

  database.splice(index, 1);

  const success = await writeJSON(database);

  return success;
};

const writeJSON = async (database: PlayerModel[]) => {
  try {
    await fs.writeFile(pathData, JSON.stringify(database), 'utf-8');
  } catch (err) {
    return false;
  }

  return true;
};
