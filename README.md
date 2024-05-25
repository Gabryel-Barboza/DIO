# Repositório com o matérial do bootcamp da [Digital Innovation One](https://web.dio.me)
Estão inclusos os projetos feitos nos diretórios de desafios. <br>
Altere a **Branch** atual para alguma das opções disponíveis para visualizar outros cursos.

# Trabalhando com Python 🐍

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

## Adicionando o módulo de data 📅
Está implementado no histórico das transações a data de realização. Também foi adicionado um novo limite para transações diárias.
* A função extrato agora mostra a data em que a operação foi realizada.
* Antes de realizar uma transação, é verificado se a quantidade de transações daquele dia ultrapassa o limite de 10 transações diárias.
* É exibido ao usuário e cancelada a transação, caso exceda o limite diário.

[BancoV5.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/POO/Desafios/bancov5.py)

## Manipulando e guardando usuários em arquivos 📓
O sistema agora conta com a capacidade de armazenar seus usuários e respectivas contas em arquivos.csv, após a reinicialização do programa os usuários são reconstruidos no sistema bancário, além de guardar um log com data das operações realizadas. O programa também obteve uma refatoração de código, mudando algumas de suas funcionalidades.
* O decorador gerador de log agora armazena suas informações em um arquivo log.txt, além de exibir-lás no terminal.
* Novas funções abrir_arquivo, inicializar_classe, cadastrar_cliente e cadastrar_conta para melhor modularização do código. Inicializar_classe recria as informações obtidas do arquivo no sistema.
* Algumas refatorações em códigos existentes para adequação ao programa.
* O histórico de transações ainda não é salvo entre execuções, então será perdido na saida do programa.

[BancoV6.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/POO/Desafios/bancov6.py)
