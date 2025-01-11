from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import User

from .user_words_mnm import user_words


class Word(Base):
    __tablename__ = "words"

    word: Mapped[str] = mapped_column(unique=True, nullable=False)
    level: Mapped[str] = mapped_column(nullable=False)
    pos: Mapped[str] = mapped_column(nullable=False)
    definition_url: Mapped[str] = mapped_column(nullable=True)
    voice_url: Mapped[str] = mapped_column(nullable=True)
    tg_id: Mapped[int] = mapped_column(nullable=False)
    created_date: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    count: Mapped[int] = mapped_column(default=0, nullable=False)
    is_skipped: Mapped[bool] = mapped_column(default=False, nullable=False)

    # Связь с пользователями через промежуточную таблицу
    users: Mapped[list["User"]] = relationship(
        "User", secondary=user_words, back_populates="words"
    )

    def __str__(self) -> str:
        return f"Word {self.word}:{self.id}"
