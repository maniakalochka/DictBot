from .sql_repo import SQLAlchemyRepository
from models.word import Word
from sqlalchemy import update, insert
from database.db import async_session


class WordRepository(SQLAlchemyRepository):
    model = Word

    async def skip_word(self, word: str) -> None:
        async with async_session() as session:
            stmt = (
                update(self.model)
                .where(self.model.word == word)
                .values(is_skipped=True)
            )
            await session.execute(stmt)
            await session.commit()
