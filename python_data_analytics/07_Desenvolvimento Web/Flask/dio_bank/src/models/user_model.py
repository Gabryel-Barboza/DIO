from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from . import Role
# Importe circular: user_model importa role_model no qual também importa user_model, um fica executando o outro.
# Opte por usar import package.a
import src.models.role_model

from . import db

# Implementando os modelos de tabelas, o Flask adiciona automaticamente algumas características como __tablename__ e relationship()


class User(db.Model):
    # Utilizando estruturas de dados com a classe Mapped, versão moderna do SQLAlchemy
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    role_id: Mapped[int] = mapped_column(ForeignKey('role.id'))
    role: Mapped['src.models.role_model.Role'] = relationship(back_populates='user')

    # O método de representação da classe para prints, !r para o formatador chamar o método __repr__ antes de exibir o atributo. Outras flags como !s para __str__ e !a para ascii
    def __repr__(self):
        return f'User(id={self.id}, username={self.username}, password={self.password}, active={self.active}, role_id={self.role_id})'
