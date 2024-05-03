import csv
from abc import ABC, abstractmethod
from datetime import datetime, timedelta, timezone
from pathlib import Path
from time import sleep

# Modifique o decorador de log para salvar as informações em um arquivo
# O decorador deve registrar o seguinte para cada chamada de função:
# Data e hora atuais, nome da função, argumentos da função, valor retornado pela função
# Deve ser chamado de log.txt, caso já exista os logs devem ser adicionados ao final do arquivo
# Cada entrada de log deve estar em uma nova linha
# Extra: Salvar clientes e contas em arquivos csv e importar na inicialização do programa


class Cliente:
    # Construtor inicial cliente
    def __init__(self, **kw):
        self.endereco = kw["endereco"]
        self.contas = []

    # Realiza as operações de depósito e saque. Utiliza cliente, Deposito ou Saque e Conta de Cliente

    def realizar_transacao(self, transacao, conta):
        transacoes_diarias = len(conta.historico.transacoes_diarias())
        if transacoes_diarias == 10:
            print(
                f"Limite de transações diárias excedido! {transacoes_diarias} operações realizadas."
            )
            return False
        elif transacao.registrar(conta):
            return True
        return False

    # Instanciar ContaCorrente e adicionar a contas, retorno para tratar em cadastro()

    def adicionar_conta(self, **kwargs):
        # Necessário receber argumentos por key-value com os campos entre [""] a seguir
        conta = ContaCorrente(
            cliente=self,
            saldo=kwargs["saldo"],
            numero=kwargs["numero"],
            limite=kwargs["limite"],
            limite_saques=kwargs["limite_saques"],
            saques_diarios=kwargs["saques_diarios"],
            historico=Historico(),
        )
        self.contas.append(conta)
        return conta

    # Método para retornar as contas para cada instância

    def mostrar_contas(self):
        for conta in ContaIterador(self.contas):
            print(conta)

    def __str__(self):
        return f"Endereço : {self.endereco}, Contas: {len(self.contas)}"


class PessoaFisica(Cliente):
    # Instancia padrão para Cliente
    def __init__(self, **kw):
        super().__init__(**kw)
        self.cpf = int(kw["cpf"])
        self.nome = kw["nome"]
        self.data_nascimento = kw["data_nascimento"]

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.cpf}"

    def __str__(self):
        return (
            ", ".join(
                [
                    f"Nome : {self.nome}",
                    f"CPF : {self.cpf}",
                    f"Data de nascimento : {self.data_nascimento}, ",
                ]
            )
            + super().__str__()
        )


class Conta:
    # Criando conta com saldo e cliente recebidos de **kw e número de conta sequencial
    def __init__(self, **kw):
        self.cliente = kw["cliente"]
        self._saldo = float(kw["saldo"])
        self._agencia = "0001"
        self._numero = int(kw["numero"])
        self._historico = kw["historico"]

    # Propriedades
    @property
    def saldo(self):
        return self._saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    @property
    def historico(self):
        return self._historico

    # método de classe para adicionar nova conta a cliente existente
    # herdado por conta corrente
    @classmethod
    def nova_conta(cls, **kw):
        return cls(**kw)

    # Depositar e Sacar de Conta
    # Verificar as restrições impostas em desafios anteriores
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        else:
            print("Valor inválido")
        return False

    # Veja em main() para realizar as operações
    def sacar(self, valor):
        # Se valor negativo
        if valor <= 0:
            print("Valor inválido")
        # Se valor maior que saldo da conta
        elif valor > self.saldo:
            print("Saldo Insuficiente")
        else:
            self._saldo -= valor
            return True
        return False

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'Número da conta : {self.numero}', f'Saldo : {self.saldo}', f'Agência : {self.agencia}', f'Histórico de Transações : {self.historico.historico}'])}"


class ContaCorrente(Conta):
    # Criando ContaCorrente com seus atributos e instanciando Conta
    def __init__(self, **kw):
        super().__init__(**kw)
        self.limite = int(kw["limite"])
        self.LIMITE_SAQUES = int(kw["limite_saques"])
        self.saques_diario = int(kw["saques_diarios"])

    def sacar(self, valor):
        # Se quantidade de saques diário maior que o limite diário
        if self.saques_diario < self.LIMITE_SAQUES:
            # Se valor maior limite de saque
            if valor > self.limite:
                print(f"Saque máximo de R${self.limite:.2f}")
            else:
                self.saques_diario += 1
                return super().sacar(valor)
        else:
            print("Limite de saques diários atingido!")
        return False

    def __repr__(self):
        return f"{self.__class__.__name__}:{self.saldo}:{self.numero}:{self.limite}:{self.LIMITE_SAQUES}:{self.saques_diario}"


