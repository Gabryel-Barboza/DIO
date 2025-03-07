import pytest
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


@pytest.mark.parametrize('published,total', [('on', 2), ('off', 1)])
async def test_get_posts_by_status(
    client: AsyncClient, access_token: str, published: str, total: int
):
    params = {'published': published, 'limit': 10}
    headers = {'Authorization': f'Bearer {access_token}'}

    response = await client.get('/posts/', params=params, headers=headers)

    content = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(content) == total


async def test_get_posts_limit_success(client: AsyncClient, access_token: str):
    params = {'published': 'on', 'limit': 1}
    headers = {'Authorization': f'Bearer {access_token}'}

    response = await client.get('/posts/', params=params, headers=headers)

    content = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(content) == 1


async def test_get_posts_not_authenticated_fail(client: AsyncClient):
    params = {'published': 'on', 'limit': 1}

    response = await client.get('/posts/', params=params, headers={})

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
