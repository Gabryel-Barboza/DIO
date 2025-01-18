-- Views, isolando dados e complexidade de querys e tabelas.
-- Tabelas virtuais, armazenadas em memória volátil
USE information_schema;

-- Verificando views existentes
SELECT * FROM VIEWS WHERE table_schema='company';

USE company;

-- Criando uma view, nomeando as colunas em view(atributos). Se já existir, substitui
CREATE OR REPLACE VIEW v_data(Data_hoje) AS
	SELECT current_date();

DROP VIEW v_data;

SELECT * FROM v_data;

DESCRIBE v_data;

CREATE OR REPLACE VIEW employee_salary_27000_view AS
	SELECT concat(Fname, ' ' , Minit) 'Name', Salary, Dno 'Department_number' FROM employee
		WHERE Salary >= 27000;
        
SELECT * FROM employee_salary_27000_view;

-- As tabelas virtuais são exibidas
SHOW TABLES;

-- Views baseadas em junções
CREATE OR REPLACE VIEW employee_dependent_view AS
	SELECT concat(Fname, ' ' , Minit) 'Name', Salary, Dno 'Department_number', Dependent_name FROM employee
		INNER JOIN dependent ON Ssn=Essn;
        
SELECT * FROM employee_dependent_view;

-- Atualizando Views
-- Um UPDATE statement na view vai refletir na tupla da tabela original
-- Não é possível usar o INSERT INTO, a estrutura da view não é a mesma da tabela referente.
SELECT * FROM employee_salary_27000_view;

UPDATE employee_salary_27000_view 
	SET Department_number=1
    WHERE Salary=34000.00
    LIMIT 1;

-- Tupla da tabela original recebe o valor
SELECT * FROM employee WHERE Fname='John';

UPDATE employee_salary_27000_view 
	SET Department_number=5
    WHERE Name='John B'
    LIMIT 1;

-- Alterar valores de tabelas distintas na mesma view
SELECT * FROM employee_dependent_view;

-- Não é permitido modificar duas tabelas distintas na mesma query
UPDATE employee_dependent_view 
	SET Department_number=1, Dependent_name='Mary'
    WHERE Name='John B'
    LIMIT 1;
    
SELECT * FROM employee_dependent_view;