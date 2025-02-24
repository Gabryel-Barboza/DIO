from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

import src.models.user_model

from . import db


class Role(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    user: Mapped[list['src.models.user_model.User']] = relationship(
        back_populates='role'
    )

    def _repr__(self):
        return f'Role(id={self.id},name={self.name})'
