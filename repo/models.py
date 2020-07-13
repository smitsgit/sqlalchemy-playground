from repo.base import SqlAlchemyBase
from sqlalchemy import Column, Integer, String


class User(SqlAlchemyBase):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
