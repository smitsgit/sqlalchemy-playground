from repo.base import SqlAlchemyBase
from sqlalchemy import Column, Integer, String


class User(SqlAlchemyBase):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    cool_name = Column(String)
    nickname = Column(String)
    age = Column(Integer, default=10, nullable=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.full_name}', '{self.nick_name}')"
