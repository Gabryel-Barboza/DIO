# SQLite2Mongo
Description. Package created only for learning purposes, automatically creates a predefined SQLite database and add functions to interact with it. Also add functions to connect to a MongoDB database, extract from SQLite and insert on MongoDB.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable) to install sqlite2mongo.
```bash
pip install sqlite2mongo
```
## Usage
```python
from sqlite2mongo import sqlite_app, mongo_app

sqlite_app.insert_data(
    Cliente(nome="Marcelo Nonato", cpf=0, endereco=""),
    Conta(tipo="conta_corrente", num=1, agencia="", saldo=0, id_cliente=1)
    )

documents = mongo_app.create_documents()

connection = mongo_app.connect(url)
db = connection.bank
collection = db.collection
mongo_app.add_to_collection(documents, collection)
```
## Author
Gabryel_Brz
## License
[MIT](https://choosealicense.com/licenses/mit/)
