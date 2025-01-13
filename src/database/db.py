from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import NullPool

from core.config import settings
from models.base import Base

if settings.MODE == "TEST":
    DATABASE_URL = settings.TEST_DB_URL
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = settings.DB_URL
    DATABASE_PARAMS = {"poolclass": NullPool}


engine: AsyncEngine = create_async_engine(
    url=DATABASE_URL, echo=True, **DATABASE_PARAMS
)

# Session Factory
async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, autoflush=True, expire_on_commit=False
)
