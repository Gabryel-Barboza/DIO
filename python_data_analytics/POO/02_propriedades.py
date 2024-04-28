# Propertys
# Argumentos computados ou gerenciados
# São formas de definir os métodos como propriedades para alguma classe
# Sem o decorador @property, a classe funcionará como um método normalmente
class Foo:
    def __init__(self, x=None):
        self._x = x

    # Para os atributos abaixo funcionarem, é preciso uma propriedade
    # Importante os métodos terem nomes diferentes! Caso contrário causará uma recursão
    @property
    def x(self):
        return self._x or 0
    

    # Ao se utilizar propriedades, os métodos se tornam atributos e devem ser tratados como tal
    # Logo, não é retornado o valor mas sim modificado diretamente
    @x.setter
    def x(self, valor):
        self._x = valor


    # O deleter não é utilizado para retirar da memória o valor, mas apenas modificar para algo que não possua valor
    # Assim, pode-se incrementar novamente esse valor a qualquer momento
    @x.deleter
    def x(self):
        self._x = 0
        #del self._x



foo = Foo(10)

# Não é possivel receber ao atributo, necessário outro decorador para isso
foo.x = 10

# "Deletando" o atributo
del foo.x

# Exibir o atributo privado _x
print(foo.x)