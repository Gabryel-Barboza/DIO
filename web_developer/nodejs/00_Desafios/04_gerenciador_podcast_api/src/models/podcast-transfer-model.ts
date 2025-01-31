import { PodcastModel } from './podcast-model';

// DTO - Data Transfer Object
export interface PodcastTransferModel {
  statusCode: number;
  body: PodcastModel[];
}
