import random
import string

tamanho = int(input("Tamanho da senha: "))

# Recebe todos os carácteres disponíveis para criação de senhas
chars = string.ascii_letters + string.digits + "!@#$%&*()-=+"
# print(chars)

# Seleciona um elemento aleatório de uma sequência
rnd = random.SystemRandom()  # os.urandom

print("Senha gerada com sucesso! Sua nova senha é:")
print("".join(rnd.choice(chars) for i in range(tamanho)))
