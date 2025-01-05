-- Esquema para criação da modelagem E-commerce

DROP DATABASE IF EXISTS ecommerce;

CREATE DATABASE IF NOT EXISTS ecommerce;
USE ecommerce;

-- Criando tabelas da modelagem

CREATE TABLE cliente(
	id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(15) NOT NULL,
    sobrenome VARCHAR(50) NOT NULL,
    rua VARCHAR(15) NOT NULL,
    bairro VARCHAR(15) NOT NULL,
    complemento VARCHAR(15) NOT NULL,
    cidade VARCHAR(15) NOT NULL,
    estado VARCHAR(15) NOT NULL
);

-- pessoa_fisica é generalização de cliente
-- cpf deve ser único
CREATE TABLE pessoa_fisica(
	id_cliente INT PRIMARY KEY,
    cpf CHAR(11) NOT NULL,
    CONSTRAINT unique_cpf UNIQUE (cpf),
    CONSTRAINT fk_pessoa_fisica_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

-- pessoa_juridica é generalização de cliente
-- cnpj deve ser único
CREATE TABLE pessoa_juridica(
	id_cliente INT PRIMARY KEY,
    cnpj CHAR(15) NOT NULL,
    CONSTRAINT unique_cnpj UNIQUE (cnpj),
    CONSTRAINT fk_pessoa_juridica_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

-- Entidade fraca, cartão depende de cliente
CREATE TABLE cartao(
	id_cliente INT,
	id_cartao INT,
    tipo_cartao ENUM("crédito", "débito") NOT NULL,
    nome_titular VARCHAR(50) NOT NULL,
    numeracao_cartao CHAR(16) NOT NULL,
    data_validade DATE NOT NULL,
    PRIMARY KEY (id_cliente, id_cartao),
    CONSTRAINT unique_cartao UNIQUE (numeracao_cartao),
    CONSTRAINT fk_cartao_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente) 
);

CREATE TABLE pedido(
	id_pedido INT PRIMARY KEY AUTO_INCREMENT,
	id_cliente INT,
    status_pedido ENUM("Em andamento", "Processando", "Enviado", "Entregue") DEFAULT "Processando",
    descricao VARCHAR(50),
    tipo_pagamento ENUM("Boleto","Pix","Cartão","Dois Cartões"),
    frete FLOAT,
    CONSTRAINT fk_pedido_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

-- Entidade fraca, entrega depende de pedido
CREATE TABLE entrega(
	id_pedido INT,
	id_entrega INT,
    status_entrega VARCHAR(30) NOT NULL,
    codigo_rastreio VARCHAR(30) NOT NULL,
    PRIMARY KEY (id_pedido, id_entrega),
    CONSTRAINT fk_entrega_pedido FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido)
);

CREATE TABLE produto(
	id_produto INT PRIMARY KEY AUTO_INCREMENT,
    categoria VARCHAR(30),
    descricao VARCHAR(50),
    valor FLOAT NOT NULL,
    dimensionamento VARCHAR(12)
);

CREATE TABLE estoque(
	id_estoque INT PRIMARY KEY AUTO_INCREMENT,
    local VARCHAR(30)
);

CREATE TABLE fornecedor(
	id_fornecedor INT PRIMARY KEY AUTO_INCREMENT,
    razao_social VARCHAR(30),
    nome_fantasia VARCHAR(30),
    cnpj CHAR(15)
);

CREATE TABLE fornecedor_terceiro(
	id_fornecedor_terceiro INT PRIMARY KEY AUTO_INCREMENT,
    razao_social VARCHAR(30),
    nome_fantasia VARCHAR(30),
    local VARCHAR(50)
);

-- Tabelas de relacionamentos
CREATE TABLE pedido_x_produto(
	id_pedido INT,
    id_produto INT,
    quantidade INT DEFAULT 1,
    PRIMARY KEY (id_pedido, id_produto),
    CONSTRAINT fk_pedido_x_produto_pedido FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido),
    CONSTRAINT fk_pedido_x_produto_produto FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
);

CREATE TABLE produto_em_estoque(
	id_produto INT,
    id_estoque INT,
    quantidade INT DEFAULT 1,
    PRIMARY KEY (id_produto, id_estoque),
    CONSTRAINT fk_produto_em_estoque_produto FOREIGN KEY (id_produto) REFERENCES produto (id_produto),
    CONSTRAINT fk_produto_em_estoque_estoque FOREIGN KEY (id_estoque) REFERENCES estoque (id_estoque)
);

CREATE TABLE fornecedor_x_produto(
	id_fornecedor INT,
    id_produto INT,
    PRIMARY KEY (id_fornecedor, id_produto),
    CONSTRAINT fornecedor_x_produto_fornecedor FOREIGN KEY (id_fornecedor) REFERENCES fornecedor (id_fornecedor),
    CONSTRAINT fornecedor_x_produto_produto FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
);

CREATE TABLE terceiro_x_produto(
	id_fornecedor_terceiro INT,
    id_produto INT,
    quantidade INT DEFAULT 1,
    PRIMARY KEY (id_fornecedor_terceiro, id_produto),
    CONSTRAINT terceiro_x_produto_fornecedor FOREIGN KEY (id_fornecedor_terceiro) REFERENCES fornecedor_terceiro (id_fornecedor_terceiro),
    CONSTRAINT terceiro_x_produto_produto FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
);
