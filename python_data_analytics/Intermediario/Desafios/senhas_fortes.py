import re
def verificar_forca_senha(senha):


  comprimento_minimo = 8
  tem_letra_maiuscula = False
  tem_letra_minuscula = False
  tem_numero = False
  tem_caractere_especial = False

  # Verificando o comprimento da senha
  if len(senha) < comprimento_minimo:
    return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

  # TODO: Verifique se a senha contém letras maiúsculas e minúsculas
  if (re.search("[a-z]", senha) != None):
    tem_letra_minuscula = True
    
  if (re.search("[A-Z]", senha) != None):
    tem_letra_maiuscula = True
      
  # Verificando se a senha contém sequências comuns
  sequencias_comuns = ["123456", "abcdef"]
  for sequencia in sequencias_comuns:
    if sequencia in senha:
      return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."

  # Verificando se a senha contém palavras comuns
  palavras_comuns = ["password", "123456", "qwerty"]
  if senha in palavras_comuns:
    return "Sua senha e muito comum. Tente uma senha mais complexa."

  # TODO: Verificar o comprimento mínimo e critérios de validação
  if (re.search("[0-9]", senha) != None):
    tem_numero = True
  
  if (re.search("[!@#$%¨&*]", senha) != None):
    tem_caractere_especial = True
  
  if (tem_letra_maiuscula and tem_letra_minuscula) and (tem_numero and tem_caractere_especial):
    return "Sua senha atende aos requisitos de seguranca. Parabens!"
  else:
    return "Sua senha nao atende aos requisitos de seguranca"

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)