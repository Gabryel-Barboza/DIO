# Python DB API
# É a interface de integração com bancos de dados relacionais
# Permite realizar as operações de bancos de dados através do Python. Possui integração com diversos bancos de dados, através de conectores baixados na internet.
# Procure por Python "SGDB" Connector para utilizar outros bancos de dados. O sqlite já está disponivel por padrão no python

import sqlite3

# Conectando ao banco de dados, extensão convencionada padrão para bancos de dados ou .sqlite
conexao = sqlite3.connect("./PythonDB/meu_banco.db")
print(conexao)

# Baixe uma extensão como o SQLite Viewer para visualizar o arquivo no VsCode

# EXECUTANDO QUERYS SQL

cursor = conexao.cursor()


def criar_tabela(cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150));"
    )


# INSERTS


def inserir_registro(conexao, cursor, data):

    # O comando a seguir funciona, porém é propício aos ataques SQL Injections
    """
    cursor.execute(f"INSERT INTO clientes (nome, email) VALUES ('{nome}', '{email}');")
    """

    # Uma melhor maneira de realizar essa ação é com "querys preparadas", recebendo uma tupla de dados

    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)

    # Os valores não serão inseridos ainda, isso pois é necessário realizar uma ação de commit para qualquer query de inserção, alteração e entre outros..
    # Isso visa realizar querys em transações única

    conexao.commit()


# INSERTS em lotes
def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?);", dados)
    # O arquivo irá receber uma lista de tuplas
    conexao.commit()


# UPDATES
def atualizar_registros(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()


# DELETES
def deletar_registros(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()


# CONSULTAS/SELECTS


def recuperar_cliente(cursor, id):
    data = (id,)
    cursor.execute("SELECT * FROM clientes WHERE id=?;", data)
    # Para retornar o resultado, utilize o método fetchone para uma linha ou fetchall para todas as linhas do SELECT
    # Retorna None se não encontrar
    return cursor.fetchone()


def recuperar_clientes(cursor):
    cursor.execute("SELECT * FROM clientes ORDER BY nome")
    return cursor.fetchall()


# MAIN

# inserir_registro(conexao, cursor, data=("Kaio", "rafael@email.com"))
# atualizar_registros(conexao, cursor, "Rafael", "rafael@email.com", "2")
# inserir_registro(conexao, cursor, ("Kaio", "kaio@email.com"))
# deletar_registros(conexao, cursor, 3)
# atualizar_registros(conexao, cursor, "Karynne", "karynne@email.com", 6)

dados = [
    ("Cleber", "cleber@email.com"),
    ("Patricia", "patricia@email.com"),
    ("karynne", "karynne@email.com"),
]
# inserir_muitos(conexao, cursor, dados)
# O mesmo que um loop, porém com uma única transação, ao invés de várias de uma vez
"""
for dado in dados:
    inserir_registro(conexao, cursor, dado[0], dado[1])
"""

cliente = recuperar_cliente(cursor, 1)
print(cliente)
clientes = recuperar_clientes(cursor)
print(clientes)

#print(cliente["nome"])

# Altera o row factory para uma instância de sqlite Row
cursor.row_factory = sqlite3.Row
cliente = recuperar_cliente(cursor, 2)
print(cliente["nome"])

