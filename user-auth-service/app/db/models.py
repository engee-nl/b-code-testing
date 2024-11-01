from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum

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

'''
Event Source : Log events
class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    event_type = Column(String, index=True)  # e.g., "sign_up", "sign_in"
    data = Column(JSON)                      # Additional data if available
    date = Column(DateTime(timezone=True), server_default=now())
'''