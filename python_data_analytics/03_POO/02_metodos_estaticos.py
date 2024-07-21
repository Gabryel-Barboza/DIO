# Métodos estáticos e de classes

# Métodos de classe apontam para a própria classe, podendo modificá-las
# Métodos estáticos não apontam para a classe, não permitindo a função da mesma

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade


    # Ao ser executado abaixo, será criado uma nova instância e depois uma instância com o método
    '''
    def criar_pessoa_data(self, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)
    '''


    # Método de classe, utilizado sem a necessidade de uma instância. Utilize cls no lugar de self
    @classmethod
    def criar_pessoa_data(cls, ano, mes, dia, nome):
        #print(cls) - cls referencia da classe
        idade = 2024 - ano
        return cls(nome, idade)
    

    # Método estático
    # Não precisa de instância para ser executado também, contudo não tem apontamento da classe
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18


p = Pessoa("Gabryel", 20)

#p2 = Pessoa().criar_pessoa_data(2004, 9, 7, "Gabryel")

p2 = Pessoa.criar_pessoa_data(2004, 9, 7, "Gabryel")
print(p2.nome, p2.idade)

print(Pessoa.maior_de_idade(20))
print(Pessoa.maior_de_idade(17))