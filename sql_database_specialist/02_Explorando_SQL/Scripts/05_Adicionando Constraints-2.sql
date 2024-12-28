-- Alterando tabelas existentes e adicionando constraints
USE company;

SHOW TABLES;

SELECT * FROM information_schema.table_constraints 
WHERE constraint_schema='company';

SELECT * FROM information_schema.referential_constraints;

-- Informações do esquema
SELECT * FROM information_schema.schemata;

DESC employee;

-- Alterando tabelas
-- Adicionando novas constraints para a tabela employee
ALTER TABLE employee
	ADD CONSTRAINT fk_employee_super FOREIGN KEY (Super_ssn) REFERENCES employee (ssn)
    ON DELETE SET NULL -- Quando deletado atribuir nulo
    ON UPDATE CASCADE; -- Quando atualizado o estado, refletir em tabelas filhas

-- Alterando colunas existentes
ALTER TABLE employee MODIFY Dno INT NOT NULL DEFAULT 1;

DESC department;

-- Alterando constraints
ALTER TABLE department DROP CONSTRAINT fk_dept_employee;

ALTER TABLE department 
	ADD CONSTRAINT fk_dept_employee 
	FOREIGN KEY (Mgr_ssn) REFERENCES employee (Ssn)
	ON UPDATE CASCADE;

ALTER TABLE dept_locations DROP CONSTRAINT fk_dept_locations_department;

ALTER TABLE dept_locations
	ADD CONSTRAINT fk_dept_locations_department
    FOREIGN KEY (Dnumber) REFERENCES department (Dnumber)
    ON DELETE CASCADE -- Ao deletar, refletir em tabelas filhas
    ON UPDATE CASCADE;
