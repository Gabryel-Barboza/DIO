import json

from flask import request
from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'PHP']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    
    def post(self):
        dados = json.loads(request.data)
        if dados not in lista_habilidades:
            lista_habilidades.append(dados)
        else:
            dados = "Habilidade já existente na lista!"
        return dados


class Habilidade(Resource):
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self, id):
        lista_habilidades.pop(id)
        return ''
