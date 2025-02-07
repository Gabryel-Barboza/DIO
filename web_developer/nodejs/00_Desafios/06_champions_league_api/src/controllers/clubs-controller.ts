import { Request, Response } from 'express';
import { serviceGetClubs } from '../services/clubs-service';

export const getClubs = async (req: Request, res: Response) => {
  const response = await serviceGetClubs();

  res.status(response.statusCode).json(response.body);
};
