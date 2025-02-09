-- Eventos em SQL

USE company;

SHOW TABLES;
SHOW TABLES FROM information_schema;

SELECT * 
FROM information_schema.routines 
  WHERE routine_schema NOT LIKE 'sys';

-- Verificar eventos criados
SELECT *
FROM information_schema.events;

-- Verificando variável de evento
SHOW VARIABLES WHERE variable_name LIKE '%event%';

-- Por padrão o agendador de eventos está desligado
SET GLOBAL event_scheduler = ON; -- event_scheduler = 1;

DESC project;


-- Criando eventos

-- Eventos de execução única

delimiter |
CREATE EVENT criar_tabelas
  -- Executar na data atual, daqui uma hora
  ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 MINUTE
  -- É deletado após conclusão por padrão, para deixar explicito: ON COMPLETION NOT PRESERVE
  DO BEGIN
    CREATE TABLE teste_event(
      id INT PRIMARY KEY,
      nome VARCHAR(30)
    );

    CREATE TABLE teste_event2(
      id INT PRIMARY KEY,
      nome VARCHAR(30),
      id_teste INT ,
      FOREIGN KEY (id_teste) REFERENCES teste_event(id)
    );
  END|
delimiter ;

SHOW TABLES;

DROP TABLE IF EXISTS teste_event, teste_event2;

-- Eventos rotineiros
-- Ter precaução quanto a esse tipo de evento, se um intervalo de execução tiver intersecção com outro
-- novas instâncias serão criadas.

DROP EVENT IF EXISTS criar_relatorio;

delimiter |
CREATE EVENT criar_relatorio
  -- Agendando evento para executar a cada dia, começando a partir deste timestamp e neste horário
  -- repetir até este timestamp
  ON SCHEDULE EVERY 1 DAY STARTS '2024-01-01 00:00:00' ENDS '2024-04-01'
  -- Não deletar o evento após conclusão
  ON COMPLETION PRESERVE
  DO BEGIN -- Faça isso
  -- Recriando view
  -- View para facilitar o acesso de dados específicos
    CREATE OR REPLACE VIEW employee_project_view AS 
      (SELECT concat(e.Fname, ' ', e.Lname) 'Full Name', e.Ssn, e.Salary, w.Pno, w.Hours, p.Pname, p.Dnumber, p.Plocation   
      FROM employee e INNER JOIN works_on w ON e.Ssn=w.Essn
      INNER JOIN project p ON w.Pno=p.Pnumber);

END|
delimiter ;

-- Verificar avisos de execução, os eventos são silenciosos quanto aos erros
-- Utilizar error handlers para prevenir problemas
SHOW WARNINGS;

-- Eventos com intervalos de data inválidos são desabilitados apenas, incluem datas de início que já passaram

-- Verificar eventos em execução
SHOW PROCESSLIST;

DROP EVENT IF EXISTS call_f;

-- Eventos que chamam rotinas
CREATE EVENT call_p
  ON SCHEDULE EVERY 1 DAY
  DO CALL p();

-- Alterando eventos
ALTER EVENT call_p
  ON SCHEDULE EVERY 2 DAY
  DO CALL f();

-- Habilitar eventos
ALTER EVENT criar_relatorio
  ENABLE;

ALTER EVENT call_p
  DISABLE;

-- Renomeando
ALTER EVENT call_p
  RENAME TO call_f;

SHOW DATABASES;

-- Movendo entre databases
ALTER EVENT company.call_f
  RENAME TO conjuntos.call_f;
