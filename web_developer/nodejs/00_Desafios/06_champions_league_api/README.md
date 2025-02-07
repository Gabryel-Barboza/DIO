# Champions League API com Express ⚽

Uma API para controlar o registro de jogadores e clubs da Champions League. Desenvolvida durante o curso de Node.Js e amplamente aprimorada com novas funcionalidades. <br>
Foi implementada com as operações básicas de um sistema CRUD, seguindo um modelo de arquitetura N-layers.

<div style="max-width: 400px; max-height: 300px; margin: 10px auto;">
  <img width="400px" height="300px" alt="GIF de um jogador da Champions League" src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGsydzBvbjh0bTQ0bm9yenRhaHhpYXFkM3E5bGtvM3Z3Z2V2MjdzbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9oRLF9WCYHhkY/giphy.gif" />
</div>

## Features 💡

As funcionalidades da API separadas por tipo de objeto.

<div style="max-width: 300px; max-height: 300px;">
  <img width="300px" height="300px" alt="GIF de um jogador de futebol animado" src="https://media.giphy.com/media/l2SqbkmCEv70lavCg/giphy.gif?cid=790b7611c6z6qk9kai1j3ch8grpzy655oyq0dql6fhns4ipe&ep=v1_gifs_search&rid=giphy.gif&ct=g"  />
</div>
<br>

### Players (Jogadores) ⛹‍️‍♂️
  - Recuperar lista de jogadores  --> **GET**
  - Recuperar jogador por ID  --> **GET**
  - Inserir novo jogador  --> **POST**
  - Atualizar registro de jogador  --> **PUT**
  - Atualizar parcialmente o registro de um jogador  --> **PATCH**
  - Deletar um jogador  --> **DELETE**
### Clubs 👥
  - Recuperar lista de clubs  --> **GET**
  - Recuperar club por ID  --> **GET**
  - Inserir novo club  --> **POST**
  - Atualizar registro de club  --> **PUT**
  - Atualizar parcialmente o registro de um club  --> **PATCH**
  - Deletar um club  --> **DELETE**
 
Um exemplo de requisições utilizando o ThunderClient:
<br><br>

<img width="200px" height="400px" alt="Requisições no ThunderClient" src="https://github.com/user-attachments/assets/331cf956-da69-4454-86c5-5f218383017d" />

<hr>
Um modelo de requisição com método POST, só é aceito se atender a todos os requisitos de um modelo de jogador. As requisições suportam apenas o formato JSON.
<br><br>
<img height="300px" src="https://github.com/user-attachments/assets/7d720db6-fcbd-4dc1-8052-ee8b88df7c66" />

Os dados são armazenados em um repositório de arquivos JSON para cada tipo de objeto. Esse JSON é reescrito para guardar novos registros de objetos. <br>

**TODO**: Impedir a alteração do atributo estatísticas com método PATCH caso o objeto esteja incompleto, igual aos outros métodos. 

## Implementação  ⚙️

O ID é atribuído dinamicamente, não sendo possível defini-lo ou altera-lo com qualquer requisição, a requisição é aceita mas o ID permanece dinâmico. 
O jogador é criado ou atualizado seguindo o modelo. <br>
<br><br>

<img width="300px" height="300px" src="https://github.com/user-attachments/assets/750ae3b7-ce9c-4e5c-9fc8-68964fdd0148" />
<br>

O club é criado ou atualizado seguindo o modelo: 
<br><br>
<img width="300px" height="300px" src="https://github.com/user-attachments/assets/d63e1da1-cc90-4ae3-b8ff-9927ce68d12d" />
<br>

A arquitetura do projeto é a seguinte: 
<br><br>
<img width="300px" height="300px" src="https://github.com/user-attachments/assets/b000d7f0-cd69-47b5-96a2-a893be8fdc29"/>

<br>

O arquivo `.env` armazena a configuração da porta.

## Endpoints 🔚

Os endpoints para manipular jogadores: 
<br><br>
<img width="400px" height="300px" src="https://github.com/user-attachments/assets/63c9eb1f-ea8a-4f21-b149-4aa764f25ccd"/>

<br>

Os endpoints para manipular clubs: 
<br><br>
[img clubs]
<br>

## Como utilizar 📔

Faça o clone do projeto e entre um terminal dentro da pasta "06_champions_league_api", insira o comando `npm install`. <br>
Inicialize o servidor com `npm run start` e faça as requisições a um endpoint, utilizando softwares como Postman, Insomnia ou a extensão ThunderClient.
