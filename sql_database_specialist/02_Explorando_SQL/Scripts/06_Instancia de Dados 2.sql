-- Inserindo dados no bd com restrições

USE company;

SHOW TABLES;

DESC employee;

-- Primeiro valor inserido com campo nulo devido a integridade referencial,
INSERT INTO employee VALUES
	('John', 'B', 'Smith', '123456789', '1965-01-09', '731-Fondren-Houston-TX', 'M', '30000', null, '5');
    
-- Os atributos foram colocados em ordem quanto ao super_ssn,
-- permitindo a inserção sem falha da integridade referencial
INSERT INTO employee VALUES
	('James', 'E', 'Borg', 888665555, '1937-11-10', '450-Stone-Houston-TX', 'M', 55000, NULL, 1),
    ('Franklin', 'T', 'Wong', 333445555, '1955-12-08', '638-Voss-Houston-TX', 'M', 40000, 888665555, 5),
    ('Ramesh', 'K', 'Narayan', 666884444, '1962-09-15', '975-Fire-Oak-Humble-TX', 'M', 38000, 333445555, 5),
    ('Jennifer', 'S', 'Wallace', 987654321, '1941-06-20', '291-Berry-Bellaire-TX', 'F', 43000, 888665555, 4),
    ('Alicia', 'J', 'Zelaya', 999887777, '1968-01-19', '3321-Castle-Spring-TX', 'F', 25000, 987654321, 4),
    ('Joyce', 'A', 'English', 453453453, '1972-07-31', '5631-Rice-Houston-TX', 'F', 25000, 333445555, 5),
    ('Ahmad', 'V', 'Jabbar', 987987987, '1969-03-29', '980-Dallas-Houston-TX', 'M', 25000, 987654321, 4);

SELECT * FROM employee;

DESC dependent;

ALTER TABLE dependent MODIFY Age INT;

-- Essa query é realizada sem erros, já que employee está persistida com os valores respectivos também
-- Pode-se adicionar valores nulos caso não indique a lista de atributos, o resultado é o mesmo
INSERT INTO dependent VALUES
	(333445555, 'Alice', 'F', '1986-04-05', 'Daughter', NULL),
	(333445555, 'Theodore', 'M', '1983-10-25', 'Son', NULL),
    (333445555, 'Joy', 'F', '1958-05-03', 'Spouse', NULL),
    (987654321, 'Abner', 'M', '1942-02-28', 'Spouse', NULL),
    (123456789, 'Michael', 'M', '1988-01-04', 'Son', NULL),
    (123456789, 'Alice', 'F', '1988-12-30', 'Daughter', NULL),
    (123456789, 'Elizabeth', 'F', '1967-05-05', 'Spouse', NULL);

-- Age pode ser retirada agora, pois é um atributo derivado. Foi adicionada apenas como exemplo
ALTER TABLE dependent DROP COLUMN Age;

SELECT * FROM dependent;

DESCRIBE department;

INSERT INTO department VALUES
	('Research', 5, 333445555, '1988-05-22', '1986-05-22'),
    ('Administration', 4, 987987987, '1995-01-01', '1994-01-01'),
    ('Headquarters', 1, 888665555, '1981-06-19', '1980-06-19');

SELECT * FROM department;

DESC dept_locations;

INSERT INTO dept_locations VALUES
	(1, 'Houston'),
    (4, 'Stafford'),
    (5, 'Bellaire'),
    (5, 'Sugarland'),
    (5, 'Houston');
    
SELECT * FROM dept_locations;

DESC project;

INSERT INTO project VALUES
	('ProductX', 1, 'Bellaire', 5),
    ('ProductY', 2, 'Sugarland', 5),
    ('ProductZ', 3, 'Houston', 5),
    ('Computerization', 10, 'Stafford', 4),
    ('Reorganization', 20, 'Houston', 1),
    ('Newbenefits', 30, 'Stafford', 4);
    
SELECT * FROM project;

DESC works_on;

INSERT INTO works_on VALUES
	(123456789, 1, 32.5),
    (123456789, 2, 7.5),
    (666884444, 3, 40.0),
    (453453453, 1, 20.0),
    (453453453, 2, 20.0),
    (333445555, 2, 10.0),
    (333445555, 3, 10.0),
    (333445555, 10, 10.0),
    (333445555, 20, 10.0),
    (999887777, 30, 30.0),
    (999887777, 10, 10.0),
    (987987987, 10, 35.0),
    (987987987, 30, 5.0),
    (987654321, 30, 20.0),
    (987654321, 20, 15.0),
    (888665555, 20, 0.0);

SELECT * FROM works_on;