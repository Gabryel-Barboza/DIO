# Repositório com o matérial do bootcamp da [Digital Innovation One](https://web.dio.me)
Estão inclusos os projetos feitos nos diretórios de desafios. <br>
Altere a **Branch** atual para alguma das opções disponíveis para visualizar outros cursos.

# Desafios
* [Modelagem E-Commerce](https://github.com/Gabryel-Barboza/DIO/tree/SQL/sql_database_specialist/Desafios/Modelagem%20E-commerce)
* [Modelagem Oficina](https://github.com/Gabryel-Barboza/DIO/tree/SQL/sql_database_specialist/Desafios/Modelagem%20Oficina)
* [Esquema Lógico E-commerce](https://github.com/Gabryel-Barboza/DIO/tree/SQL/sql_database_specialist/Desafios/Esquema%20L%C3%B3gico%20E-commerce)
* [Esquema Lógico Oficina](https://github.com/Gabryel-Barboza/DIO/tree/SQL/sql_database_specialist/Desafios/Esquema%20L%C3%B3gico%20Oficina)
* [Criando índices e SQL dinâmico](https://github.com/Gabryel-Barboza/DIO/tree/SQL/sql_database_specialist/Desafios/Indexes%20%26%20Procedures)
* [Controle de Acesso e Automatização de Dados](https://github.com/Gabryel-Barboza/DIO/tree/SQL/sql_database_specialist/Desafios/Views%20%26%20Triggers)
* [Transações no MySQL]()

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

# Explorando o SQL 📜
Seguindo os conteúdos do curso, neste módulo foi feita a criação de um banco de dados e também foram apresentadas as operações com consultas SQL.
Conceitos de chave primária e estrangeira, tipos de dados e entre outros.
Todos os principais statements utilizados em consultas SQL, incluindo: 
```sql
CREATE TABLE, ALTER TABLE
INSERT, UPDATE, DELETE
CASE
SELECT, ORDER BY, GROUP BY, HAVING, JOIN, INNER JOIN, OUTER JOIN
```
Por fim, a criação de diversas consultas e exercícios:
* [Primeiro Script SQL](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/01_Primeiro%20Script.sql)
* [Criando o Primeiro Esquema](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/02_Criando%20um%20Esquema.sql)
* [Esquemas II](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/03_Esquema%20de%20Company.sql)
* [Instâncias de Dados](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/04_Instancias%20de%20Dados.sql)
* [Constraints I](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/05_Adicionando%20Constraints-1.sql)
* [Constraints II](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/05_Adicionando%20Constraints-2.sql)
* [Instâncias com Restrições](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/06_Instancia%20de%20Dados%202.sql)
* [Recuperação de Dados](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/07_Recuperando%20Dados.sql)
* [Pseudônimos/Alias](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/08_Aliasing.sql)
* [Entendendo o DDL](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/09_Explorando%20comandos%20DDL.sql)
* [Expressões](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/10_Express%C3%B5es%20SQL.sql)
* [Operadores](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/11_Operadores.sql)
* [Subquery](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/12_Subquerys.sql)
* [Cláusulas SQL](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/13_Cl%C3%A1usulas%20SQL.sql)
* [CASE Statement](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/14_CASE%20Statement.sql)
* [Junções I](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/15_JOIN%20entre%20tabelas.sql)
* [Junções II](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/02_Explorando_SQL/Scripts/16_JOIN%20Statement.sql)

## Esquema Lógico de E-commerce
Como desafio do módulo, foi feita a modelagem do seguinte banco de dados, e um posterior refinamento, e implementado o esquema lógico com SQL: <br>
![Modelagem%20E-commerce.png](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/Desafios/Esquema%20L%C3%B3gico%20E-commerce/Modelagem%20E-commerce.png)
<br>

Logo após, criadas consultas com inserções e recuperações de dados para responder determinadas perguntas quanto ao seu contexto:
* [Esquema Lógico E-commerce](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/Desafios/Esquema%20L%C3%B3gico%20E-commerce/Esquema%20do%20Banco%20de%20Dados%20E-commerce.sql)
* [Instância de Dados](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/Desafios/Esquema%20L%C3%B3gico%20E-commerce/Inst%C3%A2ncia%20de%20Dados%20no%20E-commerce.sql)
* [Recuperação de Dados](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/Desafios/Esquema%20L%C3%B3gico%20E-commerce/Recuperando%20Dados%20do%20Banco.sql)

## Esquema Lógico de Oficina
Outro desafio realizado foi a modelagem e implementação de um esquema de oficina, seguindo o seguinte esquema conceitual: <br>
![Oficina.png](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/Desafios/Esquema%20L%C3%B3gico%20Oficina/Oficina.png)
<br>

Etapas de implementação do banco de dados:
* [Esquema Lógico de Oficina](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/Desafios/Esquema%20L%C3%B3gico%20Oficina/Esquema%20do%20Banco%20de%20Dados%20Oficina.sql)
* [Instância de Dados no Esquema](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/Desafios/Esquema%20L%C3%B3gico%20Oficina/Inst%C3%A2ncia%20de%20Dados.sql)
* [Recuperação de Dados com SELECT](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/Desafios/Esquema%20L%C3%B3gico%20Oficina/Recuperando%20Dados.sql)

# Consultas SQL com Técnicas Avançadas ⁉️
Neste tópico foram abordadas diversas técnicas que facilitam a manipulação do banco de dados e permitem maior complexidade. Portanto, os temas aprendidos incluem:

A criação de visualizações para determinados cenários, exploração do SQL dinâmico com rotinas, automatização do banco de dados com gatilhos e eventos, indexação de bancos de dados.
* [Views](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/03_T%C3%A9cnicas_Avan%C3%A7adas_SQL/Scripts/01_Views_MySQL.sql)
* [Tabelas padrão MySQL](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/03_T%C3%A9cnicas_Avan%C3%A7adas_SQL/Scripts/02_Explorando_MySQL.sql)
* [SQL dinâmico](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/03_T%C3%A9cnicas_Avan%C3%A7adas_SQL/Scripts/03_Functions_Procedures.sql)
* [Mais rotinas](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/03_T%C3%A9cnicas_Avan%C3%A7adas_SQL/Scripts/03_Functions_Procedures.sql)
* [Events](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/03_T%C3%A9cnicas_Avan%C3%A7adas_SQL/Scripts/05_Events.sql)
* [Triggers](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/03_T%C3%A9cnicas_Avan%C3%A7adas_SQL/Scripts/06_Triggers.sql)
* [Index](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/03_T%C3%A9cnicas_Avan%C3%A7adas_SQL/Scripts/07_indices.sql)

Como adicional para realização do desafio, um novo banco de dados para universidade foi criado e modelado da maneira disposta a seguir:

![Modelagem Universidade](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/Desafios/Indexes%20%26%20Procedures/modelagem/Modelagem%20Universidade.drawio.png)

# Transações
Por fim, para este tema é abordada as transações e suas propriedades, tais como mecanismos de locking, COMMIT e ROLLBACK, SAVEPOINTS, isolamento e concorrência do banco de dados. 

Além destes, a ferramenta de backup `mysqldump` é usada para gerar um [dump](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/04_Transa%C3%A7%C3%B5es/Scripts/company_backup.sql), ou script SQL para criar novamente o banco de dados company.

* [Criando transações](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/04_Transa%C3%A7%C3%B5es/Scripts/01_Criando_Transa%C3%A7%C3%B5es.sql)
* [Bloqueio de transações](https://github.com/Gabryel-Barboza/DIO/blob/SQL/sql_database_specialist/04_Transa%C3%A7%C3%B5es/Scripts/02_Locking.sql)
