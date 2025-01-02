-- Comandos SQL com CASE

USE company;

SELECT Fname, Salary, Dno FROM employee;

-- Atualizando registros com condições estruturadas
-- Desabilite o safe mode do Workbench em Edit - Preferences - SQL Editor e reconecte
-- Ou use LIMIT de no máximo 3 para contornar a restrição. Apenas os três primeiros registros são alterados!
UPDATE employee SET Salary =
	CASE -- início bloco CASE
		WHEN Dno=5 THEN Salary + 2000 -- Condições e expressões
        WHEN Dno=4 THEN Salary + 1500
        WHEN Dno=1 THEN Salary + 3000
        ELSE Salary + 0 -- Valor padrão se nenhuma condição executada
    END; -- fim bloco CASE
    
-- Recuperando registros com CASE
SELECT Fname, Ssn, Salary, Dno, Dname FROM employee, department
	WHERE Dno=Dnumber
	ORDER BY Dno;

SELECT CONCAT(Fname, ' ', Lname) AS 'Employee Name',
	CASE
		WHEN Dno=5 THEN 'Research'
        WHEN Dno=4 THEN 'Administration'
        WHEN Dno=1 THEN 'Headquarters'
	END AS 'Department'
	FROM employee;
    
-- CASE statement e agrupamentos
SELECT Dno,
	CASE
		WHEN Dno=5 THEN 'Research'
        WHEN Dno=4 THEN 'Administration'
        WHEN Dno=1 THEN 'Headquarters'
	END AS 'Department', COUNT(*) 'Total Empregados'
	FROM employee
    GROUP BY 1; -- Cria os grupos com a primeira coluna do statement
    
-- CASE dentro de funções de agregação
-- Se determinado empregado aparecer no cálculo, utilizar 0, caso contrário utilize o salário
SELECT  Dnumber, 
	SUM(CASE WHEN Ssn=888665555 THEN 0 ELSE Salary END) 'Somatória de Salários'
	FROM employee, department	
	WHERE Dno=Dnumber
    GROUP BY Dnumber;
