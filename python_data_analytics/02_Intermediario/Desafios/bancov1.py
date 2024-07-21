from time import sleep

# Fomos contratados por um grande banco para desenvolver o seu novo sistema. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.​
# Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.​
# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
# Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.​Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:​ 1500.45 = R$ 1500.45


def depositar(deposito):
    global saldo
    # Se deposito positivo, saldo recebe depósito e é adicionado uma movimentação a extrato_bancario
    if (deposito > 0):
        saldo += deposito
        extrato_bancario.append(f"Depósito realizado de R${deposito:.2f}")
        print(f"Seu saldo agora é de R${saldo:.2f}")
    else:
        print("Depósito inválido, tente novamente!")


def sacar(quantia):
    global saldo
    global saque_diario
    # Se saldo menor que quantia de saque
    if (saldo < quantia):
        print("Saldo insuficiente!")
    # Se quantia de saque maior que limite diário
    elif (quantia > 500):
        print("Quantia ultrapassou o limite diário. Seu limite diário é de R$500,00")
    # Se quantia de saque negativa
    elif (quantia <= 0):
        print("Quantia de saque inválida!")
    # Retirar saque de saldo, decrementar um de saque_diario e adicionar movimentação
    else:
        saldo -= quantia
        saque_diario -= 1
        extrato_bancario.append(f"Saque realizado de R${quantia:.2f}")
        print(f"Saldo restante: R${saldo:.2f}")
        

def extrato():
    # Se extrato vázio
    if (len(extrato_bancario) == 0):
        print("Nenhuma movimentação realizada.")
    # Printando o extrato
    else:
        print("="*20 + " EXTRATO " + "="*20)
        for acao in extrato_bancario:
            print(acao)
        print("="*49)
        # Opção para sair, facilitar visualização de extrato
        print("S para sair")
        while True:
            resposta = str(input().strip())[0].upper()
            if resposta == "S":
                break


menu = "="*20 + f"\n{'Menu'.center(20)}\n" + "="*20
saldo, saque_diario = 0, 3
extrato_bancario = []

print(menu)
while True:
    escolha = str(input("""Escolha uma opção : 
    [0] Sair
    [1] Depositar
    [2] Sacar
    [3] Extrato
   : """))
    # tratamento de erros de tipo
    try:
        escolha = int(escolha)
    except:
        print("\033[31mPor favor, digite um número.\033[m")
    
    if (escolha == 0):
        break

    if (escolha == 1):
        # Tratamento de erros de tipo
        while True:
            try:
                deposito = float(input("Qual valor deseja depositar? \n: "))
                break
            except:
                print("Valor inválido!")
        depositar(deposito)
        sleep(1)

    elif (escolha == 2):
        # Caso limite diário não excedido, continuar função saque
        if saque_diario > 0:
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
                sacar(valor)
            else:
                print("Saldo não disponível para saque. Realize um depósito primeiro")
        else:
            print("Limite de saques diários esgotado. Tente novamente outro dia!")
        sleep(1)

    elif (escolha == 3):
        # Exibir extrato
        extrato()
        sleep(1)
    
    else:
        print("\033[31mOpção Inválida!\033[m")
        sleep(1)
    