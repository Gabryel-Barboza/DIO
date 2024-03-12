saldo = 2000.0;
saque = float(input("Informe o valor do saque: "));

# Condicional simples
if saldo >= saque:
    print("Realizando saque!");

if saldo < saque:
    print("Não foi possivel realizar o saque. Saldo insuficiente!");

# Condicional Composta
idade = int(input("Digite sua idade : "));
if idade >= 18:
    print("Sucesso!");
else:
    print("Falhou!");

resposta = int(input("Escolha uma opção: \n [1] Sacar \n [2] Extrato\n: "))

if resposta == 1:
    print("Sacando dinheiro");
elif resposta == 2:
    print("Extrato:");
else:
    print("Opção inválida!");

# Condicional Aninhada
idade = int(input("Digite sua idade : "));
if 18 <= idade <= 70:
    print("Voto obrigatório");
else:
    if idade >= 16 or idade > 70:
        print("Voto opcional");
    else:
        print("Não vota");

# Operador ternário
print("Voto obrigatório") if (18 <= idade <= 70) else print("Voto opcional") if (idade >= 16 or idade > 70) else print("Não vota");
