// Desenvolvendo em TypeScript
// Instalação do módulo com npm i typescript

function main() {
  // Inferência de tipos
  let nome = 'Gabryel';
  //nome = 1; erro de tipo de dados
  console.log(nome);

  // Declaração de tipo de dados
  let nomeCompleto: string = 'Gabryel Barboza';
  console.log(nomeCompleto);
}

main();
// Criando script para automatizar processo de transpilação npx tsc arquivo
// Criando arquivo do compilador tsc com npx tsc --init