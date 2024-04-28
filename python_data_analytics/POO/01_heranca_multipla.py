# Herança múltipla
# É quando se herda mais de uma classe base
# Nesse exemplo, Ornitorrinco herda duas classes pai
class Animal:
    def __init__(self, **kw):
        self.numero_patas = kw["nro_patas"]


    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.cor_pelo = kw["cor_pelo"]


class Ave(Animal):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.cor_bico = kw["cor_bico"]


class Cachorro(Mamifero):
    #def __init__(self, pelo="Caramelo", nro_patas = 4):
    def __init__(self, **kw):
        super().__init__(**kw)


class Gato(Mamifero):
    #def __init__(self, pelo="Cinza", nro_patas = 4):
    def __init__(self, **kw):
        super().__init__(**kw)


class Leao(Mamifero):
    #def __init__(self, pelo, nro_patas = 4):
    def __init__(self, **kw):
        super().__init__(**kw)


        # Method Resolution Order - MRO
        print(Leao.__mro__)
        # Ordem de execução dos métodos, o método __str__ é um exemplo, onde a primeira classe da lista mro com esse método é que será executado
    def __str__(self):
        return "Leão"


class Ornitorrinco(Mamifero, Ave):
    #def __init__(self, pelo, cor_bico, nro_patas = 4):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        

c1 = Cachorro(nro_patas=4, cor_pelo="Marrom")
print(c1)
# Um problema que ocorre na instânciação de classes de heranças múltiplas, é a confusão de parametros
# Isso pois, enquanto uma classe pai aceita só 3 argumentos, outra vai aceitar 4. Assim, causando conflitos no código
# Para resolucionar esse problema, é utilizado o modelo chave-valor ou keyargs
# o1 = Onitorrinco("Vermelho", "Amarelo")
o1 = Ornitorrinco(nro_patas=4, cor_pelo="Vermelho", cor_bico="Amarelo")
print(o1)
l1 = Leao(nro_patas=4, cor_pelo="marrom")
print(l1)
