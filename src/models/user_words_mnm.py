from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from .base import Base

# Промежуточная таблица для связи многие-ко-многим
user_words = Table(
    "user_words",
    Base.metadata,
    Column("user_id", ForeignKey("users.id", ondelete="CASCADE")),
    Column("word_id", ForeignKey("words.id", ondelete="CASCADE")),
    PrimaryKeyConstraint("user_id", "word_id"),
)
