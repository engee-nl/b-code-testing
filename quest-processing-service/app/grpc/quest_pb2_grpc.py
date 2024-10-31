# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import quest_pb2 as quest__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in quest_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class QuestServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetQuestInfo = channel.unary_unary(
                '/quest.QuestService/GetQuestInfo',
                request_serializer=quest__pb2.QuestRequest.SerializeToString,
                response_deserializer=quest__pb2.QuestResponse.FromString,
                _registered_method=True)
        self.GetAllQuests = channel.unary_unary(
                '/quest.QuestService/GetAllQuests',
                request_serializer=quest__pb2.QuestListRequest.SerializeToString,
                response_deserializer=quest__pb2.QuestListResponse.FromString,
                _registered_method=True)


class QuestServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetQuestInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllQuests(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QuestServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetQuestInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetQuestInfo,
                    request_deserializer=quest__pb2.QuestRequest.FromString,
                    response_serializer=quest__pb2.QuestResponse.SerializeToString,
            ),
            'GetAllQuests': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllQuests,
                    request_deserializer=quest__pb2.QuestListRequest.FromString,
                    response_serializer=quest__pb2.QuestListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'quest.QuestService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('quest.QuestService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class QuestService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetQuestInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/quest.QuestService/GetQuestInfo',
            quest__pb2.QuestRequest.SerializeToString,
            quest__pb2.QuestResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAllQuests(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/quest.QuestService/GetAllQuests',
            quest__pb2.QuestListRequest.SerializeToString,
            quest__pb2.QuestListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
