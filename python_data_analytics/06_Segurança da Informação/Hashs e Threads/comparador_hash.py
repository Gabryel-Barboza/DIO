import hashlib
from pathlib import Path

ROOT_PATH = Path(__file__).parent
arquivo1 = "a.txt"
arquivo2 = "b.txt"

# Retorna um objeto hash utilizando o algoritmo de hash ripemd160. Alguns algoritmos disponíveis: md5, sha1, sha256...
hash1 = hashlib.new("ripemd160")
hash1.update(open(ROOT_PATH / arquivo1, "rb").read())
hash2 = hashlib.new("ripemd160")
hash2.update(open(ROOT_PATH / arquivo2, "rb").read())

# Compara os hash se iguais, .digest() retorna o hash
if hash1.digest() != hash2.digest():
    print(f"O arquivo '{arquivo1}' é diferente de '{arquivo2}.'")
else:
    print("Os arquivos são iguais.")

# .hexdigest() retorna o hash em hexadecimal
print(f"Hash de '{arquivo1}':\n {hash1.hexdigest()}")
print(f"Hash de '{arquivo2}':\n {hash2.hexdigest()}")
