import pytest_asyncio
from fastapi import status
from httpx import AsyncClient


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


async def test_update_post_success(client: AsyncClient, access_token: str):
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {'title': 'update post 1'}
    post_id = 1

    response = await client.patch(f'/posts/{post_id}', headers=headers, json=data)

    assert response.status_code == status.HTTP_202_ACCEPTED


async def test_update_post_not_authenticated_fail(client: AsyncClient):
    data = {'title': 'update post 1'}
    post_id = 1

    response = await client.patch(f'/posts/{post_id}', headers={}, json=data)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
