import { getHTTPResponse } from '../utils/http-helper';
import { HttpResponse } from '../models/http-response-model';
import {
  getClubsRepository,
  getClubById,
  insertClubInRepository,
  updateClubInRepository,
  deleteClubInRepository,
} from '../repositories/club-repository';
import { ClubModel } from '../models/club-model';

export const serviceGetClubs = async (): Promise<HttpResponse> => {
  const data = await getClubsRepository();

  if (data.length > 0) return await getHTTPResponse('OK', data);

  return await getHTTPResponse('NO_CONTENT', data);
};

export const serviceGetClub = async (id: number): Promise<HttpResponse> => {
  const data = await getClubById(id);

  if (data) return await getHTTPResponse('OK', data);

  return await getHTTPResponse('NOT_FOUND', data);
};

export const serviceCreateClub = async (json: any): Promise<HttpResponse> => {
  let response = null;
  let lastIndex = (await getClubsRepository()).length;

  try {
    if (await checkIsClubModel(json)) {
      if ('id' in json) delete json.id;

      const club: ClubModel = { id: lastIndex + 1, ...json };
      const success = await insertClubInRepository(club);

      if (success) response = await getHTTPResponse('CREATED', club);
      else response = await getHTTPResponse('INTERNAL_SERVER_ERROR', []);
    } else {
      throw new Error('Invalid data received.');
    }
  } catch (err) {
    if (err instanceof Error) response = getHTTPResponse('BAD_REQUEST', { message: err.message });
    else response = getHTTPResponse('INTERNAL_SERVER_ERROR', 'Unknown error');
  }

  return response;
};

export const serviceUpdateClub = async (
  id: number,
  data: any,
  partialUpdate: boolean = false
): Promise<HttpResponse> => {
  const club = await getClubById(id);
  let isClubModel: boolean = false;
  let success: boolean = false;

  if (!club) return await getHTTPResponse('NOT_FOUND', club);

  if ('id' in data) data.id = club.id;

  if (partialUpdate) isClubModel = await checkIsClubModel(data, partialUpdate);
  else isClubModel = await checkIsClubModel(data);

  if (isClubModel) {
    success = partialUpdate
      ? await updateClubInRepository(id, data, partialUpdate)
      : await updateClubInRepository(id, data);
  } else return await getHTTPResponse('BAD_REQUEST', { message: 'Invalid data received' });

  if (success) return await getHTTPResponse('OK', { message: 'Club updated successfully' });
  else return await getHTTPResponse('INTERNAL_SERVER_ERROR', []);
};

export const serviceDeleteClub = async (id: number): Promise<HttpResponse> => {
  const club = getClubById(id);

  if (!club) return await getHTTPResponse('NOT_FOUND', []);

  const success = await deleteClubInRepository(id);

  if (!success) return await getHTTPResponse('INTERNAL_SERVER_ERROR', []);

  return await getHTTPResponse('OK', { message: 'Club deleted successfully' });
};

const checkIsClubModel = async (json: any, partialUpdate?: boolean): Promise<boolean> => {
  if (Object.keys(json).length === 0) return false;

  const clubModel: ClubModel = {
    id: 0,
    name: '',
    country: '',
    foundation: 0,
    president: '',
    website: '',
    image: '',
  };

  const clubKeys = Object.keys(clubModel);
  const jsonKeys = Object.keys(json);

  if (partialUpdate) return jsonKeys.every((key) => clubKeys.includes(key));
  else return clubKeys.every((key) => jsonKeys.includes(key));
};
