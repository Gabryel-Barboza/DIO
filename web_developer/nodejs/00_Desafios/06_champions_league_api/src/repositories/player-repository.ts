import { PlayerModel } from '../models/player-model';
import fs from 'fs/promises';
import path from 'path';

let database: PlayerModel[];
const pathData = path.resolve(__dirname, '../data/players.json');

export const getPlayersRepository = async (): Promise<PlayerModel[]> => {
  const data = await fs.readFile(pathData, 'utf-8');
  database = JSON.parse(data);
  return database;
};

export const getPlayerById = async (id: number): Promise<PlayerModel | undefined> => {
  database = await getPlayersRepository();
  return database.find((player) => player.id === id);
};

export const insertPlayerInRepository = async (player: PlayerModel): Promise<boolean> => {
  database.push(player);

  return true;
};

export const updatePlayerInRepository = async (
  id: number,
  data: any,
  partialUpdate?: boolean
): Promise<Object | undefined> => {
  const index = database.findIndex((player) => player.id === id);

  if (partialUpdate) {
    let player = database[index];
  } else {
    database.splice(index, 1, data);
  }

  return { message: 'Player updated successfully' };
};

export const deletePlayerInRepository = async (id: number): Promise<Object | undefined> => {
  const index = database.findIndex((player) => player.id === id);

  database.splice(index, 1);

  return { message: 'Player deleted successfully' };
};
