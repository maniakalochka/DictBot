from database.db import async_session
from sqlalchemy import insert, select


class SQLAlchemyRepository:
    model = None

    async def check_exist(self, **kwargs):
        async with async_session() as session:
            stmt = select(self.model).filter_by(**kwargs)
            result = await session.execute(stmt)
            existing_record = result.scalars().first()
            return existing_record

    async def create_if_does_not_exist(self, **kwargs):
        existing_record = await self.check_exist(**kwargs)
        if existing_record:
            return existing_record.id

        async with async_session() as session:
            stmt = insert(self.model).values(**kwargs).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()
