# Versão final da aplicação utilizando ORM, veja outra implementação no commit anterior
# Veja o app_teste para explicações sobre o Flask e rotas

import os

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from src.models import db

# Instancia um objeto do Flask Migrate, sistema de versionamento para BD
migrate = Migrate()
# Instancia um objeto do Flask-JWT, sistema de autenticação
jwt = JWTManager()


# Método para criação da aplicação, App Factory
def create_app(environment: str = os.getenv('ENVIRONMENT')):
    # instância da aplicação flask, procura por um arquivo de configuração na pasta raiz do arquivo atual.
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(f'src.config.{environment.title()}Config')

    # Inicializa o app com a extensão do db
    db.init_app(app)
    # Inicializa o migrate na aplicação, para criar o diretório migrations utilize flask --app src.app db init
    migrate.init_app(app, db)
    # Criando o versionamento com flask --app src.app db migrate -m "msg commit"
    # Exclua o db.sqlite para criar a configuração, após execute flask --app src.app db upgrade
    # Utilize flask --app src.app db downgrade [versão] para retorna um commit

    # Inicializando JWT
    jwt.init_app(app)

    # Importando controladores e registrando blueprints
    from src.controllers import (
        auth_controller,
        post_controller,
        role_controller,
        user_controller,
    )

    app.register_blueprint(user_controller.app)
    app.register_blueprint(post_controller.app)
    app.register_blueprint(auth_controller.app)
    app.register_blueprint(role_controller.app)

    return app


# Inicialize a aplicação em modo debug:
# ENVIRONMENT=development poetry run flask --app src.app run --debug
