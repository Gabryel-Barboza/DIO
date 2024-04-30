import functools

def meu_decorador(funcao):
    # Com a utilização dos param *args e **kwargs é possivel a criação de um decorador genérico
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar a função")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar a função")
        return resultado
    
    return envelope


@meu_decorador
def ola_mundo(nome, idade):
    print(f"Olá, mundo {nome}!")
    # retorno de função decorada
    return nome.upper()
    

# Agora, pode-se passar quantos parametros quiser
print(ola_mundo("Gabryel", 20))

# Instropecção
# Capacidade de objetos reconhecerem seus atributos

print(print)
print(print.__name__)

# Sem o módulo functools.wrap a função retorna function meu_decorador.<locals>.envelope
# envelope e não ola_mundo
print(ola_mundo)
print(ola_mundo.__name__)
