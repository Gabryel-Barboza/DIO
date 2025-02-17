"""Application to integrate Python with MongoDB. Is utilized with the SQLite integration app to extract data from
the relational database and insert into a MongoDB Collection.
"""

import pymongo as pym
from sqlite_app import Cliente, Conta, return_data


def create_clientes():
    """Método para extrair da tabela Cliente e formatar os dados para um dicionário.
    
    :return: Retorna uma lista com todos os dicionários de Cliente.
    """
    # Recebendo dados
    # Os campos são retornados conforme o método __repr__ de cada classe
    lista_clientes = []
    lista_dicionarios = []
    clientes = return_data(Cliente)

    # Formatando as linhas de Cliente recebidas, removendo caracteres e dividindo cada cliente em substrings
    # Uma lista de listas
    for row in clientes:
        cliente = str(row).replace("(", "").replace(")", "").removeprefix("Cliente").split(",")
        lista_clientes.append(cliente)
        
    # Criando um dicionário para cada cliente
    for cliente in lista_clientes:
        resultado = {}

        # Para cada lista dentro de cliente, pega a posição do campo desejado e retira a parte de "campo:"
        resultado["id"] = cliente[0].split(":")[1]
        resultado["nome"] = cliente[1].split(":")[1]
        resultado["cpf"] = cliente[2].split(":")[1]
        resultado["endereco"] = cliente[3].split(":")[1]
        resultado["contas"] = []
        lista_dicionarios.append(resultado)
        # Dicionário criado e anexado a lista

    return lista_dicionarios


def create_contas():
    """Método para extrair da tabela Conta e formatar os dados para um dicionário.

    :return: Retorna uma lista com todos os dicionários de Conta.
    """
    # O processo é o mesmo de create_clientes()
    lista_contas = []
    lista_dicionarios = []
    contas = return_data(Conta)

    for row in contas:
        conta = str(row).replace("(", "").replace(")", "").removeprefix("Conta").split(",")
        lista_contas.append(conta)
    
    for conta in lista_contas:
        resultado = {}

        resultado["id_cliente"] = conta[5].split(":")[1]
        resultado["tipo_conta"] = conta[1].split(":")[1]
        resultado["agencia"] = conta[2].split(":")[1]
        resultado["numero_conta"] = conta[3].split(":")[1]
        resultado["saldo"] = conta[4].split(":")[1]
        lista_dicionarios.append(resultado)
    
    return lista_dicionarios


def append_conta(clientes, contas, documents):
    """Método para anexar as contas em seus respectivos clientes.

    :param clientes: Recebe uma lista de clientes de create_clientes().
    :param contas: Recebe uma lista de contas de create_contas().
    :param documents: Uma lista utilizada para guardar os novos dicionários.
    :return: Retorna uma lista com os dicionários após o anexo de contas.
    """
    for cliente in clientes:
        # Para cada cliente em clientes, cria uma cópia em document e anexa todas as contas equivalentes.
        for conta in contas:
            if cliente["id"] == conta["id_cliente"]:
                cliente["contas"].append(conta)

        documents.append(cliente)


def create_documents():
    """Método para a extração de objetos das tabelas e conversão para dicionários.

    :return: Uma lista de dicionários com os documentos formatados para inserir na coleção.
    """
    # Cria uma lista de documentos para receber os dicionários após sua formatação correta.
    documents = []
    clientes = create_clientes()
    contas = create_contas()
    append_conta(clientes, contas, documents)
    return documents


def add_to_collection(documents, col):
    """Método para adicionar documentos de uma lista de dicionários a coleção clientes do MongoDB.

    :documents: Recebe uma lista de dicionários
    :col: Recebe uma collection do MongoDB para ser adicionado
    :return: Retorna _ids dos documentos inseridos no MongoDB.
    """
    result = col.insert_many(documents).inserted_ids
    return result


# Inserir URL para conexão com MongoDB Cloud
def connect(url):
    """Retorna um objeto MongoClient com a conexão na url recebida.

    :param url: Recebe a url para conexão ao MongoDB, local ou Cloud
    :return: Retorna um objeto de conexão com o banco de dados
    """
    return pym.MongoClient(url)

