from flask import Flask, request
from flask_restful import Api, Resource
from models import Atividades, Pessoas

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada'
            }
        return response
    
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
        }
        return response
    
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        return {'status':'sucesso', 'mensagem':'Pessoa excluída com sucesso'}


class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'nome': p.nome, 'idade': p.idade, 'id': p.id} for p in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {'nome': pessoa.nome, 'idade': pessoa.idade, 'id': pessoa.id}
        return response


class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'atividade': a.nome, 'pessoa': a.pessoa.nome, 'id': a.id} for a in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)
