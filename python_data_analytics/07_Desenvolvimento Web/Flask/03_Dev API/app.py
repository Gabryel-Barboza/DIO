import json

from flask import Flask, jsonify, request

app = Flask(__name__)

desenvolvedores = [
    {"id": 0, "nome": "Gabryel", "habilidades": ["Python", "Flask"]},
    {"id": 1, "nome": "Rafael", "habilidades": ["JavaScript", "Angular"]},
]


@app.route("/dev/<int:id>/", methods=["GET", "PUT", "DELETE"])
def desenvolvedor(id):
    # Retorna um json com o id requisitado
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "ID de desenvolvedor não encontrada"
            response = {"status": "error", "mensagem": mensagem}
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrador da api"
            response = {"status": "error", "mensagem": mensagem}
        return jsonify(response)

    # Altera o id requisitado para o json recebido
    elif request.method == "PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    # Deleta o id requisitado
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({"status": "sucesso", "mensagem": "Registro excluído"})


@app.route("/dev", methods=["GET", "POST"])
def lista_desenvolvedores():
    # Retorna uma lista de registros
    if request.method == "GET":
        return jsonify(desenvolvedores)
    # Adiciona um novo registro
    elif request.method == "POST":
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])


if __name__ == "__main__":
    app.run(debug=True)
