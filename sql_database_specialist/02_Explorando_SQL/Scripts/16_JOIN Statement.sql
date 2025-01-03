-- Junções não correspondentes

USE company;

SELECT * FROM employee;
SELECT * FROM dependent;

-- INNER JOIN
SELECT * FROM employee INNER JOIN dependent ON Ssn=Essn;

SELECT * FROM employee JOIN dependent ON Ssn=Essn;

-- OUTER JOIN
-- Junção de correspondência e de tuplas não correspondentes

--SELECT * FROM employee FULL OUTER JOIN dependent ON Ssn=Essn; -- Necessita da orientação no MySQL

-- LEFT JOIN
-- O mesmo que LEFT OUTER JOIN, retorna tuplas não coincidentes da tabela à esquerda
SELECT * FROM employee LEFT JOIN dependent ON Ssn=Essn;

SELECT * FROM employee LEFT OUTER JOIN dependent ON Ssn=Essn;

-- RIGHT JOIN
-- Retorna as tuplas com prioridade a direita. Por questões semânticas, descreva que é um OUTER JOIN
SELECT * FROM dependent RIGHT OUTER JOIN employee ON Ssn=Essn;
-- Se não existir tuplas sem correspondência, retorna apenas a intercessão

SELECT * FROM department;
SELECT * FROM dept_locations;

-- NATURAL JOIN
-- Deixe o SGBD procurar um atributo comum, possuindo mesmo domínio e papel
SELECT * FROM department NATURAL JOIN dept_locations;

-- FULL OUTER JOIN e FULL EXCLUDING JOIN, ANTI LEFT JOIN e ANTI RIGHT JOIN
