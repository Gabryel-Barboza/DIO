-- Transactions
USE company;

SET @@AUTOCOMMIT = 0;
SELECT @@AUTOCOMMIT;

START TRANSACTION;
	SELECT * FROM employee;
	INSERT INTO employee VALUES ('Cleber', 'G', 'Silva', '098765432', '1980-05-10', NULL, 'M', 30000, 222345679, 5);
	ROLLBACK;

-- Procedures e Transactions
DELIMITER ||
CREATE PROCEDURE insert_values_employee(
	Fname VARCHAR(15), Minit CHAR(1), Lname VARCHAR(15), Ssn CHAR(9), Bdate DATE, Address VARCHAR(30), 
	Sex CHAR(1), Salary DECIMAL(10,2), Super_ssn CHAR(9), Dno INT
)
BEGIN
	-- Estrutura para tratemento de erros geralmente
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
	BEGIN
		SHOW ERRORS LIMIT 1;
		ROLLBACK;
	END;
	
	START TRANSACTION;
		INSERT INTO employee VALUES 
			(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno);

		COMMIT;
	
END||
DELIMITER ;

-- Faltando o campo Dno, retorna um erro
CALL insert_values_employee('Cleber', 'G', 'Silva', '098765432', '1980-05-10', NULL, 'M', 30000, 222345679);

-- Backup de ecommerce

-- Completo = banco de dados + rotinas + eventos 
-- mysqldump -u root -p -R -E company > company_full_backup.sql

-- Dividido = esquema do banco de dados ou registros
-- Registros: mysqldump -u root -p --no-create-info company > company_data_backup.sql
-- Esquema: mysqldump -u root -p --no-data company > company_schema_backup.sql

-- Recovery
-- mysql -u root -p < arquivo_backup.sql
