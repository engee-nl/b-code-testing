from pydantic import BaseModel

class RewardResponse(BaseModel):
    reward_id: int
    reward_name: str
    reward_item: str
    reward_qty: int