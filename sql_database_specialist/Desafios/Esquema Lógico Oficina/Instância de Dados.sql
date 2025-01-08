-- Instanciando dados no esquema de Oficina

-- Instancias geradas por IA para melhor popular o banco de dados

INSERT INTO cliente (id_cliente, nome, sobrenome, endereco, telefone) VALUES
    (1, 'Lucas', 'Almeida', 'Rua A, 123, São Paulo, SP', '11912345678'),
    (2, 'Ana', 'Santos', 'Rua B, 456, Curitiba, PR', '21998765432'),
    (3, 'Bruno', 'Pereira', 'Rua C, 789, Belo Horizonte, MG', '31987654321'),
    (4, 'Mariana', 'Costa', 'Rua D, 101, Rio de Janeiro, RJ', '41956781234'),
    (5, 'Carlos', 'Silva', 'Rua E, 112, Porto Alegre, RS', '51934567890');

INSERT INTO veiculo (id_veiculo, id_cliente, tipo_veiculo, modelo_veiculo, marca_veiculo) VALUES
    (1, 1, 'Carro', 'Civic', 'Honda'),
    (2, 1, 'Moto', 'CB650R', 'Honda'),
    (3, 2, 'Carro', 'Corolla', 'Toyota'),
    (4, 2, 'Carro', 'Hilux', 'Toyota'),
    (5, 3, 'Caminhão', 'Actros', 'Mercedes-Benz'),
    (6, 4, 'Carro', 'Polo', 'Volkswagen'),
    (7, 5, 'Carro', 'Onix', 'Chevrolet'),
    (8, 5, 'Moto', 'Ninja 400', 'Kawasaki');

INSERT INTO ordem_servico (id_ordem_servico, id_cliente, data_emissao, data_prevista_conclusao, status_servico, descricao, valor_total) VALUES
    (1, 1, '2025-01-05', '2025-01-10', 'Em andamento', 'Troca de óleo e filtro', 150.00),
    (2, 2, '2025-01-02', '2025-01-08', 'Peça faltando', 'Revisão geral', 500.00),
    (3, 3, '2025-01-03', '2025-01-09', 'Em espera', 'Substituição de freios', 250.00),
    (4, 4, '2025-01-04', '2025-01-12', 'Concluído', 'Troca de embreagem', 1200.00),
    (5, 5, '2025-01-01', '2025-01-15', 'Em andamento', 'Reparo na suspensão', 800.00);

INSERT INTO mecanico (id_mecanico, nome, sobrenome, endereco, especialidade) VALUES
    (1, 'Pedro', 'Silva', 'Rua Z, 987, São Paulo, SP', 'Motores'),
    (2, 'João', 'Oliveira', 'Rua X, 654, Curitiba, PR', 'Freios'),
    (3, 'Lucas', 'Costa', 'Rua Y, 321, Belo Horizonte, MG', 'Suspensão'),
    (4, 'Marcos', 'Santos', 'Rua W, 432, Rio de Janeiro, RJ', 'Elétrica'),
    (5, 'Ricardo', 'Lima', 'Rua V, 543, Porto Alegre, RS', 'Revisão');

INSERT INTO servico (id_servico, nome_servico, tipo_servico, valor) VALUES
    (1, 'Troca de óleo', 'Manutenção', 200.00),
    (2, 'Revisão geral', 'Manutenção', 500.00),
    (3, 'Troca de freio', 'Reparo', 300.00),
    (4, 'Troca de embreagem', 'Reparo', 800.00),
    (5, 'Troca de pneus', 'Reparo', 600.00),
    (6, 'Reparo na suspensão', 'Reparo', 700.00),
    (7, 'Alinhamento', 'Manutenção', 150.00),
    (8, 'Troca de bateria', 'Manutenção', 400.00),
    (9, 'Substituição de filtros', 'Manutenção', 120.00),
    (10, 'Revisão elétrica', 'Manutenção', 350.00);

INSERT INTO peca (id_peca, nome_peca, tipo_peca, valor) VALUES
    (1, 'Óleo lubrificante', 'Manutenção', 50.00),
    (2, 'Pastilhas de freio', 'Reparo', 150.00),
    (3, 'Embreagem', 'Reparo', 400.00),
    (4, 'Filtro de óleo', 'Manutenção', 30.00),
    (5, 'Pneu', 'Reparo', 500.00),
    (6, 'Suspensão traseira', 'Reparo', 700.00),
    (7, 'Bateria automotiva', 'Manutenção', 400.00),
    (8, 'Filtro de ar', 'Manutenção', 80.00),
    (9, 'Filtro de combustível', 'Manutenção', 90.00),
    (10, 'Velas de ignição', 'Manutenção', 120.00);

INSERT INTO mecanico_analisa_veiculo (id_mecanico, id_veiculo, tipo_servico) VALUES
    (1, 1, 'Revisão'),
    (2, 3, 'Reparo'),
    (3, 5, 'Revisão'),
    (4, 6, 'Reparo'),
    (5, 8, 'Revisão');

INSERT INTO mecanico_gera_ordem (id_mecanico, id_ordem_servico) VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),  
    (5, 5);

INSERT INTO mecanico_executa_ordem (id_mecanico, id_ordem_servico) VALUES
    (1, 1),  
    (1, 3),  
    (2, 2),  
    (2, 4),  
    (3, 5),  
    (3, 1),  
    (4, 4),  
    (4, 5),  
    (5, 2),  
    (5, 3);

INSERT INTO servico_em_ordem (id_servico, id_ordem_servico) VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5);

INSERT INTO peca_em_ordem (id_peca, id_ordem_servico, quantidade) VALUES
    (1, 1, 2),
    (2, 3, 4),
    (3, 4, 1),
    (6, 5, 2);
