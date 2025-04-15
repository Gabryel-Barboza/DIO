-- Criando índices para company

USE company;
SHOW TABLES;
SELECT * FROM employee e;
DESC department;

-- Qual o departamento com maior número de pessoas?
SELECT d.Dname 'Departamento', COUNT(*)'Total de Funcionários'
	FROM department d INNER JOIN employee e ON Dnumber=Dno
	GROUP BY d.Dname
	ORDER BY COUNT(*) DESC;

-- Quais são os departamentos por cidade? 
SELECT d.Dname, dl.Dlocation
	FROM department d INNER JOIN dept_locations dl USING (Dnumber);

-- Relação de empregrados por departamento
SELECT e.Ssn, CONCAT(e.Fname, ' ', e.Minit, ' ', e.Lname) 'Fullname', d.Dname, d.Dnumber, d.Mgr_ssn
	FROM employee e INNER JOIN department d ON e.Dno = d.Dnumber
	ORDER BY d.Dnumber;

-- Número de empregados por projeto
SELECT Pname, Pnumber, COUNT(*) 'Funcionários trabalhando'
	FROM project p 
	INNER JOIN works_on wo ON p.Pnumber = wo.Pno
	INNER JOIN employee e ON e.Ssn = wo.Essn
	GROUP BY p.Pname, p.Pnumber;
	

-- Criar índice para nome e sobrenome em employee
CREATE INDEX idx_name_employee ON employee (Fname, Lname);
SHOW INDEX FROM employee;
-- DROP INDEX idx_fullname_employee ON employee;

-- Verificar índices disponíveis em outras tabelas
SHOW INDEX FROM project;
SHOW INDEX FROM department;
SHOW INDEX FROM dependent;


-- Índices para e-commerce
USE ecommerce;
SHOW TABLES;

-- Cliente x cartões cadastrados
SELECT c.id_cliente, CONCAT(c.nome, ' ', c.sobrenome) 'Nome', c.telefone, c2.id_cartao, 
		c2.nome_titular , c2.numeracao_cartao, c2.tipo_cartao
	FROM cliente c INNER JOIN cartao c2 USING (id_cliente);

-- Cliente x pedido x produto
SELECT c.id_cliente, CONCAT(c.nome, ' ', c.sobrenome) 'Nome', c.estado, 
		p.id_pedido, p.status_pedido, p2.descricao, p2.valor, p.frete
	FROM cliente c 
	INNER JOIN pedido p ON c.id_cliente = p.id_cliente
	INNER JOIN pedido_x_produto pxp ON p.id_pedido = pxp.id_pedido
	INNER JOIN produto p2 ON pxp.id_produto = p2.id_produto;

-- Fornecedor x produto x estoque
SELECT f.id_fornecedor, f.razao_social, f.cnpj, p.id_produto, p.categoria, p.descricao, p.dimensionamento
	FROM fornecedor f 
	INNER JOIN fornecedor_x_produto fxp ON f.id_fornecedor = fxp.id_fornecedor
	INNER JOIN produto p ON fxp.id_produto = p.id_produto;


CREATE INDEX idx_nome_cliente ON cliente (nome, sobrenome);
SHOW INDEX FROM cliente;
SHOW INDEX FROM cartao;
CREATE INDEX idx_cnpj_fornecedor ON fornecedor (cnpj);
SHOW INDEX FROM fornecedor;
CREATE INDEX idx_descricao_produto ON produto (categoria, descricao);
SHOW INDEX FROM produto;
-- DROP INDEX idx_descricao_produto ON produto;
