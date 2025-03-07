from datetime import datetime

from pydantic import BaseModel


# Modelo de objeto para ser recebido de uma rota com método POST
class PostIn(BaseModel):
    title: str
    content: str
    published_on: datetime | None = None
    published: bool = False


class PostUpdateIn(BaseModel):
    title: str | None = None
    content: str | None = None
    published_on: datetime | None = None
    published: bool | None = None
