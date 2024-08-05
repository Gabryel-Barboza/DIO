# Desenvolva uma api que gerencie um cadastro de tarefas. A api terá uma lista de tarefas que deverá ter os seguintes campos: id, responsável, tarefa e status.
# A api deverá permitir listar todas as tarefas e também incluir novas tarefas. Também deve ser possivel consultar uma tarefa através do ID, alterar o status e excluir
# Nenhuma outra alteração deve ser permitida além do status da tarefa

import json

from flask import Flask, jsonify, request

app = Flask(__name__)
lista_tarefas = [{'id': 0, 'responsavel': 'Gabryel', 'tarefa': 'Criar a API', 'status': 'pendente'}]

# Retorna todas as tarefas
@app.route('/', methods=['GET'])
def listar_tarefas():
    return jsonify(lista_tarefas)

# Recebe o id e retorna a respectiva tarefa se Get, se Patch altera o status da tarefa e Delete para excluir a tarefa
@app.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def listar_tarefa(id):
    try:
        if request.method == 'GET':
            return jsonify(lista_tarefas[id])
        
        elif request.method == 'PATCH':
            dados = json.loads(request.data)
            if len(dados.keys()) > 1 or dados.get('status', {}) == {}:
                return 'Não é permitido a alteração de outros campos além do status da tarefa!'
            else:
                lista_tarefas[id]['status'] = dados['status']
                return jsonify(lista_tarefas[id])
            
        else:
            lista_tarefas.pop(id)
            return ''
    except IndexError:
        return 'ID não encontrado!' 
    except Exception:
        return 'Erro desconhecido!'

# Cria uma tarefa nova se no mesmo padrão de json
@app.route('/', methods=['POST'])
def criar_tarefa():
    tarefa = json.loads(request.data)
    tarefa['id'] = len(lista_tarefas)
    if len(tarefa.keys()) < len(lista_tarefas[0].keys()):
        return 'Quantidade de campos inválida, verificar os campos corretos para inserir.' 
    for key in lista_tarefas[0].keys():
        if key not in tarefa.keys():
            return 'Campos inválidos, verificar os campos corretos para inserir.'
    else:
        lista_tarefas.append(tarefa)
        return jsonify(tarefa)


if __name__ == '__main__':
    app.run(debug=True)
