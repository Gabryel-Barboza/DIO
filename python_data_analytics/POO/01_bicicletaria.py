class Bicicleta:
    # pass

    # Construtor
    # self ou this, apenas convenção qualquer nome pode ser utilizado
    # 1º argumento necessário para a instância
    # __método especial__
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor


    def buzinar(self):
        print("Plim Plim")


    def parar(self):
        print("Parando a bicicleta")
        print("Parada")


    def correr(self):
        print("Vrummm....")


    def get_cor(self):
        return self.cor

    
    # O mesmo que toString do Java, utilizado para retornar os atributos de uma classe
    '''def __str__(self):
        return f"Bicicleta: Cor: {self.cor}, Modelo: {self.modelo}, Ano: {self.ano}, Valor: {self.valor}"
        '''
    
    
    def __str__(self):
        # Instância, classe, nome da classe
        # Forma preferível, se a classe mudar o código continua funcionando
        # __dict__ retorna um dicionário com os atributos
        return f"{self.__class__.__name__}: {' '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

# O método abaixo é o mesmo que a chamada da instância resumida acima. Implícita 
b2 = Bicicleta("verde", "adidas", 2000, 189)
Bicicleta.buzinar(b2)

b2.get_cor()
print(b2.__str__())
# ou apenas
print(b2)
# Isso é possivel após a definição do método str