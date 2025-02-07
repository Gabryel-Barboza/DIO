import { PlayerModel } from '../models/player-model';
import fs from 'fs/promises';
import path from 'path';

let database: PlayerModel[] = [];
const pathData = path.resolve(__dirname, '../data/players.json');

export const getPlayersRepository = async (): Promise<PlayerModel[]> => {
  const data = await fs.readFile(pathData, 'utf-8');
  if (data.length > 0) database = JSON.parse(data);

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
  try {
    await fs.writeFile(pathData, JSON.stringify(database), 'utf-8');
  } catch (err) {
    return false;
  }

  return true;
};

export const updatePlayerInRepository = async (
  id: number,
  data: any,
  partialUpdate?: boolean
): Promise<boolean> => {
  database = await getPlayersRepository();
  const index = database.findIndex((player) => player.id === id);

  // Atualizar o objeto parcialmente, trocando as propriedades especificadas por data
  if (partialUpdate) {
    let player = database[index];
    Object.keys(player).forEach((pKey) => {
      Object.keys(data).forEach((dKey) => {
        if (dKey === pKey) (player as any)[pKey] = data[dKey];
      });
    });
    database.splice(index, 1, player);
  } else {
    // Atualizar o objeto completamente, trocando o objeto inteiro por data
    database.splice(index, 1, data);
  }

  try {
    await fs.writeFile(pathData, JSON.stringify(database), 'utf-8');
  } catch (err) {
    return false;
  }

  return true;
};

export const deletePlayerInRepository = async (id: number): Promise<boolean> => {
  database = await getPlayersRepository();
  const index = database.findIndex((player) => player.id === id);

  database.splice(index, 1);

  try {
    await fs.writeFile(pathData, JSON.stringify(database), 'utf-8');
  } catch (err) {
    return false;
  }

  return true;
};
