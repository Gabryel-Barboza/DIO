import hashlib

# Criando um gerador de hash para vários tipos de algoritmo hash
while True:
    print("### MENU ###")
    escolha = int(input("""Escolha o tipo de Hash (0 - Sair): 
    [1] - MD5
    [2] - SHA1
    [3] - SHA256
    [4] - SHA512
    :"""))

    match (escolha):
        case 0:
            break
        case 1:
            hash = hashlib.md5(b"Python Security") # Mesmo que encode()
        case 2:
            hash = hashlib.sha1(b"Python Security")
        case 3:
            hash = hashlib.sha256(b"Python Security")
        case 4:
            hash = hashlib.sha512(b"Python Security")
        case _:
            print("Opção inválida!")
            continue

    print("O hash da string é :", hash.hexdigest())
