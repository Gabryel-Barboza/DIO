import { PodcastTransferModel } from '../models/podcast-transfer-model';
import { getRepoPodcast } from '../repositories/podcasts-repository';
import { StatusCode } from '../utils/status-code';

export const serviceFilterEpisodes = async (
  url: string | undefined
): Promise<PodcastTransferModel> => {
  const responseFormat: PodcastTransferModel = {
    statusCode: 0,
    body: [],
  };

  const queryString = url?.split('?p=')[1] ?? '';
  const data = await getRepoPodcast(queryString);

  responseFormat.statusCode = data.length > 0 ? StatusCode.OK : StatusCode.NO_CONTENT;
  responseFormat.body = data;

  return responseFormat;
};
