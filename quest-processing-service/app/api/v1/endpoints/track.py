from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.models import UserQuest
from app.db.session import SessionLocal
from app.schemas.progress import UserQuestUpdate, UserQuestResponse
from app.services.tracking_service import track_sign_in, track_sign_up, claim_reward
from app.core.auth import get_current_user

router = APIRouter()

def get_session_local():
    yield SessionLocal()

'''
@router.post("/progress", response_model=UserQuestResponse)
def track_progress(progress_data: UserQuestUpdate, db: Session = Depends(get_session_local), current_user: dict = Depends(get_current_user)):
    quest = update_user_quest_progress(db, progress_data.user_id, progress_data.quest_id)
    if not quest:
        raise HTTPException(status_code=404, detail="Quest progress not found")
    return quest
'''

@router.post("/signin")
def track_signin(db: Session = Depends(get_session_local), current_user: dict = Depends(get_current_user)):
    # Track sign-in and update quest progress
    user_id = current_user.get("user_id")
    quest_status = track_sign_in(db, user_id, quest_name="sign-in-three-times")
    if quest_status is None:
        raise HTTPException(status_code=404, detail="Quest not found or already completed")

    return {"message": "Sign-in tracked", "status": quest_status}

@router.post("/signup")
def track_signup(db: Session = Depends(get_session_local), current_user: dict = Depends(get_current_user)):
    # Track sign-in and update quest progress
    user_id = current_user.get("user_id")
    quest_status = track_sign_up(db, user_id, quest_name="sign-up")
    if quest_status is None:
        raise HTTPException(status_code=404, detail="Quest not found or already completed")

    return {"message": "Sign-up tracked", "status": quest_status}


@router.post("/claim_reward")
def claim_reward_endpoint(quest_name: str, db: Session = Depends(get_session_local), current_user: dict = Depends(get_current_user)):
    try:
        user_id = current_user.get("user_id")
        reward_data = claim_reward(db, user_id, quest_name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return reward_data