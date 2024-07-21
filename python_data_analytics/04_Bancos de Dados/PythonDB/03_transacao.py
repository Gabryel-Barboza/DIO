import sqlite3

conexao = sqlite3.connect("./PythonDB/meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

# O 2º insert a seguir ocorrerá um erro, porém o 1º ainda será executado
# Para resolver esse problema, utilizamos a estrutura try-except

try:
    cursor.execute("INSERT INTO clientes ( nome, email) VALUES (?, ?)", ("Test1e", "teste1@email.com"))

    '''conexao.commit()'''

    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?, ?)", ("1", "Teste2", "teste@email.com"))

    conexao.commit()
except Exception as e:
    print(e)
    # Retornando ao estado antes das alterações
    conexao.rollback()
finally:
    # É muito utilizado o bloco finally para executar o commit, porém ele não irá tratar os erros que podem acontecer no comando
    # Por isso, o commit é mais interessante de ser realizado ao final do bloco try
    '''conexao.commit()'''
    pass