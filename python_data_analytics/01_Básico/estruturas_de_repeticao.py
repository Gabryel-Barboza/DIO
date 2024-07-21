texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# For iterando uma sequência
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else: # Executado quando o laço termina
    print()
    print("Fim do laço")

# For com range
# start(opcional), stop(obrigatório) e step(opcional)
for c in range (10):
    print(c, end=" ")

print()

for c in range(10, 0, -1):
    print(c, end=" ")
print()

# Comando While
    
opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n:"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print()

# Comando break
while True:
    opcao = int(input("Digite um número: "))

    if opcao == 0:
        break

# Comando continue
for c in range(10):

    if c % 2 ==0:
        continue # pula para o próximo laço
    print(c, end=" ")
    
