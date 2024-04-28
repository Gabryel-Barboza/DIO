# Polimorfismo
len("python")
len([10, 20, 30])
# Polimorfismo de sobrecarga

# Várias formas de uma mesma função
# Mesmo nome, assinaturas diferentes
# Assinaturas de métodos são diferenciadas pelos parâmetros, dependendo da quantidade e do tipo de parâmetro.

print("Python")
msg = "Python"
print(3, 2, 1)
print(msg)


# Polimorfismo de sobreescrita
# Mesmo nome e assinatura, classes diferentes
# Sobrescreve o método herdado da classe pai
class Passaro:
    def voar(self): 
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal voa")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")


# FIXME - Exemplo ruim
class Aviao(Passaro):
    def voar(self):
        print("Avião decolando...")


def plano_de_voo(passaro):
    passaro.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())
