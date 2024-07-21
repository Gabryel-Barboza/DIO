# Encapsulamento
# O encapsulamento em Python é convencional, diferentemente de outras linguagens, no Python não existe palavra reservada e por isso todos as classes são públicas
# No entanto, quando algum método ou atributo se inicia com "_", isso quer dizer que não deve ser acessado diretamente, mas sim utilizar os métodos disponíveis para isso

class Conta:
    def __init__(self, agencia, saldo=0):
        self._saldo = saldo
        self.agencia = agencia

    
    def depositar(self, valor):
        self._saldo += valor


    def sacar(self, valor):
        self._saldo -= valor


    def mostrar_saldo(self):
        return self._saldo
    


conta = Conta("0001", 100)
# O comando abaixo funciona, porém não segue a convenção do encapsulamento
print(conta._saldo)
#conta._saldo -= 10
conta.sacar(10)
print(conta.mostrar_saldo())

