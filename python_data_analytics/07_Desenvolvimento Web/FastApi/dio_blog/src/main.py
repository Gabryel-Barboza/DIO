from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .controllers import auth_controller, post_controller
from .databases.database import database, engine, metadata


# FastAPI usa o paradigma assíncrono
@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.models import post_model  # noqa

    await database.connect()  # Executado na inicialização
    metadata.create_all(engine)
    yield
    await database.disconnect()  # Executado antes de encerrar


# Criando metadados manualmente
tags_metadata = [
    {'name': 'auth', 'description': 'Operações para autenticação e validação.'},
    {
        'name': 'post',
        'description': 'Operações para manipular posts.',
        'externalDocs': {
            'description': 'Documentação externa',
            'url': 'http://www.documentação.com',
        },
    },
]

servers = [
    {'url': 'http://localhost:8000', 'description': 'Ambiente de desenvolvimento'},
    {'url': 'https://dio-blog.onrender.com', 'description': 'Ambiente de produção'},
]


# Possui similaridades com o Flask
app = FastAPI(
    title='DIO Blog API',
    summary='API para recuperar posts de blog.',
    version='1.0.0',
    description="""
# Como a API funciona? 

## Endpoints
    """,
    openapi_tags=tags_metadata,
    servers=servers,
    # openapi_url=None,  # Desabilita as rotas padrão /docs e /redoc da documentação automática
    lifespan=lifespan,
)

# Importando rotas e definindo tags para documentação
app.include_router(post_controller.router, tags=['post'])
app.include_router(auth_controller.router, tags=['auth'])

# Adicionando CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_headers=['*'],
    allow_methods=['*'],
)


# Tratando exceções generalizadas
@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exec: Exception):
    return JSONResponse(status_code=exec.status_code or 500, content=exec.message)


# Execute o servidor com uvicorn caminho:instância_app --reload (recarrega servidor se alteração)
# uvicorn src.main:app --reload
