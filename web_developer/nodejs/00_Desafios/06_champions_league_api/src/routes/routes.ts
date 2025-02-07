import { Router } from 'express';
import {
  getPlayers,
  getPlayer,
  createPlayer,
  updatePlayer,
  partialUpdatePlayer,
  deletePlayer,
} from '../controllers/players-controller';
import { getClubs } from '../controllers/clubs-controller';

const router = Router(); // Instanciando o gerenciador de rotas

// Criando rotas de métodos HTTP
router.get('/players', getPlayers); // Rota para listar todos os jogadores
router.get('/players/:id', getPlayer); // Rota para listar um jogador específico, utiliza Route Params
router.post('/players', createPlayer);
router.put('/players/:id', updatePlayer);
router.patch('/players/:id', partialUpdatePlayer);
router.delete('/players/:id', deletePlayer);

router.get('/clubs', getClubs);

export default router;
