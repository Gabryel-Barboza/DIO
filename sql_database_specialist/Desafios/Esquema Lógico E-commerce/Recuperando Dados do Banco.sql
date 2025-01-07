-- Criando consultas para analisar os dados

USE ecommerce;

SHOW TABLES;
DESC cliente;

SELECT * FROM pessoa_fisica NATURAL JOIN cliente;

-- Cliente de pessoa física e todos os seus dados formatados
SELECT id_cliente, cpf, concat(nome, ' ', sobrenome) 'Nome Completo', concat(rua, ' ', bairro, ' ', complemento, ' ', cidade, ' ', estado) 'Endereço', telefone
    FROM cliente INNER JOIN pessoa_fisica USING (id_cliente);

-- Cliente de pessoa jurídica e todos os seus dados formatados
SELECT id_cliente, cnpj, concat(nome, ' ', sobrenome) 'Nome Completo', concat(rua, ' ', bairro, ' ', complemento, ' ', cidade, ' ', estado) 'Endereço', telefone
    FROM cliente INNER JOIN pessoa_juridica USING (id_cliente);

-- Junção entre várias tabelas com dados do cliente, pedido e produto comprado
SELECT c.id_cliente, concat(c.nome, ' ', c.sobrenome) 'Nome Completo', c.estado, p.id_pedido,  p.status_pedido, p.frete, p.tipo_pagamento, pr.id_produto, pr.categoria, pr.descricao, pr.valor
    FROM cliente c INNER JOIN pedido p USING (id_cliente)
    INNER JOIN pedido_x_produto px ON (p.id_pedido=px.id_pedido)
    INNER JOIN produto pr ON (px.id_produto=pr.id_produto);


-- Filtrando informações de cliente que possui cartão
SELECT c.id_cliente, c.nome, ca.id_cartao, ca.nome_titular, ca.tipo_cartao, ca.numeracao_cartao, ca.data_validade 
    FROM cliente c, cartao ca
    WHERE c.id_cliente=ca.id_cliente
    ORDER BY ca.nome_titular;

-- Verificando quem possui e quem não possui cartão
SELECT c.id_cliente, c.nome, ca.id_cartao, ca.nome_titular, ca.tipo_cartao, ca.numeracao_cartao, ca.data_validade
    FROM cliente c LEFT OUTER JOIN cartao ca USING (id_cliente)
    ORDER BY id_cartao DESC;

-- Produtos cadastrados no estoque de São Paulo
SELECT * 
    FROM produto INNER JOIN produto_em_estoque USING (id_produto)
    INNER JOIN estoque USING (id_estoque)
    WHERE local='São Paulo - SP';


-- Entregas agrupadas por etapa
SELECT status_entrega, count(*) 'Total' 
    FROM entrega
    GROUP BY status_entrega
    ORDER BY Total DESC;

-- Pedidos e preço médio agrupados por categoria de produto
SELECT categoria, count(*) 'Total de Pedidos', AVG(valor) 'Preço Médio'
    FROM pedido INNER JOIN pedido_x_produto USING (id_pedido)
    INNER JOIN produto USING (id_produto)
    GROUP BY categoria;

-- Tipos de pagamentos mais utilizados pelos clientes
SELECT tipo_pagamento, count(*) 'Total de usuários' 
    FROM pedido
    GROUP BY tipo_pagamento HAVING count(*) > 2;

-- Relação de produtos, fornecedores e estoques;
SELECT p.id_produto, p.categoria, p.descricao, p.valor, f.id_fornecedor, f.razao_social, f.cnpj, pe.quantidade, e.local 'Local de Estoque'
    FROM produto p 
    INNER JOIN fornecedor_x_produto fp ON p.id_produto=fp.id_produto
    INNER JOIN fornecedor f ON f.id_fornecedor=fp.id_fornecedor
    INNER JOIN produto_em_estoque pe ON p.id_produto=pe.id_produto
    INNER JOIN estoque e ON pe.id_estoque=e.id_estoque
    ORDER BY categoria;

-- Relação de nomes dos fornecedores de terceiros e nomes dos produtos;
SELECT f.id_fornecedor_terceiro, f.razao_social, f.nome_fantasia, f.local, p.id_produto, p.categoria, p.descricao, p.valor 
    FROM fornecedor_terceiro f INNER JOIN terceiro_x_produto tp ON f.id_fornecedor_terceiro=tp.id_fornecedor_terceiro
    INNER JOIN produto p ON tp.id_produto=p.id_produto
    ORDER BY razao_social;
