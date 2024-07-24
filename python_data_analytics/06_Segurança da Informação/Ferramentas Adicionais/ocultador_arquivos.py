import ctypes
from pathlib import Path

# Programa que oculta arquivos ou diretórios

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW("./Ferramentas Adicionais/ocultar.txt", atributo_ocultar)

if retorno:
    print("Arquivo ocultado")
else:
    print("Falha na execução do programa")
