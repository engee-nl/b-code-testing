from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.models import Quest
from app.db.session import SessionLocal
from app.schemas.quest import QuestResponse
from app.services.quest_service import get_quest_by_id
from app.core.auth import get_current_user

router = APIRouter()

def get_session_local():
    yield SessionLocal()

@router.get("/get/{quest_id}", response_model=QuestResponse)
def get_quest(quest_id: int, db: Session = Depends(get_session_local), current_user: dict = Depends(get_current_user)):
    '''
    quests = db.query(Quest).all()
    print( repr(quests) )
    for questData in quests:
        print(f"Quest ID: {questData.quest_id}, Quest Name: {questData.name}, Streak: {questData.streak}, Duplication: {questData.duplication}, AutoClaim: {questData.auto_claim}")
        print( repr(questData.rewards.reward_id) )
    raise HTTPException(status_code=404, detail="Quest not found")
    '''
    quest = get_quest_by_id(db, quest_id)
    if not quest:
        raise HTTPException(status_code=404, detail="Quest not found")
    
    return QuestResponse(
        quest_id=quest.quest_id,
        reward_id=quest.reward_id,
        auto_claim=quest.auto_claim,
        streak=quest.streak,
        duplication=quest.duplication,
        name=quest.name,
        description=quest.description,
        rewards={"reward_id": quest.rewards.reward_id, "reward_name": quest.rewards.reward_name, "reward_item": quest.rewards.reward_item, "reward_qty": quest.rewards.reward_qty}
    )