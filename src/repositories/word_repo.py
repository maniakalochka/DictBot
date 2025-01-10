from .sql_repo import SQLAlchemyRepository
from models.word import Word


class WordRepository(SQLAlchemyRepository):
    model = Word
