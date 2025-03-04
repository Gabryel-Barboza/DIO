from datetime import UTC, datetime

from pydantic import BaseModel


# Modelo de objeto para ser recebido de uma rota com método POST
class PostIn(BaseModel):
    title: str
    date_published: datetime = datetime.now(UTC)
    published: bool = False


class Foo(BaseModel):
    bar: str
