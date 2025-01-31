# Nome do Aplicativo
Gerenciador de Podcasts.

## Descrição
App para gerenciamento de podcast em um catálogo, disponibilizando episódios separados por categorias.

## Domínio
Podcasts em vídeo.

## Features
- Listar episódios de podcasts em sessões categorizadas
  - [saúde, games, tecnologia, fitness, humor, mentalidade]
- Filtrar episódios por canal de podcast

## How-to

### Feature
- Listar episódios de podcasts em sessões categorizadas

### Implementação
Retornar em API REST (json) o nome do canal, título episódio, capa de imagem e link
```js
[
  {
    podcastName: "Curso em Video",
    episode: "DO FUNDÃO À LIDERANÇA EM TECNOLOGIAS EMERGENTES - Experience Podcast 37 - Lucas Oliveira",
    videoId: "Ql6eD-wUmhw",
    thumbnail: "https://i.ytimg.com/vi/Ql6eD-wUmhw/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLB4SGbNY98IdFAmKeeba19laF3AhQ",
    link: "https://www.youtube.com/watch?v=Ql6eD-wUmhw",
    categories: ['tecnologia', 'mentalidade']
  }
]
```
Padrão de url identificado nas thumbs: dominio/videoid/resolucao?parametro-opcional
maxresdefault.jpg ou hqdefault.jpg