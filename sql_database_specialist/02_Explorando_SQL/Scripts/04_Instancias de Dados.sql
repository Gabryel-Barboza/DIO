USE first_example;
DESC person;

-- Inserindo dados na tabela
-- Antes da palavra chave VALUES pode ser especificada as colunas com () para inserção, caso contrário será necessário um valor para todos os atributos
-- Valores númericos não precisam ser colocados entre ''. 
-- O padrão de data utilizado é aaaa/mm/dd
INSERT INTO person VALUES (
	'4', 'Gabryel', 'Barboza', 'M', '2000-10-10', 'Rua X', 'Cidade Y', 'Estado Z', 'Brasil', '20000-200'
),
	(
	'3', 'Gabryel', 'Barboza', 'M', '2000-10-10', 'Rua X', 'Cidade Y', 'Estado Z', 'Brasil', '20000-200'
);
-- Ao ocorrerem erros na operação, toda a transação é cancelada. Nesse exemplo, a primeira instância está válida
-- no entanto, a segunda já existe uma dentro da tabela de mesma chave, acarretando em erros.

-- Inserindo dados com Integridade referencial
-- A chave estrangeira não permite a inserção de instâncias, caso o valor inserido não exista no atributo referenciado
DESC favorite_food;
INSERT INTO favorite_food VALUES (
	'2', 'Lasanha'
);

-- Removendo instâncias da tabela, cláusula where necessária para identificar instâncias
DELETE FROM person WHERE person_id=2;

SELECT * FROM person;