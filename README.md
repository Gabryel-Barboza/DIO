# Repositório com o matérial do bootcamp da [Digital Innovation One](https://web.dio.me)
Estão inclusos os projetos feitos nos diretórios de desafios.

## Criação de um sistema bancário 💸
Primeiro desafio do módulo, implementando um sistema bancário com as funções de depositar, sacar e extrato.
* É permitido o saque máximo de R$500,00 e possui um limite diário de 3 operações.
* Nessa versão, é realizado as operações com usuário único.

[BancoV1.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/Intermediario/Desafios/bancov1.py)

## Atualizando o sistema bancário ✔
Foi implementada novas funções de cadastrar usuário e cadastrar conta bancária, como também atualizada as funções anteriores.
* O cadastro de usuários e contas é armazenado em uma lista com dicionários.
* Todas as operações são realizadas com funções e seus argumentos.

[BancoV2.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/Intermediario/Desafios/bancov2.py)

## Implementando o sistema bancário com POO 💯
O programa foi refeito com o paradigma orientado ao objeto, permitindo grandes interações e a capacidade de criar instâncias de clientes e contas.
* Cliente é instanciado como uma PessoaFisica e adquire informações como cpf, entre outros.
* Conta é instanciada como ContaCorrente e possui suas determinadas limitações de saque.
* Todas as operações foram recriadas como classes e seus respectivos atributos.
* Um Cliente possui várias Contas e com atributos individuais. Também está disponível o histórico de transação para cada conta e funções para exibição.
* Por fim, um menu para interação por terminal foi adaptado para tratar os dados e erros de entrada e enviá-los as respectivas classes.

[BancoV3.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/POO/Desafios/bancov3.py)

## Aprimorando o programa ✨
Foi adicionado decoradores, iteradores e geradores para o programa, permitindo maior controle dos dados.
* Um decorador para a exibição da operação realizada e a hora de operação.
* Um gerador para criar um relatório com todas as transações, agora possibilitando a filtragem por Depósitos e Saques.
* Um Iterador para retornar todas as contas de um cliente.

[BancoV4.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/POO/Desafios/bancov4.py)
