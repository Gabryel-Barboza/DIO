from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, scoped_session, sessionmaker

# TODO: Atualizar para versão moderna SQLAlchemy

engine = create_engine('sqlite:///atividades.db')
session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def save(self):
        session.add(self)
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f'Pessoa: {self.nome}'


class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoas')

    def save(self):
        session.add(self)
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f'Atividade: {self.nome}'


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
