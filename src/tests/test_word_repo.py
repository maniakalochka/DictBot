import pytest
from repositories.word_repo import WordRepository
from models.word import Word

from sqlalchemy.sql import select


@pytest.mark.asyncio
async def test_create_word_if_does_not_exist(async_session):
    repo = WordRepository()
    word_data = {
        "word": "test_word",
        "level": "A1",
        "pos": "noun",
        "definition_url": "https://www.google.com",
        "voice_url": "https://www.google.com",
        "tg_id": 1234567,
        "count": 0,
    }

    word_id = await repo.create_if_does_not_exist(**word_data)
    assert word_id is not None
    result = await async_session.execute(select(Word).where(Word.id == word_id))
    word = result.scalar_one()
    assert word.tg_id == 1234567
    assert word.word == "test_word"
    assert word.level == "A1"
    assert word.voice_url == "https://www.google.com"
