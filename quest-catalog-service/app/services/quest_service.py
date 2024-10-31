from sqlalchemy.orm import Session
from app.db.models import Quest

def get_quest_by_id(db: Session, quest_id: int):
    return db.query(Quest).filter(Quest.quest_id == quest_id).first()