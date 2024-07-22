// Promises e Assincronismo
// É a execução de um comando de forma assincrona, em paralelo ao código e que retornará em algum momento não determinado.

const randomNumber = new Promise((resolve, reject) => {
    // Executando o código depois de um segundo, simulando um atraso de execução
    setTimeout(() => {
        const numero = parseInt(Math.random() * 100);
        // Se éxito na execução
        resolve(numero);
    }, 1000)
    // Se falha na execução
    // reject();
});

// Estrutura do try-catch
try {
    // Tente executar
} catch (error) {
    // Se ocorrer um erro execute
} finally {
    // Execute ao final sempre
}

// Estrutura de promises
// then é executado após receber o retorno da promise, podem ser aninhados ou encadeados inúmeras vezes. Recomenda-se encadeiar como boa prática.
randomNumber.then((value => value + 10))
            .then((value) => console.log(value))
            .catch((error) => console.log(error))
            .finally(() => console.log('Processo finalizado!'));

console.log('Executado antes da promise');


// Manipulando arquivos com assincronismo

const fs = require('fs'); // Importando módulos pelo Node
const path = require('path');  
const { text } = require('stream/consumers');
// Criando caminho absoluto para o arquivo
const filePath = path.resolve(__dirname, 'tarefas.csv')

//fs.readFile(); -- antigo
const lerArquivo = fs.promises.readFile(filePath); // Lendo o arquivo indicando pela variável de caminho
lerArquivo
.then((arquivo) => arquivo.toString('utf8')) // Após finalizar a leitura, converter o arquivo para String com codificação UTF8
.then((texto) => texto.split('\n').slice(1)) // Separar o texto em pedaços por quebra de linha, retornar a partir do índice 1
.then((linhas) => linhas.map((linha) => {
    const [nome, feito] = linha.split(';');
    return {
        nome,
        feito: feito.trim() === 'true'
    }
})) // Retornar objetos com o nome e o status da tarefa
.then((listaTarefas) => console.log(listaTarefas))
.catch((error) => console.log(`Falha na execução. ${error}`))


// Async - Define funções como assíncronas e permite a palavra reservada await para abstrair promises
async function buscarArquivo() {
    // Mesmo funcionamento da estrutura de promises, mas abstraída para uma estrutura procedural
    try {
        const promessaLeitura = await fs.promises.readFile(filePath);
        const textoArquivo = promessaLeitura.toString('utf8');
        const linhas = textoArquivo.split('\n').slice(1);
        const listaTarefas = linhas.map((linha) => {
            const [nome, feito] = linha.split(';');
            return {
                nome,
                feito: feito.trim() === 'true'
            }
        });
        console.log(listaTarefas);
    } catch (error) {

    } finally {
        
    }
}

buscarArquivo();
