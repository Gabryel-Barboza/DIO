import socket
import sys

def main():
    try:
        # Criando a variável para comunicação, recebe os parâmetros de familia de protocolos, tipo e protocolo
        # AF_INET = IP, SOCK_STREAM = TCP, 0 = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as exc:
        print(f"Falha na conexão! \n {exc}")
        sys.exit() # Fechando o programa

    print("Socket criado com sucesso")

    # Host e porta de conexão
    host_alvo = input("Digite o IP ou host para conexão: ")
    porta_alvo = input("Digite a porta para conexão: ")
    try:
        # Se conecta ao cliente
        s.connect((host_alvo, int(porta_alvo)))
        print(f"Cliente TCP conectado com sucesso no host: {host_alvo} | porta: {porta_alvo}")
        # Finalizando a conexão após 2s
        s.shutdown(2)
    except socket.error as exc:
        print(f"Falha na conexão com o host! \n{exc}")
        sys.exit()


# Chamar a função apenas se arquivo executado diretamente, evita executar em importações de módulo
if __name__ == "__main__":
    main()
