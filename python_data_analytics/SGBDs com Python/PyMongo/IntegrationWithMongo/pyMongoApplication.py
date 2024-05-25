from pprint import pprint
import pymongo as pym
from datetime import datetime

# Insira o URL para instanciar uma conexão
client = pym.MongoClient("#")

#  Criando o Banco de dados test
# Verifica no cluster se uma conexão existe, caso contrário cria um
db = client.test

# Criando uma collection test_collection
collection = db.test_collection
print("="*40)
print(db.list_collection_names())
print(collection)
print("="*40)

# Criando documento para inserção no db, necessário o uso de dicionários para a passagem de Json
documento = {
    "author": "Gabryel",
    "text": "Minha primeira aplicação com MongoDB e Python",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.now()
}

# Coleção posts
posts = db.posts
# Inserção de documetos
# Recuperando _id após inserção de documento
post_id = posts.insert_one(documento).inserted_id

print(post_id)
print(posts)
print("="*40)
# Recuperando valor dentro de posts
print(posts.find_one())
# Módulo com print formatado para dicionários
pprint(posts.find_one())
print("="*40)

# Bulk Inserts
new_document = [{
    "author": "Gabryel",
    "text": "Outro documento",
    "tags": ["pymongo", "bulk_insert"],
    "date": datetime.now()
},
{
    "author": "João",
    "text": "Outro documento de estrutura diferente",
    "title": "Mongo is fun",
    "date": datetime.now()
}]

# Inserindo a lista de documentos e retornando seus ids
result = posts.insert_many(new_document).inserted_ids
pprint(result)

# Iterando posts.find para printar todos os documentos dentro da coleção
for documento in posts.find():
    print("-"*20)
    pprint(documento)
print("="*40)


