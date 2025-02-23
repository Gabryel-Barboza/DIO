# Primeiro arquivo executado pelo PyTest em um diretório e disponível para este escopo
# o app Flask vai estar disponível para os testes de integração
import pytest

from src.app import Role, User, create_app, db


# Fixtures são funções que podem ser detectadas em runtime e anexadas para outras funções
# Possuem escopos dos níveis: class, function(padrão), module, package, session, determinando até onde vão disponíveis
# Se escopo de função, para cada vez que é invocada cria app. Para módulo é apenas uma vez por módulo
@pytest.fixture()
def app():
    # Configurando app com banco de dados em memória
    app = create_app(
        {
            'SECRET_KEY': 'test',
            'SQLALCHEMY_DATABASE_URI': 'sqlite://',
            'JWT_SECRET_KEY': 'test',
        }
    )
    with app.app_context():
        # Criando modelos definidos
        db.create_all()
        # Retorna o app e interrompe a execução até a próxima chamada
        yield app
        # Retorna a execução a partir daqui


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture()
def access_token(client):
    role = Role(name='admin')
    db.session.add(role)
    db.session.commit()

    user = User(username='Gabryel', password='123', role_id=role.id)
    db.session.add(user)
    db.session.commit()

    # Criando token de autenticação
    result = client.post(
        '/auth/login/', json={'username': user.username, 'password': user.password}
    )

    return result.json['access_token']
