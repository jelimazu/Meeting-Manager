# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: meeting_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'meeting_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15meeting_service.proto\x12\x07meeting\"\'\n\x11GetMeetingRequest\x12\x12\n\nmeeting_id\x18\x01 \x01(\x05\"Z\n\x12GetMeetingResponse\x12\x12\n\nmeeting_id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\"E\n\x15\x41\x64\x64ParticipantRequest\x12\x12\n\nmeeting_id\x18\x01 \x01(\x05\x12\x18\n\x10participant_name\x18\x02 \x01(\t\")\n\x16\x41\x64\x64ParticipantResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"-\n\x17ListParticipantsRequest\x12\x12\n\nmeeting_id\x18\x01 \x01(\x05\"3\n\x0bParticipant\x12\x16\n\x0eparticipant_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"F\n\x18ListParticipantsResponse\x12*\n\x0cparticipants\x18\x01 \x03(\x0b\x32\x14.meeting.Participant2\x83\x02\n\x0eMeetingService\x12\x45\n\nGetMeeting\x12\x1a.meeting.GetMeetingRequest\x1a\x1b.meeting.GetMeetingResponse\x12Q\n\x0e\x41\x64\x64Participant\x12\x1e.meeting.AddParticipantRequest\x1a\x1f.meeting.AddParticipantResponse\x12W\n\x10ListParticipants\x12 .meeting.ListParticipantsRequest\x1a!.meeting.ListParticipantsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meeting_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETMEETINGREQUEST']._serialized_start=34
  _globals['_GETMEETINGREQUEST']._serialized_end=73
  _globals['_GETMEETINGRESPONSE']._serialized_start=75
  _globals['_GETMEETINGRESPONSE']._serialized_end=165
  _globals['_ADDPARTICIPANTREQUEST']._serialized_start=167
  _globals['_ADDPARTICIPANTREQUEST']._serialized_end=236
  _globals['_ADDPARTICIPANTRESPONSE']._serialized_start=238
  _globals['_ADDPARTICIPANTRESPONSE']._serialized_end=279
  _globals['_LISTPARTICIPANTSREQUEST']._serialized_start=281
  _globals['_LISTPARTICIPANTSREQUEST']._serialized_end=326
  _globals['_PARTICIPANT']._serialized_start=328
  _globals['_PARTICIPANT']._serialized_end=379
  _globals['_LISTPARTICIPANTSRESPONSE']._serialized_start=381
  _globals['_LISTPARTICIPANTSRESPONSE']._serialized_end=451
  _globals['_MEETINGSERVICE']._serialized_start=454
  _globals['_MEETINGSERVICE']._serialized_end=713
# @@protoc_insertion_point(module_scope)