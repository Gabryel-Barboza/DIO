# Repositório com o matérial do bootcamp da [Digital Innovation One](https://web.dio.me)
Estão inclusos os projetos feitos nos diretórios de desafios. <br>
Altere a **Branch** atual para alguma das opções disponíveis para visualizar outros cursos.

# Desafios
* [Modelagem E-Commerce](https://github.com/Gabryel-Barboza/DIO/tree/SQL/sql_database_specialist/Desafios/Modelagem%20E-commerce)
* [Modelagem Oficina](https://github.com/Gabryel-Barboza/DIO/tree/SQL/sql_database_specialist/Desafios/Modelagem%20Oficina)

# Modelagem de Dados 📝
Para este tópico o foco está na interpretação de diagramas de Entidade Relacionamento Extendido, além da construção de projetos conceituais. <br>
Com a utilização do MySQL Workbench foram realizados exercícios de modelagem de diferentes cenários, que podem ser visualizados na pasta [01_Modelagem_Dados](https://github.com/Gabryel-Barboza/DIO/tree/SQL/sql_database_specialist/01_Modelagem_Dados). <br>
* [Ordem de Serviço](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/01_Modelagem_Dados/Ordem%20de%20Serviço.png)
* [Universidade](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/01_Modelagem_Dados/Universidade_refinado.png)

## E-Commerce
Como primeiro desafio para este módulo, foi feita a modelagem de um contexto de E-commerce apresentado na imagem a seguir. Este modelo pode ser acessado com o Worbench na pasta [Desafios](https://github.com/Gabryel-Barboza/DIO/tree/SQL/sql_database_specialist/Desafios/Modelagem%20E-commerce).

![E-commerce](https://github.com/user-attachments/assets/d6387d4d-a280-492e-b7fe-4e73044fc443)

A narrativa para esta modelagem é: <br>
Um cliente pode ser uma pessoa física ou jurídica, possuindo o respectivo documento, como também cadastrar um ou mais cartões para o meio de pagamento. Ele também pode realizar um ou mais pedidos, esse pedido pode possuir mais de uma tentativa de entrega, o pedido vai estar relacionado a uma quantidade de produtos. <br>
Para o produto é dado um fornecedor ou vendedor de terceiros, a quem determina a quantidade em estoque. <br>

## Oficina
Para o segundo desafio temos um cenário de uma Oficina. <br>
Um Cliente possui um ou mais veículos, esse veículo é analisado por mecânicos para determinar o tipo de serviço. Após a análise, é gerado uma OS com o orçamento do serviço, esse orçamento é feito a partir do valor de cada peça e serviço necessário para o trabalho. Uma equipe de mecânicos irá executar essa OS após a autorização do cliente.
![Oficina](https://github.com/user-attachments/assets/9d8efae0-eda2-4ed0-9c97-170123011751)

