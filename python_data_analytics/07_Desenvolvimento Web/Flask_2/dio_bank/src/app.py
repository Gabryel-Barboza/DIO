# Versão final da aplicação utilizando ORM, veja outra implementação no commit anterior
# Veja o app_teste para explicações sobre o Flask e rotas

from datetime import datetime

import click
import sqlalchemy as sa
from flask import Flask, current_app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


# Instancia uma engine SQLAlchemy com o modelo
db = SQLAlchemy(model_class=Base)
# Instancia um objeto do Flask Migrate
migrate = Migrate()


# Implementando os modelos de tabelas, o Flask adiciona automaticamente algumas características como __tablename__ e relationship()
class User(db.Model):
    # Utilizando estruturas de dados com a classe Mapped, versão moderna do SQLAlchemy
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    active: Mapped[bool] = mapped_column(sa.Boolean, default=True)

    # O método de representação da classe para prints, !r para o formatador chamar o método __repr__ antes de exibir o atributo. Outras flags como !s para __str__ e !a para ascii
    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username!r}, active={self.active!r})"


class Post(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(sa.String, nullable=False)
    body: Mapped[str] = mapped_column(sa.String, nullable=False)
    # Utiliza o tipo de dados datetime e recebe uma coluna com a hora atual. Func são as funções utilitárias do SQLAlchemy.
    created: Mapped[datetime] = mapped_column(sa.DateTime, server_default=sa.func.now())
    author_id: Mapped[int] = mapped_column(sa.ForeignKey('user.id'))

    def __repr__(self):
        return f"Post(id={self.id!r}, title={self.title!r}, author_id={self.author_id!r})"


# Registrando o comando init-db para inicialização do banco de dados
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    global db
    with current_app.app_context():
        db.create_all()
    click.echo('Initialized the database.')


# Método para criação da aplicação, App Factory da documentação
def create_app(test_config=None):
    # instância da aplicação flask, procura por um arquivo de configuração na pasta raíz do arquivo atual.
    app = Flask(__name__, instance_relative_config=True)
    # Configura variáveis de ambiente e o caminho do database
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI="sqlite:///blog.sqlite",
    )

    if test_config is None:
        # Se não estiver em ambiente de testes, carregue o arquivo de configuração
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carregar a configuração para testes
        app.config.from_mapping(test_config)

    # Adiciona o CLI à aplicação e inicializa o app com a extensão do db
    app.cli.add_command(init_db_command)
    db.init_app(app)
    
    # Inicializa o migrate na aplicação, para criar o diretório migrations utilize flask --app src.app db init
    migrate.init_app(app, db)
    # Criando o versionamento com flask --app src.app db migrate -m "msg commit"
    # Exclua o db.sqlite para criar a configuração, após execute flask --app src.app db upgrade
    # Utilize flask --app src.app db downgrade [versão] para retorna um commit

    # Registrando controladores e blueprints
    from src.controllers import post, user
    app.register_blueprint(user.app)
    app.register_blueprint(post.app)

    return app


# Inicialize o database com o comando init-db ao final:
# poetry run flask --app src.app init-db
# Inicialize a aplicação:
# poetry run flask --app src.app run --debug

