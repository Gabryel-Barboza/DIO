import json

import uvicorn
from fastapi import FastAPI

# App teste de FastAPI
app =  FastAPI()

# Retorna um json com os dados de pessoas
@app.get('/index')
def persons():
    pessoas = {
        'number': [1, 2, 3, 4, 5],
        'name': ['Mahesh', 'Alex', 'David', 'John', 'Chris'],
        'age': [25, 26, 27, 28, 29],
        'city': ['Bangalore', 'London' 'San Francisco', 'Toronto', 'Paris'],
        'country': ['India', 'UK', 'USA', 'Canada', 'France']
    }
    return json.dumps(pessoas)


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
