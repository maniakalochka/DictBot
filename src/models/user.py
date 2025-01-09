from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_date: Mapped[datetime] = mapped_column(default=datetime.now())
    is_active: Mapped[bool] = mapped_column(default=True)

    def __str__(self):
        return f"Username {self.username}, TG_ID {self.tg_id}, DB_ID {self.id}"
