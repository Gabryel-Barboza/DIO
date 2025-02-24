from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from . import db


class Post(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    body: Mapped[str] = mapped_column(String, nullable=False)
    # Utiliza o tipo de dados datetime e recebe uma coluna com a hora atual. Func são as funções utilitárias do SQLAlchemy.
    created: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    def __repr__(self):
        return f'Post(id={self.id!r},title={self.title!r},created={self.created},author_id={self.author_id!r})'
