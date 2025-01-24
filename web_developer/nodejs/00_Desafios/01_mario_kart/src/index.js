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

// User inputs
async function readInput(message) {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const result = new Promise((resolve) => rl.question(message, resolve));
  await result;
  rl.close();
  return result;
}

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

// Async functions
async function rollDice() {
  // Métodos builtin
  return Math.floor(Math.random() * 6) + 1;
}

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
  } else { // Map
    switch (true) {
      case random < 0.16:
        result = 'Luigi Raceway';
        break;
      case random < .32:
        result = 'Moo Moo Farm';
        break;
      case random < .48:
        result = 'Donut Plains 1';
        break;
      case random < .72:
        result = 'Bowser Castle 1';
        break;
      case random < .88:
        result = 'Peach Beach';
        break;
      default:
        result = 'Yoshi Falls';
    }
  }
  return result;
}

// Encapsulate
async function logRollResult(characterName, block, diceResult, attribute) {
  // Expressões em JavaScript
  console.log(
    `${characterName} rolou um dado de ${block} com o valor ${diceResult} + ${attribute} = ${
      diceResult + attribute
    }!`
  );
}

async function checkRoundWinner(pointsList) {
  let maxPoints = 0;
  let indexPlayer;

  for (let c = 0; c < pointsList.length; c++) {
    if (pointsList[c] > maxPoints) {
      maxPoints = pointsList[c];
      indexPlayer = c;
    }
  }

  return indexPlayer;
}

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

    let playerPoints = [];
    let powerPoints = [];

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
      const indexPlayer = await checkRoundWinner(powerPoints);
      // Verificando o vencedor do desafio
      for (let c = 0; c < players.length; c++) {
        // Clean ifs - pode retirar as chaves se possuir a seguinte estrutura
        if (c === indexPlayer)
          console.log(
            `${players[c].nome} ganhou o confronto! Menos um ponto para os jogadores restantes`
          );
        else if (players[c].pontos > 0) players[c].pontos--;
      }
    } else {
      // Verificando quem ganhou os outros desafios.
      const indexPlayer = await checkRoundWinner(playerPoints);

      for (let c = 0; c < players.length; c++) {
        if (c === indexPlayer) {
          console.log(
            `${players[c].nome} ganhou o desafio! Mais um ponto adicionado ao jogador.`
          );
          players[c].pontos++;
        }
      }
    }

    console.log('==================================================');
  }

  return players;
}

async function declareWinner(players) {
  console.log('Resultado final:');

  let maxPoints = 0;
  let player;
  for (let c = 0; c < players.length; c++) {
    if (players[c].pontos > maxPoints) {
      maxPoints = players[c].pontos;
      player = players[c];
    }
  }
  console.log(`${player.nome} é o vencedor! Parabéns!!`);
}

// Auto-invoke functions
(async function main() {
  // Funções anonimas e arrow functions
  // Spread operator ... - rest parameter
  // Ifs ternários
  let players = [];
  players = await startRace(5);

  if (players) {
    // Functions chains
    await playRaceEngine(players);
    console.log('Fim!');
    declareWinner(players);
  }
})();
