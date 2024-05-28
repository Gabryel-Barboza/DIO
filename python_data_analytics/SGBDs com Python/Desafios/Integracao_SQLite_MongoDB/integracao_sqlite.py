"""Application that integrates Python to SQLite. This is used to insert and extract data from the Relational DB.
"""

# import sqlalchemy as sqla
# import sqlalchemy.orm as sqlaorm

from pprint import pprint

from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    select,
    text,
    update,
)
from sqlalchemy.orm import Session, declarative_base, relationship

# Criando conexão com o banco de dados, pysqlite é a DBAPI utilizada por padrão e pode ser omitida.
# echo: Criar log de script SQL, future: utilizar padrão de código sqlalchemy 2.0
conexao = create_engine(
    "sqlite+pysqlite:///./Integracao_SQLite_MongoDB/sqlite.db", echo=False, future=True
)

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
    Column("num", Integer, unique=True),
    Column("id_cliente", ForeignKey("cliente.id"), nullable=False)

schema.create_all(conexao)
)"""

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

    def __repr__(self):
        return f"Cliente(id:{self.id}, nome:{self.nome}, cpf:{self.cpf}, endereco:{self.endereco})"


class Conta(Base):
    __tablename__ = "conta"

    id = Column(Integer, primary_key=True)
    tipo = Column(String(30))
    agencia = Column(String(15))
    num = Column(Integer, unique=True)
    saldo = Column(Float, default=0)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="contas")

    def __repr__(self):
        return f"Conta(id:{self.id}, tipo:{self.tipo}, agencia:{self.agencia}, num:{self.num}, saldo:{self.saldo}, id_cliente:{self.id_cliente})"


# Métodos de manipulação do database


# Inserindo linhas
def insert_data(*args):
    """Método para a inserção de uma lista de dados passados por parâmetro no database.
    Os dados são automaticamente inseridos na tabela definida pela instância da classe.
    :param args: Recebe uma lista de instâncias que serão inseridas no database.
    """
    with Session(conexao) as sessao:
        try:
            sessao.add_all(args)
            print("\nInserção realizada com sucesso. \n ")
            sessao.commit()
        except Exception as exc:
            print("Ocorreu um erro ao inserir os dados: \n", exc)


# Deletando linhas
def delete_data(table, id):
    """Método para deletar uma linha especificada pelos parâmetros.
    :param table: Tabela para filtrar a linha requisitada.
    :param id: Valor do campo id da linha a ser excluída.
    """
    with Session(conexao) as sessao:
        try:
            # Retorna a linha da tabela selecionada com a primary key
            row = sessao.get(table, id)
            sessao.delete(row)
            print("\nLinha deletada com sucesso. \n ", row)
            sessao.commit()
        except Exception as exc:
            print("Ocorreu um erro ao deletar os dados: \n", exc)


# Retornando linhas
def return_data(table):
    with Session(conexao) as sessao:
        rows = sessao.execute(select(table)).fetchall()
        return rows


# Persistindo o schema no database, se o schema já existe é ignorado
Base.metadata.create_all(conexao)
