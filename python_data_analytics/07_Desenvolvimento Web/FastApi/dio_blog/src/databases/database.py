import sqlalchemy as sa

import databases
from src.config import settings

# Em versões mais recentes, o FastAPI possui a biblioteca SQLModel recomendada para interação com DB
# Veja a documentação sobre SQL

# Usando SQLAlchemy Core e databases
metadata = sa.MetaData()
database = databases.Database(settings.database_url)

if settings.environment == 'production':
    engine = sa.create_engine(settings.database_url)
else:
    engine = sa.create_engine(
        settings.database_url, connect_args={'check_same_thread': False}
    )
