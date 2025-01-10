from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from datetime import datetime
from typing import TYPE_CHECKING

from .word import Word

from .user_words_mnm import user_words


class User(Base):
    __tablename__ = "users"

    tg_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_date: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    is_active: Mapped[bool] = mapped_column(default=True)

    # Связь с словами через промежуточную таблицу
    words: Mapped[list["Word"]] = relationship(
        "Word", secondary=user_words, back_populates="users"
    )

    def __str__(self) -> str:
        return f"Username {self.username}, TG_ID {self.tg_id}, DB_ID {self.id}"
