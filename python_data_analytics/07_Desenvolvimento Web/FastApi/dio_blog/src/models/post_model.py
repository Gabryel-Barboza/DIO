from sqlalchemy import Boolean, Column, DateTime, Integer, String, Table

from src.databases.database import metadata

posts = Table(
    'posts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(150), nullable=False, unique=True),
    Column('content', String(250)),
    Column('published_on', DateTime, nullable=True),
    Column('published', Boolean, default=False),
)
