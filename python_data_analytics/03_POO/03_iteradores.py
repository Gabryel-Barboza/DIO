# Iteradores
# São objetos iteráveis, ou seja, que possuem uma sequência de dados que podem ser lidos
# Classes iteradoras possuem os métodos especiais __iter__ e __next__()

class MeuIterador():
    # Inicializando iterador, um contador é necessário para saber a posição do iterável
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0


    # Retorna o próprio objeto
    def __iter__(self):
        return self
        # Return None


    # Retorna o valor da posição definida
    def __next__(self):
        # Tente executar
        try:
            # recebe número da posição indicada na lista. Causa erro se posição inválida
            numero = self.numeros[self.contador]
            self.contador += 1
            # Retorno do valor da lista * 2
            return numero * 2
        # Se erro, execute isso
        except:
            # Parar iteração
            raise StopIteration


for i in MeuIterador(numeros = [1, 2, 3]):
    print(i)