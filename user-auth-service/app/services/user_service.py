from sqlalchemy.orm import Session
from app.db.models import User
from app.core.security import get_password_hash
from app.schemas.user import UserCreate

def get_user_by_username(db: Session, user_name: str):
    return db.query(User).filter(User.user_name == user_name).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(user_name=user.user_name, hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user