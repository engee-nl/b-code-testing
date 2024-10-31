import grpc
from app.grpc import quest_pb2, quest_pb2_grpc
from app.core.config import settings

def get_quest_info(quest_name: str):
    with grpc.insecure_channel(settings.GRPC_SERVER_URL) as channel:
        stub = quest_pb2_grpc.QuestServiceStub(channel)
        request = quest_pb2.QuestRequest(quest_name=quest_name)
        response = stub.GetQuestInfo(request)
        return response
        
def get_all_quests():
    with grpc.insecure_channel(settings.GRPC_SERVER_URL) as channel:
        stub = quest_pb2_grpc.QuestServiceStub(channel)
        request = quest_pb2.QuestListRequest()
        response = stub.GetAllQuests(request)
        return response.quests