from integracao_sqlite import (
    Cliente,
    Conta,
    Session,
    conexao,
    insert_data,
    pprint,
    select,
    update,
)

# Inserindo dados

insert_data(
    Cliente(nome="Gabryel Barboza", cpf=11111111111, endereco="R -- Q -- L -- Goiás"),
    Cliente(nome="Gabryel Barboza", cpf=22222222222, endereco="R -- Q -- L -- Brasília"),
    Cliente(nome="Kaio Gomes", cpf=33333333333, endereco="R -- Q -- L -- São Paulo"),
    Cliente(nome="Rafael Silva", cpf=44444444444, endereco="R -- Q -- L -- Rio de Janeiro"),
    Cliente(nome="Marcelo Nonato", cpf=55555555555, endereco="R -- Q -- L -- Amazonas"),
    Conta(tipo="conta_corrente", num=1, agencia="1111-01", saldo=350.50, id_cliente=1),
    Conta(tipo="conta_poupanca", num=2, agencia="1111-01", saldo=470.00, id_cliente=1),
    Conta(tipo="conta_corrente", num=3, agencia="1111-01", saldo=350.43, id_cliente=2),
    Conta(tipo="conta_corrente", num=4, agencia="1111-01", saldo=7000.00, id_cliente=3),
    Conta(tipo="conta_corrente", num=5, agencia="1111-01", saldo=870.50, id_cliente=4),
    Conta(tipo="conta_poupanca", num=6, agencia="1111-01", saldo=2000.75, id_cliente=4),
    Conta(tipo="conta_corrente", num=7, agencia="1111-01", saldo=1400.50, id_cliente=5),
    Conta(tipo="conta_poupanca", num=8, agencia="1111-01", saldo=250.10, id_cliente=5),
)

# Atualizando os dados
with Session(conexao) as sessao:
    try:
        sessao.execute(
            update(Cliente).where(Cliente.id == 2).values(nome="Brayan Barbosa")
        )
        sessao.commit()
    except Exception as exc:
        print("Ocorreu um erro ao atualizar os dados. \n ", exc)

# Deletando os dados
"""delete_data(Cliente, 3)
insert_data(Cliente(nome="Kaio", cpf=123, endereco="R -- Q -- L -- São Paulo"))
"""

# Retornando dados da tabela
with Session(conexao) as sessao:

    # Todos os clientes
    pprint(sessao.execute(select(Cliente)).fetchall())

    print()

    # Campos específicos
    pprint(sessao.execute(select(Cliente.nome, Cliente.cpf)).fetchall())

    print()

    # Todas contas dos clientes
    pprint(sessao.execute(select(Conta)).fetchall())

    print()

    # Clientes com nome específico
    rows = sessao.execute(select(Cliente).where(Cliente.nome == "Gabryel Barboza"))
    pprint(rows.fetchall())

    print()

    # Clientes e Contas
    rows = sessao.execute(select(Cliente, Conta).join(Cliente.contas))
    pprint(rows.fetchall())
