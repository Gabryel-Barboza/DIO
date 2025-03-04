from datetime import UTC, datetime

from fastapi import APIRouter, Cookie, Header, Response, status
from typing_extensions import Annotated

from src.schemas.post_schema import Foo, PostIn
from src.views.post_view import PostOut

router = APIRouter(prefix='/posts')

fake_db = [
    {
        'title': 'Criando APIs com Flask',
        'date_published': datetime.now(UTC),
        'published': True,
    },
    {
        'title': 'Aplicações Fullstack com Django',
        'date_published': datetime.now(UTC),
        'published': True,
    },
    {
        'title': 'Criando APIs com FastAPI',
        'date_published': datetime.now(UTC),
        'published': True,
    },
    {
        'title': 'Interação com Bancos de dados com SQLAlchemy',
        'date_published': datetime.now(UTC),
        'published': True,
    },
]


# Data types do path parameter são definidos com annotations do Python.
@router.get('/{id}')
def get_posts(id: int):
    return fake_db[id]


# Query Parameters
# Se diferenciam dos Path parameters, não recebem argumentos no caminho da rota
# endpoint?skip=10&limit=10
# Booleans aceitam os valores true, True, 1, yes, on e seus inversos
# Annotated são objetos para notação de tipo com possibilidade de métodos
@router.get('/')
def read_posts(
    response: Response,
    skip: int = 0,
    limit: int = 10,
    published: bool = 1,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None,
    response_model=list[PostOut],
):
    print(f'Cookie: {ads_id}')
    print(f'User-agent: {user_agent}')

    response.set_cookie(key='user', value='gabryel@email.com')

    return [
        post for post in fake_db[skip : skip + limit] if post['published'] is published
    ]


# Tipo de status code para retorno
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    return post


# Modelos de resposta com tipo de retorno ou parâmetro de retorno, response_model tem prioridade
@router.get('/', response_model=Foo)
def foobar() -> Foo:
    return {'bar': 'foo', 'message': 'hello, world'}
