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

-- Criando índices
ALTER TABLE customer ADD INDEX index_email (email);
