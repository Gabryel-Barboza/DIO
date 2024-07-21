class Cachorro:
    # Construtor
    # Primeiro método executado ao instanciar um objeto
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    
    def falar(self):
        print("auau")

    
    # Destrutor
    # método executado ao destruir uma instância
    # O Python possui um coletor de lixo automático, permitindo melhor gerenciamento de memória
    def __del__(self):
        print("Removendo instância da classe")


def criar_cachorro():
        c = Cachorro("Zeus", "Branco e preto", False)
        print(c.nome)


c1 = Cachorro("Davy", "marrom", False)
c1.falar()
del c1

# Inicializando um objeto, realizando métodos e terminando a função
# Perceba que a instância também é encerrada, através do coletor de lixo
criar_cachorro()
print()