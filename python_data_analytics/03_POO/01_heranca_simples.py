# Herança simples 
# É herdar de apenas uma única classe pai/base

# Veiculo, classe comum a todos os outros
# Um carro, moto ou caminhão herdam de veiculo, pois todos possuem cor, placa e numero_rodas
# Também são herdados os métodos
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    

    def ligar_motor(self):
        print("Ligando motor")


    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    # Construtor da classe Caminhao
    # Ao ser implementado, o construtor de Caminhao sobreescreve o construtor de Veiculo
    # Então é necessário referenciar a classe pai e passar o construtor para se obter os atributos novamente
    def __init__(self, cor, placa, numero_rodas,carregado=False):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado


    def esta_carregado(self):
        if self.carregado:
            print("Estou carregado")
        else:
            print("Não estou carregado")


# Todos os veiculos possuem os atributos definidos da classe pai
m1 = Motocicleta("preta", "abc1234", 2)
print(m1)
m1.ligar_motor()

c1 = Carro("azul", "def9876", 4)
print(c1)
c1.ligar_motor()

cm1 = Caminhao("vermelho", "klm3567", 6, True)
print(cm1)
cm1.ligar_motor()