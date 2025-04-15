-- Triggers

USE ecommerce;
SHOW TRIGGERS;
SHOW TABLES;
DESC pedido;

-- Trigger para evento antes de inserção
DROP TRIGGER cartao_check_expire_date;
-- Impede que um cartão com a data de validade expirada seja inserido
DELIMITER ||
CREATE TRIGGER cartao_check_expire_date BEFORE INSERT ON cartao
FOR EACH ROW
BEGIN
	IF (NEW.data_validade <= NOW()) THEN
		-- Emite um sinal de erro com a mensagem seguinte
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'A data de validade do cartão está inválida ou expirada!';
	END IF;
END||
DELIMITER ;

SELECT * FROM cartao;
INSERT INTO cartao VALUES (1, default, 'crédito', 'Lucas Almeida', '1111222233334442', '2025-03-12');
DELETE FROM cartao WHERE id_cartao = LAST_INSERT_ID();

USE company;
DESC employee;

-- Bônus de salário em update para departamento específico
drop trigger salary_update_department;
DELIMITER ||
CREATE TRIGGER salary_update_department BEFORE UPDATE ON employee
FOR EACH ROW 
BEGIN
	IF (NEW.Dno = 1) THEN
		SET NEW.Salary = NEW.Salary * 1.20;
	END IF;
END||
DELIMITER ;

SELECT * FROM employee;
INSERT INTO employee VALUES 
	('Kaio', 'N', 'Silva', '123456987', '1990-10-10', '09-Gama-GO', 'M', 25000, '888665555', 5);
UPDATE employee SET Dno = 1 WHERE Ssn = '123456987';

-- Salvando em outra tabela empregados demitidos - old.atribute
CREATE TABLE resigned_employee(
	Fname VARCHAR(15) NOT NULL,
	Minit CHAR(1),
	Lname VARCHAR(15) NOT NULL,
	Ssn CHAR(9) NOT NULL,
	Bdate DATE,
	Address VARCHAR(30),
	Sex CHAR(1),
	Salary DECIMAL(10,2),
	Super_ssn CHAR(9),
	Dno INT NOT NULL
);

DELIMITER ||
CREATE TRIGGER insert_resigned_employees BEFORE DELETE ON employee
FOR EACH ROW
BEGIN
	-- Cadastrando funcionários demitidos com o valor antigo
	INSERT INTO resigned_employee VALUES 
		(OLD.Fname, OLD.Minit, OLD.Lname, OLD.Ssn, OLD.Bdate, OLD.Address, OLD.Sex, OLD.Salary, OLD.Super_ssn, OLD.Dno);
END||
DELIMITER ;

-- Empregados demitidos são automaticamente inseridos na tabela
DELETE FROM employee WHERE Ssn = '123456987';
SELECT * FROM resigned_employee;
SELECT * FROM employee;

SHOW TRIGGERS;