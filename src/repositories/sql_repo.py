from database.db import async_session
from sqlalchemy import insert


class SQLAlchemyRepository:
    model = None

    async def create_if_does_not_exist(self, **kwargs):
        async with async_session() as session:
            stmt = insert(self.model).values(**kwargs).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()
