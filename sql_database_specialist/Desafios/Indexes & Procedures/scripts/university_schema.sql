-- Criando o esquema para a modelagem de universidade

DROP DATABASE IF EXISTS university;
CREATE DATABASE university CHARSET utf8mb4 COLLATE utf8mb4_general_ci;

USE university;
SHOW TABLES;

CREATE TABLE pessoa(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(20) NOT NULL,
	sobrenome VARCHAR(50) NOT NULL,
	cpf CHAR(11) NOT NULL,
	data_nascimento DATE,
	endereco VARCHAR(100),
	CONSTRAINT unq_cpf_pessoa UNIQUE (cpf)
);

CREATE TABLE professor(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_pessoa INT,
	id_departamento INT,
	registro CHAR(10) NOT NULL,
	CONSTRAINT fk_professor_pessoa FOREIGN KEY (id_pessoa) REFERENCES pessoa (id)
);

CREATE TABLE aluno(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_pessoa INT,
	matricula CHAR(10) NOT NULL,
	CONSTRAINT fk_aluno_pessoa FOREIGN KEY (id_pessoa) REFERENCES pessoa (id)
);

CREATE TABLE departamento(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_professor INT,
	nome_departamento VARCHAR(50) NOT NULL,
	campus VARCHAR(50) NOT NULL,
	CONSTRAINT fk_departamento_professor FOREIGN KEY (id_professor) REFERENCES professor (id)
);

ALTER TABLE professor 
	ADD CONSTRAINT fk_professor_departamento FOREIGN KEY (id_departamento) REFERENCES departamento (id);

CREATE TABLE curso(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_departamento INT,
	nome_curso VARCHAR(50) NOT NULL,
	carga_horaria INT NOT NULL,
	CONSTRAINT fk_curso_departamento FOREIGN KEY (id_departamento) REFERENCES departamento (id)
);

CREATE TABLE disciplina(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_curso INT,
	id_professor INT,
	nome_disciplina VARCHAR(50) NOT NULL,
	CONSTRAINT fk_disciplina_curso FOREIGN KEY (id_curso) REFERENCES curso (id),
	CONSTRAINT fk_disciplina_professor FOREIGN KEY (id_professor) REFERENCES professor (id)
);

CREATE TABLE periodo(
	id INT PRIMARY KEY AUTO_INCREMENT,
	semestre VARCHAR(20) NOT NULL,
	data_semestre DATE NOT NULL
);

CREATE TABLE extensao(
	id INT PRIMARY KEY AUTO_INCREMENT,
	titulo VARCHAR(50) NOT NULL,
	carga_horaria INT NOT NULL
);

CREATE TABLE aluno_realiza_extensao(
	id_aluno INT,
	id_extensao INT,
	PRIMARY KEY (id_aluno, id_extensao),
	CONSTRAINT fk_aluno_realiza_extensao_aluno FOREIGN KEY (id_aluno) REFERENCES aluno (id)
	ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT fk_aluno_realiza_extensao_extensao FOREIGN KEY (id_extensao) REFERENCES extensao (id)
	ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE aluno_matriculado_curso(
	id_aluno INT,
	id_curso INT,
	PRIMARY KEY (id_aluno, id_curso),
	CONSTRAINT fk_aluno_matriculado_curso_aluno FOREIGN KEY (id_aluno) REFERENCES aluno (id) 
	ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT fk_aluno_matriculado_curso_curso FOREIGN KEY (id_curso) REFERENCES curso (id)
	ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE periodo_oferta_disciplina(
	id_disciplina INT,
	id_periodo INT,
	PRIMARY KEY (id_disciplina, id_periodo),
	CONSTRAINT fk_periodo_oferta_disciplina_disciplina FOREIGN KEY (id_disciplina) REFERENCES disciplina (id) 
	ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT fk_periodo_oferta_disciplina_periodo FOREIGN KEY (id_periodo) REFERENCES periodo (id)
	ON UPDATE CASCADE ON DELETE CASCADE
);

SHOW TABLES;
SHOW KEYS FROM professor;
SELECT * FROM information_schema.REFERENTIAL_CONSTRAINTS rc 
	WHERE CONSTRAINT_SCHEMA = 'university';

-- Inserção de dados


INSERT INTO pessoa (id, nome, sobrenome, cpf, data_nascimento, endereco) VALUES
(1, 'Lucas', 'Silva', '12345678901', '1990-04-15', 'Rua das Flores, 123'),
(2, 'Ana', 'Costa', '23456789012', '1985-11-23', 'Av. Central, 456'),
(3, 'Paulo', 'Oliveira', '34567890123', '1992-07-19', 'Rua do Sol, 789'),
(4, 'Mariana', 'Almeida', '45678901234', '2000-03-12', 'Rua das Palmeiras, 321'),
(5, 'João', 'Santos', '56789012345', '1998-09-30', 'Av. Brasil, 987');

INSERT INTO professor (id, id_pessoa, id_departamento, registro) VALUES
(1, 1, NULL, 'P123456789'),
(2, 2, NULL, 'P234567890');

INSERT INTO aluno (id, id_pessoa, matricula) VALUES
(1, 3, 'A123456789'),
(2, 4, 'A234567890'),
(3, 5, 'A345678901');

INSERT INTO departamento (id, id_professor, nome_departamento, campus) VALUES
(1, 1, 'Departamento de Computação', 'Campus Central'),
(2, 2, 'Departamento de Matemática', 'Campus Sul');

UPDATE professor SET id_departamento = 1 WHERE id = 1;
UPDATE professor SET id_departamento = 2 WHERE id = 2;

INSERT INTO curso (id, id_departamento, nome_curso, carga_horaria) VALUES
(1, 1, 'Ciência da Computação', 3200),
(2, 2, 'Matemática Aplicada', 3000);

INSERT INTO disciplina (id, id_curso, id_professor, nome_disciplina) VALUES
(1, 1, 1, 'Estrutura de Dados'),
(2, 2, 2, 'Cálculo I'),
(3, 1, 1, 'Banco de Dados');

INSERT INTO periodo (id, semestre, data_semestre) VALUES
(1, '2024.1', '2024-01-10'),
(2, '2024.2', '2024-07-15');

INSERT INTO extensao (id, titulo, carga_horaria) VALUES
(1, 'Oficina de Robótica', 20),
(2, 'Projeto de Educação Financeira', 30),
(3, 'Palestra de Segurança Digital', 10);

INSERT INTO aluno_realiza_extensao (id_aluno, id_extensao) VALUES
(1, 1),
(2, 1),
(2, 2),
(3, 3);

INSERT INTO aluno_matriculado_curso (id_aluno, id_curso) VALUES
(1, 1),
(2, 2),
(3, 1);

INSERT INTO periodo_oferta_disciplina (id_disciplina, id_periodo) VALUES
(1, 1),
(2, 1),
(3, 2);


SELECT * 
	FROM pessoa p INNER JOIN professor p2  ON p.id = p2.id_pessoa;
