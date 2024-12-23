SHOW DATABASES;

-- Criando o primeiro exemplo de banco de dados, constraint if not exists para ignorar erro "database exists"
CREATE DATABASE IF NOT EXISTS first_example;

USE first_example;

SHOW TABLES;

-- Criando a tabela
CREATE TABLE person(
-- person_id smallint unsigned primary key -- pode ser definida ao final
	person_id SMALLINT UNSIGNED,
	fname VARCHAR(20),
	lname VARCHAR(20),
	gender ENUM('M', 'F'),
	birth_date DATE,
	street VARCHAR(30),
	city VARCHAR(20),
	state VARCHAR(20),
	country VARCHAR(20),
	postal_code VARCHAR(20),
    CONSTRAINT pk_person PRIMARY KEY (person_id) -- Definindo primary key e nomeando a restrição como pk_person
);	

-- Descrever o esquema da tabela
DESC person;

CREATE TABLE favorite_food(
	person_id SMALLINT UNSIGNED,
    food VARCHAR(20),
    -- Criando uma primary key composta
    CONSTRAINT pk_favorite_food PRIMARY KEY (person_id, food),
    -- Criando uma chave estrangeira com a tabela person
    CONSTRAINT fk_favorite_food_person_id FOREIGN KEY (person_id) references person(person_id)
);

-- Recuperando informações de schema do banco de dados
SHOW DATABASES;
SELECT * FROM information_schema.table_constraints
WHERE constraint_schema = 'first_example';