-- Consultas Aninhadas
USE company;

DESC works_on;

SELECT * FROM employee e, works_on w, project p
	WHERE w.Essn=e.Ssn AND w.Pno=p.Pnumber;

-- Exemplos de informações recuperadas dentro de subquerys
-- Recupera o número de um projeto de um gerente específico e retorna todos os funcionários associados aquele mesmo projeto.
SELECT DISTINCT Pnumber, Fname, Lname from project P, employee E, works_on w
	WHERE (E.Ssn=w.Essn AND P.Pnumber=w.Pno) AND P.Pnumber IN (
		SELECT DISTINCT Pno FROM works_on, employee
			WHERE (Essn=ssn AND Lname='Smith')
    ) OR (
		SELECT Pnumber FROM project p, department d, employee
			WHERE (d.Mgr_ssn=Ssn AND Lname='Smith' AND p.Dnumber=d.Dnumber)
    );

-- Selecionando empregados de determinado gerente
SELECT DISTINCT e.Fname, e.Lname, e.Ssn, e.Super_ssn FROM employee e
	WHERE e.Super_ssn IN (
		SELECT Ssn FROM employee s
        );

-- Cláusulas Unique e Exists

-- Verificando empregados que possuem dependentes
-- As querys internas não influenciam nas externas, portanto não é possível colocar um campo de dependent fora da subquery
SELECT Fname, Lname FROM employee e
	WHERE EXISTS (
		SELECT * FROM dependent d
			WHERE e.Ssn = d.Essn
	);
    
-- Verificando empregados que não possuem dependentes
SELECT Fname, Lname FROM employee e
	WHERE NOT EXISTS (
		SELECT * FROM dependent d
			WHERE e.Ssn = d.Essn
	);

-- Seleciona gerentes de departamento e com um conjunto existente de dependentes
SELECT Fname, Lname FROM employee e, department d
	WHERE (e.Ssn = d.Mgr_ssn) AND EXISTS (
		SELECT * FROM dependent 
			WHERE e.Ssn = Essn
	);
    
-- Seleciona empregados com a contagem de dependentes maior ou igual a 2
SELECT Fname, Lname FROM employee
	WHERE (SELECT COUNT(*) FROM dependent WHERE Essn=Ssn) >= 2;