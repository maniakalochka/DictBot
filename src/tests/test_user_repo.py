import pytest
from repositories.user_repo import UserRepository
from models.user import User

# from conftest import async_session
from sqlalchemy.sql import select


@pytest.mark.asyncio
async def test_create_user_if_does_not_exist(async_session):
    repo = UserRepository()
    user_data = {"tg_id": 123456, "username": "test_user", "is_active": True}

    user_id = await repo.create_if_does_not_exist(**user_data)
    assert user_id is not None
    result = await async_session.execute(select(User).where(User.id == user_id))
    user = result.scalar_one()
    assert user.tg_id == 123456
    assert user.username == "test_user"
    assert user.is_active == True
