-- Views

USE company;
SHOW TABLES;

-- Número de empregados por departamento e localidade 
CREATE OR REPLACE VIEW employee_department_location_view AS
	SELECT d.Dname 'Department Name' , dl.Dlocation 'Department Location', COUNT(*) 'Employees'
		FROM employee e 
		INNER JOIN department d ON e.Dno = d.Dnumber
		INNER JOIN dept_locations dl ON d.Dnumber = dl.Dnumber
		GROUP BY d.Dname, dl.Dlocation;

SELECT * FROM employee_department_location_view;

-- Lista de departamentos e seus gerentes 
CREATE OR REPLACE VIEW department_manager_view AS
	SELECT CONCAT(e.Fname, ' ', e.Minit, ' ', e.Lname) 'Manager Name', e.Salary, 
			d.Mgr_ssn 'Manager Ssn', d.Dnumber 'Department Number', d.Dname 'Department Name'
		FROM department d 
		INNER JOIN employee e ON d.Mgr_ssn = e.Ssn;

SELECT * FROM department_manager_view;

-- Projetos com maior número de empregados (ex: por ordenação desc) 
CREATE OR REPLACE VIEW project_employees_view AS
	SELECT p.Pname 'Project', COUNT(*) 'Employees Assigned' 
		FROM project p 
		INNER JOIN works_on wo ON p.Pnumber = wo.Pno 
		INNER JOIN employee e ON e.Ssn = wo.Essn
		GROUP BY p.Pname;

SELECT * FROM project_employees_view;

-- Lista de projetos, departamentos e gerentes 
CREATE OR REPLACE VIEW project_department_manager_view AS
	SELECT p.Pname 'Project', p.Plocation 'Project Location', d.Dname 'Department Name', e.Ssn 'Manager SSN', 
			CONCAT(e.Fname, ' ', e.Minit, ' ', e.Lname) 'Manager Name', wo.Hours 
		FROM project p 
		INNER JOIN works_on wo ON p.Pnumber = wo.Pno 
		INNER JOIN employee e ON e.Ssn = wo.Essn 
		INNER JOIN department d ON d.Mgr_ssn = e.Ssn;

SELECT * FROM project_department_manager_view;

-- Quais empregados possuem dependentes e se são gerentes 
CREATE OR REPLACE VIEW manager_dependent_view AS
	SELECT e.Ssn, e.Fname, e.Lname, dt.Dependent_name, dt.Relationship
		FROM employee e 
		INNER JOIN dependent dt ON e.Ssn = dt.Essn
		INNER JOIN department d ON e.Ssn = d.Mgr_ssn;
		

SELECT * FROM manager_dependent_view;


-- Criando usuários para controle de acesso
-- 'nome_usuario'@'localhost ou % ou host' e padrão de autenticação
CREATE USER 'gerente'@'localhost' IDENTIFIED BY 'Senha123@mudar';

-- Dando todos os privilégios nas tabelas para o usuário
GRANT ALL PRIVILEGES ON company.* TO 'gerente'@'localhost';
