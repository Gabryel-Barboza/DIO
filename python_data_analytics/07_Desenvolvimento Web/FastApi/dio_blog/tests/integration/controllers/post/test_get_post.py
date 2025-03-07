import pytest_asyncio
from fastapi import status
from httpx import AsyncClient


# autouse: usar método antes de todos os outros testes
@pytest_asyncio.fixture(autouse=True)
async def populate_posts(db):
    from src.controllers import post_controller
    from src.schemas.post_schema import PostIn

    await post_controller.create_post(
        PostIn(title='post 1', content='some content', published=True)
    )
    await post_controller.create_post(
        PostIn(title='post 2', content='some content', published=True)
    )
    await post_controller.create_post(
        PostIn(title='post 3', content='some content', published=False)
    )


async def test_get_post_success(client: AsyncClient, access_token: str):
    headers = {'Authorization': f'Bearer {access_token}'}
    post_id = 1

    response = await client.get(f'/posts/{post_id}', headers=headers)

    content = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert content['id'] == post_id


async def test_get_post_not_authenticated_fail(client: AsyncClient):
    post_id = 1

    response = await client.get(f'/posts/{post_id}', headers={})

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
