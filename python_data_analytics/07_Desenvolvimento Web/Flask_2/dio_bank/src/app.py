# Veja o app_teste para explicações sobre o projeto

import os

from flask import Flask


# Método para criação da aplicação, App Factory da documentação
def create_app(test_config=None):
    # instância da aplicação flask, procura por um arquivo de configuração na pasta raíz do arquivo atual.
    app = Flask(__name__, instance_relative_config=True)
    # Configura variáveis de ambiente e o caminho do database
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='diobank.sqlite',
    )

    if test_config is None:
        # Se não estiver em ambiente de testes, carregue o arquivo de configuração
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carregar a configuração para testes
        app.config.from_mapping(test_config)

    # Importa o módulo db do pacote atual
    from . import db
    db.init_app(app)

    return app


# Inicialize a aplicação com o comando init-db ao final:
# poetry run flask --app dio_bank.src.app init-db
