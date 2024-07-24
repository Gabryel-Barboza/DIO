import os
from time import sleep
from pathlib import Path

# Lendo o arquivo com os hosts e utilizando a ferramenta ping em cada host do arquivo

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / "hosts.txt", "r", encoding="utf-8") as arquivo:
    hosts = arquivo.read().splitlines()
    for host in hosts:
        print("Verificando o IP: " + host)
        os.system(f"ping -n 2 {host}")
        print()
        sleep(5)
