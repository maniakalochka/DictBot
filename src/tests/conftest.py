import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from models.base import Base

DATABASE_URL = "sqlite+aiosqlite:///./test_database.db"


@pytest.fixture(scope="function")
async def async_engine():
    """Создаёт асинхронный движок базы данных."""
    engine = create_async_engine(DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()


@pytest.fixture(scope="function")
async def async_session(async_engine):
    """Создаёт асинхронные сессии для тестов."""
    async_session_factory = async_sessionmaker(
        bind=async_engine, expire_on_commit=False, class_=AsyncSession
    )
    async with async_session_factory() as session:
        yield session
        await session.rollback()
