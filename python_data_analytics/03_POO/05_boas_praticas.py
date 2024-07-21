from pathlib import Path

# Boas práticas com manipulação de arquivos

ROOT_PATH = Path(__file__).parent

# Tratamento de erros para verificar se a leitura do arquivo teve sucesso
try:

    # Bloco with fecha automaticamente o arquivo ao sair do seu bloco
    with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
        #arquivo.close()
        arquivo.readline()
    # Tentando ler o arquivo após a finalização do bloco with
    try:
        print(arquivo.read())
    except ValueError:
        print("Arquivo fechado")
    
except IOError as exc:
    print("Falha ao ler o arquivo")
    print(exc)

# Codificação padrão para todos os arquivos
# arquivos de codificação diferente causam conflitos de escrita e leitura
try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Aprendendo a manipular arquivos com PŸthon")
except IOError as exc:
    print(exc)

# Caso o arquivo contenha caracteres não suportados, será causado um erro
try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="ascii") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(exc.strerror)
except UnicodeError as exc:
    print(exc)