# Controllers ou orquestradores das rotas, conduzindo a aplicação para determinados métodos
# Usuários do site de blogs

from http import HTTPStatus

# Blueprints no Flask
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from sqlalchemy import inspect

from src.app import User, db
from src.utils import requires_role

# Instanciando uma blueprint com o identificador user, caminho de importação ao arquivo atual e a rota em users
# No padrão REST as rotas são nomeadas no plural
app = Blueprint('user', __name__, url_prefix='/users')


def _create_user():
    data = request.json
    user = User(
        username=data['username'],
        password=data['password'],
        role_id=data['role_id'],
    )
    db.session.add(user)
    db.session.commit()


def _list_users():
    # Realiza a query no database e retorna um objeto cursor iterável
    query = db.select(User)

    # Retorna um objeto de scalars, apenas com os valores do objeto pai e não uma tupla de objetos
    users = db.session.execute(query).scalars()
    # print(list(results))

    # Para a lista ser serializável, é necessário pegar os valores do objeto. O jsonify não consegue extrair os valores automaticamente
    return [
        {
            'id': user.id,
            'username': user.username,
            'role': {
                'id': user.role_id,
                'role': user.role.name,
            },
        }
        for user in users
    ]


# Se a rota da blueprint já possui o prefixo /users, então podemos definir apenas um / no decorador, ficando /users/ na rota final'
# Rota para listar ou criar usuários
@app.route('/', methods=['GET', 'POST'])
@jwt_required()  # Precisa estar autenticado para acessar
@requires_role('admin')  # Precisa possuir a determinada permissão
def handle_user():
    if request.method == 'POST':
        _create_user()
        # Retornando um status code para o cliente, hardcoded 201 ou descritivo com o objeto de http
        return {'message': 'User created'}, HTTPStatus.CREATED
    else:
        return {
            'users': _list_users(),
        }  # Status code padrão 200


# Rota de requisição de usuário por id
@app.route('/<int:user_id>')
@jwt_required()
def get_user(user_id):
    user = db.get_or_404(User, user_id)
    return {
        'id': user.id,
        'username': user.username,
        'role': {
            'id': user.role_id,
            'role': user.role.name,
        },
    }


# Rota para alteração de usuário por id, método PATCH é mais utilizado para alterações, pois são alterações parciais de um elemento e não completas
@app.route('/<int:user_id>', methods=['PATCH'])
@jwt_required()
@requires_role('admin')
def update_user(user_id):
    user = db.get_or_404(User, user_id)  # Adiciona o user a sessão do db
    data = request.json

    # Atualizando as colunas dinamicamente
    mapper = inspect(User)
    for column in mapper.attrs:
        if column.key in data:
            setattr(user, column.key, data[column.key])
    db.session.commit()

    # Atualizando as colunas hardcoded:
    """if 'username' in data:
        user.username = data['username']
        #db.session.add(user) # Não é necessário um add para objetos já na sessão
        db.session.commit()
    """
    return {'message': 'User patched'}


# Rota para exclusão de usuário por id
@app.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
@requires_role('admin')
def remove_user(user_id):
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()
    return {}, HTTPStatus.NO_CONTENT


# Registrando blueprint no módulo principal
