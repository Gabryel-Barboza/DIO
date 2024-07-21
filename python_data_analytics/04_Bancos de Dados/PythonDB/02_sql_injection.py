import sqlite3

conexao = sqlite3.connect("./PythonDB/meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


# Um dos problemas causadores de SQL Injection é a concatenação na string, permitindo que o usuário malicioso coloque comandos indo além do permitido
# Como exemplo, um comando com id e outra condição: 1 OR 1=1

id_cliente = input("Informe o id: ")
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")
clientes = cursor.fetchall()
# Será retornada toda a base de dados
for cliente in clientes:
    print(dict(cliente))


# Por isso, utilize as ? nas querys parametrizadas para tratar esse problema, impedindo a utilização de comandos SQL
id_cliente = input("Informe o id: ")
cursor.execute(f"SELECT * FROM clientes WHERE id=?", (id_cliente,))
clientes = cursor.fetchall()
for cliente in clientes:
    print(dict(cliente))
