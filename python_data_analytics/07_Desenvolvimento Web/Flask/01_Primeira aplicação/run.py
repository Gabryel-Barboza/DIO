from flask import Flask
# Inicializando o flask nesse arquivo
app = Flask(__name__)

# Definindo função para ser executado na rota da URN, "/" para a base da URI, <numero> define um path param recebido na URN
# Método padrão GET, o navegador não conseguirá acessar sem esse método
@app.route('/<int:numero>', methods=["GET", "POST"])
def ola(numero):
    return f"Olá, Mundo! {numero}"


# Só executa o flask se arquivo executado como main, evita execução se importado para outros módulos
if __name__ == "__main__":
    # modo debug reinicializa automaticamente com alterações no código
    app.run(debug=True)

# Utilize o Postman para realizar os testes