class Transacao(ABC):
    # Interface
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    # Realiza operação de depositar em conta, se retornado sucesso adiciona ao histórico
    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)
            return True


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    # Realiza operação de saque em conta, se retornado sucesso adiciona ao histórico
    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)
            return True


class Historico:
    # Histórico de transações realizadas
    def __init__(self):
        self._historico = []

    # Propriedades para retorno da quantidade de transações feitas
    @property
    def historico(self):
        return len(self._historico)

    # Recebendo transação e guardando um dicionário no histórico
    def adicionar_transacao(self, transacao):
        self._historico.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            }
        )

    def gerador_historico(self, tipo=None):
        # Retorna uma transação do tipo definido pelo parametro ou todas se None
        for transacao in self._historico:
            if tipo is None or transacao["tipo"] == tipo:
                yield transacao

    # Retornar a quantidade de transações diárias
    def transacoes_diarias(self):
        data_hoje = datetime.now().date()
        # Retorna uma lista com transações que correspondam a data_hoje
        # Pega a string de transacao["data"], converte para um objeto datetime e compara a sua parte de data com data_hoje
        transacao_diaria = [
            (
                transacao
                if datetime.strptime(transacao["data"], "%d/%m/%Y %H:%M").date()
                == data_hoje
                else None
            )
            for transacao in self._historico
        ]
        return transacao_diaria


class ContaIterador:
    # Iterador para as contas de Cliente
    def __init__(self, contas: list):
        self.contas = contas
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self.contador]
            self.contador += 1
            return conta
        except IndexError:
            raise StopIteration


# Programa principal


def retornar_cliente(clientes, cpf):
    # Retorna um cliente especifico de uma lista
    if clientes:
        for cliente in clientes:
            if cpf == cliente.cpf:
                return cliente
    return None


def retornar_conta(nro_conta, contas):
    # Retorna uma conta especifica de uma lista
    if contas:
        for conta in contas:
            if conta.numero == nro_conta:
                return conta
    return None


# Decorador para retornar a operação e hora da operação


def gerador_log(funcao):
    def criar_log(*args):
        retorno = funcao(*args)
        # Pode retornar valores ou booleans
        # Se operação bem sucedida criar um log
        if retorno:

            # Data e hora com fuso-horário GMT-3.
            # Não foi utilizado Pytz apenas para permitir sua execução a qualquer momento sem necessidade de instalação de terceiros
            data = datetime.now(timezone(timedelta(hours=-3), "BRT"))

            # Se arquivo não existir, cria um novo e retorna o arquivo aberto
            with abrir_arquivo("log.txt", "a") as log:
                try:
                    # Nome função, argumentos função, valor closure função
                    log.write(
                        f"<{data}>--<{funcao.__name__.upper()}>--<Clientes:{len(args[0])}>--<{retorno}>\n"
                    )
                except IOError:
                    log.write(
                        f"<{data}> ERRO NA CRIAÇÃO DO LOG...<{funcao.__name__.upper()}>\n"
                    )

            print("=" * 40)
            print(f"Operação de {funcao.__name__.upper()} realizada com sucesso...")
            print(data)
            print("=" * 40)

        # Retorna o mesmo, independente do valor. Realizar o teste na chamada da função
        return retorno

    return criar_log


@gerador_log
def depositar(clientes):
    # Deposita o valor na conta selecionada de cliente
    cpf = validacao_cpf()
    print("Número da conta")
    nro_conta = validacao_int()
    cliente = retornar_cliente(clientes, cpf)
    if cliente:
        conta = retornar_conta(nro_conta, cliente.contas)
        if conta:
            print("Qual o valor para depósito?")
            valor = validacao_float()
            if valor == 0:
                return False
            try:
                deposito = Deposito(valor)
                if cliente.realizar_transacao(deposito, conta):
                    print(f"Saldo: R${conta.saldo}")
                    return True
            except IOError:
                return False
        else:
            print("Nenhuma conta registrada")
    else:
        print("Cadastro não encontrado...")
    return False


@gerador_log
def sacar(clientes):
    # Saca o valor na conta selecionada por nro_conta de Cliente
    cpf = validacao_cpf()
    cliente = retornar_cliente(clientes, cpf)
    if cliente:
        # Executa quando cliente não está vázio
        print("Número da conta")
        nro_conta = validacao_int()

        conta = retornar_conta(nro_conta, cliente.contas)
        if conta:
            if conta.saldo > 0:
                # Executa se tiver saldo na conta
                print(f"Saldo: R${conta.saldo}")
                print("Qual o valor para saque?")
                valor = validacao_float()
                if valor == 0:
                    return True
                try:
                    saque = Saque(valor)
                    if cliente.realizar_transacao(saque, conta):
                        return True
                except IOError:
                    return False
            else:
                print(f"Saldo: R${conta.saldo}\nSaldo insuficiente para saque ")
        else:
            print("Nenhuma conta registrada")
    else:
        print("Cadastro não encontrado...")
    return False


