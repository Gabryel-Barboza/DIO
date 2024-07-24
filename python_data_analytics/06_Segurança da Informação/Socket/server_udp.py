import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com sucesso")

host = "localhost"
port = 5432

# Linkando o servidor ao host e porta
s.bind((host, port))
mensagem = "Servidor: Olá, Cliente!"

# Enquanto verdadeiro, esperar por mensagem de client
while True:
    dados, end = s.recvfrom(4096)

    # Se recebido dados, enviar mensagem para o client conectado
    if dados:
        print("Servidor enviando mensagem...")
        s.sendto(mensagem.encode(), end)
