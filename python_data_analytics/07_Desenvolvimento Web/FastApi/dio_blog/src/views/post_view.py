from datetime import datetime

from pydantic import BaseModel


class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published_on: datetime | None
    published: bool = False
