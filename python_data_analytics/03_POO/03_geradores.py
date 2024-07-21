# Geradores
# São tipos especiais de iteradores, não armazenam todos seus valores na memória, mas sim alguns por vez, permitindo grande economia
# São definidos usando funções regulares, no lugar de return se utiliza yield

# Características
# Quando gerado um item e consumido, ele é esquecido e não pode ser acessado
# O estado interno do gerador é mantido entre chamadas
# Sua execução é pausada na declaração yield e retomada dali


def meu_gerador(numeros: list[int]):    
    for num in numeros:
        yield num * 2


for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)

