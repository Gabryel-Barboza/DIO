import csv
import os
from pathlib import Path
from time import sleep

# Manipulação de arquivos Comma Separated Values (CSV)

ROOT_PATH = Path(__file__).parent

try:
    # Adicione o parametro newline para a leitura correta de campos com \n para arquivos csv
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        # Instanciando o arquivo
        escritor = csv.writer(arquivo)
        # Escrevendo uma linha, aceita um iterável
        escritor.writerow(["id", "nome"])
        escritor.writerow(["1", "Maria"])
        escritor.writerow(["2", "João"])
        escritor.writerow(["3", "Gabryel"])
        # Escrevendo várias linhas, aceita lista de listas
        escritor.writerows([["4", "Kaio"], ["5", "Karynne"], ["6", "Brayan"]])

except IOError as exc:
    print(exc)


# Lendo arquivos csv
try:
    with open(ROOT_PATH / "usuarios.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        
        for row in leitor:
            print(row)
    
except IOError as exc:
    print(exc.strerror)

print("="*20)

# Lendo com formato de dicionário
try:
    with open(ROOT_PATH / "usuarios.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        print(leitor.fieldnames)
        
        for row in leitor:
            print(row["id"], row["nome"])
    
except IOError as exc:
    print(exc.strerror)


sleep(10)
os.remove(ROOT_PATH / "usuarios.csv")
