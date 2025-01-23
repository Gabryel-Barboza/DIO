-- Rotinas e SQL Dinâmico
-- Rotinas são armazenadas na tabela routines em information_schema

SHOW DATABASES;

SHOW TABLES FROM information_schema;

SELECT * FROM information_schema.routines WHERE routine_schema='company' OR routine_schema='manipulation';

USE manipulation;

-- Criando uma função simples, deterministic para tipo de retorno exato. Not deterministic por padrão
-- Função simples, sem compound statements e apenas um retorno
CREATE FUNCTION first_function (num1 INT, num2 INT)
RETURNS INT DETERMINISTIC -- Tipo de valor que vai ser retornado
    RETURN num1 + num2; -- Valor retornado

-- Invocando a função
SELECT first_function(10, 10);

-- Criando uma procedure

USE company;

-- Procedures possuem compound statements, comandos compostos de outros comandos, portanto precisa de delimitadores
-- Delimitadores do bloco de procedure, evita confusão de ponto e vírgula dos statements na interpretação do mysql, trocando o delimitador. {//, |, $$}
delimiter //
CREATE PROCEDURE IF NOT EXISTS info_employee()
BEGIN -- Início
    -- Bloco para criar SQL dinâmico
    SELECT * FROM employee;
END// -- Fim do statement com //

delimiter ; -- Retornando ao padrão

-- Invocando procedure
CALL info_employee();

-- Deletando procedure
DROP PROCEDURE info_employee;

-- Se existir deletar a função
DROP FUNCTION IF EXISTS criar_media_salario;

-- Criando função mais complexa
delimiter |
CREATE FUNCTION IF NOT EXISTS criar_media_salario()
RETURNS DECIMAL DETERMINISTIC 
BEGIN
    -- Declarando variáveis locais com DECLARE variável tipo_dados
    DECLARE media DECIMAL(10,2) DEFAULT 0; 
    SELECT AVG(Salary) INTO media FROM employee; -- Inserir o resultado de SELECT na variável media
    RETURN media;
END|
delimiter ;

SELECT criar_media_salario() 'Média Salarial';

delimiter |
-- Declarações de variáveis não locais
CREATE FUNCTION IF NOT EXISTS data_hoje()
RETURNS DATE DETERMINISTIC
BEGIN
    SELECT NOW() INTO @dia; -- Variáveis referenciadas com @
    RETURN @dia;
END|
delimiter ;

SELECT data_hoje();

delimiter |
CREATE PROCEDURE IF NOT EXISTS calcular_salarios()
BEGIN
    -- Declarando e inicializando variáveis com SET
    SET @var = 1; -- Pode definir mínimo na cláusula having
    SET @salario_medio = (SELECT AVG(Salary) FROM employee);
    SELECT Dno 'Departamento', count(*) 'Quantidade acima da média de salário' FROM employee 
        WHERE Salary >= @salario_medio
        GROUP BY Dno ;
END|
delimiter ;

CALL calcular_salarios();

-- É possível verificar a variável se na mesma sessão
SELECT ROUND(@salario_medio, 2);
SELECT @dia;

delimiter |
-- Parâmetros de rotinas
-- IN por padrão, variável apenas de entrada. OUT para variável que será exportado o valor. INOUT para ambos
CREATE PROCEDURE calcular_quadrado(num1 INT, OUT resultado INT)
BEGIN
    SELECT num1 * num1 INTO resultado;
END|

delimiter ;

-- O resultado é atribuido para a variável
CALL calcular_quadrado(5, @resultado);
SELECT @resultado;

-- PREPARE CALL 
-- permite executar comandos e inserir querys parametrizadas
PREPARE num FROM 'CALL calcular_quadrado(?,@resultado)';

-- Utilizando uma variável para executar a query
SET @base = 10;
EXECUTE num USING @base;

SELECT @resultado;


-- Estruturas de controle

-- Bloco CASE
delimiter |
CREATE PROCEDURE p()
BEGIN 
    DECLARE v INT DEFAULT 1;
    
    -- statement CASE independente
    CASE v
        WHEN 2 THEN SELECT v; -- Se valor 2 retorna v
        WHEN 3 THEN SELECT 0; -- Se 3 retorna 0
        ELSE
            BEGIN -- novo bloco de código se falso
                SELECT 'NENHUM ENCONTRADO';
            END;
    END CASE;
END|
delimiter ;

-- Bloco IF
delimiter |
CREATE PROCEDURE f()
BEGIN
    DECLARE f INT DEFAULT 1;
    DECLARE v CHAR;
    -- bloco IF independente
    IF f <= 5 
        THEN SET v = 'a'; -- atribuir valor à variável v
    ELSEIF f <= 10
        THEN SET v = 'b';
    ELSE
        SET v = 'c';
    END IF;
    SELECT v;
END|
delimiter ;


-- Estruturas de repetição

delimiter |
-- Parâmetro de procedure
CREATE PROCEDURE iterar(lim INT)
BEGIN
-- Loop de execução indefinida, finalizado com bloco IF
    label: LOOP -- Inicia um loop de nome label
        SET @P1 = @P1 + 1; -- incremento de variáveis
        
        IF @P1<10 THEN -- Enquanto P1 menor que 10
            ITERATE label; -- continue a próxima iteração
        END IF;
        
        LEAVE label; -- Sair do loop label
    END LOOP label; -- Fim bloco loop 
    
    SET @P1 = 0;
    -- Loop de execução controlada com verificação no final. Label opcional
    -- finalizada quando satisfeita a condição
    REPEAT
        SET @P1 = @P1 + 1;
    UNTIL @P1 >= lim END REPEAT;
	
	SET @P1 = 0;
	-- Loop de execução controlada com verificação no inicio. Label opcional
	WHILE @P1 < lim DO
		SET @P1 = @P1 + 1;
	END WHILE;
END |

delimiter ;
	
SELECT @P1;

DROP PROCEDURE iterar;