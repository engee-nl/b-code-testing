from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.db.models import User
from app.db.session import SessionLocal
from app.core.security import get_password_hash, create_access_token, verify_password
from app.services.user_service import create_user, get_user_by_username
import httpx
from app.core.config import settings
from httpx import RequestError

router = APIRouter()

def get_session_local():
    yield SessionLocal()

@router.post("/signup", response_model=UserResponse)
async def signup(user: UserCreate, db: Session = Depends(get_session_local)):
    db_user = get_user_by_username(db, user.user_name)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    user = create_user(db=db, user=user)
    access_token = create_access_token(data={"sub": user.user_name, "user_id": user.user_id})

    # Notify Quest Processing Service about sign-up event
    # TODO : Circuit Breaker Pattern
    try:
        async with httpx.AsyncClient() as client:
            await client.post(
                f"{settings.QUEST_PROC_SERVICE_URL}/signup",
                json={"user_id": user.user_id},
                headers={"Authorization": f"Bearer {access_token}"}
            )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    # TODO : log sign up event with log_event(); 

    return {"user_id": user.user_id, "user_name": user.user_name, "token": access_token}


@router.post("/signin", response_model=UserResponse)
async def signin(user: UserLogin, db: Session = Depends(get_session_local)):
    db_user = get_user_by_username(db, user.user_name)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid user name or password")
    
    access_token = create_access_token(data={"sub": db_user.user_name, "user_id": db_user.user_id})

    # Notify Quest Processing Service about sign-in event
    # TODO : Circuit Breaker Pattern
    try:
        async with httpx.AsyncClient() as client:
            await client.post(
                f"{settings.QUEST_PROC_SERVICE_URL}/signin",
                json={"user_id": db_user.user_id},
                headers={"Authorization": f"Bearer {access_token}"}
            )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # TODO : log sign in event with log_event(); 

    return {"user_id": db_user.user_id, "user_name": db_user.user_name, "token": access_token}

# def notifyQuestProcessingService(user_id: int):

'''
TODO : Event Source Implementation
def log_event(db: Session, user_id: int, event_type: str, data: dict):
    event = Event(user_id=user_id, event_type=event_type, data=data, date=datetime.utcnow())
    db.add(event)
    db.commit()
    return event
'''

    