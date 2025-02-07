import { Request, Response } from 'express';

import {
  serviceGetPlayers,
  serviceGetPlayer,
  serviceCreatePlayer,
  serviceUpdatePlayer,
  serviceDeletePlayer,
} from '../services/players-service';

export const getPlayers = async (req: Request, res: Response) => {
  const response = await serviceGetPlayers();
  res.status(response.statusCode).json(response.body);
};

export const getPlayer = async (req: Request, res: Response) => {
  const id = parseInt(req.params.id);
  const response = await serviceGetPlayer(id);

  res.status(response.statusCode).json(response.body);
};

export const createPlayer = async (req: Request, res: Response) => {
  const data = req.body;
  const response = await serviceCreatePlayer(data);

  res.status(response.statusCode).json(response.body);
};

export const updatePlayer = async (req: Request, res: Response) => {
  const id = parseInt(req.params.id);
  const data = req.body;
  const response = await serviceUpdatePlayer(id, data);

  res.status(response.statusCode).json(response.body);
};

export const partialUpdatePlayer = async (req: Request, res: Response) => {
  const id = parseInt(req.params.id);
  const data = req.body;
  const response = await serviceUpdatePlayer(id, data, true);

  res.status(response.statusCode).json(response.body);
};

export const deletePlayer = async (req: Request, res: Response) => {
  const id = parseInt(req.params.id);
  const response = await serviceDeletePlayer(id);

  res.status(response.statusCode).json(response.body);
};
