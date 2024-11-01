from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import now
from enum import Enum as PyEnum

Base = declarative_base()

class QuestStatus(PyEnum):
    CLAIMED = "claimed"
    NOT_CLAIMED = "not_claimed"

class UserQuest(Base):
    __tablename__ = "user_quests"
    user_id = Column(Integer, primary_key=True, index=True)
    quest_id = Column(Integer, primary_key=True, index=True)
    progress_streak = Column(Integer, default=0)
    status = Column(Enum(QuestStatus), default=QuestStatus.NOT_CLAIMED)
    completion_count = Column(Integer, default=0)
    date = Column(DateTime(timezone=True), server_default=now())

class UserReward(Base):
    __tablename__ = "user_rewards"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    reward_id = Column(Integer, index=True)
    reward_name = Column(String)  
    reward_item = Column(String)  # "gold" or "diamond"
    reward_qty = Column(Integer)  # Quantity of the reward
    date = Column(DateTime(timezone=True), server_default=now())

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    event_type = Column(String, index=True)  # e.g., "quest_completed", "reward_claimed"
    data = Column(JSON)                      # Additional data, such as quest ID, reward details
    date = Column(DateTime(timezone=True), server_default=now())