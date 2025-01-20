-- Rotinas e SQL Dinâmico

SHOW DATABASES;

SHOW TABLES FROM manipulation;
USE manipulation;

-- Criando uma função simples, deterministic para tipo de retorno 
CREATE FUNCTION first_function (num1 INT, num2 INT)
RETURNS INT DETERMINISTIC -- Tipo de valor que vai ser retornado
    RETURN num1 + num2; -- Valor retornado

-- Invocando a função
SELECT first_function(10, 10);

-- Criando uma procedure

USE company;

-- Delimitadores do bloco de procedure, evita confusão de ponto e vírgula dos statements na interpretação do mysql, trocando o delimitador. {//, |, $$}
delimiter //
CREATE PROCEDURE info_employee()
BEGIN
    SELECT * FROM employee;
    SELECT * FROM department;
END//

delimiter ;

-- Invocando procedure
CALL info_employee();

-- Deletando procedure
DROP PROCEDURE info_employee;

