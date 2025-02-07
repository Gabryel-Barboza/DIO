import { PlayerModel } from '../models/player-model';

const database: PlayerModel[] = [
  {
    id: 1,
    name: 'Lionel Messi',
    club: 'Paris Saint-Germain',
    nationality: 'Argentinian',
    position: 'Forward',
    statistics: {
      Overall: 93,
      Pace: 85,
      Shooting: 94,
      Passing: 91,
      Dribbling: 95,
      Defending: 38,
      Physical: 65,
    },
  },
  {
    id: 2,
    name: 'Cristiano Ronaldo',
    club: 'Manchester United',
    nationality: 'Portuguese',
    position: 'Forward',
    statistics: {
      Overall: 91,
      Pace: 87,
      Shooting: 93,
      Passing: 82,
      Dribbling: 88,
      Defending: 35,
      Physical: 77,
    },
  },
  {
    id: 3,
    name: 'Neymar Jr',
    club: 'Paris Saint-Germain',
    nationality: 'Brazilian',
    position: 'Forward',
    statistics: {
      Overall: 91,
      Pace: 91,
      Shooting: 85,
      Passing: 86,
      Dribbling: 94,
      Defending: 32,
      Physical: 60,
    },
  },
  {
    id: 4,
    name: 'Kevin De Bruyne',
    club: 'Manchester City',
    nationality: 'Belgian',
    position: 'Midfielder',
    statistics: {
      Overall: 91,
      Pace: 76,
      Shooting: 86,
      Passing: 93,
      Dribbling: 88,
      Defending: 64,
      Physical: 78,
    },
  },
  {
    id: 5,
    name: 'Robert Lewandowski',
    club: 'Bayern Munich',
    nationality: 'Polish',
    position: 'Forward',
    statistics: {
      Overall: 92,
      Pace: 78,
      Shooting: 92,
      Passing: 79,
      Dribbling: 86,
      Defending: 44,
      Physical: 82,
    },
  },
  {
    id: 6,
    name: 'Kylian Mbappe',
    club: 'Paris Saint-Germain',
    nationality: 'French',
    position: 'Forward',
    statistics: {
      Overall: 91,
      Pace: 97,
      Shooting: 88,
      Passing: 80,
      Dribbling: 92,
      Defending: 36,
      Physical: 76,
    },
  },
  {
    id: 7,
    name: 'Virgil van Dijk',
    club: 'Liverpool',
    nationality: 'Dutch',
    position: 'Defender',
    statistics: {
      Overall: 90,
      Pace: 76,
      Shooting: 60,
      Passing: 71,
      Dribbling: 72,
      Defending: 91,
      Physical: 86,
    },
  },
  {
    id: 8,
    name: 'Mohamed Salah',
    club: 'Liverpool',
    nationality: 'Egyptian',
    position: 'Forward',
    statistics: {
      Overall: 90,
      Pace: 93,
      Shooting: 87,
      Passing: 81,
      Dribbling: 90,
      Defending: 45,
      Physical: 75,
    },
  },
  {
    id: 9,
    name: 'Sadio Mane',
    club: 'Liverpool',
    nationality: 'Senegalese',
    position: 'Forward',
    statistics: {
      Overall: 89,
      Pace: 94,
      Shooting: 83,
      Passing: 80,
      Dribbling: 88,
      Defending: 44,
      Physical: 76,
    },
  },
  {
    id: 10,
    name: 'Luka Modric',
    club: 'Real Madrid',
    nationality: 'Croatian',
    position: 'Midfielder',
    statistics: {
      Overall: 89,
      Pace: 74,
      Shooting: 76,
      Passing: 89,
      Dribbling: 90,
      Defending: 72,
      Physical: 67,
    },
  },
];

export const getPlayersRepository = async (): Promise<PlayerModel[]> => {
  return database;
};

export const getPlayerById = async (id: number): Promise<PlayerModel | undefined> => {
  return database.find((player) => player.id === id);
};

export const insertPlayerInRepository = async (player: PlayerModel): Promise<boolean> => {
  database.push(player);

  return true;
};

export const updatePlayerInRepository = async (
  id: number,
  data: any,
  partialUpdate?: boolean
): Promise<Object | undefined> => {
  const index = database.findIndex((player) => player.id === id);

  if (partialUpdate) {
    let player = database[index];
    
  } else {
    database.splice(index, 1, data);
  }

  return { message: 'Player updated successfully' };
};

export const deletePlayerInRepository = async (id: number): Promise<Object | undefined> => {
  const index = database.findIndex((player) => player.id === id);

  database.splice(index, 1);

  return { message: 'Player deleted successfully' };
};
