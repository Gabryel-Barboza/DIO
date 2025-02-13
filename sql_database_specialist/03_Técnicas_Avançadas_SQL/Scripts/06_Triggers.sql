-- Gatilhos -> ações para serem executadas durante eventos ocorridos no db

USE company;

SELECT * FROM employee;

-- gatilhos são acionados em alterações de estado do banco de dados (INSERT, DELETE, UPDATE)

-- BEFORE INSERTs -> antes da inserção realiza uma ação
delimiter |
-- Trigger para cada linha inserida
CREATE TRIGGER super_ssn_check BEFORE INSERT ON employee
FOR EACH ROW
  BEGIN
  -- Se número do departamento tal, atributo Mgr_ssn recebe tal valor
    CASE NEW.Dno
    -- NEW similar a this de POO, referencia um novo atributo de instância
      WHEN 1 THEN SET NEW.Super_ssn = '333445555';  
      WHEN 2 THEN SET NEW.Super_ssn = NULL;
      WHEN 3 THEN SET NEW.Super_ssn = NULL;
      WHEN 4 THEN SET NEW.Super_ssn = '123456789';
      WHEN 5 THEN SET NEW.Super_ssn = '987654321';
    END CASE;
  END|
delimiter ;

SHOW TRIGGERS FROM company;

SELECT * FROM employee;

-- Automaticamente o atributo Super_ssn é alterado
INSERT INTO employee VALUES ('Gabryel', 'B', 'Silva', '222345679', '2000-01-01', '450-Stone-Houston-TX', 'M', 30000.00, '123456789', 5);

DROP TRIGGER super_ssn_check;


-- AFTER INSERTs -> depois da inserção uma ação é realizada

DROP TRIGGER null_value_check;
-- Verifica se valor de Address nulo após a inserção
delimiter |
CREATE TRIGGER null_value_check AFTER INSERT ON employee
FOR EACH ROW
  IF (NEW.Address IS NULL) THEN 
    -- SELECT 'Update your address!' AS message; Triggers não retornam valores
    INSERT INTO user_messages (message, Ssn) VALUES ('Update the user address!', NEW.Ssn);
  END IF;
|
delimiter ;


-- Criando uma tabela para guardar logs
CREATE TABLE user_messages(
  id INT AUTO_INCREMENT PRIMARY KEY,
  message VARCHAR(100) NOT NULL,
  Ssn CHAR(9),
  CONSTRAINT fk_user_messages_employee FOREIGN KEY (Ssn) REFERENCES employee (Ssn)
);

INSERT INTO employee VALUES ('Kaio', 'G', 'Nonato', '223345679', '2000-01-01', null, 'M', 30000.00, '123456789', 5);

-- Mensagem inserida na tabela
SELECT * FROM user_messages;


-- BEFORE UPDATE

DROP TABLE account;
CREATE TABLE account (
  id INT PRIMARY KEY,
  acc_num INT NOT NULL,
  amount DECIMAL(10, 2)
);

delimiter |
CREATE TRIGGER check_amount BEFORE UPDATE ON account
FOR EACH ROW
  BEGIN
    IF (NEW.amount < 0) THEN
      SET NEW.amount = 0;
    ELSEIF (NEW.amount > 100) THEN
      SET NEW.amount = 10;
    END IF;
  END|
delimiter ;

INSERT INTO account VALUES (1, 1, 97.50), (2, 2, 50.98), (3, 3, 75.67);

UPDATE account SET amount=-50 WHERE id=1;
UPDATE account SET amount=97.50 WHERE id=1;
-- Alteração ocorre apenas quando o atributo de condição está presente
UPDATE account SET acc_num=1 WHERE id=1;

SELECT * FROM account;
