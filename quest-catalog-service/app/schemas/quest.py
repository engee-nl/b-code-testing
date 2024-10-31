from pydantic import BaseModel
from app.schemas.reward import RewardResponse
from typing import List

class QuestResponse(BaseModel):
    quest_id: int
    reward_id: int
    auto_claim: bool
    streak: int
    duplication: int
    name: str
    description: str | None
    rewards: RewardResponse