-- Junções
USE company;

DESC employee;
DESC works_on;
-- JOIN sem cláusula de junção -- Produto cartesiano
SELECT * FROM employee JOIN works_on;

-- O mesmo que CROSS JOIN
SELECT * FROM employee CROSS JOIN works_on;

-- JOIN com cláusula de junção -- Intercessão
SELECT * FROM employee JOIN works_on ON Ssn=Essn;

SELECT * FROM employee, works_on WHERE Ssn=Essn;

-- O mesmo que INNER JOIN
SELECT * FROM employee 
	INNER JOIN works_on ON Ssn=Essn;
    
-- Recuperando dados de uma tabela de junção
SELECT Fname, Lname, Address
	FROM (employee JOIN department ON Dno=Dnumber)
    WHERE Dname='Research';

-- Cláusula de junção com atributos de mesmo nome, USING
SELECT Dname, Dept_create_date, Dlocation
	FROM department JOIN dept_locations USING (Dnumber);

-- Cláusula WHERE filtra as instâncias da nova tabela de junção
SELECT Dname, Dlocation, COUNT(*) 'Total Departamentos' 
	FROM department JOIN dept_locations USING (Dnumber)
    WHERE Dname NOT LIKE 'Headquarters'
    GROUP BY Dname, Dlocation;

-- Junções entre mais tabelas

SELECT CONCAT(Fname, ' ', Lname) 'Employee Name', Dno, Pname, Pno, Plocation
	FROM employee
	INNER JOIN works_on ON Ssn=Essn
    INNER JOIN project ON Pno=Pnumber
    WHERE Pname LIKE 'Product%'
    ORDER BY Pnumber;
    
SELECT Dnumber, Dname, CONCAT(Fname, ' ', Lname) 'Manager', Salary, ROUND(Salary*0.05) 'Bônus'
	FROM department
	INNER JOIN dept_locations USING (Dnumber)
    INNER JOIN employee ON Ssn=Mgr_ssn
    ;

SELECT DISTINCT Dnumber, Dname, CONCAT(Fname, ' ', Lname) 'Manager', Dependent_name
	FROM department
	INNER JOIN dept_locations USING (Dnumber)
    INNER JOIN (dependent INNER JOIN employee ON Ssn=Essn) ON Ssn=Mgr_ssn
    ;
    
-- Forçando a ordem de execução dos JOINs, impede o otimizador do SGBD de mudar a ordem
SELECT STRAIGHT_JOIN CONCAT(Fname, ' ', Lname) 'Employee Name',
		Dno, Pname, Pno, Plocation
	FROM employee
	INNER JOIN works_on ON Ssn=Essn
	INNER JOIN project ON Pno=Pnumber
	WHERE Pname LIKE 'Product%'
	ORDER BY Pnumber;