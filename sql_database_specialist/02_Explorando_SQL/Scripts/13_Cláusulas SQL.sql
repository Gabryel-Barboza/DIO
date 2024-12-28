# Cláusulas de Ordenação
USE company;

-- Ordena a projeção com base na coluna, por padrão em ordem crescente
SELECT * FROM employee
	ORDER BY Dno;

-- Mais colunas para determinar uma ordenação, caso a primeira coluna tenha valores iguais
SELECT * FROM employee
	ORDER BY Fname, Lname;

SELECT d.Dname, concat(e.Fname, ' ', e.Lname) 'Employee Name', Address 
	FROM employee e, department d
	WHERE (e.Ssn=d.Mgr_ssn AND e.Dno=d.Dnumber)
    ORDER BY d.Dname, e.Fname, e.Lname;

-- Definindo sentido de ordenação com DESC, ASC é valor padrão
SELECT * FROM employee
	ORDER BY Salary DESC, Fname ASC;

# Funções de Agregação

SELECT * FROM employee;
-- Conta o número de registros de um atributo
SELECT COUNT(*) FROM employee;

-- Contagem de registros distintos
SELECT COUNT(DISTINCT SALARY) FROM employee;

-- Conta o número de registros após a filtragem
SELECT COUNT(*) 'Total Departamentos de Pesquisa'
	FROM employee, department
	WHERE Dno=Dnumber AND Dname='Research';

-- AVG e ROUND, Verifica a média de Salary e arredonda em 2 casas decimais
SELECT Dno, COUNT(*) 'Total Departamentos de Pesquisa', ROUND(AVG(Salary), 2) 'Média Salarial'
	FROM employee, department
    WHERE Dno=Dnumber AND Dname='Research';
    
SELECT AVG(Salary) 'Média Salarial', SUM(Salary) 'Somatória de Salários', MAX(Salary) 'Valor máximo', MIN(Salary) 'Valor mínimo' 
	FROM employee;
    
# Cláusulas de Agrupamento

-- Realiza a contagem de empregados por gerente
SELECT Super_ssn, COUNT(*) 'Total de Empregados' 
	FROM employee
	GROUP BY Super_ssn;

-- Cria grupos com os valores distintos de Dno, realiza a contagem de registros e a média dentro de cada grupo 
SELECT Dno, COUNT(*) 'Total de Empregados', ROUND(AVG(Salary), 2) 'Média Salarial'
	FROM employee
	GROUP BY Dno;
    
SELECT Pnumber, Pname, COUNT(*) 'Total de empregados'
	FROM project, works_on
	WHERE Pnumber=Pno
    GROUP BY Pnumber, Pname
    ORDER BY Pnumber;

-- Cláusula HAVING
-- Após a criação dos grupos, é filtrado para retornar apenas grupos com a função count(*) > 2
-- Nesse cenário, o projeto ProdutoX não é retornado pois possue 2 instâncias apenas
SELECT Pnumber, Pname, COUNT(*) 'Total Empregados'
	FROM project, works_on
    WHERE Pnumber=Pno
    GROUP BY Pnumber, Pname
    HAVING COUNT(*) > 2;
    
SELECT Dno, COUNT(*) 'Total Empregados' 
	FROM employee
    WHERE Salary > 30000
	GROUP BY Dno
    HAVING COUNT(*) >= 2;

-- Realizando agrupamentos com base em subquerys
SELECT Dno, COUNT(*) 'Total Empregados'
	FROM employee
    WHERE Salary > 20000 AND Dno IN (
		SELECT Dno FROM employee
			GROUP BY Dno
            HAVING COUNT(*) >= 3
    )
    GROUP BY Dno
    ORDER BY Dno ASC;
