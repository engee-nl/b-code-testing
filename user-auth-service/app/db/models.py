from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserStatus(PyEnum):
    NEW = "new"
    NOT_NEW = "not_new"
    BANNED = "banned"

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    gold = Column(Integer, default=0)
    diamond = Column(Integer, default=0)
    status = Column(Enum(UserStatus), default=UserStatus.NEW)