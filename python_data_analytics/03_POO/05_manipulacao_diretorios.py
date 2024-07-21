import os
import shutil
from pathlib import Path
from time import sleep

# Módulos para a manipulação dos arquivos e diretórios
#arquivo = open("./POO/novo-arquivo.txt")
# Comandos estilo bash

# Imprime o caminho do arquivo.py atual
'''print(__file__)'''
# Pathlib para manipulação dos caminhos
print("caminho: ")
ROOT_PATH = Path(__file__).parent
print(ROOT_PATH)

print("="*50)
print("caminho-pai: ")
print(ROOT_PATH.parent)
print("="*50)


# Se diretório já existente retorna um erro
try:
    # Cria um diretório
    # Utiliza o caminho + / + diretorio para criação
    os.mkdir(ROOT_PATH / "novo-diretorio")
except:
    pass

'''os.mkdir("./POO/novo-diretorio")'''

# Veja o explorador de arquivos para visualizar a criação e interação com o arquivo novo.txt
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()


# Renomeando arquivos
sleep(2)
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# Removendo arquivos
sleep(2)
os.remove(ROOT_PATH / "alterado.txt")


# Movendo arquivos
try:
    arquivo = open(ROOT_PATH / "arquivo-movido.txt", "w")
    arquivo.close()

    sleep(2)
    # Caminho do arquivo; Caminho da nova pasta incluindo o arquivo 
    shutil.move(ROOT_PATH / "arquivo-movido.txt", ROOT_PATH / "novo-diretorio" / "arquivo-movido.txt")

    sleep(2)
    os.remove(ROOT_PATH / "novo-diretorio/arquivo-movido.txt")
except:
    pass