from sqlalchemy.orm import Session
from app.db.models import UserQuest, QuestStatus, UserReward, Event
from app.grpc.quest_client import get_quest_info, get_all_quests
from datetime import datetime

def track_sign_in(db: Session, user_id: int, quest_name: str):
    # User can only have a quest one time [1:1]
    sync_quest_and_user(db, user_id)

    # Fetch quest details from the Quest Catalog Service
    quest = get_quest_info(quest_name)
    if not quest:
        return None

     # Retrieve or create a UserQuest entry for the user
    user_quest = db.query(UserQuest).filter(
        UserQuest.user_id == user_id,
        UserQuest.quest_id == quest.quest_id
    ).first()

    if user_quest.completion_count >= quest.duplication:
        return "Max completion reached"

    # Increment progress if the quest has not been fully completed
    if user_quest.status == QuestStatus.NOT_CLAIMED:
        user_quest.progress_streak += 1
        log_event(db, user_id, "quest_completed_once", { "quest_id" : quest.quest_id, "progress_streak" : user_quest.progress_streak })

        # Check if progress meets the quest streak requirement
        if user_quest.progress_streak >= quest.streak:
            user_quest.status = QuestStatus.CLAIMED
            user_quest.progress_streak = 0
            user_quest.completion_count += 1
            log_event(db, user_id, "quest_completed_all", { "quest_id" : quest.quest_id, "completion_count" : user_quest.completion_count })

            if user_quest.completion_count < quest.duplication:
                user_quest.status = QuestStatus.NOT_CLAIMED
        
    db.commit()
    return user_quest.status

def track_sign_up(db: Session, user_id: int, quest_name: str):
    return None

def sync_quest_and_user(db: Session, user_id: int):
    quests = get_all_quests()
    for questData in quests:
        user_quest = db.query(UserQuest).filter(
            UserQuest.user_id == user_id,
            UserQuest.quest_id == questData.quest_id
        ).first()

        print(f"Quest ID: {questData.quest_id}, Quest Name: {questData.name}, Streak: {questData.streak}, Duplication: {questData.duplication}")

        if user_quest is None:
            # Create a new UserQuest entry for the user
            user_quest = UserQuest(user_id=user_id, quest_id=questData.quest_id, progress_streak=0, completion_count=0)
            db.add(user_quest)
            
    db.commit()
    return None

def claim_reward(db: Session, user_id: int, quest_name: str):

    # Fetch quest details from the Quest Catalog Service
    quest = get_quest_info(quest_name)
    if not quest:
        return None
    
    #print(f"Quest ID: {quest.quest_id}, Quest Name: {quest.name}, Streak: {quest.streak}, Duplication: {quest.duplication}, AutoClaim: {quest.auto_claim}")

    # Check user quest completion in `user_quests`
    user_quest = db.query(UserQuest).filter(
        UserQuest.user_id == user_id,
        UserQuest.quest_id == quest.quest_id
    ).first()

    if user_quest is None or user_quest.completion_count < 1:
        raise ValueError("Quest not completed yet")
    
    quest_reward = quest.rewards

    if not quest.rewards:
        quest_reward = None

    if not bool(quest.rewards):
        quest_reward = None

    if quest_reward is None:
        raise ValueError("Quest does not have a reward")

    # Check the number of times the reward has already been claimed
    reward_count = db.query(UserReward).filter(
        UserReward.user_id == user_id,
        UserReward.reward_id == quest_reward.reward_id
    ).count()

    # Ensure the user has not exceeded the claim limit (e.g., duplication limit)
    if reward_count >= quest.duplication:
        raise ValueError("Reward has already been claimed the maximum number of times")

    # Insert reward into `user_rewards`
    new_reward = UserReward(
        user_id=user_id,
        reward_id=quest_reward.reward_id,
        reward_name=quest_reward.reward_name,
        reward_item=quest_reward.reward_item, 
        reward_qty=quest_reward.reward_qty
    )
    db.add(new_reward)
    db.commit()

    log_event(db, user_id, "reward_claimed", { "quest_id" : quest.quest_id, "reward_id" : quest_reward.reward_id, "reward_name" : quest_reward.reward_name, "reward_item" : quest_reward.reward_item, "reward_qty" : quest_reward.reward_qty })
    return {"message": "Reward claimed successfully", "reward": {"item": new_reward.reward_item, "qty": new_reward.reward_qty}}

def log_event(db: Session, user_id: int, event_type: str, data: dict):
    event = Event(user_id=user_id, event_type=event_type, data=data, date=datetime.utcnow())
    db.add(event)
    db.commit()
    return event