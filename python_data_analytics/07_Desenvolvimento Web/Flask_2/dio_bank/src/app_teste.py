# Exercícios do curso atualizado Python Backend Developer

# Utilizando poetry para instalação. poetry init -> poetry env info (path) -> f1 (select interpreter) -> poetry add flask

from flask import Flask, request, url_for

# Aplicação flask para o arquivo app.py
app = Flask(__name__)


# Rotas de URI para a execução da função ou endpoints
@app.route('/')
def hello_world():
    # retorno para o usuário
    return '<h1>Olá, mundo</h1>'


# Métodos devem possuir nomes diferentes
@app.route('/olamundo/')
def ola_mundo():
    return '<h1>Olá, mundo!</h1>'


# Regras com variáveis
# Parâmetros recebidos no path
@app.route('/olamundo/<user>')
def ola_usuario(user):
    return f'<h1> Olá, {user}</h1>'


# Tipagem dos parâmetros recebidos, por padrão é str
@app.route('/calculo/<int:n1>/<int:n2>')
def calcular(n1, n2):
    return f'A soma de {n1} e {n2} é: {n1 + n2}'


# Redirecionamento de rotas
# Existe distinção entre rotas com ou sem a / ao final, onde um é redirecionado para /about/ se omitida a barra na URI inserida
@app.route('/about/')
def about():
    return 'Página sobre nós'


# Nesse caso se a barra for inserida no caminho, a página não é encontrada. É obrigado inserir o caminho corretamente sem a barra ao final.
# Permite identificar recursos
@app.route('/project')
def project():
    return 'Página do projeto'


with app.test_request_context():
    # Retornando a URL dos métodos dinâmicamente, permite alterar as rotas e receber a URL correta pelo nome do método. Recomendado no lugar de hardcoded URLs
    print(url_for('ola_usuario', user='Gabryel'))
    print(url_for('about'))
    print(url_for('project'))


# Métodos HTTP
# Utilize o Postman ou Insomnia para outros métodos além de GET
# methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'], por padrão apenas GET.
@app.route('/metodos/', methods=['GET', 'POST'])
def metodos():
    # Verificando tipo de método recebido na rota com request
    if request.method == 'GET':
        # Por que retornar um dicionario? Por convenção é utilizado arquivos JSON em APIs, por algumas vantagens ao XML, o Flask converte automaticamente dicionários para Json.
        # Utiliza-se o método jsonify do Flask automaticamente
        return {'status': 'sucesso', 'mensagem': 'Olá, mundo!'}
    elif request.method == 'POST':
        return {'status': 'sucesso', 'mensagem': 'Olá, POST!'}


# Rodando a aplicação com o botão run ou poetry run flask --app src.app run --debug. O caminho é definido por '.'
# Código pin para terminal na aplicação web quando erro

# Criando a aplicação com o padrão de arquitetura MVC com 4 camadas: controller, model, view e repository
