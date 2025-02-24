from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import db


class Role(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    user: Mapped[list['user.User']] = relationship(back_populates='role')

    def _repr__(self):
        return f'Role(id={self.id},name={self.name})'
