import { ClubModel } from '../models/club-model';
import fs from 'fs/promises';
import path from 'path';

let database: ClubModel[] = [];
const pathData = path.resolve(__dirname, '../data/clubs.json');

export const getClubsRepository = async (): Promise<ClubModel[]> => {
  try {
    const data = await fs.readFile(pathData, 'utf-8');
    if (data.length > 0) database = JSON.parse(data);
  } catch (err) {
    console.log('Erro na leitura do arquivo JSON de clubs')
  }

  return database;
};

export const getClubById = async (id: number): Promise<ClubModel | undefined> => {
  database = await getClubsRepository();

  return database.find((club) => club.id === id);
};

export const insertClubInRepository = async (club: ClubModel): Promise<boolean> => {
  database = await getClubsRepository();
  database.push(club);

  const success = await writeJSON(database);

  return success;
};

export const updateClubInRepository = async (
  id: number,
  data: any,
  partialUpdate?: boolean
): Promise<boolean> => {
  database = await getClubsRepository();
  const index = database.findIndex((club) => club.id === id);

  if (partialUpdate) {
    let club = database[index];
    const dataKeys = Object.keys(data);
    const clubKeys = Object.keys(club);

    clubKeys.forEach((cKeys) => {
      dataKeys.forEach((dKeys) => {
        if (dKeys === cKeys) {
          (club as any)[cKeys] = data[dKeys];
        }
      });
    });

    database.splice(index, 1, club);
  } else {
    database.splice(index, 1, data);
  }

  const success = await writeJSON(database);

  return success;
};

export const deleteClubInRepository = async (id: number): Promise<boolean> => {
  database = await getClubsRepository();
  const index = database.findIndex((club) => club.id === id);

  database.splice(index, 1);
  const success = await writeJSON(database);

  return success;
};

const writeJSON = async (database: ClubModel[]) => {
  try {
    await fs.writeFile(pathData, JSON.stringify(database), 'utf-8');
  } catch (err) {
    return false;
  }

  return true;
};
