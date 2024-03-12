# DECLARAÇÃO DE LISTAS

frutas = ["laranja", "maçã", "uva"]
print(frutas)

lista = []

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

print("="*20)


# ACESSORES

# Acesso direto
print(frutas[0])
print(frutas[1])
print(frutas[-1])
print(frutas[-2])

lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista_aninhada[0])
print(lista_aninhada[0][0])
print(lista_aninhada[-1][-1])

# Fatiamento

lista = ["p", "y", "t", "h", "o", "n"]
#         0    1    2    3    4    5
print(lista[1:])
print(lista[2:6]) # Stop - 1
print(lista[0:3:2])
print(lista[::-1])

print("="*20)

# Iterando listas
for c in lista_aninhada:
    print(c)

# Variáveis de escopo
for i, j in enumerate(lista_aninhada):
    print(f"Linha {i}:")
    for i, j in enumerate(j):
        print(f"Coluna {i}: {j}")
    print()


# LIST COMPREHENSION
    
pares = []
'''numeros = list(range(20))
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)'''

numeros = [numero for numero in range(10)]
#          retorno     iteração
pares = [numero for numero in numeros if numero % 2 == 0]
#        retorno     iteração            condição
print(pares)

quadrado = []
'''for numero in numeros:
    quadrado.append(numero ** 2)'''
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)


# Listas referenciadas
quadrado = [quadrado for numero in numeros]
print(quadrado)