from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Instancia uma engine SQLAlchemy com o modelo
db = SQLAlchemy(model_class=Base)
