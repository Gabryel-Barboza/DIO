# Para esse segundo exemplo, é utilizado as propriedades para obter determinados atributos de uma classe

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    

    # Como esse bloco não está sendo utilizado para aplicar alguma lógica, é recomendado deixar apenas o atributo nome público e remover a propriedade
    # Caso contrário, é interessante para adicionar um setter especifíco ou outros
    @property
    def nome(self):
        return self._nome
    

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    

    # O código a seguir possui mesmo funcionamento, porém com o python o conceito de propriedades é o melhor utilizado
    # Forma utilizada em outras linguagens
    '''
    def get_nome(self):
        return self._nome
    

    def get_idade(self):
        return 2024 - self._ano_nascimento
    '''

pessoa = Pessoa("Gabryel", 2004)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")