def extrato(clientes):
    cpf = validacao_cpf()
    cliente = retornar_cliente(clientes, cpf)
    if cliente:
        # Executa quando cliente não está vázio
        print("Número da conta")
        nro_conta = validacao_int()

        conta = retornar_conta(nro_conta, cliente.contas)
        if conta:
            # Se histórico não estiver vazio
            if conta.historico.historico > 0:
                # Selecione uma opção para filtrar as transações
                print(
                    "Selecione uma opção :\n [1] Transações\n [2] Depósitos\n [3] Saques"
                )
                opcao = validacao_int()
                match opcao:
                    case 1:
                        tipo = None
                    case 2:
                        tipo = "Deposito"
                    case 3:
                        tipo = "Saque"
                    case _:
                        print("Opção inválida! Retornando todas as transações...")
                        tipo = None

                sleep(1)
                # Variável para verificar movimentações
                tem_transacao = False
                # Chama o método gerador para retornar o histórico
                for cont, transacao in enumerate(
                    conta.historico.gerador_historico(tipo)
                ):
                    print(f"{cont+1}º Transação:\n \t{transacao}")
                    tem_transacao = True
                # Se nenhuma transacao do tipo é retornada, o for não inicia e tem_transacao continua falso
                if not tem_transacao:
                    print("Nenhuma movimentação realizada")

                # Sair da visualização
                while True:
                    print("Digite algo para sair : ")
                    resp = input()
                    if resp is not None:
                        break
            else:
                print("Nenhuma movimentação realizada")
        else:
            print("Nenhuma conta registrada")
    else:
        print("Cadastro não encontrado...")


def validacao_int():
    # Método para validação de string para int
    while True:
        escolha = str(input(": "))
        try:
            escolha = int(escolha)
            break
        except ValueError:
            print("\033[31mDigite um número\033[m")
    return escolha


def validacao_float():
    while True:
        valor = str(input(": R$").replace(",", "."))
        try:
            valor = float(valor)
            break
        except ValueError:
            print("\033[31mDigite um número decimal válido\033[m")
    return valor


def validacao_cpf():
    while True:
        cpf = str(input("CPF : ")).replace(".", "").replace("-", "")
        try:
            cpf = int(cpf)
            break
        except ValueError:
            print("CPF inválido! Digite novamente...")
    return cpf


@gerador_log
def cadastrar_cliente(clientes):
    # Validação CPF
    cpf = validacao_cpf()
    # Se cpf já cadastrado parar função cadastro
    if retornar_cliente(clientes, cpf):
        print("CPF já cadastrado!")
        cliente = None
        return cliente

    nome = str(input("Nome : "))
    data_nascimento = str(input("Data de nascimento : "))

    print("--- Endereço ---")
    uf = str(input("UF : "))
    cidade = str(input("Cidade : "))
    bairro = str(input("Bairro : "))
    logradouro = str(input("Logradouro : "))

    endereco = " ".join([cidade, bairro, logradouro, "-", uf])
    cliente = [nome, cpf, data_nascimento, endereco]

    return cliente


@gerador_log
def cadastrar_conta(clientes, contas):
    print("Vamos verificar seu cadastro...")
    cpf = validacao_cpf()
    # Retorna o cliente com o cpf informado
    cliente = retornar_cliente(clientes, cpf)

    if cliente:
        # Limite máximo de contas
        if len(cliente.contas) < 3:
            nro_conta = len(contas) + 1
            contas.append(
                cliente.adicionar_conta(
                    numero=nro_conta,
                    saldo=0,
                    limite=500,
                    limite_saques=3,
                    saques_diarios=0,
                )
            )
            return True
        else:
            print("Você só pode criar até três contas.")
    else:
        print("Cadastro não encontrado...")

    return False


def abrir_arquivo(caminho, modo, newline=None):
    # ROOT_PATH = caminho da pasta-pai do arquivo atual
    # Se arquivo não existe, criar arquivo
    try:
        open(ROOT_PATH / caminho, "r", encoding="utf-8", newline=newline).close()
    except FileNotFoundError:
        open(ROOT_PATH / caminho, "w", encoding="utf-8", newline=newline).close()

    arquivo = open(ROOT_PATH / caminho, modo, encoding="utf-8", newline=newline)
    return arquivo


