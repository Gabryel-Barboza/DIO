import { Request, Response } from 'express';

import {
  serviceGetPlayers,
  serviceGetPlayer,
  serviceCreatePlayer,
  serviceUpdatePlayer,
  serviceDeletePlayer,
} from '../services/players-service';

// Retorna uma resposta com a lista de jogadores
export const getPlayers = async (req: Request, res: Response) => {
  const response = await serviceGetPlayers();
  res.status(response.statusCode).json(response.body);
};

// Retorna uma resposta com um jogador específico
export const getPlayer = async (req: Request, res: Response) => {
  const id = parseInt(req.params.id);
  const response = await serviceGetPlayer(id);

  res.status(response.statusCode).json(response.body);
};

// Cria um jogador e retorna uma resposta
export const createPlayer = async (req: Request, res: Response) => {
  const data = req.body;
  const response = await serviceCreatePlayer(data);

  res.status(response.statusCode).json(response.body);
};

// Atualiza um jogador e retorna uma resposta
export const updatePlayer = async (req: Request, res: Response) => {
  const id = parseInt(req.params.id);
  const data = req.body;
  const response = await serviceUpdatePlayer(id, data);

  res.status(response.statusCode).json(response.body);
};

// Atualiza parcialmente um jogador e retorna uma resposta
export const partialUpdatePlayer = async (req: Request, res: Response) => {
  const id = parseInt(req.params.id);
  const data = req.body;
  const response = await serviceUpdatePlayer(id, data, true);

  res.status(response.statusCode).json(response.body);
};

// Deleta um jogador e retorna uma resposta
export const deletePlayer = async (req: Request, res: Response) => {
  const id = parseInt(req.params.id);
  const response = await serviceDeletePlayer(id);

  res.status(response.statusCode).json(response.body);
};
