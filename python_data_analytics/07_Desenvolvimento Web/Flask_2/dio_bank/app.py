# Curso de Python Backend Developer atualizado

# Utilizando poetry para instalação. poetry init -> poetry env info (path) -> f1 (select interpreter) -> poetry add flask

from flask import Flask

# Aplicação flask para o arquivo app.py
app = Flask(__name__)

# Rotas de URI para a execução da função
@app.route('/')
def hello_world():
    # retorno para o usuário
    return '<h1>Olá, mundo</h1>'

# Rodando a aplicação com o botão run ou poetry run flask --app app run --debug
# Código pin para terminal na aplicação web quando erro
