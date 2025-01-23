-- Mais exemplos de procedures

USE company;
DESCRIBE employee;

delimiter $
CREATE PROCEDURE IF NOT EXISTS insert_into_employee()
BEGIN
    INSERT INTO employee (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) 
        VALUES ('Maria', 'B', 'Smith', '123456824', '1965-08-10', '731-Fondren-Houston-TX', 'F', '35000.00', '123456789', '5');
END$

delimiter ;

-- Rotinas sem parâmetros podem ser chamadas sem ()
CALL insert_into_employee;
SELECT * FROM employee;

DROP PROCEDURE insert_into_employee;

-- Permitindo inserir valores com variáveis
delimiter $
CREATE PROCEDURE IF NOT EXISTS insert_into_employee(
    IN Fname_p VARCHAR(15),
    IN Minit_p CHAR,
    IN Lname_p VARCHAR(15),
    IN Ssn_p CHAR(9),
    IN Bdate_p DATE,
    IN Address_p VARCHAR(30),
    IN Sex_p CHAR,
    IN Salary_p DECIMAL(10,2),
    IN Super_ssn_p CHAR(9),
    IN Dno_p INT
    )
BEGIN
    INSERT INTO employee (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) 
        VALUES (Fname_p, Minit_p, Lname_p, Ssn_p, Bdate_p, Address_p, Sex_p, Salary_p, Super_ssn_p, Dno_p);
    SELECT * FROM employee WHERE Ssn=Ssn_p;
END$

delimiter ;

CALL insert_into_employee(
    'Cláudio', 'B', 'Texeira', '123859824', '1990-08-10', '731-Fondren-Houston-TX', 'M', '40000.00', '123456789', '4');

-- Outros exemplos
CREATE DATABASE test_proc;
USE test_proc;

CREATE TABLE user(
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha CHAR(32) NOT NULL,
    data_cadastro DATETIME NOT NULL
);

delimiter |
CREATE PROCEDURE procedure_test(IN nome_p VARCHAR(30), IN email_p VARCHAR(50), IN senha_p VARCHAR(20))
BEGIN
    -- Se tamanho da senha < 8
    IF (LENGTH(senha_p) < 8) THEN 
        SELECT 'Senha fraca' AS Message_error;
    ELSE
        -- Senha inserida com criptografia MD5 e data com função now()
        INSERT INTO user (nome, email, senha, data_cadastro) 
            VALUES (nome_p, email_p, MD5(senha_p), NOW());
        SELECT 'Operação Bem Sucedida';
    END IF;
END|

delimiter ;

CALL procedure_test('Gabryel', 'gabryel@email.com', '123456789');
SELECT * FROM user;

DROP DATABASE test_proc;
DROP PROCEDURE procedure_test;

--TODO: Outras funções armazenadas