# Desafio: A Aventura do Explorador
# Você é um intrépido explorador em uma jornada por uma terra desconhecida repleta de desafios emocionantes. Ao se deparar com uma floresta misteriosa, você percebe que a única maneira de atravessá-la é desvendando seus caminhos por meio de um código em Python. Prepare-se para a "Aventura do Explorador"!

# Entrada
quantidade_passos = int(input())
if (quantidade_passos <= 0):
  print("Nenhum passo dado na floresta.")
else:
  contador = 0
  while contador < quantidade_passos:
    contador += 1
    print(f"Explorador: {contador} passo") if contador == 1 else print(f"Explorador: {contador} passos")
  
#TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
# Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
# Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.