from time import sleep

# Criar duas novas funções: cadastrar usuário e cadastrar conta bancária, opcional: adicionar mais funções. Atualizar as funções existentes para receberem parametros com algumas regras, na função saque deve receber argumentos por nome apenas e na função deposito apenas argumentos por posição. Para o extrato, deve-se receber argumentos por ambos os métodos, exemplos: saldo - posicional e extrato - nomeado
# Função cadastrar usuário: deve armazenar usuários em uma lista, possuindo os atributos nome, data de nascimento, CPF e endereço. Endereço é uma string formada por logradouro - bairro - cidade/sigla estado. Não se pode cadastrar usuários de mesmo CPF.
# Função cadastrar conta corrente: deve armazenar contas em uma lista, uma conta é composta por agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta só pode ter um usuário 

def cadastrar_usuario(cpf):
    print()
    # Recebendo os valores e atribuindo ao dicionário
    nome = str(input("Nome : "))
    data_nascimento = str(input("Data de nascimento : "))
    print("----Endereço----")
    logradouro = input("Logradouro : ").strip()
    bairro = input("Bairro : ").strip()
    cidade = input("Cidade : ").strip()
    estado = input("Estado (Sigla) : ").strip()
    # Concatenando os campos acima em endereco
    endereco = " ".join([logradouro, bairro, cidade, estado])
    
    usuarios["cpf"].append(cpf)
    usuarios["nome"].append(nome)
    usuarios["data_nascimento"].append(data_nascimento)
    usuarios["endereco"].append(endereco)
    print(usuarios["endereco"])
    print("Vamos criar a sua conta corrente")


def cadastrar_conta_corrente(cpf_usuario):
    global numero_conta
    print()
    contas["numero_conta"].append(numero_conta)
    numero_conta += 1
    contas["usuario"].append(cpf_usuario)


def depositar(deposito, saldo, historico, /):
    # Se deposito positivo, saldo recebe depósito e é adicionado uma movimentação a extrato_bancario
    if (deposito > 0):
        saldo += deposito
        historico.append(f"Depósito realizado de R${deposito:.2f}")
        return saldo
    else:
        return saldo


def sacar(*, quantia, saldo, saque_diario, historico):
    # Se limite de saque não atingido
    if saque_diario < LIMITE_DIARIO:
        # Se saldo menor que quantia de saque
        if (saldo < quantia):
            print("Saldo insuficiente!")
            return saldo, saque_diario
        # Se quantia de saque maior que limite diário
        elif (quantia > 500):
            print("Quantia ultrapassou o limite diário. Seu limite diário é de R$500,00")
            return saldo, saque_diario
        # Se quantia de saque negativa
        elif (quantia <= 0):
            print("Quantia de saque inválida!")
            return saldo, saque_diario
        # Retirar saque de saldo, decrementar um de saque_diario e adicionar movimentação
        else:
            saldo -= quantia
            print(f"Saldo: R${saldo:.2f}")
            saque_diario += 1
            historico.append(f"Saque realizado de R${quantia:.2f}")
            return saldo, saque_diario
    else:
        print("Limite diário atingido")
        return saldo, 0


def extrato(saldo, /, *, historico):
    # Se extrato vazio
    if (len(historico) == 0):
        print("Nenhuma movimentação realizada.")
    # Printando o extrato
    else:
        print("="*20 + " EXTRATO " + "="*20)
        for acao in historico:
            print(acao)
        print("="*49)
        print(f"Saldo disponível: R${saldo:.2f}")
        # Opção para sair, facilitar visualização de extrato
        print("S para sair")
        while True:
            resposta = str(input().strip())[0].upper()
            if resposta == "S":
                break


saldo, LIMITE_DIARIO, vezes_saque = 0, 3, 0
extrato_bancario = []
numero_conta = 1
contas = {"agencia": "0001", "numero_conta": [], "usuario": []}
usuarios = {"nome": [], "data_nascimento": [], "cpf": [], "endereco": []}

# Menu inicial
menu = "="*20 + f"\n{'Menu'.center(20)}\n" + "="*20
print(menu)
while True:
    escolha = str(input("""Escolha uma opção : 
    [0] Sair
    [1] Cadastro
    [2] Depositar
    [3] Sacar
    [4] Extrato
   : """))
    # tratamento de erros de tipo
    try:
        escolha = int(escolha)
    except:
        print("\033[31mPor favor, digite um número.\033[m")
    
    match escolha:
        # Sair
        case 0:
            break
        
        # Cadastrar
        case 1:
            print("Olá, vamos verificar seu cadastro")
            try:
                # Receber cpf e retirar '.' e '-'
                cpf = str(input("Digite o seu CPF : "))
                cpf = cpf.replace(".", "")
                cpf = cpf.replace("-", "")
                cpf = int(cpf)

                # Verificando se CPF já existe
                if cpf in usuarios["cpf"]:
                    print("CPF já existente")
                    # Selecionar ação
                    opcao = str(input("Selecione uma opção: \n [0] Sair \n [1] Cadastrar conta \n: ").strip())
                    # Tratamento de tipos
                    while True:
                        try:
                            opcao = int(opcao)
                            break
                        except:
                            print("Opção inválida. Digite novamente")

                    match opcao:
                        # Sair
                        case 0:
                            break
                        # Cadastrar conta
                        case 1:
                            cadastrar_conta_corrente(cpf)
                        # Opção inválida
                        case _:
                            print("Opção inválida. Retornando ao menu")
                else:
                    print("Nenhum usuário encontrado com o CPF inserido")
                    print("Començando cadastro do usuário")
                    sleep(1)
                    cadastrar_usuario(cpf)
                    cadastrar_conta_corrente(cpf)
            except:
                print("Ocorreu um erro. Retornado ao menu")
                
            sleep(1)

        # Depositar
        case 2:
        # Tratamento de erros de tipo
            while True:
                try:
                    deposito = float(input("Qual valor deseja depositar? \n: "))
                    saldo = depositar(deposito, saldo, extrato_bancario)
                    print(f"Seu saldo é de R${saldo:.2f}")
                    break
                except:
                    print("Valor inválido!")
            sleep(1)    

        # Sacar
        case 3:
            # Se saldo positivo, continuar função saque
            if saldo > 0:
                print(f"Saldo: {saldo:.2f}")
                # Tratamento de erros de tipo
                while True:
                    try:
                        valor = float(input("Quanto deseja sacar?\n: "))
                        break
                    except:
                        print("Valor inválido!")
                saldo, vezes_saque = sacar(quantia=valor, saldo=saldo, saque_diario=vezes_saque, historico=extrato_bancario)
            else:
                print("Sem saldo disponível para saque, faça um deposito primeiro")
            sleep(1)

        case 4:
            # Exibir extrato
            extrato(saldo, historico=extrato_bancario)
            sleep(1)

        # Default
        case _:
            print("\033[31mOpção Inválida!\033[m")
            sleep(1)
        
    print("="*20)
    