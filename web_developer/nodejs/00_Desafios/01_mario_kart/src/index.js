const readline = require('readline');

// Objects
const characters = [
  {
    nome: 'Mario',
    velocidade: 4,
    manobrabilidade: 3,
    poder: 3,
  },
  {
    nome: 'Peach',
    velocidade: 3,
    manobrabilidade: 4,
    poder: 2,
  },
  {
    nome: 'Yoshi',
    velocidade: 2,
    manobrabilidade: 4,
    poder: 4,
  },
  {
    nome: 'Bowser',
    velocidade: 5,
    manobrabilidade: 2,
    poder: 5,
  },
  {
    nome: 'Luigi',
    velocidade: 3,
    manobrabilidade: 4,
    poder: 4,
  },
  {
    nome: 'Donkey Kong',
    velocidade: 2,
    manobrabilidade: 2,
    poder: 5,
  },
];

// Asynchronous functions
/**
 * Prints a query message, read an input line and return the result.
 * @param {number} message the message to be printed
 * @returns {*} the user input
 */
async function readInput(message) {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  // User inputs
  const result = new Promise((resolve) => rl.question(message, resolve));
  await result;
  rl.close();

  return result;
}

/**
 * Receives the total number of players and assign each to a character
 * @param {int} numPlayers the number of players
 * @returns {list} a list containing the players object
 */
async function startRace(numPlayers) {
  let players = [];

  // Se players maior que 8 cancela a corrida
  if (numPlayers > 8) {
    console.log('Quantidade máxima ultrapassada, até 8 players permitidos!');
    return players;
  } else {
    for (let c = 1; c <= numPlayers; c++) {
      // Interpolação de strings|Template strings
      // Escolhendo personagem - array começa em 0 então indice -1
      const characterIndex = await readInput(
        `P${c} escolha seu personagem: 1 - Mario | 6 - Donkey Kong: `
      );
      const characterPlayer = characters[characterIndex - 1];

      const player = {
        nome: `P${c}:${characterPlayer.nome}`,
        personagem: characterPlayer,
        pontos: 0,
      };
      players.push(player);
    }

    return players;
  }
}

/**
 * Rolls a random dice number.
 * @returns {int} the number landed
 */
async function rollDice() {
  // Métodos builtin
  return Math.floor(Math.random() * 6) + 1;
}

/**
 * Receives the object type and choose one of that type, {blocks == challenges}.
 * @param {*} type the type of object to return
 * @returns {string} the object name
 */
async function getRandomObject(type) {
  let random = Math.random();
  let result;

  // Estrutura condicional switch-case
  if (type === 'block') {
    switch (true) {
      case random < 0.33:
        result = 'Reta';
        break;
      case random < 0.66:
        result = 'Curva';
        break;
      default:
        result = 'Confronto';
    }
  } else {
    // Map
    switch (true) {
      case random < 0.16:
        result = 'Luigi Raceway';
        break;
      case random < 0.32:
        result = 'Moo Moo Farm';
        break;
      case random < 0.48:
        result = 'Donut Plains 1';
        break;
      case random < 0.72:
        result = 'Bowser Castle 1';
        break;
      case random < 0.88:
        result = 'Peach Beach';
        break;
      default:
        result = 'Yoshi Falls';
    }
  }

  return result;
}

/**
 * Log the player resulting points in that block.
 * @param {*} characterName the object name of the player
 * @param {str} block a string with the name of the attribute of the block. {SPEED|MANEUVERS|POWER}.
 * @param {int} diceResult the rollDice() result.
 * @param {int} attribute the player's character attribute of the block;
 */
// Encapsulate
async function logRollResult(characterName, block, diceResult, attribute) {
  // Expressões em JavaScript
  console.log(
    `${characterName} rolou um dado de ${block} com o valor ${diceResult} + ${attribute} = ${
      diceResult + attribute
    }!`
  );
}

async function setPlayerPoints(players, block) {}

/**
 * Check points lists to get the index with most points. Players list should follow the same index.
 * @param {list<int>} pointsList the list to get the maximum value from. {playerPoints|powerPoints}
 * @returns {list<int>} the list of indexes to search the players list
 */
