import os
# Tratamento de erros com Arquivos

# Tente executar
try:
    arquivo = open("novo-diretorio")

# Se exceção, execute isso
# Atribue log da exceção a variável
except FileNotFoundError as exc:
    print("Arquivo não encontrado")
    print(exc)

print("="*50)


try:
    open("./POO/novo-diretorio")
except IsADirectoryError as exc:
    print("Caminho é um diretório e não um arquivo")
    print(exc)
except PermissionError as exc:
    print("Você não tem permissão para abrir o arquivo")
    print(exc)
except IOError as exc:
    print("Erro ao abrir o arquivo")
    print(exc)
except Exception as exc:
    print("Algum erro ocorreu ao abrir o arquivo")
    print(exc)

print("="*50)
