import asyncio

# Módulo de compatibilidade com paradigma assíncrono do Pytest
import pytest_asyncio

# Biblioteca para criar um cliente de requisições assíncrono
# FastAPI possui um cliente síncrono
from httpx import ASGITransport, AsyncClient

from src.config import settings

settings.database_url = 'sqlite:///testes.db'


# Fixtures para criar namespaces de funções para serem utilizadas em outros módulos
@pytest_asyncio.fixture
async def db(request):
    from src.databases.database import database, engine, metadata
    from src.models.post_model import posts  # noqa

    await database.connect()
    metadata.create_all(engine)

    # Método de término do programa
    def teardown():
        async def _teardown():
            await database.disconnect()
            metadata.drop_all(engine)

        # Executa funções assíncronas em códigos síncronos
        asyncio.run(_teardown())

    # Adiciona métodos para quando o software é finalizado, trabalha com código síncrono
    request.addfinalizer(teardown)


@pytest_asyncio.fixture
async def client(db):
    from src.main import app

    # Criando client de requisições assíncrono

    # Camada de transporte assíncrona da aplicação
    transport = ASGITransport(app=app)
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    # Bloco de contexto assíncrono
    async with AsyncClient(
        base_url='http://test', transport=transport, headers=headers
    ) as client:
        yield client


@pytest_asyncio.fixture
async def access_token(client: AsyncClient):
    response = await client.post('/auth/login', json={'user_id': '1'})
    return response.json()['access_token']
