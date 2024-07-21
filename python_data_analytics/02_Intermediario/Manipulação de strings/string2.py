nome = "Gabryel"
idade = 19
altura = 1.80
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Gabryel",
"idade": 19,
"altura": 1.80,
"profissao":"Programador",
"linguagem": "Python"}

# Old
print("Nome: %s Idade: %d Altura: %f Profissão: %s" % (nome, idade, altura, profissao))

print()
#.format
print("Nome: {} Idade: {} Altura: {} Profissão: {}".format(nome, idade, altura, profissao))

print()

print("Nome: {0} Altura: {2} Idade: {1} Profissão: {3}".format(nome, idade, altura, profissao))

print()

print("Nome: {name} Altura: {height} Idade: {age} Profissão: {prof}".format(name=nome, age=idade, height=altura, prof=profissao))

print()

print("Nome: {nome} Altura: {altura} Idade: {idade} Profissão: {profissao}".format(**dados))

print()
# f-strings
print(f"Nome: {nome} Altura: {altura:2.1f} Idade: {idade} Profissão: {profissao}")
