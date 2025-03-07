import os

import sqlalchemy as sa

import databases

DATABASE_URL = os.getenv('DATABASE_URL') or 'sqlite:///./blog.db'

# Usando SQLAlchemy Core e databases
metadata = sa.MetaData()
database = databases.Database(DATABASE_URL)

engine = sa.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})