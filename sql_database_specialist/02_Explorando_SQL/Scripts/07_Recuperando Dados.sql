-- Criando statements de recuperação de dados

USE company;

SELECT * FROM employee;
SELECT * FROM department;

-- Selecionando colunas específicas de tabelas diferentes, somente instâncias onde o Ssn de um seja igual ao Mgr_ssn do outro
-- Gerente e departamento
SELECT Ssn, Fname, Dname FROM employee e, department d 
	WHERE (e.Ssn = d.Mgr_ssn);

SELECT * FROM dependent;

-- Sem a cláusula WHERE todos os campos de uma tabela são mesclados a outra.
-- Empregado e dependente
SELECT Ssn, Fname, Dependent_name, Relationship FROM employee e, dependent d
	WHERE (e.Ssn = d.Essn);

-- Filtrando mais colunas com operadores lógicos
SELECT Bdate, Address FROM employee
	WHERE Fname='John' AND Minit='B' AND Lname='Smith';


SELECT * FROM department;

-- Comparação de datas
SELECT Dname, Dnumber FROM department WHERE Dept_create_date > '1981-01-01';

-- Empregado e departamento
SELECT Fname, Ssn, Address, Dname FROM employee, department
	WHERE Dnumber=Dno;


SELECT * FROM project;

-- Recuperando valores de três tabelas
SELECT Fname, Ssn, Pname, Pnumber, Dnumber FROM employee, works_on, project
	WHERE employee.Ssn = works_on.Essn AND project.Pnumber = works_on.Pno;
    
