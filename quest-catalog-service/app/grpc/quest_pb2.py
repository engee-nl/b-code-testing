# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: quest.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'quest.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bquest.proto\x12\x05quest\"\"\n\x0cQuestRequest\x12\x12\n\nquest_name\x18\x01 \x01(\t\"\x12\n\x10QuestListRequest\"Y\n\x06Reward\x12\x11\n\treward_id\x18\x01 \x01(\x05\x12\x13\n\x0breward_name\x18\x02 \x01(\t\x12\x13\n\x0breward_item\x18\x03 \x01(\t\x12\x12\n\nreward_qty\x18\x04 \x01(\x05\"\x88\x01\n\rQuestResponse\x12\x10\n\x08quest_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06streak\x18\x03 \x01(\x05\x12\x13\n\x0b\x64uplication\x18\x04 \x01(\x05\x12\x12\n\nauto_claim\x18\x05 \x01(\x08\x12\x1e\n\x07rewards\x18\x06 \x01(\x0b\x32\r.quest.Reward\"9\n\x11QuestListResponse\x12$\n\x06quests\x18\x01 \x03(\x0b\x32\x14.quest.QuestResponse2\x8c\x01\n\x0cQuestService\x12\x39\n\x0cGetQuestInfo\x12\x13.quest.QuestRequest\x1a\x14.quest.QuestResponse\x12\x41\n\x0cGetAllQuests\x12\x17.quest.QuestListRequest\x1a\x18.quest.QuestListResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'quest_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_QUESTREQUEST']._serialized_start=22
  _globals['_QUESTREQUEST']._serialized_end=56
  _globals['_QUESTLISTREQUEST']._serialized_start=58
  _globals['_QUESTLISTREQUEST']._serialized_end=76
  _globals['_REWARD']._serialized_start=78
  _globals['_REWARD']._serialized_end=167
  _globals['_QUESTRESPONSE']._serialized_start=170
  _globals['_QUESTRESPONSE']._serialized_end=306
  _globals['_QUESTLISTRESPONSE']._serialized_start=308
  _globals['_QUESTLISTRESPONSE']._serialized_end=365
  _globals['_QUESTSERVICE']._serialized_start=368
  _globals['_QUESTSERVICE']._serialized_end=508
# @@protoc_insertion_point(module_scope)