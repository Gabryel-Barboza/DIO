from fastapi import FastAPI

# Possui similaridades com o Flask
app = FastAPI()

fake_db = [
    {'title': 'Criando APIs com Flask'},
    {'title': 'Aplicações Fullstack com Django'},
    {'title': 'Criando APIs com FastAPI'},
    {},
]


# Data types do path parameter são definidos com annotations do Python.
@app.get('/posts/{subject}')
def get_posts(subject: int):
    return {
        'posts': [
            {'title': 'Criando APIs com Flask'},
            {'title': 'Criando APIs com FastAPI'},
        ]
    }


# Query Parameters
@app.get('/posts')
def read_posts(skip: int = 0, limit: int = 0):
    return fake_db


# Execute o servidor com uvicorn caminho:instância_app --reload (recarrega servidor se alteração)
# uvicorn src.main:app --reload