def cadastro(clientes, contas):
    print("=" * 10 + "CADASTRO" + "=" * 10)
    print(" [1] Cadastrar Cliente\n [2] Cadastrar Conta\n [3] Listar Contas")
    escolha = validacao_int()
    match escolha:

        # Cadastro Cliente
        case 1:
            # Chamar função cadastrar cliente e receber informações
            cliente = cadastrar_cliente(clientes)
            if cliente:
                clientes.append(
                    PessoaFisica(
                        nome=cliente[0],
                        cpf=cliente[1],
                        data_nascimento=cliente[2],
                        endereco=cliente[3],
                    )
                )
                if cadastrar_conta(clientes, contas):
                    return True
            return False
        # Cadastro Conta para Cliente
        case 2:
            if len(clientes):
                if cadastrar_conta(clientes, contas):
                    return True
            else:
                print("Nenhum cadastro encontrado, cadastre um cliente primeiro")
            return False

        # Mostrar contas
        case 3:
            if len(clientes):
                cpf = validacao_cpf()
                cliente = retornar_cliente(clientes, cpf)

                if cliente:
                    # Titulo
                    print("=" * 30)
                    print(cliente)
                    print("=" * 12 + "CONTAS" + "=" * 12)
                    # Se cliente tem contas
                    if cliente.contas:
                        cliente.mostrar_contas()
                        # Sair da visualização
                        while True:
                            print("Digite algo para sair : ")
                            resp = input()
                            if resp is not None:
                                break
                    else:
                        print("Nenhuma conta registrada")

                    return True
                else:
                    print("Cadastro não encontrado...")
            else:
                print("Nenhum cadastro encontrado, cadastre um cliente primeiro")
        case _:
            print("Opção inválida. Retornando ao menu...")
            return False


def menu():
    print("=" * 30 + f"\n{'MENU'.center(30)}\n" + "=" * 30)
    print(
        "Escolha a opção desejada : \n [0] Salvar e Sair\n [1] Cadastro\n [2] Depositar\n [3] Sacar\n [4] Extrato"
    )
    escolha = validacao_int()
    return escolha


def inicializar_classe(clientes, contas):
    # Instancia objetos de Cliente e Contas por um arquivo CSV
    # Só é executado se clientes.csv tiver linhas, caso contrário o for cancela a iteração
    with abrir_arquivo("clientes.csv", "r", newline="") as arquivo_clientes:
        leitor = csv.DictReader(arquivo_clientes)
        for row in leitor:
            # Instanciando uma PessoaFisica com os dados recebidos
            cliente = PessoaFisica(
                nome=row["nome"],
                cpf=row["cpf"],
                data_nascimento=row["data_nascimento"],
                endereco=row["endereco"],
            )
            clientes.append(cliente)
            # Tratando a coluna de contas
            # Dividindo a coluna contas em várias contas separadas por ,
            lista_contas = row["contas"].split(",")
            for conta in lista_contas:
                # Dividindo os valores dentro de cada conta separadas por :
                valores = conta.split(":")
                # Instanciando ContaCorrente com método de Cliente
                cc = cliente.adicionar_conta(
                    saldo=valores[1],
                    numero=valores[2],
                    limite=valores[3],
                    limite_saques=valores[4],
                    saques_diarios=valores[5].replace("]", ""),
                )
                contas.append(cc)


def main():
    clientes = []
    contas = []
    inicializar_classe(clientes, contas)
    while True:
        escolha = menu()
        match escolha:
            case 0:
                print("Salvando usuários...")
                # CRIANDO REGISTRO NO ARQUIVO
                # O arquivo é recriado novamente, adicionando os valores novos
                with abrir_arquivo("clientes.csv", "w", newline="") as arquivo_clientes:
                    try:
                        # Escrevendo Registros
                        escritor = csv.writer(arquivo_clientes)
                        # Para cada cliente é escrito uma linha
                        escritor.writerow(
                            ["nome", "cpf", "data_nascimento", "endereco", "contas"]
                        )
                        for cliente in clientes:
                            escritor.writerow(
                                [
                                    cliente.nome,
                                    cliente.cpf,
                                    cliente.data_nascimento,
                                    cliente.endereco,
                                    cliente.contas,
                                ]
                            )
                    except IOError as exc:
                        print(exc.strerror)
                    break

            case 1:  # Cadastro

                if not cadastro(clientes, contas):
                    print("Falha ao realizar o cadastro")
                sleep(1)

            case 2:  # Deposito

                if len(clientes):
                    if not depositar(clientes):
                        print("Falha ao realizar o depósito")
                else:
                    print("Nenhuma conta cadastrada, realize o cadastro primeiro")
                sleep(1)

            case 3:  # Saque

                if len(clientes):
                    if not sacar(clientes):
                        print("Falha ao realizar o saque")
                else:
                    print("Nenhuma conta cadastrada, realize o cadastro primeiro")
                sleep(1)

            case 4:  # Extrato

                if len(clientes):
                    extrato(clientes)
                else:
                    print("Nenhuma conta cadastrada, realize o cadastro primeiro")
                sleep(1)

            case _:
                print("Opção inválida")


ROOT_PATH = Path(__file__).parent
main()
