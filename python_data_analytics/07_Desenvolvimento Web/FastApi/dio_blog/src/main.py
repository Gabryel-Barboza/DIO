from contextlib import asynccontextmanager

from fastapi import FastAPI

from .controllers import auth_controller, post_controller
from .databases.database import database, engine, metadata

# Em versões mais recentes, o FastAPI possui a biblioteca SQLModel recomendada para interação com DB
# Veja a documentação sobre SQL


# FastAPI usa o paradigma assíncrono
@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.models import post_model  # noqa

    await database.connect()  # Executado na inicialização
    metadata.create_all(engine)
    yield
    await database.disconnect()  # Executado antes de encerrar


# Possui similaridades com o Flask
app = FastAPI(lifespan=lifespan)
app.include_router(post_controller.router)
app.include_router(auth_controller.router)


# Execute o servidor com uvicorn caminho:instância_app --reload (recarrega servidor se alteração)
# uvicorn src.main:app --reload
