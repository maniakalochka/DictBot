from models.user import User
from .sql_repo import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User
