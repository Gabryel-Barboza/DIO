-- Criando o esquema de Oficina

DROP DATABASE IF EXISTS oficina;
CREATE DATABASE IF NOT EXISTS oficina DEFAULT CHARSET utf8mb4;

USE oficina;

-- tabela cliente
CREATE TABLE cliente(
	id_cliente INT PRIMARY KEY,
    nome VARCHAR(15) NOT NULL,
    sobrenome VARCHAR(30) NOT NULL,
    endereco VARCHAR(100),
    telefone CHAR(11) NOT NULL,
    CONSTRAINT unique_telefone UNIQUE (telefone)
);

-- tabela veículo
CREATE TABLE veiculo(
	id_veiculo INT PRIMARY KEY,
    id_cliente INT,
    tipo_veiculo VARCHAR(20) NOT NULL,
    modelo_veiculo VARCHAR(20) NOT NULL,
    marca_veiculo VARCHAR(20),
    CONSTRAINT fk_veiculo_cliente FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
);

-- tabela ordem de serviço
CREATE TABLE ordem_servico(
	id_ordem_servico INT PRIMARY KEY,
    id_cliente INT,
    data_emissao DATE NOT NULL,
    data_prevista_conclusao DATE,
    status_servico ENUM('Em espera', 'Peça faltando', 'Em andamento', 'Concluído') NOT NULL,
    descricao VARCHAR(100),
    CONSTRAINT fk_ordem_servico_cliente FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
);

-- tabela mecânico
CREATE TABLE mecanico(
	id_mecanico INT PRIMARY KEY,
    nome VARCHAR(15) NOT NULL,
    sobrenome VARCHAR(30) NOT NULL,
    endereco VARCHAR(100),
    especialidade VARCHAR(20),
    CONSTRAINT unique_mecanico UNIQUE (nome, sobrenome)
);

-- tabela serviço
CREATE TABLE servico(
	id_servico INT PRIMARY KEY,
    nome_servico VARCHAR(30) NOT NULL,
    tipo_servico VARCHAR(20) NOT NULL,
    valor FLOAT NOT NULL,
    CONSTRAINT unique_servico UNIQUE (nome_servico, tipo_servico)
);

-- tabela peça
CREATE TABLE peca(
	id_peca INT PRIMARY KEY,
    nome_peca VARCHAR(30) NOT NULL,
    tipo_peca VARCHAR(20) NOT NULL,
    valor FLOAT NOT NULL,
    CONSTRAINT unique_peca UNIQUE (nome_peca, tipo_peca)
);

-- Tabelas de Relacionamentos

CREATE TABLE mecanico_analisa_veiculo(
	id_mecanico INT,
    id_veiculo INT,
    tipo_servico ENUM('Revisão', 'Reparo'),
    PRIMARY KEY (id_mecanico, id_veiculo),
    CONSTRAINT fk_mecanico_a_veiculo_mecanico FOREIGN KEY (id_mecanico) REFERENCES mecanico (id_mecanico),
    CONSTRAINT fk_mecanico_a_veiculo_veiculo FOREIGN KEY (id_veiculo) REFERENCES veiculo (id_veiculo)
);

CREATE TABLE mecanico_gera_ordem(
	id_mecanico INT,
    id_ordem_servico INT,
    PRIMARY KEY (id_mecanico, id_ordem_servico),
    CONSTRAINT fk_mecanico_g_ordem_mecanico FOREIGN KEY (id_mecanico) REFERENCES mecanico (id_mecanico),
    CONSTRAINT fk_mecanico_g_ordem_ordem FOREIGN KEY (id_ordem_servico) REFERENCES ordem_servico (id_ordem_servico)
);

CREATE TABLE mecanico_executa_ordem(
	id_mecanico INT,
    id_ordem_servico INT,
    PRIMARY KEY (id_mecanico, id_ordem_servico),
    CONSTRAINT fk_mecanico_x_ordem_mecanico FOREIGN KEY (id_mecanico) REFERENCES mecanico (id_mecanico),
    CONSTRAINT fk_mecanico_x_ordem_ordem FOREIGN KEY (id_ordem_servico) REFERENCES ordem_servico (id_ordem_servico)
);

CREATE TABLE servico_em_ordem(
	id_servico INT,
    id_ordem_servico INT,
    PRIMARY KEY (id_servico, id_ordem_servico),
    CONSTRAINT fk_servico_e_ordem_servico FOREIGN KEY (id_servico) REFERENCES servico (id_servico),
    CONSTRAINT fk_servico_e_ordem_ordem FOREIGN KEY (id_ordem_servico) REFERENCES ordem_servico (id_ordem_servico)
);

CREATE TABLE peca_em_ordem(
	id_peca INT,
    id_ordem_servico INT,
    quantidade INT DEFAULT 1,
    PRIMARY KEY (id_peca, id_ordem_servico),
    CONSTRAINT fk_peca_e_ordem_peca FOREIGN KEY (id_peca) REFERENCES peca (id_peca),
    CONSTRAINT fk_peca_e_ordem_ordem FOREIGN KEY (id_ordem_servico) REFERENCES ordem_servico (id_ordem_servico)
);
