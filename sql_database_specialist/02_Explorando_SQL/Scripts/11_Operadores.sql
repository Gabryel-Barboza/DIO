-- Operadores Like e Between

USE company;

SELECT * FROM department;

-- Operador % para indicar 0 ou mais caracteres na posição
SELECT concat(Fname, ' ', Lname) 'Name', Address FROM employee
	WHERE Address LIKE '%Houston%';

SELECT concat(Fname, ' ', Lname) 'Name', Dname 'Department Name', Address
	FROM employee, department
    WHERE (Dno=Dnumber AND Address LIKE '%Houston%');

-- Verificando intervalos numéricos
SELECT Fname, Salary FROM employee
	WHERE (Salary >= 30000 AND Salary <= 40000);

SELECT Fname, Salary FROM employee
	WHERE (Salary BETWEEN 30000 AND 40000);

-- Operadores Union, Intersection e Except
-- Necessitam de tabelas de mesma estrutura

CREATE DATABASE IF NOT EXISTS conjuntos;

USE conjuntos;

CREATE TABLE R(
	A CHAR(2)
);

CREATE TABLE S(
	A CHAR(2)
);

INSERT INTO R VALUES ('a1'), ('a2'), ('a2'), ('a3');

INSERT INTO S VALUES ('a1'), ('a2'), ('a3'), ('a4'), ('a5');

SELECT * FROM R, S;

-- Union - une dois conjuntos, retirando redundâncias
-- Utiliza subquerys e realiza a união
(SELECT R.A FROM R) UNION (SELECT S.A FROM S);

-- Intersection - cria um conjunto a partir de sua interseção
-- Não possui palavra chave, criada com operador IN. Cláusula DISTINCT para retirar redundâncias
SELECT DISTINCT R.A FROM R WHERE A IN (SELECT S.A FROM S);

-- Except - cria um conjunto com valores não presentes no outro conjunto
-- Inverso de intersection, com NOT IN
SELECT S.a FROM S WHERE A NOT IN (SELECT R.A FROM R);
