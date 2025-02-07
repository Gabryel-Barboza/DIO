import { Router } from 'express';
import {
  getPlayers,
  getPlayer,
  createPlayer,
  updatePlayer,
  partialUpdatePlayer,
  deletePlayer,
} from '../controllers/players-controller';
import {
  getClubs,
  getClub,
  createClub,
  updateClub,
  partialUpdateClub,
  deleteClub,
} from '../controllers/clubs-controller';

const router = Router(); // Instanciando o gerenciador de rotas

// Criando rotas de métodos HTTP
// Rotas para manipulação de jogadores
router.get('/players', getPlayers); // Rota para listar todos os jogadores
router.get('/players/:id', getPlayer); // Rota para listar um jogador específico, utiliza Route Params
router.post('/players', createPlayer); // Rota para criar um novo jogador
router.put('/players/:id', updatePlayer); // Rota para atualizar um jogador
router.patch('/players/:id', partialUpdatePlayer); // Rota para atualizar parcialmente um jogador
router.delete('/players/:id', deletePlayer); // Rota para excluir um jogador

// Rotas para manipulação de clubes
router.get('/clubs', getClubs);
router.get('/clubs/:id', getClub);
router.post('/clubs', createClub);
router.put('/clubs/:id', updateClub);
router.patch('/clubs/:id', partialUpdateClub);
router.delete('/clubs/:id', deleteClub);

export default router;
