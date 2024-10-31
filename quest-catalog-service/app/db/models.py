from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from typing import List

Base = declarative_base()

class Quest(Base):
    __tablename__ = "quests"
    quest_id = Column(Integer, primary_key=True, index=True)
    reward_id = Column(Integer, ForeignKey("rewards.reward_id"), nullable=False)
    auto_claim = Column(Boolean, default=False)
    streak = Column(Integer, default=1)
    duplication = Column(Integer, default=1)
    name = Column(String, index=True)
    description = Column(String, index=True)
    rewards = relationship("Reward", foreign_keys=[reward_id], lazy="joined")

class Reward(Base):
    __tablename__ = "rewards"
    reward_id = Column(Integer, primary_key=True, index=True)
    reward_name = Column(String)  
    reward_item = Column(String)  # "gold" or "diamond"
    reward_qty = Column(Integer)  # Quantity of the reward