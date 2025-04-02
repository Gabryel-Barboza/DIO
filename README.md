# Repositório com o matérial do bootcamp da [Digital Innovation One](https://web.dio.me)
Estão inclusos os projetos feitos nos diretórios de desafios. <br>
Altere a **Branch** atual para alguma das opções disponíveis para visualizar outros cursos.

# Trabalhando com Python 🐍
## Desafios 📈

[BancoV1.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/02_Intermediario/Desafios/bancov1.py) - 
[BancoV2.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/02_Intermediario/Desafios/bancov2.py) -
[BancoV3.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/03_POO/Desafios/bancov3.py) - 
[BancoV4.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/03_POO/Desafios/bancov4.py) - 
[BancoV5.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/03_POO/Desafios/bancov5.py) -
[BancoV6.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/03_POO/Desafios/bancov6.py)
<br> <br> 
[Integração SQLite e MongoDB](https://github.com/Gabryel-Barboza/DIO/tree/main/python_data_analytics/04_Bancos%20de%20Dados/Desafios/Integracao_SQLite_MongoDB) -
[ProjetoPandas](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/05_Tratamento%20de%20Dados/Desafio/ProjetoPandas.ipynb) -
[Distribuições no PyPi](https://test.pypi.org/project/sqlite2mongo/)
<br> <br>
Abaixo está a documentação de cada projeto:

## Criação de um sistema bancário 💸
Primeiro desafio do módulo, implementando um sistema bancário com as funções de depositar, sacar e extrato.
* É permitido o saque máximo de R$500,00 e possui um limite diário de 3 operações.
* Nessa versão, é realizado as operações com usuário único.

[BancoV1.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/02_Intermediario/Desafios/bancov1.py)

## Atualizando o sistema bancário ✔
Foi implementada novas funções de cadastrar usuário e cadastrar conta bancária, como também atualizada as funções anteriores.
* O cadastro de usuários e contas é armazenado em uma lista com dicionários.
* Todas as operações são realizadas com funções e seus argumentos.

[BancoV2.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/02_Intermediario/Desafios/bancov2.py)

## Implementando o sistema bancário com POO 💯
O programa foi refeito com o paradigma orientado ao objeto, permitindo grandes interações e a capacidade de criar instâncias de clientes e contas.
* Cliente é instanciado como uma PessoaFisica e adquire informações como cpf, entre outros.
* Conta é instanciada como ContaCorrente e possui suas determinadas limitações de saque.
* Todas as operações foram recriadas como classes e seus respectivos atributos.
* Um Cliente possui várias Contas e com atributos individuais. Também está disponível o histórico de transação para cada conta e funções para exibição.
* Por fim, um menu para interação por terminal foi adaptado para tratar os dados e erros de entrada e enviá-los as respectivas classes.

[BancoV3.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/03_POO/Desafios/bancov3.py)

## Aprimorando o programa ✨
Foi adicionado decoradores, iteradores e geradores para o programa, permitindo maior controle dos dados.
* Um decorador para a exibição da operação realizada e a hora de operação.
* Um gerador para criar um relatório com todas as transações, agora possibilitando a filtragem por Depósitos e Saques.
* Um Iterador para retornar todas as contas de um cliente.

[BancoV4.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/03_POO/Desafios/bancov4.py)

## Adicionando o módulo de data 📅
Está implementado no histórico das transações a data de realização. Também foi adicionado um novo limite para transações diárias.
* A função extrato agora mostra a data em que a operação foi realizada.
* Antes de realizar uma transação, é verificado se a quantidade de transações daquele dia ultrapassa o limite de 10 transações diárias.
* É exibido ao usuário e cancelada a transação, caso exceda o limite diário.

[BancoV5.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/03_POO/Desafios/bancov5.py)

## Manipulando e guardando usuários em arquivos 📓
O sistema agora conta com a capacidade de armazenar seus usuários e respectivas contas em arquivos.csv, após a reinicialização do programa os usuários são reconstruidos no sistema bancário, além de guardar um log com data das operações realizadas. O programa também obteve uma refatoração de código, mudando algumas de suas funcionalidades.
* O decorador gerador de log agora armazena suas informações em um arquivo log.txt, além de exibir-lás no terminal.
* Novas funções abrir_arquivo, inicializar_classe, cadastrar_cliente e cadastrar_conta para melhor modularização do código. Inicializar_classe recria as informações obtidas do arquivo no sistema.
* Algumas refatorações em códigos existentes para adequação ao programa.
* O histórico de transações ainda não é salvo entre execuções, então será perdido na saida do programa.

[BancoV6.py](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/03_POO/Desafios/bancov6.py)

# Frameworks em Python 🐍
Para este módulo, será desenvolvido programas em Python juntamente com bibliotecas para integração com outros sistemas da computação, tais como bancos de dados, desenvolvimento web e entre outros.
## Integração com Banco de Dados 🏦
Nesse tópico foi desenvolvidos programas para aprender sobre o **Python DBAPI**, como também a utilização de frameworks para integração com bancos de dados relacionais (**SQLite**) e não relacionais (**MongoDB**). Os frameworks utilizados, respectivamente, foram SQLAlchemy e Pymongo. <br>
Para acessar os programas realizados, navegue até a pasta [04_Banco de Dados](https://github.com/Gabryel-Barboza/DIO/tree/main/python_data_analytics/04_Bancos%20de%20Dados). <br>
<hr>
Como desafio desse tópico foi criada aplicações para integrar com o SQLite e MongoDB, e também realizar as respectivas operações. A seguir está a modelagem do banco de dados desenvolvido nesse desafio:
<br>

![modelo_database_desafio](https://github.com/Gabryel-Barboza/DIO/assets/73187678/53044ffd-cc8a-41ef-ac1e-b38706af81ed)

<br>

* Uma aplicação de integração com SQLite, permitindo manipular dados dentro do banco relacional.
* Schema desenvolvido com ORM do SQLAlchemy, permitindo mapeamento de classes e objetos.
* Uma aplicação de integração com MongoDB Cloud, para inserir dados do banco SQL em um cluster na nuvem do MongoDB.
* Os dados inseridos dentro do SQLite são automaticamente convertidos para documentos e inseridos em coleções do MongoDB.

## Tratamento de Dados 🎲
Para este módulo, as bibliotecas Pandas e Matplotlib foram utilizadas para tratar dados de planilhas csv e Excel, como também criar gráficos. Acesse os exercícios na pasta [05_Tratameto de dados](https://github.com/Gabryel-Barboza/DIO/tree/main/python_data_analytics/05_Tratamento%20de%20Dados). <br>
Como desafio do módulo, foi utilizada a planilha em Excel SuperMarket para analisar e tratar os dados.
* Renomeadas as colunas para o Português
* Substituidos os campos nulos
* Realizado uma análise exploratória da planilha
* Criado gráficos com base na análise

[ProjetoPandas](https://github.com/Gabryel-Barboza/DIO/blob/main/python_data_analytics/05_Tratamento%20de%20Dados/Desafio/ProjetoPandas.ipynb)

## Segurança da Informação 🛡
O objetivo deste módulo foi desenvolver algumas ferramentas para compreender conceitos de Segurança da Informação. Entre as ferramentas desenvolvidas possuem: 
* Programas para realizar requisições com o protocolo ICMP (Ping), único host ou múltiplos hosts.
* Programas para criação de um cliente TCP, UDP e servidor UDP simples. Como também a comunicação entre eles.
* Ferramentas de comparação e criação de Hash. Programas geradores de senhas fortes e de Wordlists.
* Programa para entender o funcionamento de Multithreading em Python, através de uma corrida de carros.
* Outras ferramentas como web scraping e web crawlers simples, verificadores de IP externo e de geolocalização de telefone.

[06_Segurança da Informação](https://github.com/Gabryel-Barboza/DIO/tree/main/python_data_analytics/06_Segurança%20da%20Informação)

## Desenvolvimento Web 📲
Neste tópico foram desenvolvidas APIs, isso através de três dos frameworks mais populares do Python. Em primeiro modo é utilizado o <br>
Flask para aprender os conceitos de frameworks web, criando uma API simples para postagem de blogs. Depois, com o Django está desenvolvido <br>
um projeto fullstack simples, com o foco voltado para o back end da aplicação. Por fim, o FastAPI para criar uma API de <br>
sistema bancário com documentação automática e outras funcionalidades.
* Conceitos de frameworks e [desenvolvimento web](https://github.com/Gabryel-Barboza/DIO/tree/main/python_data_analytics/07_Desenvolvimento%20Web/Flask)
* [Projeto de API completo para blog de postagens](https://github.com/Gabryel-Barboza/DIO/tree/main/python_data_analytics/07_Desenvolvimento%20Web/Flask/dio_bank)
* [Projeto Fullstack para aprender Django](https://github.com/Gabryel-Barboza/DIO/tree/main/python_data_analytics/07_Desenvolvimento%20Web/Django/mysite)
* [Projeto FastAPI assíncrono](https://github.com/Gabryel-Barboza/DIO/tree/main/python_data_analytics/07_Desenvolvimento%20Web/FastApi/dio_blog)
