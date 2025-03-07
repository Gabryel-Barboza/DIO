from fastapi import APIRouter, Depends, status

from src.databases.database import database
from src.models.post_model import posts
from src.schemas.post_schema import PostIn, PostUpdateIn
from src.services.security_service import login_required
from src.views.post_view import PostOut

router = APIRouter(prefix='/posts', dependencies=[Depends(login_required)])


# Data types do path parameter são definidos com annotations do Python.
@router.get('/{id}', response_model=PostOut | dict)
async def get_post(id: int):
    statement = posts.select().where(posts.c.id == id)

    user = await database.fetch_one(statement)

    return user if user else {}


# Query Parameters
# Se diferenciam dos Path parameters, não recebem argumentos no caminho da rota
# endpoint?skip=10&limit=10
# Booleans aceitam os valores true, True, 1, yes, on e seus inversos
# Veja commit anterior para padrão com cookies e Annotated
# Annotated são objetos para notação de tipo com possibilidade de métodos
@router.get('/')
async def get_posts(
    skip: int = 0,
    limit: int = 10,
    published: bool = 1,
):
    statement = (
        posts.select()
        .where(posts.c.id > skip)
        .where(posts.c.published == published)
        .limit(limit)
    )

    return await database.fetch_all(statement)


# Tipo de status code para retorno
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_post(post: PostIn):
    statement = posts.insert().values(
        title=post.title,
        content=post.content,
        published_on=post.published_on,
        published=post.published,
    )
    last_id = await database.execute(statement)

    return {**post.model_dump(), 'id': last_id}


@router.patch('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def change_post(id: int, partial_post: PostUpdateIn):
    if partial_post:
        partial_post = partial_post.model_dump(exclude_unset=True)
        statement = posts.update().where(posts.c.id == id).values(**partial_post)
        await database.execute(statement)

    return {}


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    statement = posts.delete().where(posts.c.id == id)
    await database.execute(statement)

    return {}


# TODO: Separar lógica para camada de serviços
