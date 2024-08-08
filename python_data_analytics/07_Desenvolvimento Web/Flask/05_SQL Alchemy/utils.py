from models import Pessoas


def inserir_pessoas():
    pessoa = Pessoas(nome='Gabryel', idade=20)
    pessoa.save()


def consultar_pessoa():
    pessoa = Pessoas.query.all()
    for p in pessoa:
        print(f'{p.nome}: {p.idade}')   
    

def alterar_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Gabryel').first()
    pessoa.idade = 19
    pessoa.save()


def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Gabryel').first()
    pessoa.delete()


if __name__ == '__main__':
    inserir_pessoas()
    consultar_pessoa()
    print('='*50)
    alterar_pessoa()
    excluir_pessoa()
    consultar_pessoa()

