from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from base import Base

# Промежуточная таблица для связи многие-ко-многим
user_words = Table(
    "user_words",
    Base.metadata,
    ForeignKey("users.id", ondelete="CASCADE"),
    ForeignKey("words.id", ondelete="CASCADE"),
    PrimaryKeyConstraint("user_id", "word_id"),
)