async function checkRoundWinner(pointsList) {
  let maxPoints = Math.max(pointsList);
  let indexPlayers = [];

  // Para cada elemento recupera o indice
  for (let c in pointsList) {
    if (pointsList[c] === maxPoints) {
      indexPlayers.push(c);
    }
  }

  return indexPlayers;
}

/**
 * Prints the leaderboard with the players scores.
 * @param {list} players the list of players
 */
async function checkLeaderboard(players) {
  console.log('================== Leaderboard ===================');
  for (let c of players) {
    console.log(`\t${c.nome} -- ${c.pontos} ponto(s)`);
    // TODO: Add sorting by points
  }
  console.log('==================================================');
}

/**
 * Starts the race and get the winners for each round.
 * @param {list} players the list of players
 */
async function playRaceEngine(players) {
  // Bloco de repetição for
  for (let round = 1; round <= 5; round++) {
    console.log('==================================================');
    console.log(`Rodada ${round}`);
    const block = await getRandomObject('block');
    const map = await getRandomObject('map');
    console.log(`--- Bloco: ${block} --- Mapa: ${map} --- `);

    let diceRolls = [];
    for (let c = 0; c < players.length; c++) {
      const diceNumber = await rollDice();
      diceRolls.push(diceNumber);
    }
    // Prevenir array undefined para somas
    let playerPoints = [];
    let powerPoints = [];
    playerPoints.length = players.length;
    powerPoints.length = players.length;
    playerPoints.fill(0);
    powerPoints.fill(0);

    // Recebendo os pontos de habilidade para cada jogador
    for (let c = 0; c < players.length; c++) {
      const character = players[c].personagem;

      // Estrutura condicional - adicionando os pontos de cada player
      if (block == 'Reta') {
        logRollResult(
          players[c].nome,
          'VELOCIDADE',
          diceRolls[c],
          character.velocidade
        );
        playerPoints[c] += diceRolls[c] + character.velocidade;
      } else if (block == 'Curva') {
        logRollResult(
          players[c].nome,
          'MANOBRABILIDADE',
          diceRolls[c],
          character.manobrabilidade
        );
        playerPoints[c] += diceRolls[c] + character.manobrabilidade;
      } else {
        // Confronto
        logRollResult(players[c].nome, 'PODER', diceRolls[c], character.poder);
        powerPoints[c] += diceRolls[c] + character.poder;
      }
    }

    console.log('==================================================');

    if (block === 'Confronto') {
      // Verificando quem marcou mais pontos em confronto
      const indexPlayers = await checkRoundWinner(powerPoints);

      // Verificando quem está na lista de ganhadores
      for (let c in players) {
        // Clean ifs - pode retirar as chaves se possuir a seguinte estrutura
        if (c === indexPlayers.filter((index) => index === c)[0])
          console.log(
            `${players[c].nome} obteve o máximo de pontos! Menos um ponto para os jogadores restantes.`
          );
        else players[c].pontos--;
      }
      // Verificando quem ganhou os outros desafios.
    } else {
      const indexPlayers = await checkRoundWinner(playerPoints);
      let playerList = indexPlayers.map((index) => players[index]);
      for (let p of playerList){
        console.log(`${p.nome} ganhou o desafio! Mais um ponto.`);
        p.pontos++;
      }
    }
    checkLeaderboard(players);
  }
}

async function declareWinner(players) {
  console.log('Resultado final:');

  let maxPoints = 0;
  let player;
  for (let p of players) {
    if (p.pontos > maxPoints) {
      maxPoints = p.pontos;
      player = p;
    }
  }

  if (player) {
    console.log(`\t${player.nome} ganhou a competição! Parabéns!!`);
  } else {
    console.log('\tEmpate!');
  }
}

// Auto-invoke functions
(async function main() {
  // Funções anonimas e arrow functions
  // Spread operator ... - rest parameter
  // Ifs ternários
  let players = [];
  players = await startRace(5);

  if (players.length > 0) {
    // Functions chains
    await playRaceEngine(players);
    console.log('Fim!');
    declareWinner(players);
  }
})();
