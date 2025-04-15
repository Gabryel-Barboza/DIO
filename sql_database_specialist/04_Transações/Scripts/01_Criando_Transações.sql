-- Transações no MySQL

-- Desabilitar autocommit para statements SQL isolados, transações por padrão não possuem autocommit
-- Configuração é aplicada por sessão, logo é resetada em novas instâncias do cliente
SELECT @@autocommit;
SET @@AUTOCOMMIT = 0;

CREATE DATABASE test_transactions;
USE test_transactions;
SHOW TABLES;

DROP TABLE orders;
CREATE TABLE orders(
	id_order INT,
	product_name VARCHAR(50)
);

INSERT INTO orders VALUES (1, 'playstation');

-- Criando transações sequênciais
START TRANSACTION;
	SELECT MAX(id_order) + 1 INTO @orderNumbers
		FROM orders;

	SELECT @orderNumbers;
	
	INSERT INTO orders VALUES(@orderNumbers, 'Computador');
	
	ROLLBACK; -- Sinal de reversão
	COMMIT; -- Confirmando operações se nenhum erro

START TRANSACTION;
	SELECT * FROM orders;
	COMMIT;

-- Transações concorrentes, faça o teste com duas instâncias do MySQL Client

-- Modificando isolamento de transações, impede que a modificação que está ocorrendo em uma
-- transação possa ser visualizada em outra antes de ser confirmada. Por padrão REPEATABLE READ
-- REPEATABLE READ evita a leitura do banco em estados desatualizados, repetindo a operação para cada transação
SHOW SESSION VARIABLES LIKE '%isolation%';
SELECT @@TRANSACTION_ISOLATION;

-- Alterado para a sessão atual, modifique globalmente com GLOBAL no lugar de SESSION
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITED;

-- Insira um registro em uma instância por transação e tente ler em outra antes do commit. Testar mecanismo de locking

-- Savepoints - pontos de salvamento em transações
START TRANSACTION;
	SELECT MAX(id_order) + 1 INTO @orderNumbers
		FROM orders;

	INSERT INTO orders VALUES (@orderNumbers, 'Fogão');
	-- Salvando uma cópia do estado atual da transação
	SAVEPOINT antes_insercao_geladeira;
	
	-- Não foi atualizado o ID
	INSERT INTO orders VALUES (@orderNumbers, 'Geladeira');
	
	SELECT * FROM orders;
	-- Retornando antes da inserção
	ROLLBACK TO SAVEPOINT antes_insercao_geladeira;
	
	COMMIT;
	
	ROLLBACK;

-- Procedures
DROP PROCEDURE sql_fail;
DELIMITER //
CREATE PROCEDURE sql_fail()
BEGIN
	-- Declarando estrutura de tratamento de erro que sai após a execução
	DECLARE exit HANDLER FOR SQLEXCEPTION
	BEGIN
		-- Retornar erros antes do rollback para não perder o log
		SHOW ERRORS LIMIT 1;
		SELECT 'Erro na transação atual detectado, revertendo operações...' Warning;
		ROLLBACK;
	END;
	
	START TRANSACTION;
	SELECT MAX(id_order) + 1 INTO @orderNumbers
		FROM orders;

	INSERT INTO orders VALUES (@orderNumbers, 'Fogão');
	SET @orderNumbers = @orderNumbers + 1;
	INSERT INTO orders VALUES (@orderNumbers, 'Geladeira', 3);
	
	COMMIT;
END//
DELIMITER ;

CALL sql_fail();

SELECT * FROM information_schema.ROUTINES r  WHERE ROUTINE_SCHEMA = 'test_transactions';

-- Verificando engines
SHOW ENGINES;

SHOW ENGINE InnoDB STATUS;

SHOW ENGINE InnoDB MUTEX;

SHOW ENGINE performance_schema STATUS;
