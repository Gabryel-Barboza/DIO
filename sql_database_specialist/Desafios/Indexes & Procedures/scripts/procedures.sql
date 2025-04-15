-- Procedures

SHOW DATABASES;

-- Manipulação de dados para ecommerce
USE ecommerce;

DROP PROCEDURE IF EXISTS create_operation;

-- Criando um procedimento para receber um tipo de operação e executá-la com os parâmetros apropriados
DELIMITER ||
CREATE PROCEDURE create_operation(
	operation INT, table_name VARCHAR(50), table_columns VARCHAR(255), params VARCHAR(255)
)
BEGIN
	CASE operation
		-- Recuperando dados
		WHEN 0 THEN
		BEGIN
			-- Criando uma query SQL com os valores recebido
			SET @sql_text = CONCAT('SELECT ', table_columns, ' FROM ', table_name, ' ', params);
			-- Preparando para execução
			PREPARE select_table FROM @sql_text;
			EXECUTE select_table;
			-- Desalocando objeto da sessão global
			DEALLOCATE PREPARE select_table;
		END;
		-- Inserindo dados
		WHEN 1 THEN
		BEGIN
			SET @sql_text = CONCAT('INSERT INTO ', table_name, ' VALUES ', params);
			PREPARE insert_values FROM @sql_text;
			EXECUTE insert_values;
			DEALLOCATE PREPARE insert_values;

			-- Retornando último dado inserido para o usuário
			SET @sql_text = CONCAT('SELECT * FROM ', table_name, ' WHERE id_', table_name, ' = ', LAST_INSERT_ID());
			PREPARE select_last FROM @sql_text;
			EXECUTE select_last;
			DEALLOCATE PREPARE select_last;
		END;
		-- Atualizando dados
		WHEN 2 THEN
		BEGIN
			SET @sql_text = CONCAT('UPDATE ', table_name, ' SET ', table_columns, ' ', params);
			PREPARE update_table FROM @sql_text;
			EXECUTE update_table;
			DEALLOCATE PREPARE update_table;
		END;
		-- Removendo dados
		WHEN 3 THEN 
		BEGIN
			SET @sql_text = CONCAT('DELETE FROM ', table_name, ' ', params);
			PREPARE select_table FROM @sql_text;
			EXECUTE select_table;
			DEALLOCATE PREPARE select_table;
		END;
		-- Se escolha inválida
		ELSE
			SELECT 'Invalid operation selected! Aborting operations...' AS 'Invalid Operation!';
	END CASE;
END||
DELIMITER ;

SELECT * FROM information_schema.ROUTINES r WHERE ROUTINE_SCHEMA = 'ecommerce';

-- Parametros: operação, tabela, colunas (somente SELECT e UPDATE), clausulas adicionais
-- Recuperando a tabela de clientes
CALL create_operation(0, 'cliente', '*', '');

-- Inserindo um novo cliente
CALL create_operation(1, 'cliente', '', 
	'(default, "Gabryel", "Barboza", "61999999999", "Rua 11", "Nobre", "", "Valparaíso", "GO")'
);

-- Atualizando um cliente
CALL create_operation(2, 'cliente', 'complemento="Apto 11"', 'WHERE id_cliente=12');

-- Deletando um cliente
CALL create_operation(3, 'cliente', '', 'WHERE id_cliente=12');
