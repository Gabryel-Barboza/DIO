// Imports
const readline = require('node:readline');

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
function readInput(message, callback) {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const result = rl.question(message, callback);
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
    for (let c = 1; c < numPlayers; c++) {
      // Escolhendo personagem - array começa em 0 então indice -1
      // Interpolação de strings|Template strings
      const characterPlayer = readInput(
        `P${c} escolha seu personagem: 1 - Mario | 6 - Donkey Kong: `,
        (index) => characters[index - 1]
      );

      const player = {
        nome: `P${c}:${characterPlayer.nome}`,
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

async function getRandomBlock() {
  let random = Math.random();
  let result;

  // Estrutura condicional switch-case
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

async function playRaceEngine(character1, character2) {
  // Bloco de repetição for
  for (let round = 1; round <= 5; round++) {
    console.log(`Rodada ${round}`);
    let block = await getRandomBlock();
    console.log(`Bloco: ${block}`);

    const diceResult1 = await rollDice();
    const diceResult2 = await rollDice();

    let testSkill1 = 0;
    let testSkill2 = 0;

    // Estrutura condicional - testes de resultados
    if (block == 'Reta') {
      testSkill1 = diceResult1 + character1.velocidade;
      testSkill2 = diceResult2 + character2.velocidade;

      logRollResult(
        player1.nome,
        'VELOCIDADE',
        diceResult1,
        player1.velocidade
      );
      logRollResult(
        player2.nome,
        'VELOCIDADE',
        diceResult2,
        player2.velocidade
      );
    } else if (block == 'Curva') {
      testSkill1 = diceResult1 + character1.manobrabilidade;
      testSkill2 = diceResult2 + character2.manobrabilidade;

      logRollResult(
        player1.nome,
        'MANOBRABILIDADE',
        diceResult1,
        player1.manobrabilidade
      );
      logRollResult(
        player2.nome,
        'MANOBRABILIDADE',
        diceResult2,
        player2.manobrabilidade
      );
    } else {
      // Confronto
      let powerResult1 = diceResult1 + character1.poder;
      let powerResult2 = diceResult2 + character2.poder;

      logRollResult(player1.nome, 'PODER', diceResult1, player1.poder);
      logRollResult(player2.nome, 'PODER', diceResult2, player2.poder);

      // Verificando quem marcou pontos em confronto
      if (powerResult1 < powerResult2 && character1.pontos > 0) {
        console.log(
          `${character2.nome} ganhou! ${character1.nome} perdeu um ponto.`
        );
        character1.pontos--;
      } else if (powerResult2 < powerResult1 && character2.pontos > 0) {
        console.log(
          `${character1.nome} ganhou! ${character2.nome} perdeu um ponto.`
        );
        character2.pontos--;
      }

      // If ternário
      console.log(powerResult1 === powerResult2 ? 'EMPATE' : '');
    }

    // Verificando o vencedor
    if (testSkill1 > testSkill2) {
      console.log(`${player1.nome} marcou um ponto!`);
      player1.pontos++;
    } else if (testSkill2 > testSkill1) {
      console.log(`${player2.nome} marcou um ponto!`);
      player2.pontos++;
    }

    console.log('==================================================');
  }
}

async function declareWinner(character1, character2) {
  console.log('Resultado final:');
  console.log(`${character1.nome}: ${character1.pontos} pontos.`);
  console.log(`${character2.nome}: ${character2.pontos} pontos.`);

  // Clean ifs - pode retirar as chaves se possuir a seguinte estrutura
  if (character1.pontos > character2.pontos)
    console.log(`${character1.nome} venceu a partida!`);
  else if (character2.pontos > character1.pontos)
    console.log(`${character2.nome} venceu a partida!`);
  else console.log('Foi empate!');
}

// Auto-invoke functions
(async function main() {
  // Funções anonimas e arrow functions
  let players = [];
  players = await startRace(5);

  // if (players) {
  //   // Functions chains
  //   await playRaceEngine(player1, player2);
  //   console.log('Fim!');
  // }
})();
