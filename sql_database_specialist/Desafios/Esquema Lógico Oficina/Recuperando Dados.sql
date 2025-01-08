-- Recuperando dados com SELECT

USE oficina;

SHOW TABLES;
DESC mecanico_gera_ordem;
SELECT * FROM mecanico_gera_ordem; 

-- Clientes e seus veículos
SELECT id_cliente, concat(nome, ' ', sobrenome) 'Nome Completo', endereco, telefone, id_veiculo, tipo_veiculo, modelo_veiculo, marca_veiculo
	FROM cliente INNER JOIN veiculo USING (id_cliente);

-- Mecânicos responsáveis pela análise dos veículos
SELECT m.id_mecanico, concat(m.nome, ' ', m.sobrenome) 'Nome Completo', m.especialidade, mv.tipo_servico, v.id_veiculo, v.tipo_veiculo, v.modelo_veiculo, v.marca_veiculo
	FROM mecanico m
    INNER JOIN mecanico_analisa_veiculo mv ON m.id_mecanico=mv.id_mecanico
    INNER JOIN veiculo v ON mv.id_veiculo=v.id_veiculo;

-- Mecânicos responsáveis por gerar uma ordem de serviço
SELECT os.id_ordem_servico, os.data_emissao, os.data_prevista_conclusao, os.status_servico, os.descricao, concat(m.nome, ' ', m.sobrenome) 'Nome Mecânico'
	FROM ordem_servico os
    INNER JOIN mecanico_gera_ordem mg ON os.id_ordem_servico=mg.id_ordem_servico
    INNER JOIN mecanico m ON mg.id_mecanico=m.id_mecanico;
    
-- Mecânicos responsáveis pela execução dos serviços
SELECT os.id_ordem_servico, os.data_emissao, os.data_prevista_conclusao, os.status_servico, os.descricao, concat(m.nome, ' ', m.sobrenome) 'Nome do Mecânico'
	FROM ordem_servico os
    INNER JOIN mecanico_executa_ordem mx ON os.id_ordem_servico=mx.id_ordem_servico
    INNER JOIN mecanico m ON mx.id_mecanico=m.id_mecanico;

-- Mecânicos x Serviços realizados
SELECT concat(m.nome, ' ', m.sobrenome) 'Nome do Mecânico', count(*) 'Serviços realizados'
	FROM ordem_servico os
    INNER JOIN mecanico_executa_ordem mx ON os.id_ordem_servico=mx.id_ordem_servico
    INNER JOIN mecanico m ON mx.id_mecanico=m.id_mecanico
    GROUP BY m.nome, m.sobrenome
    ORDER BY nome, sobrenome;

-- Valor médio para manutenção e reparo de veículos
SELECT  tipo_peca 'Tipo de serviço', ROUND(AVG(valor),2) 'Média de preços'
	FROM peca
    GROUP BY tipo_peca;
