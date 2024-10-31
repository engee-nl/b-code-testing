from pydantic import BaseModel

class UserQuestUpdate(BaseModel):
    user_id: int
    quest_id: int
    progress: int

class UserQuestResponse(BaseModel):
    user_id: int
    quest_id: int
    progress: int
    status: str