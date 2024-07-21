# Objetos de primeira classe
# Utiliza os conceitos de funções internas e retorno de funções
def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função")
        funcao()
        print("Faz algo depois de executar a função")
    
    return envelope


@meu_decorador
def ola_mundo():
    print("Olá, mundo!")
    # Return None


# Decoradores, é atribuido a função uma outra função, permitindo que essa seja executada antes e depois da função
# A baixo, é atribuida a função meu_decorador passando a função ola_mundo como argumento, assim quando chamado é executado 1º meu_decorador e dentro dele é executado ola_mundo()
'''
ola_mundo = meu_decorador(ola_mundo)
ola_mundo()
'''

# O açúcar sintático de decoradores

# Pode se passar a função com um símbolo de @ antes da definição da outra função. Isso é o mesmo que o processo anterior
ola_mundo()
