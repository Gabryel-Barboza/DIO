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


# Atribuições de mesma lista
quadrado = [quadrado for numero in numeros]
print(quadrado)

print("="*30)
# MÉTODOS DE LISTAS

# Adicionando valores
lista = []
lista.append(1)
lista.append("Python")
lista.append([20, 3, 5])

# Copiando listas
print(lista)
l2 = lista.copy()
print(f"Id lista: {id(lista)}\n Id l2: {id(l2)}")

# Removendo items e listas
lista.clear()
print(lista)
print(l2)
l2.pop() 
print(l2)


pais = ["Brasil", "Estados Unidos", "Canadá", "Brasil", "México", "Chile", "Suécia", "Alemanhã", "Bolívia", "Brasil", "Estados Unidos", "Azerbaijão", "Rússia", "México"]

# Verificando quantidades e índices
print(pais.count("Brasil"))
pais.extend(["França", "Rússia", "Inglaterra", "Japão", "China"])
print(pais)

pais2 = pais.copy()
print(pais.index("Brasil"))

# Removendo elementos pela posição
while pais2.count("Brasil") > 0:
    indice = pais2.index("Brasil")
    print(indice)
    pais2.pop(indice)

pais2.remove("Estados Unidos")
print(pais2)

# Ordenação de listas
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.reverse()
print(linguagens)
linguagens.reverse()
print(linguagens)


linguagens.sort()
print(linguagens)
linguagens.sort(reverse=True)
print(linguagens)
linguagens.sort(key=lambda x: len(x)) #retorna o tamanho de cada string, ordena em ordem crescente
print(linguagens)
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

#
print(len(linguagens))
sorted(linguagens) # key= , reverse=
print(linguagens)
