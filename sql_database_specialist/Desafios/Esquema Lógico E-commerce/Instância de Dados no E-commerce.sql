-- Instanciando valores no esquema

USE ecommerce;

SHOW TABLES;
DESC cliente;
SELECT * FROM pedido;

-- Foi utilizado um gerador de dados para popular o banco de dados de maneira mais eficaz

INSERT INTO cliente (nome, sobrenome, telefone, rua, bairro, complemento, cidade, estado) VALUES
    ('Lucas', 'Almeida', '11912345678', 'Rua 1', 'Centro', 'Apto 1', 'São Paulo', 'SP'),
    ('Ana', 'Santos', '21998765432', 'Rua 2', 'Bairro Alto', 'Casa', 'Curitiba', 'PR'),
    ('Bruno', 'Pereira', '31987654321', 'Rua 3', 'Centro', 'Bloco B', 'Belo Horizonte', 'MG'),
    ('Mariana', 'Costa', '41956781234', 'Rua 4', 'Jardins', 'Apto 4', 'Rio de Janeiro', 'RJ'),
    ('Carlos', 'Silva', '51934567890', 'Rua 5', 'Centro', 'Casa 5', 'Porto Alegre', 'RS'),
    ('Fernanda', 'Oliveira', '61945678901', 'Rua 6', 'Centro', 'Apto 6', 'Florianópolis', 'SC'),
    ('Paulo', 'Ferreira', '71923456789', 'Rua 7', 'Centro', 'Apto 7', 'Salvador', 'BA'),
    ('Julia', 'Lima', '81976543210', 'Rua 8', 'Centro', 'Apto 8', 'Fortaleza', 'CE'),
    ('Thiago', 'Barbosa', '85989876543', 'Rua 9', 'Bairro Novo', 'Casa 9', 'Recife', 'PE'),
    ('Isabela', 'Rocha', '91912340987', 'Rua 10', 'Centro', 'Casa 10', 'Natal', 'RN');

INSERT INTO pessoa_fisica (id_cliente, cpf) VALUES
    (1, '12345678901'),
    (2, '23456789012'),
    (3, '34567890123'),
    (4, '45678901234'),
    (5, '56789012345'),
    (6, '67890123456');

INSERT INTO pessoa_juridica (id_cliente, cnpj) VALUES
    (7, '12345678000199'),
    (8, '23456789000188'),
    (9, '34567890000177'),
    (10, '45678900000166');

INSERT INTO cartao (id_cliente, tipo_cartao, nome_titular, numeracao_cartao, data_validade) VALUES
    (1, 'crédito', 'Lucas Almeida', '1111222233334444', '2025-12-31'),
    (2, 'débito', 'Ana Santos', '2222333344445555', '2024-11-30'),
    (3, 'crédito', 'Bruno Pereira', '3333444455556666', '2026-01-31'),
    (4, 'débito', 'Mariana Costa', '4444555566667777', '2025-06-30'),
    (7, 'crédito', 'Paulo Ferreira', '5555666677778888', '2027-07-31');

INSERT INTO pedido (id_cliente, status_pedido, descricao, tipo_pagamento, frete) VALUES
    (1, 'Processando', 'Compra de eletrônicos', 'Dois Cartões', 50.00),
    (2, 'Enviado', 'Compra de roupas', 'Cartão', 30.00),
    (3, 'Entregue', 'Compra de livros', 'Boleto', 20.00),
    (7, 'Em andamento', 'Compra de móveis', 'Cartão', 100.00),
    (5, 'Processando', 'Compra de eletrodomésticos', 'Boleto', 70.00),
    (6, 'Entregue', 'Compra de acessórios', 'Pix', 15.00),
    (8, 'Enviado', 'Compra de materiais escolares', 'Boleto', 25.00),
    (9, 'Em andamento', 'Compra de decoração', 'Pix', 40.00),
    (10, 'Processando', 'Compra de ferramentas', 'Pix', 60.00),
    (10, 'Processando', 'Compra de ferramentas', 'Pix', 60.00);


