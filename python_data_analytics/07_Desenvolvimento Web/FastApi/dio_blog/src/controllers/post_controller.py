from fastapi import APIRouter, Depends, status

from src.schemas.post_schema import PostIn, PostUpdate
from src.services.post_service import PostService
from src.services.security_service import login_required
from src.views.post_view import PostOut

router = APIRouter(prefix='/posts', dependencies=[Depends(login_required)])
post_service = PostService()


# Data types do path parameter são definidos com annotations do Python.
@router.get(
    '/{id}',
    status_code=status.HTTP_200_OK,
)
async def get_post(id: int) -> PostOut | dict:
    post = await post_service.read_post(id)

    return post if post else {}


# Query Parameters
# Se diferenciam dos Path parameters, não recebem argumentos no caminho da rota
# endpoint?skip=10&limit=10
# Booleans aceitam os valores true, True, 1, yes, on e seus inversos
# Veja commit anterior para padrão com cookies e Annotated
# Annotated são objetos para notação de tipo com possibilidade de métodos
@router.get(
    '/',
    status_code=status.HTTP_200_OK,
)
async def get_posts(
    skip: int = 0,
    limit: int = 10,
    published: bool = 1,
) -> list[PostOut] | dict:
    posts = await post_service.read_posts(skip, limit, published)

    return posts if posts else {}


# Tipo de status code para retorno
@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
)
async def create_post(post: PostIn) -> PostOut | dict:
    last_id = await post_service.insert_post(post)

    if not last_id:
        return {}  # TODO: status.HTTP_500_INTERNAL_SERVER_ERROR

    return {**post.model_dump(), 'id': last_id}


@router.patch(
    '/{id}',
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_post(id: int, partial_post: PostUpdate) -> None:
    await post_service.change_post(id, partial_post)

    return


@router.delete(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
)
async def delete_post(id: int):
    await post_service.remove_post(id)

    return
