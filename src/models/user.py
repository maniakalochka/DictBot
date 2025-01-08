from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    tg_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_date: Mapped[datetime] = mapped_column(default=datetime.now)
    last_activity: Mapped[datetime] = mapped_column(default=datetime.now)

    def __str__(self):
        return f"Username {self.username}, ID {self.tg_id}"
