# Champions League API com Express

Uma API para controlar o registro de jogadores e clubs da Champions League. <br>
Foi implementada com as operações básicas de um sistema CRUD, seguindo um modelo de arquitetura N-layers.

<div style="max-width: 400px; max-height: 300px; margin: 10px auto;">
  <img alt="GIF de um jogador da Champions League" src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGsydzBvbjh0bTQ0bm9yenRhaHhpYXFkM3E5bGtvM3Z3Z2V2MjdzbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9oRLF9WCYHhkY/giphy.gif" />
</div>

## Features

As funcionalidades da API separadas por tipo de objeto.

<div style="max-width: 300px; max-height: 300px;">
  <img alt="GIF de um jogador de futebol animado" src="https://media.giphy.com/media/l2SqbkmCEv70lavCg/giphy.gif?cid=790b7611c6z6qk9kai1j3ch8grpzy655oyq0dql6fhns4ipe&ep=v1_gifs_search&rid=giphy.gif&ct=g"  />
</div>
<br>

- **Players (Jogadores)**
  - Recuperar lista de jogadores
  - Recuperar jogador por ID
  - Inserir novo jogador
  - Atualizar registro de jogador
  - Atualizar parcialmente o registro de jogador
  - Deletar jogador
- **Clubs**
  - Recuperar lista de clubs
  - Recuperar club por ID
  - Inserir novo club
  - Atualizar registro de club
  - Atualizar parcialmente o registro de club
  - Deletar um club

![Captura de tela de 2025-02-06 23-55-25](https://github.com/user-attachments/assets/331cf956-da69-4454-86c5-5f218383017d)

Os dados são armazenados em um repositório de arquivos JSON para cada tipo de objeto.

## Implementação

O jogador é criado ou atualizado seguindo o modelo: <br>
![player-model-api](https://github.com/user-attachments/assets/750ae3b7-ce9c-4e5c-9fc8-68964fdd0148)
<br>

O club é criado ou atualizado seguindo o modelo: <br>
![club-model-api](https://github.com/user-attachments/assets/d63e1da1-cc90-4ae3-b8ff-9927ce68d12d)
<br>

As requisições suportam apenas o formato JSON. <br>

A arquitetura do projeto é a seguinte: <br>
![Captura de tela de 2025-02-07 00-07-11](https://github.com/user-attachments/assets/b000d7f0-cd69-47b5-96a2-a893be8fdc29)

<br>

O arquivo `.env` armazena a configuração da porta.

## Endpoints

Os endpoints para manipular jogadores: <br>
![endpoints-player](https://github.com/user-attachments/assets/63c9eb1f-ea8a-4f21-b149-4aa764f25ccd)

<br>

Os endpoints para manipular clubs: <br>
[img clubs]
<br>

## Como utilizar

Faça o clone do projeto e entre um terminal dentro da pasta "06_champions_league_api", insira o comando `npm install`. <br>
Inicialize o servidor com `npm run start` e faça as requisições a um endpoint, com softwares como Postman, Insomnia ou a extensão ThunderClient.
