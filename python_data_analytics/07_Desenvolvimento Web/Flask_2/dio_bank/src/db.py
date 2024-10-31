# Versão antiga, utilizando ORM para criar o DB agora
# Aplicação para conexão com o database da documentação Flask
import sqlite3

import click
from flask import current_app, g

# g = variável global da aplicação Flask, adiciona o objeto do banco de dados


def get_db():
    # Cria a conexão se db não existir em g
    if 'db' not in g:
        # Adiciona à configuração do app o db, tipo sqlite3
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


# Se db existir, fecha a conexão
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


# Inicializa o banco de dados com o schema definido, apaga as tabelas sempre que iniciado
def init_db():
    db = get_db()
    # Cria as tabelas com o SQL no arquivo schema.sql
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


# Cria um comando de CLI chamado init-db
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    click.echo('Initialized the database.')


# Adiciona eventos para a aplicação
def init_app(app):
    # Quando o contexto de app for encerrado, chama a função definida
    app.teardown_appcontext(close_db)
    # Adicione ao CLI da aplicação o comando
    app.cli.add_command(init_db_command)
