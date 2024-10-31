import grpc
from concurrent import futures
from app.db.session import SessionLocal
from app.db.models import Quest
from app.grpc import quest_pb2, quest_pb2_grpc
import app.core.config as config
from sqlalchemy.orm import joinedload

class QuestServiceServicer(quest_pb2_grpc.QuestServiceServicer):
    def GetQuestInfo(self, request, context):
        db = SessionLocal()
        quest = db.query(Quest).filter(Quest.name == request.quest_name).first()
        db.close()

        if not quest:
            context.abort(grpc.StatusCode.NOT_FOUND, "Quest not found")

        # Prepare quest response including rewards
        response = quest_pb2.QuestResponse(
            quest_id=quest.quest_id,
            name=quest.name,
            streak=quest.streak,
            duplication=quest.duplication,
            auto_claim=quest.auto_claim,
            rewards={"reward_id": quest.rewards.reward_id, "reward_name": quest.rewards.reward_name, "reward_item": quest.rewards.reward_item, "reward_qty": quest.rewards.reward_qty}
        )
        return response
    
    def GetAllQuests(self, request, context):
        db = SessionLocal()
        quests = db.query(Quest).all()
        db.close()

        # Prepare the list of quests and associated rewards
        response = quest_pb2.QuestListResponse()
        for quest in quests:
            quest_message = quest_pb2.QuestResponse(
                quest_id=quest.quest_id,
                name=quest.name,
                streak=quest.streak,
                duplication=quest.duplication,
                auto_claim=quest.auto_claim,
                rewards={"reward_id": quest.rewards.reward_id, "reward_name": quest.rewards.reward_name, "reward_item": quest.rewards.reward_item, "reward_qty": quest.rewards.reward_qty}
            )
            response.quests.append(quest_message)
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    quest_pb2_grpc.add_QuestServiceServicer_to_server(QuestServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Quest gRPC server running on port 50051")
    server.wait_for_termination()