from http import HTTPStatus

from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from src.app.app import bcrypt
from src.models import User, db

app = Blueprint('auth', __name__, url_prefix='/auth')


def _check_password(password_hash, password_raw):
    return bcrypt.check_password_hash(password_hash, password_raw)


# Rota para autenticação de usuários
@app.route('/login/', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    query = db.select(User).where(User.username == username)
    user = db.session.execute(query).scalar()

    # Verifica se usuário existe e se senha é a mesma criptografada
    if not user or not _check_password(user.password, password):
        return {'msg': 'Bad username or password'}, HTTPStatus.UNAUTHORIZED

    # Retorna o token de acesso
    # O token pode ser decodificado em jwt.io, não retorne informações confidenciais.
    access_token = create_access_token(identity=str(user.id))
    return {'access_token': access_token}
