# Vamos agora, adicionar uma funcionalidade à classe UsuarioTelefone, que realizar chamadas para outros usuários. Cada chamada terá uma duração em minutos e o custo será deduzido do saldo do usuário, suponha o custo de $0.10 por minuto. Você pode criar um método fazer_chamada que vai permitir que o usuário faça a chamada, ele vai receber o destinatario e duracao como parâmetros. Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano', além de adicionar o método deduzir_saldo para deduzir o valor do saldo do plano e depois retorne uma mensagem adequada como mostra no exemplo a baixo.


# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

# Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:

    def fazer_chamada(self, destinatario, duracao):
        if self.custo_chamada(duracao):
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.verificar_saldo()}"
        else:
            return "Saldo insuficiente para fazer a chamada."
      
# Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':

    def custo_chamada(self, duracao):
        custo = Plano.custo_chamada(duracao)
# Verifique se o saldo do plano é suficiente para a chamada.
        if (self.plano.verificar_saldo() >= custo):
# Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.
            self.plano.deduzir_saldo(custo)
# E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:
            return True

          
# Classe Plano, ela representa o plano de um usuário de telefone:

class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

# Crie um método para verificar_saldo e retorne o saldo atual:
    def verificar_saldo(self):
        return self.saldo
# Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:

    @classmethod
    def custo_chamada(self, minutos):
        custo = minutos * 0.10
        return custo
        
# Crie um método deduzir_saldo para deduz o valor do saldo do plano:

    def deduzir_saldo(self, custo):
        self.saldo -= custo
        return True


# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:

nome = input("Nome:")
numero = input("Número:")
saldo_inicial = float(input("Saldo:"))

# Objeto de UsuarioPrePago com os dados fornecidos:

usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input("Número de Destino:")
duracao = int(input("Duração da Chamada:"))

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:

print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
