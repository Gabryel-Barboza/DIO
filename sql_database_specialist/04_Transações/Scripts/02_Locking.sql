-- Mecanismos de lock/bloqueio

USE test_transactions;

SELECT * FROM orders o ;

-- Bloqueio à granularidade de tabela de nível leitura
-- Impede escritas de outras sessões na tabela inteira, a sessão atual só permite leitura
LOCK TABLE orders READ;

UPDATE orders SET product_name='xbox' WHERE id_order = 1;

UNLOCK TABLES;

-- Bloqueia a tabela para leitura e escrita em outras sessões, permite que a sessão atual modifique a tabela
LOCK TABLE orders WRITE;

SHOW TABLES;

-- LOCK TABLES tabela1 READ, tabela2 WRITE

-- Recomendado que o sistema de locks seja gerenciado pelo SGBD, se aproveitando do sistema de timeout em transações
