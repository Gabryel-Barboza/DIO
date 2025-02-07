import { ClubModel } from '../models/club-model';
import fs from 'fs/promises';
import path from 'path';

let database: ClubModel[];
const pathData = path.resolve(__dirname, '../data/clubs.json');

export const getClubsRepository = async (): Promise<ClubModel[] | undefined> => {
  const data = await fs.readFile(pathData, 'utf-8');
  database = JSON.parse(data);

  return database;
};
