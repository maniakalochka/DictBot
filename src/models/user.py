from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from datetime import datetime
from sqlalchemy import BigInteger, ForeignKey
from .word import Word
from typing import List


class User(Base):
    __tablename__ = "users"

    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_date: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    is_active: Mapped[bool] = mapped_column(default=True)

    words: Mapped[List["Word"]] = relationship("Word", back_populates="user")

    def __str__(self) -> str:
        return f"Username {self.username}, TG_ID {self.tg_id}, DB_ID {self.id}"
