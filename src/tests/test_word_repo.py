import pytest
from sqlalchemy.ext.asyncio.session import AsyncSession
from repositories.word_repo import WordRepository
from models.word import Word

from sqlalchemy.sql import select


@pytest.mark.asyncio
async def test_create_word_if_does_not_exist(async_session: AsyncSession) -> None:
    repo = WordRepository()
    word_data = {
        "word": "test_word",
        "level": "A1",
        "pos": "noun",
        "definition_url": "https://www.google.com",
        "voice_url": "https://www.google.com",
        "tg_id": 1234567,
        "count": 0,
        "is_skipped": False,
    }

    word_id = await repo.create_if_does_not_exist(**word_data)
    assert word_id is not None
    result = await async_session.execute(select(Word).where(Word.id == word_id))
    word = result.scalar_one()
    assert word.tg_id == 1234567
    assert word.word == "test_word"
    assert word.level == "A1"
    assert word.voice_url == "https://www.google.com"


@pytest.mark.asyncio
async def test_can_skip_word(async_session: AsyncSession) -> None:
    repo = WordRepository()
    word_data = {
        "word": "test_word",
        "level": "A1",
        "pos": "noun",
        "definition_url": "https://www.google.com",
        "voice_url": "https://www.google.com",
        "tg_id": 1234567,
        "count": 0,
        "is_skipped": False,
    }

    word_id = await repo.create_if_does_not_exist(**word_data)
    await repo.skip_word(word_id)
    result = await async_session.execute(select(Word).where(Word.id == word_id))
    word = result.scalar_one()
    assert word.is_skipped is True
