// Modelo de podcast, restringe dados do tipo a esse formato
export interface PodcastModel {
  podcastName: string;
  episode: string;
  videoId: string;
  categories: string[];
}
