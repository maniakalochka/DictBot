from .sql_repo import SQLAlchemyRepository
from models.word import Word
from models.user import User
from sqlalchemy import update, insert, select, func
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

    async def repeat_word(self, word: str) -> None:
        async with async_session() as session:
            stmt = (
                update(self.model)
                .where(self.model.word == word)
                .values(is_repeatable=True)
            )
            await session.execute(stmt)
            await session.commit()

    async def add_word_for_user(self, user_tg_id: int, word_data: dict) -> None:
        async with async_session() as session:
            # Ищем пользователя по tg_id
            user_stmt = select(User).filter(User.tg_id == user_tg_id)
            user_result = await session.execute(user_stmt)
            user = user_result.scalars().first()

            if user:
                # Создаем новое слово с данными и tg_id пользователя
                word = Word(**word_data, tg_id=user_tg_id)
                session.add(word)  # Добавляем слово в сессию

                # Добавляем связь между пользователем и словом
                user.words.append(word)

                await session.commit()

    async def get_random_word(self, user_tg_id: int) -> Word:
        async with async_session() as session:
            stmt = (
                select(self.model)
                .filter(self.model.tg_id == user_tg_id, self.model.is_skipped == False)
                .order_by(func.random())
            )  # сортировка случайным образом

            result = await session.execute(stmt)
            word = result.scalars().first()
            return word
