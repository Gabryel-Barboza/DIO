-- Utilizando Alias em querys

USE company;

-- Duas tabelas com mesmo nome de atributo
DESC department;
DESC dept_locations;

SELECT * FROM dept_locations;

-- Evitando ambiguidade
SELECT * FROM department, dept_locations
	WHERE department.Dnumber = dept_locations.Dnumber;

-- Aplicando alias em atributos e tabelas
-- AS pode ser omitido nesse cenário
SELECT Dname as Department_name, d.Dnumber, Dlocation 
	FROM department AS d, dept_locations AS l
    WHERE d.Dnumber = l.Dnumber;

-- Utilizando uma função de concatenação de colunas
SELECT concat(Fname, ' ', Lname) AS Name FROM employee;
