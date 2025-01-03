-- Adicionando constraints ao esquema relacional
CREATE SCHEMA IF NOT EXISTS company;

-- Recriando tabelas se já existirem
DROP TABLE IF EXISTS employee, department, dependent, dept_locations, project, works_on;

USE company;

SELECT * FROM information_schema.table_constraints
WHERE constraint_schema='company';

-- Informações de restrição referencial
SELECT * FROM information_schema.referential_constraints;

CREATE TABLE employee(
	Fname VARCHAR(15) NOT NULL,
    Minit CHAR,
    Lname VARCHAR(15) NOT NULL,
    Ssn CHAR(9) NOT NULL,
    Bdate DATE,
    Address VARCHAR(30),
    Sex CHAR,
    Salary DECIMAL(10, 2),
    Super_ssn CHAR(9),
    Dno INT NOT NULL,
    -- Adicionando um nome para a restrição
    CONSTRAINT chk_salary_employee CHECK (Salary > 2000.0), -- Condição de checagem do atributo Salary em instâncias
    CONSTRAINT pk_employee PRIMARY KEY (Ssn) -- No MySQL o nome é sempre PRIMARY
);

CREATE TABLE department(
	Dname VARCHAR(15) NOT NULL,
    Dnumber INT NOT NULL,
    Mgr_ssn CHAR(9),
    Mgr_start_date DATE,
    Dept_create_date DATE,
    CONSTRAINT chk_date_dept CHECK(Dept_create_date < Mgr_start_date),
    PRIMARY KEY (Dnumber),
    CONSTRAINT unique_dept_name UNIQUE (Dname),
    CONSTRAINT fk_dept_employee FOREIGN KEY (Mgr_ssn) REFERENCES employee (Ssn)
);

CREATE TABLE dept_locations(
	Dnumber INT NOT NULL,
    Dlocation VARCHAR(15) NOT NULL,
    PRIMARY KEY (Dnumber, Dlocation),
    CONSTRAINT fk_dept_locations_department FOREIGN KEY (Dnumber) REFERENCES department (Dnumber)
);

CREATE TABLE project(
	Pname VARCHAR(15) NOT NULL,
    Pnumber INT NOT NULL,
    Plocation VARCHAR(15),
    Dnumber INT NOT NULL,
    PRIMARY KEY (Pnumber),
    CONSTRAINT unique_project_name UNIQUE (Pname),
    CONSTRAINT fk_project_department FOREIGN KEY (Dnumber) REFERENCES department (Dnumber)
);

CREATE TABLE works_on(
	Essn CHAR(9) NOT NULL,
    Pno INT NOT NULL,
    Hours DECIMAL(3, 1) NOT NULL,
    PRIMARY KEY (Essn, Pno),
    CONSTRAINT fk_works_on_employee FOREIGN KEY (Essn) REFERENCES employee (Ssn),
    CONSTRAINT fk_works_on_project FOREIGN KEY (Pno) REFERENCES project (Pnumber)
);

CREATE TABLE dependent(
	Essn CHAR(9) NOT NULL,
    Dependent_name VARCHAR(15) NOT NULL,
    Sex CHAR,
    Bdate DATE,
    Relationship VARCHAR(8),
    Age INT NOT NULL,
    CONSTRAINT chk_age CHECK (Age < 22),
    PRIMARY KEY (Essn, Dependent_name),
    CONSTRAINT fk_dependent_employee FOREIGN KEY (Essn) REFERENCES employee (Ssn)
);

SHOW TABLES;
DESC department;
DESC employee;
