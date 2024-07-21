# Listas de elementos distintos
numero = set([1, 2, 1, 3, 1, 4, 3])
print(numero)

letras = set("abacaxi")
print(letras)

carros = set(("palio", "gol", "celta", "palio"))
print(carros)

linguagens = {"python", "java", "javascript", "python", "ruby", "java"}

print(linguagens)
#print(linguagens[0])
# Não suportam indexação e fatiamento
# converter para lista
linguagens = list(linguagens)
print(linguagens[0])

for indice, carro in enumerate(carros):
    print(indice, carro)

print("="*20)
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 7, 8, 9}
# União
print(conjunto_a.union(conjunto_b))

# Interseção
print(conjunto_a.intersection(conjunto_b))

# Diferença
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# Diferença Simétrica
print(conjunto_a.symmetric_difference(conjunto_b))


# Subconjuntos
# Somente com todos os elementos dentro de B, com interseção completa
print(conjunto_a.issubset(conjunto_b))
conjunto_a = {3, 4, 5}
print(conjunto_a.issubset(conjunto_b))

print(conjunto_b.issuperset(conjunto_a))

# Conjuntos disjuntos

# Somente com todos os elementos fora de b, sem interseção
print(conjunto_a.isdisjoint(conjunto_b))

# Adicionando elementos
sorteio = {1, 23}
sorteio.add(25)
sorteio.add(23)
sorteio.add(45)
print(sorteio)

sorteio2 = sorteio.copy()
# Removendo elementos e conjuntos
sorteio2.discard(23)    # Não retorna erro
sorteio2.remove(45)  # Retorna erro caso não exista
sorteio2.pop()  # Primeiro valor
print(sorteio2)
sorteio2.clear()
print(sorteio2)


len(sorteio)

