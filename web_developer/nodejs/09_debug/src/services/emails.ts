// função(variavel: tipo): tipo de retorno
async function getBaseEmail(senderName: string): Promise<string> {
  let base = await getHeaderText();

  // Erro
  base + `Olá, ${senderName} estou te enviando um email sobre a vaga.`;
  base += '\n Gostaria de me inscrever, deixarei meu currículo em anexo.';
  return base;
}

async function getHeaderText(): Promise<string> {
  return 'Texto para você';
}
export { getBaseEmail };
