"""Application that integrates Python to SQLite. This is used to insert and extract data from the Relational DB.
"""

#import sqlalchemy as sqla
#import sqlalchemy.orm as sqlaorm

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import (
    Session,
    declarative_base,
    relationship
)

# Criando conexão com o banco de dados, pysqlite é a DBAPI utilizada por padrão e pode ser omitida.
# echo: Criar log de script SQL, future: utilizar padrão de código sqlalchemy 2.0
conexao = create_engine("sqlite+pysqlite:///./Integracao_SQLite_MongoDB/sqlite.db", echo=False, future=True)

# Estruturando o banco de dados com ORM

# É a criação de um schema para o banco de dados, declarative_base() é uma shorthard de registry().generate_base()
Base = declarative_base()

# Cliente é uma classe para mapear a tabela para o ORM, o nome da tabela é definido por __tablename__
class Cliente(Base):
    __tablename__ = "cliente"

    # Nome das colunas é definido pelo nome dos atributos
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    cpf = Column(Integer, unique=True)
    endereco = Column(String(150))

    # Definindo o relacionamento Um-pra-Muitos entre tabelas,
    # nome Classe e nome variável de relacionamento
    contas = relationship("Conta", back_populates="cliente")


class Conta(Base):
    __tablename__ = "conta"

    id = Column(Integer, primary_key=True)
    tipo = Column(String(30))
    agencia = Column(String(15))
    num = Column(Integer, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="contas")


# Métodos de manipulação do database

def insert_data(*args):
    """Método para a inserção de uma lista de dados passados por parâmetro no database.
    Os dados são automaticamente inseridos na tabela definida pela instância.
    :param args: Recebe os dados que serão inseridos no database
    """
    with Session(conexao) as sessao:
        try:
            sessao.add_all(args)
            sessao.commit()
        except Exception as exc:
            print("Ocorreu um erro ao inserir os dados: \n", exc)


def update_data():
    pass

def delete_data():
    with Session(conexao) as sessao:
        try:
            sessao.execute()

        except Exception as exc:
            print("Ocorreu um erro ao deletar os dados: \n", exc)



# Persistindo o schema no database
Base.metadata.create_all(conexao)

# Inserindo dados
# A tabela a ser inserida é definida pela Instância utilizada
"""insert_data(
    Cliente(nome="Gabryel", cpf=456, endereco="R -- Q -- L -- Valparaíso de Goiás"),
    Cliente(nome="Kaio", cpf=123, endereco="R -- Q -- L -- São Paulo"),
    Conta(tipo="conta_corrente", agencia="1111-01", id_cliente=1)
    )"""




# Utilizando o SQLAlchemy Core para criar o schema
# Apenas para fins didáticos.
"""schema = MetaData()
tabela_cliente = Table(
    "cliente",
    schema,
    Column("id", Integer, primary_key=True),
    Column("nome", String(100)),
    Column("cpf", Integer, unique=True),
    Column("endereco", String(150))
)

tabela_conta = Table(
    "conta",
    schema,
    Column("id", Integer, primary_key=True),
    Column("tipo", String(30)),
    Column("agencia", String(15)),
    Column("num", Integer),
    Column("id_cliente", ForeignKey("cliente.id"), nullable=False)

schema.create_all(conexao)
)"""
