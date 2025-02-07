import { getHTTPResponse } from '../utils/http-helper';
import { HttpResponse } from '../models/http-response-model';
import { getClubsRepository } from '../repositories/club-repository';

export const serviceGetClubs = async (): Promise<HttpResponse> => {
  const data = await getClubsRepository();

  return await getHTTPResponse('OK', data);
};
