-- Criando Índices no MySQL

CREATE DATABASE IF NOT EXISTS customer_management;

USE customer_management;

CREATE TABLE IF NOT EXISTS customer(
  id_customer INT AUTO_INCREMENT PRIMARY KEY,
  customer_name VARCHAR(25),
  email VARCHAR(40),
  cpf CHAR(9),
  credit_card CHAR(13),
  contact CHAR(9),
  address VARCHAR(30)
);

-- Chaves de integridade criam índices automaticamente
SHOW INDEX FROM customer;

-- Adicionando índices
ALTER TABLE customer ADD INDEX index_email (email);

DROP TABLE customer_v2;
CREATE TABLE customer_v2(
  id_customer SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_store TINYINT UNSIGNED NOT NULL,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  email VARCHAR(100) NOT NULL,
  address_id SMALLINT UNSIGNED NOT NULL,
  active BOOLEAN NOT NULL DEFAULT TRUE,
  create_date DATETIME NOT NULL,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id_customer),
  KEY idx_fk_store (id_store), -- Define índices simples na criação da tabela
  KEY idx_fk_address (address_id)
) ENGINE = MEMORY;

-- Índices por padrão do tipo B-tree, estrutura de dados de árvore
-- Para booleanos, uma estrutura em árvore é ineficiente

SELECT * FROM information_schema.TABLES WHERE table_name = 'customer_v2';
SHOW INDEX FROM customer_v2;

--ALTER TABLE customer_v2 ADD HASH INDEX index_active_customer (active);

-- MySQL suporta índices do tipo hash apenas com a engine MEMORY
CREATE INDEX index_active_customer ON customer_v2 (active) USING HASH;

-- MEMORY cria índices hash por padrão, mas permite BTREE
CREATE INDEX idx_last_name ON customer_v2 (last_name) USING BTREE;

DROP INDEX idx_last_name ON customer_v2;

-- Índices podem ser únicos, não permitindo serem aplicados a outros campos
CREATE UNIQUE INDEX idx_last_name ON customer_v2 (last_name);

-- Também podem ser clusterizados, com o propósito de retornar blocos de incidência dos valores iguais
-- na chave de identificação e não apenas um único registro.
