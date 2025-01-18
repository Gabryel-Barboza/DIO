-- Explorando o catálogo do MySQL

SHOW DATABASES;
USE sys;

SHOW TABLES;
SHOW TABLES LIKE 'schema%';

-- Tabelas com constraint auto_increment
SELECT * FROM schema_auto_increment_columns;

-- Versão do SGBD
SELECT * FROM version;

-- Hosts conectados
SELECT * FROM host_summary;

-- Retorna o comando executado para determinada operação
SHOW CREATE VIEW sys.session;

SHOW TABLES LIKE '%list%';
-- Processos sendo executados no momento
SELECT * FROM processlist;

SHOW TABLES LIKE '%session';
-- Todas as sessões conectadas ao SGBD no momento
SELECT * FROM session;

USE information_schema;
SHOW TABLES;

-- Todas as palavras reservadas do sistema
SELECT * FROM keywords;

-- Informações de tabelas
SELECT * FROM tables WHERE table_schema='company';

-- Informações de CHECKs
SELECT * FROM check_constraints;

-- Informações de databases
SELECT * FROM schemata;

-- Informações de restrição referencial
SELECT * FROM referential_constraints;

-- Informações de usuários
SELECT * FROM mysql.user;

-- Criando um usuário
CREATE USER 'geral'@localhost IDENTIFIED BY '1234';

-- Definindo privilégios
-- O usuário só pode manipular e acessar o banco de dados ecommerce. Até as informações de schema só são retornadas desse banco de dados apenas
GRANT ALL PRIVILEGES ON ecommerce.* TO 'geral'@localhost;
