import os

print("#" * 60)
ip_host = input("Digite o IP ou host: ")
# Executando comandos cmd com o método system. -n define limite de pacotes
os.system(f"ping -n 6 {ip_host}")
