# Versão final da aplicação utilizando ORM, veja outra implementação no commit anterior
# Veja o app_teste para explicações sobre o Flask e rotas

import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, json
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

from src.models import db

# Instancia um sistema de versionamento para BD
migrate = Migrate()
# Instancia um sistema de autenticação
jwt = JWTManager()
# Instancia um sistema de criptografias
bcrypt = Bcrypt()
# Instancia um sistema de serialização de dados
ma = Marshmallow()

# Criando Documentação da API do Swagger
spec = APISpec(
    title='DIO Bank',
    version='1.0.0',
    openapi_version='3.0.3',
    info={'description': 'A API to test the Flask framework and extensions'},
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


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
    # Inicializando B-crypt
    bcrypt.init_app(app)
    # Inicializando Marshmallow
    ma.init_app(app)

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

    @app.route('/docs')
    def docs():
        return (
            spec.path(view=user_controller.get_user)
            .path(view=user_controller.remove_user)
            .to_dict()
        )

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Return JSON instead of HTML for HTTP errors."""
        # start with the correct headers and status code from the error
        response = e.get_response()
        # replace the body with JSON
        response.data = json.dumps(
            {
                'code': e.code,
                'name': e.name,
                'description': e.description,
            }
        )
        response.content_type = 'application/json'
        return response

    return app


# Inicialize a aplicação em modo debug:
# ENVIRONMENT=development poetry run flask --app src.app run --debug
