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
