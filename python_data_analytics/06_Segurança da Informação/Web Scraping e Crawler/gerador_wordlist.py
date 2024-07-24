import itertools
from pathlib import Path

# Wordlist são listas com palavras por linha, utilizadas para ataques de força brutas

ROOT_PATH = Path(__file__).parent
string = input("String: ")

# Método permutations realiza a permutação da string inserida, limita o tamanho da string com um inteiro
resultado = itertools.permutations(string, len(string))

# Escrevendo resultado em um arquivo
with open(ROOT_PATH / "wordlist.txt", "w") as arquivo:
    for i in resultado:
        arquivo.writelines(i)
        arquivo.write("\n")
