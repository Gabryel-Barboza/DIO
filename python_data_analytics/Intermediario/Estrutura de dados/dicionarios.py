# Diferencia do conjunto pelo modelo "chave-valor" na atribuição
pessoa = {"nome": "Gabryel", "idade": 19}
pessoas = dict(nome="Gabryel", idade=19)
# Adicionando campos novos
pessoa["telefone"] = "3333-1234"


print(pessoa)
print(pessoa["telefone"])

pessoa["nome"] = "João"
pessoa["idade"] = 23
pessoa["telefone"] = "9999-3333"
print(pessoa)

# Dicionários aninhados
contatos = {}
contatos["joao@email.com"] = pessoa
pessoa = {"nome": "Gabryel", "idade": 19, "telefone": "3333-1234"}
contatos["gabryel@email.com"] = pessoa
print(contatos)
print()

# Iterando dicionários
print("="*20)

for chave in contatos:
    print(f"EMAIL: {chave}\nDADOS PESSOAIS: {contatos[chave]}")

print("="*20)

for chave, valor in contatos.items(): #.keys, .values
    print(f"EMAIL: {chave}\nDADOS PESSOAIS: {valor}")

print("="*20)

for valor in contatos.values():
    print(valor)

# MÉTODOS

#{}.clear()
#{}.copy()
#.pop() ou .pop("chave")
# del {}[]
print("="*20)

# Criando chaves
dicionario = dict.fromkeys(["nome", "telefone"])
print(dicionario)
dicionario = dicionario.fromkeys(["nome", "telefone"], "vazio")
print(dicionario)

# Procura uma chave, retorna um valor definido quando não encontrada
print(dicionario.get("chave", "Não encontrado"))
print(dicionario.get("nome", {}))
print(contatos.get("gabryel@email.com"))

# Exclui o primeiro item do dicionário
print()
print("="*20)
dicionario = contatos.copy()
print(dicionario)
print("="*20)
print(dicionario.popitem())

# Verifica se chave exista, caso contrário cria com o valor definido
dicionario = contatos.copy()
dicionario.setdefault("nome", "Giovanna")
dicionario.pop("nome")
print(dicionario)
print()
print("="*20)

# Atualiza chaves ou cria, se não existir
dicionario.update({"giovanna@email.com": {"nome": "Giovanna", "Idade": 17, "telefone": "8888-7777" }})
dicionario.update({"joao@email.com": {"nome": "Joao Guilherme"}})
print(dicionario)

print("gabryel@email.com" in dicionario)
print("telefone" in dicionario["giovanna@email.com"])

