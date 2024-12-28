-- Expressões em SQL

USE company;
-- Atributos derivados
SELECT Fname, Lname, Salary, Salary * 0.11 FROM employee;
-- Funções especiais: round - arredondar na quantidade de casas especificada
SELECT Fname, Lname, Salary, round(Salary*0.11, 2) AS INSS FROM employee;

DESC project;

-- 10% de aumento para funcionários de ProductX
SELECT * FROM employee e, works_on w, project p
	WHERE (e.Ssn=w.Essn AND p.Pnumber=w.Pno AND p.Pname='ProductX');
    
SELECT Fname, Lname, Salary, 1.1*Salary FROM employee e, works_on w, project p
	WHERE (e.Ssn=w.Essn AND p.Pnumber=w.Pno AND p.Pname='ProductX'); 

SELECT concat(Fname, ' ', Lname) AS 'Complete name', Salary, 1.1*Salary AS 'Salary after increase'
	FROM employee e, works_on w, project p
	WHERE (e.Ssn=w.Essn AND p.Pnumber=w.Pno AND p.Pname='ProductX'); 
