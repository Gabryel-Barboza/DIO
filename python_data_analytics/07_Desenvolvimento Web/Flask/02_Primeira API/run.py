import json

from flask import Flask, jsonify, request

app = Flask(__name__)


# Recomendado trabalhar com JSONs ou XMLs, para retornar jsons utilizar o módulo jsonify
# Tipagem de parâmetros, por padrão string
@app.route("/<int:id>")
def pessoas(id):
    return jsonify({"id": id, "nome": "Gabryel"})


# Realizando uma soma com os parâmetros de URN
@app.route("/soma/<int:n1>/<int:n2>")
def soma(n1, n2):
    return jsonify({"Soma": n1 + n2})


# Enviando informações com método post utilizando request
@app.route("/soma", methods=["GET", "POST"])
def soma_post():
    if request.method == "GET":
        return jsonify({"Soma": "Nenhum valor encontrado"})

    elif request.method == "POST":
        # Recebe os dados da requisição, utiliza o módulo json para ler o json corretamente caso contrário será tratado como string
        dados = json.loads(request.data)
        print(dados)
        total = sum(dados["valores"])
        # Retorna os dados após a soma
        return jsonify({"soma": total})


if __name__ == "__main__":
    app.run(debug=True)

# Instale o módulo requests para realizar requisições pelo console ou em programas python. Requests != flask.request
# Comando executado no terminal
"""
import requests
import json
response = requests.get("http://127.0.0.1:5000/soma")
print(response.text)
dados = response.json()
print(dados["soma"])

response = requests.post("http://127.0.0.1:5000/soma", json={"valores": [20, 20, 20]})
dados = response.json()
print(dados)
"""
