# Manipulando arquivos

# Modos de abertura de arquivo
# "r" somente leitura, "w" gravação no arquivo, "a" anexar ao arquivo já existente

# Abrindo arquivo em modo leitura
# Modo padrão é leitura caso se omita o parâmetro
arquivo = open("./POO/lorem.txt", "r")


# Ao realizar a leitura com um método abaixo, aquela linha fica guardada e é removida da iteração
# Por isso, ao utilizar ambos o retorno não será o mesmo ou até vazio
''' print(arquivo.read())'''# Retorna a leitura completa do arquivo

print("="*20)
'''print(arquivo.readline()) 
print(arquivo.readline())''' # Lê uma linha por vez do arquivo
'''print(arquivo.readlines())''' # Lê o arquivo completo e retorna uma lista com as linhas


# O símbolo ":=" a partir do python 3.8 serve para a declaração de variáveis em expressões
# Difere-se de "=", que não permite a atribuição em expressões
while len(linha := arquivo.readline()):
    print(linha)

# Fechando arquivo. Sempre feche o arquivo após a operação para desalocar recursos computacionais
arquivo.close()