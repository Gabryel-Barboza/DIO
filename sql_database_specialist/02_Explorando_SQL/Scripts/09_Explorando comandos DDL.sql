-- Explorando comandos DDL

SELECT now() as Timestamp;

DROP DATABASE manipulation;
CREATE DATABASE IF NOT EXISTS manipulation;
USE manipulation;

SHOW TABLES;

CREATE TABLE bankAccounts(
	Id_account INT AUTO_INCREMENT PRIMARY KEY,
    Ag_num INT NOT NULL,
    Ac_num INT NOT NULL,
    Saldo FLOAT,
    CONSTRAINT unique_account_identification UNIQUE (Ag_num, Ac_num)
);

CREATE TABLE bankClient(
	Id_client INT AUTO_INCREMENT,
    Client_account INT,
    CPF CHAR(11) NOT NULL,
    RG CHAR(9) NOT NULL,
    Nome VARCHAR(50) NOT NULL,
    Endereco VARCHAR(100) NOT NULL,
    Renda_mensal FLOAT,
    PRIMARY KEY (id_client, Client_account),
    CONSTRAINT fk_account_client FOREIGN KEY (Client_account) REFERENCES bankAccounts (Id_account)
    ON UPDATE CASCADE
);

CREATE TABLE bankTransactions(
	Id_transaction INT AUTO_INCREMENT PRIMARY KEY,
    Ocorrencia DATETIME,
    Status_transaction VARCHAR(20),
    Valor_transferido FLOAT,
    Source_account INT,
    Destination_account INT,
    CONSTRAINT fk_source_transaction FOREIGN KEY (Source_account) REFERENCES bankAccounts (Id_account),
    CONSTRAINT fk_destination_transaction FOREIGN KEY (Destination_account) REFERENCES bankAccounts (Id_account)
);

-- ADD COLUMN - pode-se omitir column
ALTER TABLE bankAccounts 
	ADD LimiteCredito FLOAT NOT NULL DEFAULT 500;
    
ALTER TABLE bankAccounts
	ADD email VARCHAR(60);
    
ALTER TABLE bankAccounts
	DROP email;

DESC bankAccounts;

-- Modificando columns
-- ALTER TABLE tabela MODIFY COLUMN coluna tipo_dados condição;

-- Adicionando Constraints
-- ALTER TABLE tabela ADD CONSTRAINT constraint condição;

-- Renomeando columns e tables com RENAME
ALTER TABLE bankAccounts RENAME TO bankAccount;

SELECT * FROM information_schema.referential_constraints WHERE constraint_schema='manipulation';

ALTER TABLE bankAccount RENAME TO bankAccounts;

ALTER TABLE bankTransactions RENAME COLUMN Ocorrencia TO Ocurrence;

DESC bankClient;

-- Atualizando registros
INSERT INTO bankAccounts (Ag_num, Ac_num, Saldo) VALUES (123, 12345, 0);

INSERT INTO bankClient (Client_account, CPF, RG, Nome, Endereco, Renda_mensal)
	VALUES (1, 12345678911, 123456789, 'Fulano', 'Rua X', 2500);
    
-- Atualizando o registro da coluna Nome, onde o atributo nome possua o registro 'Fulano'
-- Se a condição não for chave primária, o Workbench impede a execução para prevenir múltiplos updates
-- Utilize a função LIMIT para limitar a 1 update e contornar a restrição
UPDATE bankClient SET Nome='Gabryel' WHERE Nome='Fulano' LIMIT 1;

DELETE FROM bankClient WHERE Nome='Fulano' LIMIT 2;

SELECT * FROM bankClient;