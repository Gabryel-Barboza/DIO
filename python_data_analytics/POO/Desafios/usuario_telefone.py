# Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone. Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe. Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos, sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.
class UsuarioTelefone:
  def __init__(self, nome, numero, plano):
    self._nome = nome
    self._numero = numero
    self._plano = plano
  # O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.
    
  @property
  def nome(self):
    return self._nome
    
  
  @property
  def numero(self):
    return self._numero
    
    
  @property
  def plano(self):
    return self._plano
    

  # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
  def __str__(self):
      return f"Usuário {self.nome} criado com sucesso."


# Entrada:
nome = input()  
numero = input()  
plano = input()
usuario = UsuarioTelefone(nome, numero, plano)

print(usuario)