# Instale o módulo sqlalchemy, utilize um ambiente virtual
# Caso preferir, import sqlalchemy as sqla e utilize sqla.nome_método
# TODO: Refatorar para SQLAlchemy 2.0

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    create_engine,
    inspect,
    select,
    func
)
from sqlalchemy.orm import (
    Session,
    declarative_base,
    relationship
)

# Cria uma classe de estrutura para o banco de dados

Base = declarative_base()

# Herdando todos os atributos de Base


class Usuario(Base):
    # Nome dado a tabela, usado como referência no código
    __tablename__ = "user_account"
    # atributos
    # Características das colunas, similar a criação de colunas do SQL
    # Primary keys possuem autoincrement por default
    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    fullname = Column(String(40))

    # Definindo um relacionamento entre tabelas, referencia o campo user de Endereco, adiciona constraint CASCADE com delete-orphans
    address = relationship(
        "Endereco", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Usuario(id={self.id}, name={self.name}, fullname={self.fullname})"


class Endereco(Base):
    __tablename__ = "user_address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(100), nullable=False, unique=True)
    # Criando uma foreign key, utiliza __tablename__ para identificar tabela
    usuario_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    # Relacionamento com Usuario, referencia ao campo address
    user = relationship("Usuario", back_populates="address")

    def __repr__(self):
        return f"Endereco(id={self.id}, email={self.email_address})"


# conectando ao banco de dados. Dialeto + DBAPI (omitida) + host - :memory: - database in memory
engine = create_engine("sqlite://")

# criando as classes como tabelas do bancos de dados.
Base.metadata.create_all(engine)

# Inspecionando o schema do banco de dados
inspetor = inspect(engine)

print(inspetor.has_table("user_account"))
print(inspetor.get_table_names())

print(inspetor.default_schema_name)

# Bloco with para tratar erros e realizar o rollback caso falhe
with Session(engine) as session:
    # Instanciando objetos Usuario
    usuario1 = Usuario(
        name="gabryel",
        fullname="Gabryel Barboza",
        address=[
            Endereco(email_address="gabryel@email.com"),
            Endereco(email_address="gabryelbrz@email.com"),
        ],
    )
    usuario2 = Usuario(
        name="brayan",
        fullname="Brayan Dinastia",
        address=[Endereco(email_address="brayan@email.com")],
    )
    usuario3 = Usuario(
        name="kaio",
        fullname="Kaio Gomes",
        address=[Endereco(email_address="kaio@email.com")],
    )

    # Enviando objetos para o banco de dados
    session.add_all([usuario1, usuario2, usuario3])
    session.commit()

# Realiza uma query SELECT em usuarios. Retorna um objeto
query = select(Usuario).where(Usuario.name.in_(["gabryel", "brayan"]))
print("\nRecuperando usuarios com filtragem por nome")
# Iterando dentro do objeto para retornar as informações
for user in session.scalars(query):
    print(user)

print("\nRecuperando endereços com filtragem por id de usuario")
query_address = select(Endereco).where(Endereco.usuario_id.in_([1]))
for address in session.scalars(query_address):
    print(address)

print("\nOrdenação de usuarios por nome decrescente")
query_order = select(Usuario).order_by(Usuario.fullname.desc())
for user in session.scalars(query_order):
    print(user)


print("\nJOINs de tabelas")
# Natural JOIN, scalars mapea apenas o primeiro resultado
query_join = select(Usuario.fullname, Endereco.email_address).join_from(Endereco, Usuario)
for join in session.scalars(query_join):
    print(join)
print(query_join)


print("\nRetornando resultados por conexão e execução de querys")
connection = engine.connect()
resultado = connection.execute(query_join)
for usuario in resultado:
    print(usuario)


print("\nRetornando a contagem de usuários")
query_count = select(func.count("*")).select_from(Usuario)
print(query_count)
for contagem in session.scalars(query_count):
    print(contagem)

session.close()
