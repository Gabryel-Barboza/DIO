import { Request, Response } from 'express';
import {
  serviceGetClubs,
  serviceGetClub,
  serviceCreateClub,
  serviceUpdateClub,
  serviceDeleteClub,
} from '../services/clubs-service';

export const getClubs = async (req: Request, res: Response) => {
  const response = await serviceGetClubs();

  res.status(response.statusCode).json(response.body);
};

export const getClub = async (req: Request, res: Response) => {
  const id = parseInt(req.params.id);
  const response = await serviceGetClub(id);

  res.status(response.statusCode).json(response.body);
};

export const createClub = async (req: Request, res: Response) => {
  const data = req.body;
  const response = await serviceCreateClub(data);

  res.status(response.statusCode).json(response.body);
};

export const updateClub = async (req: Request, res: Response) => {
  const id = parseInt(req.params.id);
  const data = req.body;
  const response = await serviceUpdateClub(id, data);

  res.status(response.statusCode).json(response.body);
};

export const partialUpdateClub = async (req: Request, res: Response) => {
  const id = parseInt(req.params.id);
  const data = req.body;
  const response = await serviceUpdateClub(id, data, true);

  res.status(response.statusCode).json(response.body);
};

export const deleteClub = async (req: Request, res: Response) => {
  const id = parseInt(req.params.id);
  const response = await serviceDeleteClub(id);

  res.status(response.statusCode).json(response.body);
};
