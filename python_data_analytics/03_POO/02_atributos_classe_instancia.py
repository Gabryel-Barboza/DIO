# Atributos de classe são definidos fora de objetos e compartilhadas entre eles, enquanto atributos de objeto são únicas para cada objeto

class Estudante:
    # Atributo de classe
    escola = "DIO"

    def __init__(self, nome, matricula):
        # Atributo de objeto
        self.nome = nome
        self.matricula = matricula


    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    

def mostrar_valores(*objts):
    for obj in objts:
        print(obj)

aluno_1 = Estudante("Gabryel", 1)
aluno_2 = Estudante("Maria", 2)

aluno_1.matricula = 3
mostrar_valores(aluno_1, aluno_2)
print("="*20)
Estudante.escola = "Python"
mostrar_valores(aluno_1, aluno_2)