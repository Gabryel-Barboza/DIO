from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    text
)

# Conexão com banco de dados, //user:password@host/dbname
# Cria o arquivo caso não exista, para outros bancos de dados veja a documentação
engine = create_engine("sqlite:///./IntegrationWithSQL/meu_banco.db")

# Criando o schema
metadata_obj = MetaData()

# Instanciando uma tabela
user = Table(
    "user", metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("user_name", String(40), nullable=False),
    Column("email_address", String(100), nullable=False),
    Column("nickname", String(50), nullable=False),
)

user_prefs = Table(
    "user_prefs", metadata_obj,
    Column("prefs_id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("user.user_id"), nullable=False),
    Column("pref_name", String(40), nullable=False),
    Column("pref_value", String(100)),
)

for table in metadata_obj.sorted_tables:
    print(table)

metadata_obj.create_all(engine)

metadata_db_obj = MetaData()
financial_info = Table(
    "financial_info",
    metadata_db_obj,
    Column("id", Integer, primary_key=True),
    Column("value", String(100), nullable=False),
)

print()
print(financial_info.primary_key)
print(financial_info.constraints)
print()
print(metadata_db_obj.tables)
print()


# Utilizando SQL
print("Executando comandos SQL")
sql_insert = text("insert into user values(:i, :x, :y, :z)")

# Bloco with para auto-rollback caso ocorra um erro de inserção
# Veja Python DBAPI para entender melhor, pesquise também na documentação do SQLAlchemy sobre querys parametrizadas
# para garantir maior segurança na criação de statements
with engine.connect() as conexao:
    conexao.execute(sql_insert, {"i": 1, "x": "Gabryel", "y": "gabriel@email.com", "z": "Biel"})
    conexao.commit()

sql = text("select * from user")
resultado = engine.connect().execute(sql)
for dado in resultado:
    print(dado)

