# Aplicações Restful, que seguem os princípios de APIs REST
# O módulo flask-restful implementa a aplicação para os padrões REST

import json

from flask import Flask, request
from flask_restful import Api, Resource
from habilidades import Habilidades, Habilidade

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {"id": 0, "nome": "Gabryel", "habilidades": ["Python", "Flask"]},
    {"id": 1, "nome": "Rafael", "habilidades": ["JavaScript", "Angular"]},
]

# Cria uma classe e define os métodos HTTP para ela
# Classe com métodos para manipulação de único desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {"status": "error", "mensagem": "ID de desenvolvedor não encontrada"}
        except Exception:
            response = {"status": "error", "mensagem": "Erro desconhecido. Procure o administrador da api"}
        # É automaticamente convertido para json pelo Flask
        return response

    def put(self, id):
        dados = json.loads(request.data)
        dados["id"] = desenvolvedores[id]["id"]
        try:
            desenvolvedores[id] = dados
            response = dados
        except IndexError:
            response = {"status": "error", "mensagem": "ID de desenvolvedor não encontrada"}
        except Exception:
            response = {"status": "error", "mensagem": "Erro desconhecido. Procure o administrador da api"}
        return response


    def delete(self, id):
        try:
            desenvolvedores[id].pop()
            response = ''
        except IndexError:
            response = {"status": "error", "mensagem": "ID de desenvolvedor não encontrada"}
        except Exception:
            response = {"status": "error", "mensagem": "Erro desconhecido. Procure o administrador da api"}
        return response


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        dados['id'] = len(desenvolvedores)
        desenvolvedores.append(dados)
        return dados
    

# Adicionando a rota para utilizar a classe
api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev/')
# Adicionando recursos de outros módulos
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(Habilidade, '/habilidades/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)