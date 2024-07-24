import socket

# Criando comunicação UDP com o tipo SOCK_DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Cliente Socket criado com sucesso")

# Definindo IP e porta, localhost refere-se a rede local ou loopback da máquina
host = "localhost"
port = 5433
mensagem = "Cliente: Olá, servidor!"

try:
    print(mensagem)
    # Envia uma mensagem ao servidor local na porta 5432, empacota a mensagem com encode antes da transmissão
    s.sendto(mensagem.encode(), (host, 5432))

    # Recebe dados do servidor de 4096b e desempacota
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(dados)
finally:
    print("Cliente: fechando a conexão!")
    s.close()
