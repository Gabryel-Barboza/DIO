from pprint import pprint
from time import sleep

import pymongo as pym

cliente = pym.MongoClient("#")

db = cliente.test
posts = db.posts

for documento in posts.find():
    pprint(documento)
print("=" * 40)


# Retornando contagem de documentos sem filtragem
print(posts.count_documents({}))
# Com filtragem
print(posts.count_documents({"author": "João"}))
print(posts.count_documents({"tags": "python"}))


pprint(posts.find_one({"tags": "pymongo"}))

# Retornos ordenados
for documento in posts.find({}).sort("date"):
    pprint(documento)


# Criando índice para a collection profiles
# Unique, logo não é possivel adicionar documentos com a chave "author" iguais
# Pode-se criar índices compostos com uma lista de tuplas
result = db.profiles.create_index([("author", pym.ASCENDING)], unique=True)

documentos = [
    {"author": "Gabryel", "name": "Indexes"},
    {"author": "Gabryel", "name": "Pymongo"},
]

# Tentando inserir documentos de mesmo índice
try:
    db.profiles.insert_many(documentos)
except Exception as exc:
    print()
    print("Não foi possivel adicionar o documento. Possivel chave duplicada: \n", exc)
    print()

# Retorna os índices da collection
print(sorted(list(db.profiles.index_information())))

print(db.list_collection_names())

# Deletando documentos e collections


def deletar_collection(collection):
    collection.drop()


def deletar_um(collection, key):
    collection.delete_one(key)


def deletar_muitos(collection, key):
    collection.delete_many(key)


# Deletar collection se existir
deletar_collection(db.teste)
teste = db.teste

documentos = [
    {"name": "Gabryel", "age": 19, "index": 1},
    {"name": "Cleber", "age": 21, "index": 1},
    {"name": "Kaio", "age": 18, "index": 1},
]

ids = teste.insert_many(documentos).inserted_ids
print()
print("Documentos Inseridos: ")
pprint(ids)
# Deletando documento
deletar_um(teste, {"name": "Kaio"})
# Verificando se foi deletado
print(teste.find_one({"name": "Kaio"}))
print(db.list_collection_names())

# Deletando muitos
deletar_muitos(teste, {"index": 1})

# Verificando se existe documentos
for documento in teste.find():
    print(documento)
print("-----")

# Deletando um database

db_teste = cliente.db
db_teste.collection.insert_one({"name": "G", "age": 19})

for documento in db_teste.collection.find({}):
    print(documento)

# Verifique no Atlas
sleep(10)
cliente.drop_database("db")

