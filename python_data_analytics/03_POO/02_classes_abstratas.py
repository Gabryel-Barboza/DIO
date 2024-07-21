from abc import ABC, abstractmethod

# Classes abstratas
# É um conceito definido pelas interfaces, chamadas de contratos em Python e nelas estão presentes métodos que serão implementados em classes herdeiras
# É feito com o módulo ABC
# Decoradores que transformam classes e método em abstratos


class ControleRemoto(ABC):
    # Classes abstratas não podem ser instanciadas
    @abstractmethod
    def ligar(self):
        pass 
    @abstractmethod
    def desligar(self):
        pass

    
    # Mesmo funcionamento de abstractmethod
    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    # Para poder instanciar, é obrigatório a implementação dos métodos
    def ligar(self):
        print("Ligando Tv")


    def desligar(self):
        print("Desligando Tv")


    @property
    def marca(self):
        return "LG"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando Ar Condicionado")


    def desligar(self):
        print("Desligando Ar Condicionado")
    

    @property
    def marca(self):
        return "Philco"


c1 = ControleTV()
c1.ligar()
c1.desligar()

c2 = ControleArCondicionado()
c2.ligar()
c2.desligar()
