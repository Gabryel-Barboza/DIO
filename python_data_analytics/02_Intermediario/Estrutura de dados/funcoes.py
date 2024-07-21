# DECLARANDO FUNÇÕES

def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}")


exibir_mensagem()
exibir_mensagem_2("Gabryel")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")


# RETORNO
def calcular_total(numeros):
    return sum(numeros)


def antecessor_e_sucessor(numero):
    antecessor = numero - 1 
    sucessor = numero + 1
    return antecessor, sucessor


def func_3():
    print("Olá, Mundo!")


print(calcular_total([25, 25, 25]))
print(antecessor_e_sucessor(999))
print(func_3())  # Sem retorno, None

# ARGUMENTOS NOMEADOS
print("="*30)

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # Possivel erro na ordem correta
salvar_carro(marca="Fiat", placa="ABC-1234", modelo="Palio", ano=1999) # Possivel erro com o nome do argumento
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # Utilizando dicionários


# *ARGS E **KWARGS
# tuplas e dicionários

def exibir_poema(data_extenso, *tupla, **dicionario):
    texto = "\n".join(tupla)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


print()
exibir_poema("13 de Março de 2024",
            "Zen of Python",
            "Beautiful is better than ugly.",
            "Explicit is better than implicit.",
            "Simple is better than complex.",
            "Complex is better than complicated.",
            "Flat is better than nested.",
            "Sparse is better than dense.",
            "Readability counts.", 
            "Special cases aren't special enough to break the rules.",
            "Although practicality beats purity.",
            "Errors should never pass silently.",
            "Unless explicitly silenced.",
            "In the face of ambiguity, refuse the temptation to guess.",
            "There should be one -- and preferably only one -- obvious way to do it.",
            "Although that way may not be obvious at first unless you're Dutch.",
            "Now is better than never.",
            "Although never is often better than *right* now.",
            "If the implementation is hard to explain, it's a bad idea.",
            "If the implementation is easy to explain, it may be a good idea.",
            "Namespaces are one honking great idea -- let's do more of those!",
            autor="Tim Peters", ano=1999)
# O interpretador age da seguinte forma: o primeiro texto entra no primeiro argumento, o resto vai entrar no *args até
# chegar em um modelo chave-valor, ae sim ele receberá nos **kwargs



# Parâmetros especiais
# Param por posição, posição e nome, e nome


# parâmetros até a '/' é obrigatório a posição correta na atribuição
def salvar_carro(marca, modelo, ano, /,placa, combustivel):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}/ {combustivel}")


salvar_carro("Fiat", "Palio", 1999, combustivel="Gasolina", placa="ABC-1234")


# parâmetros depois do '*' é obrigatório o modelo chave-valor
def salvar_carro(*, marca, modelo, ano, placa, combustivel):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}/ {combustivel}")


salvar_carro(marca="Fiat", modelo="Palio", ano=1999, combustivel="Gasolina", placa="ABC-1234")

# É possível usar os dois parametros especiais na mesma função.



# OBJETOS DE PRIMEIRA CLASSE
# São objetos retornados(closures), passados como parâmetro, atribuido a variáveis e usados em estruturas de dados.

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)
exibir_resultado(10, 10, multiplicar)
exibir_resultado(10, 10, dividir)

er = exibir_resultado
er(10, 10, multiplicar)
print()

# ESCOPO
# escopo local define as alterações em objetos MUTÁVEIS, e só pode ser utilizada dentro do bloco que foi declarada.
salario = 2000

# Com a keyword global, definimos o escopo global para uma variável. Tente retira-lá e executar o código
def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


print(salario_bonus(500))