INSERT INTO entrega (id_pedido, status_entrega, codigo_rastreio) VALUES
    (1, 'Enviado', 'BR123456789'),
    (2, 'Em transporte', 'BR987654321'),
    (3, 'Entregue', 'BR112233445'),
    (4, 'Processando', 'BR556677889'),
    (5, 'Preparando para envio', 'BR334455667'),
    (6, 'Entregue', 'BR998877665'),
    (7, 'Enviado', 'BR776655443'),
    (8, 'Em transporte', 'BR223344556'),
    (9, 'Processando', 'BR667788990'),
    (10, 'Pronto para coleta', 'BR554433221');

INSERT INTO produto (categoria, descricao, valor, dimensionamento) VALUES
    ('Eletrônicos', 'Smartphone', 1500.00, '15x7x1cm'),
    ('Roupas', 'Jaqueta', 200.00, 'M'),
    ('Livros', 'Livro de Ficção', 50.00, 'A4'),
    ('Móveis', 'Mesa de jantar', 800.00, '180x90x75cm'),
     ('Eletrodomésticos', 'Geladeira Frost Free', 2500.00, '60x70x150cm'),
    ('Roupas', 'Camiseta de algodão', 50.00, 'P/M/G'),
    ('Livros', 'Livro de ficção científica', 30.00, '21x14cm'),
    ('Eletrônicos', 'Smartphone 128GB', 2000.00, '15x8cm'),
    ('Móveis', 'Cadeira de escritório', 300.00, '60x60x120cm'),
    ('Alimentos', 'Caixa de chocolates', 25.00, '20x20x5cm'),
    ('Brinquedos', 'Boneca de pano', 40.00, '25x15cm'),
    ('Jogos', 'Jogo de tabuleiro', 120.00, '30x30x5cm'),
    ('Material de escritório', 'Conjunto de canetas', 15.00, '10x5cm'),
    ('Bebidas', 'Garrafa de vinho', 80.00, '30x10cm');

INSERT INTO estoque (local) VALUES
    ('São Paulo - SP'),
    ('Curitiba - PR'),
    ('Belo Horizonte - MG'),
    ('Rio de Janeiro - RJ');

INSERT INTO fornecedor (razao_social, nome_fantasia, cnpj) VALUES
    ('Eletrônicos LTDA', 'EletrônicosSP', '11223344000155'),
    ('Roupas SA', 'RoupasPR', '22334455000166'),
    ('Eletro Distribuidora Ltda', 'EletroDistrib', '11222333445566'),
    ('Livros & Co Ltda', 'LivrosCo', '22334455667788'),
    ('Móveis Premium Ltda', 'MoveisPremium', '33445566778899'),
    ('Alimentos Frescos Ltda', 'AlimentosFrescos', '44556677889900');

INSERT INTO fornecedor_terceiro (razao_social, nome_fantasia, local) VALUES
    ('Livros Importados LTDA', 'LivrosImp', 'Argentina'),
    ('Móveis Global SA', 'MoveisGlobal', 'Portugal'),
    ('Roupas Importadas SA', 'RoupasSA', 'China'),
    ('Eletrônicos da Ásia Ltda', 'EletronAsia', 'Coreia do Sul'),
    ('Brinquedos Mundiais Ltda', 'BrinqMundiais', 'Alemanha'),
    ('Jogos Universais Ltda', 'JogosUniv', 'EUA');

INSERT INTO pedido_x_produto (id_pedido, id_produto, quantidade) VALUES
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 1),
    (4, 4, 1),
    (5, 5, 1),
    (6, 6, 3),
    (7, 7, 2),
    (8, 8, 1),
    (9, 9, 5),
    (10, 10, 1);

INSERT INTO produto_em_estoque (id_produto, id_estoque, quantidade) VALUES
    (1, 1, 100),
    (2, 2, 50),
    (3, 3, 30),
    (4, 1, 20),
    (5, 3, 15),
    (6, 3, 200),
    (7, 4, 50),
    (8, 4, 30),
    (9, 1, 70),
    (10, 2, 25);

INSERT INTO fornecedor_x_produto (id_fornecedor, id_produto) VALUES
    (1, 1),
    (2, 2),
    (4, 3),
    (3, 5),
    (2, 6),
    (6, 10),
    (6, 14),
    (4, 7),
    (5, 9),
    (5, 11),
    (4, 12),
    (4, 13);

INSERT INTO terceiro_x_produto (id_fornecedor_terceiro, id_produto, quantidade) VALUES
    (1, 3, 50),
    (3, 2, 200),
    (2, 4, 50),
    (4, 8, 60);
