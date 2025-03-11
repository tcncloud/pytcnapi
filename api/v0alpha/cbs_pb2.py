# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v0alpha/cbs.proto
# Protobuf Python Version: 6.30.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    0,
    '',
    'api/v0alpha/cbs.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from api.commons import cbs_pb2 as api_dot_commons_dot_cbs__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi/v0alpha/cbs.proto\x12\x0b\x61pi.v0alpha\x1a\x17\x61nnotations/authz.proto\x1a\x15\x61pi/commons/acd.proto\x1a\x15\x61pi/commons/cbs.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x14\n\x12\x43reateServiceIdReq\"3\n\x12\x43reateServiceIdRes\x12\x1d\n\nservice_id\x18\x01 \x01(\tR\tserviceId\"\xc3\x04\n\x11ScheduledCallback\x12\x32\n\x15scheduled_callback_id\x18\x01 \x01(\tR\x13scheduledCallbackId\x12\x1d\n\nservice_id\x18\x64 \x01(\tR\tserviceId\x12<\n\x06status\x18\x65 \x01(\x0e\x32$.api.commons.ScheduledCallbackStatusR\x06status\x12\x39\n\nstart_time\x18\x66 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18g \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12!\n\x0cphone_number\x18h \x01(\tR\x0bphoneNumber\x12\x1b\n\tcaller_id\x18i \x01(\tR\x08\x63\x61llerId\x12\x14\n\x05notes\x18k \x01(\tR\x05notes\x12;\n\x0b\x63reate_date\x18l \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateDate\x12;\n\x0blast_update\x18m \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nlastUpdate\x12&\n\x0flast_updated_by\x18o \x01(\tR\rlastUpdatedBy\x12\'\n\x0f\x63\x61llback_skills\x18p \x03(\tR\x0e\x63\x61llbackSkillsJ\x04\x08n\x10oJ\x04\x08j\x10k\"\xb6\x01\n\x17ScheduledCallbackDetail\x12?\n\x1cscheduled_callback_detail_id\x18\x01 \x01(\tR\x19scheduledCallbackDetailId\x12\x32\n\x15scheduled_callback_id\x18\x02 \x01(\tR\x13scheduledCallbackId\x12\x10\n\x03key\x18\x64 \x01(\tR\x03key\x12\x14\n\x05value\x18\x65 \x01(\tR\x05value\"\x9c\x01\n!UpdateScheduledCallbackToReadyReq\x12\x32\n\x15scheduled_callback_id\x18\x02 \x01(\tR\x13scheduledCallbackId\x12$\n\x0eis_auto_return\x18\x03 \x01(\x08R\x0cisAutoReturn\x12\x1d\n\nservice_id\x18\x04 \x01(\tR\tserviceId\"#\n!UpdateScheduledCallbackToReadyRes\"y\n$UpdateScheduledCallbackToCanceledReq\x12\x32\n\x15scheduled_callback_id\x18\x02 \x01(\tR\x13scheduledCallbackId\x12\x1d\n\nservice_id\x18\x03 \x01(\tR\tserviceId\"&\n$UpdateScheduledCallbackToCanceledRes\"\xa8\x01\n\"UpdateScheduledCallbackToClosedReq\x12\x32\n\x15scheduled_callback_id\x18\x02 \x01(\tR\x13scheduledCallbackId\x12/\n\x14manual_dial_call_sid\x18\x03 \x01(\x03R\x11manualDialCallSid\x12\x1d\n\nservice_id\x18\x04 \x01(\tR\tserviceId\"$\n\"UpdateScheduledCallbackToClosedRes\"\x90\x03\n\x1c\x43reateCallbackWithDetailsReq\x12:\n\x08\x63\x61llback\x18\x02 \x01(\x0b\x32\x1e.api.v0alpha.ScheduledCallbackR\x08\x63\x61llback\x12O\n\x10\x63\x61llback_details\x18\x03 \x03(\x0b\x32$.api.v0alpha.ScheduledCallbackDetailR\x0f\x63\x61llbackDetails\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12\x44\n\x10\x66ormer_call_type\x18\x05 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x0e\x66ormerCallType\x12&\n\x0f\x66ormer_call_sid\x18\x06 \x01(\x03R\rformerCallSid\x12<\n\x0b\x63ountry_sid\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\ncountrySid\x12#\n\rmanager_login\x18\t \x01(\x08R\x0cmanagerLogin\"R\n\x1c\x43reateCallbackWithDetailsRes\x12\x32\n\x15scheduled_callback_id\x18\x01 \x01(\tR\x13scheduledCallbackId\"\x88\x04\n\x1aUpdateScheduledCallbackReq\x12\x32\n\x15scheduled_callback_id\x18\x02 \x01(\tR\x13scheduledCallbackId\x12\x43\n\nnew_status\x18\x03 \x01(\x0e\x32$.api.commons.ScheduledCallbackStatusR\tnewStatus\x12\x39\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12!\n\x0cphone_number\x18\x06 \x01(\tR\x0bphoneNumber\x12\x1b\n\tcaller_id\x18\x07 \x01(\tR\x08\x63\x61llerId\x12\x16\n\x06skills\x18\x08 \x03(\tR\x06skills\x12&\n\x0flast_updated_by\x18\t \x01(\tR\rlastUpdatedBy\x12\x14\n\x05notes\x18\n \x01(\tR\x05notes\x12O\n\x10\x63\x61llback_details\x18\x0b \x03(\x0b\x32$.api.v0alpha.ScheduledCallbackDetailR\x0f\x63\x61llbackDetails\x12\x12\n\x04name\x18\x0c \x01(\tR\x04nameJ\x04\x08\x01\x10\x02\"\x1c\n\x1aUpdateScheduledCallbackRes\"\xe1\x06\n\x1cScheduledCallbackWithDetails\x12\x32\n\x15scheduled_callback_id\x18\x01 \x01(\tR\x13scheduledCallbackId\x12\x1d\n\nservice_id\x18\x02 \x01(\tR\tserviceId\x12<\n\x06status\x18\x03 \x01(\x0e\x32$.api.commons.ScheduledCallbackStatusR\x06status\x12\x39\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12!\n\x0cphone_number\x18\x06 \x01(\tR\x0bphoneNumber\x12\x1b\n\tcaller_id\x18\x07 \x01(\tR\x08\x63\x61llerId\x12\x16\n\x06skills\x18\x08 \x03(\tR\x06skills\x12\x14\n\x05notes\x18\t \x01(\tR\x05notes\x12;\n\x0b\x63reate_date\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateDate\x12;\n\x0blast_update\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nlastUpdate\x12\x1d\n\ncreated_by\x18\x0c \x01(\tR\tcreatedBy\x12&\n\x0flast_updated_by\x18\r \x01(\tR\rlastUpdatedBy\x12\x12\n\x04name\x18\x0e \x01(\tR\x04name\x12&\n\x0f\x66ormer_call_sid\x18\x0f \x01(\x03R\rformerCallSid\x12\x44\n\x10\x66ormer_call_type\x18\x10 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x0e\x66ormerCallType\x12O\n\x10\x63\x61llback_details\x18\x11 \x03(\x0b\x32$.api.v0alpha.ScheduledCallbackDetailR\x0f\x63\x61llbackDetails\x12<\n\x0b\x63ountry_sid\x18\x12 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\ncountrySid\"w\n\"GetScheduledCallbackWithDetailsReq\x12\x1d\n\nservice_id\x18\x01 \x01(\tR\tserviceId\x12\x32\n\x15scheduled_callback_id\x18\x02 \x01(\tR\x13scheduledCallbackId\"k\n\"GetScheduledCallbackWithDetailsRes\x12\x45\n\x08\x63\x61llback\x18\x01 \x01(\x0b\x32).api.v0alpha.ScheduledCallbackWithDetailsR\x08\x63\x61llback\"o\n$ListScheduledCallbacksWithDetailsRes\x12G\n\tcallbacks\x18\x01 \x03(\x0b\x32).api.v0alpha.ScheduledCallbackWithDetailsR\tcallbacks\"j\n&GetNextScheduledCallbackWithDetailsReq\x12\x1d\n\nservice_id\x18\x01 \x01(\tR\tserviceId\x12!\n\x0c\x61gent_skills\x18\x03 \x03(\tR\x0b\x61gentSkills\"\x82\x01\n&GetNextScheduledCallbackWithDetailsRes\x12X\n\x12scheduled_callback\x18\x01 \x01(\x0b\x32).api.v0alpha.ScheduledCallbackWithDetailsR\x11scheduledCallback\"\x82\x02\n$ListScheduledCallbacksWithDetailsReq\x12!\n\x0cphone_number\x18\x02 \x01(\tR\x0bphoneNumber\x12\x1b\n\tcaller_id\x18\x03 \x01(\tR\x08\x63\x61llerId\x12\x42\n\x0f\x66rom_start_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rfromStartTime\x12>\n\rto_start_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0btoStartTime\x12\x16\n\x06skills\x18\x06 \x03(\tR\x06skills\"e\n,ListScheduledCallbacksWithDetailsBySkillsReq\x12\x1d\n\nservice_id\x18\x01 \x01(\tR\tserviceId\x12\x16\n\x06skills\x18\x03 \x03(\tR\x06skills2\xcb\x0f\n\x03\x43\x42S\x12\x87\x01\n\x0f\x43reateServiceId\x12\x1f.api.v0alpha.CreateServiceIdReq\x1a\x1f.api.v0alpha.CreateServiceIdRes\"2\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02%\" /api/v0alpha/cbs/createserviceid:\x01*\x12\xb7\x01\n\x19\x43reateCallbackWithDetails\x12).api.v0alpha.CreateCallbackWithDetailsReq\x1a).api.v0alpha.CreateCallbackWithDetailsRes\"D\xba\xb8\x91\x02\n\n\x03\x08\x90\x03\n\x03\x08\xac\x02\x82\xd3\xe4\x93\x02/\"*/api/v0alpha/cbs/createcallbackwithdetails:\x01*\x12\xc3\x01\n\x1eUpdateScheduledCallbackToReady\x12..api.v0alpha.UpdateScheduledCallbackToReadyReq\x1a..api.v0alpha.UpdateScheduledCallbackToReadyRes\"A\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x34\"//api/v0alpha/cbs/updatescheduledcallbacktoready:\x01*\x12\xcf\x01\n!UpdateScheduledCallbackToCanceled\x12\x31.api.v0alpha.UpdateScheduledCallbackToCanceledReq\x1a\x31.api.v0alpha.UpdateScheduledCallbackToCanceledRes\"D\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x37\"2/api/v0alpha/cbs/updatescheduledcallbacktocanceled:\x01*\x12\xd7\x01\n#GetNextScheduledCallbackWithDetails\x12\x33.api.v0alpha.GetNextScheduledCallbackWithDetailsReq\x1a\x33.api.v0alpha.GetNextScheduledCallbackWithDetailsRes\"F\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x39\"4/api/v0alpha/cbs/getnextscheduledcallbackwithdetails:\x01*\x12\xc7\x01\n\x1fUpdateScheduledCallbackToClosed\x12/.api.v0alpha.UpdateScheduledCallbackToClosedReq\x1a/.api.v0alpha.UpdateScheduledCallbackToClosedRes\"B\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x35\"0/api/v0alpha/cbs/updatescheduledcallbacktoclosed:\x01*\x12\xaa\x01\n\x17UpdateScheduledCallback\x12\'.api.v0alpha.UpdateScheduledCallbackReq\x1a\'.api.v0alpha.UpdateScheduledCallbackRes\"=\xba\xb8\x91\x02\x05\n\x03\x08\x90\x03\x82\xd3\xe4\x93\x02-\"(/api/v0alpha/cbs/updatescheduledcallback:\x01*\x12\xcf\x01\n\x1fGetScheduledCallbackWithDetails\x12/.api.v0alpha.GetScheduledCallbackWithDetailsReq\x1a/.api.v0alpha.GetScheduledCallbackWithDetailsRes\"J\xba\xb8\x91\x02\n\n\x03\x08\x90\x03\n\x03\x08\xac\x02\x82\xd3\xe4\x93\x02\x35\"0/api/v0alpha/cbs/getscheduledcallbackwithdetails:\x01*\x12\xd4\x01\n!ListScheduledCallbacksWithDetails\x12\x31.api.v0alpha.ListScheduledCallbacksWithDetailsReq\x1a\x31.api.v0alpha.ListScheduledCallbacksWithDetailsRes\"G\xba\xb8\x91\x02\x05\n\x03\x08\x90\x03\x82\xd3\xe4\x93\x02\x37\"2/api/v0alpha/cbs/listscheduledcallbackswithdetails:\x01*0\x01\x12\xed\x01\n)ListScheduledCallbacksWithDetailsBySkills\x12\x39.api.v0alpha.ListScheduledCallbacksWithDetailsBySkillsReq\x1a\x31.api.v0alpha.ListScheduledCallbacksWithDetailsRes\"R\xba\xb8\x91\x02\x05\n\x03\x08\xac\x02\x82\xd3\xe4\x93\x02\x42\"=/api/v0alpha/cbs/listscheduledcallbackswithdetailsbyskillsreq:\x01*Bh\n\x0f\x63om.api.v0alphaB\x08\x43\x62sProtoP\x01\xa2\x02\x03\x41VX\xaa\x02\x0b\x41pi.V0alpha\xca\x02\x0b\x41pi\\V0alpha\xe2\x02\x17\x41pi\\V0alpha\\GPBMetadata\xea\x02\x0c\x41pi::V0alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v0alpha.cbs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.v0alphaB\010CbsProtoP\001\242\002\003AVX\252\002\013Api.V0alpha\312\002\013Api\\V0alpha\342\002\027Api\\V0alpha\\GPBMetadata\352\002\014Api::V0alpha'
  _globals['_CBS'].methods_by_name['CreateServiceId']._loaded_options = None
  _globals['_CBS'].methods_by_name['CreateServiceId']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002%\" /api/v0alpha/cbs/createserviceid:\001*'
  _globals['_CBS'].methods_by_name['CreateCallbackWithDetails']._loaded_options = None
  _globals['_CBS'].methods_by_name['CreateCallbackWithDetails']._serialized_options = b'\272\270\221\002\n\n\003\010\220\003\n\003\010\254\002\202\323\344\223\002/\"*/api/v0alpha/cbs/createcallbackwithdetails:\001*'
  _globals['_CBS'].methods_by_name['UpdateScheduledCallbackToReady']._loaded_options = None
  _globals['_CBS'].methods_by_name['UpdateScheduledCallbackToReady']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0024\"//api/v0alpha/cbs/updatescheduledcallbacktoready:\001*'
  _globals['_CBS'].methods_by_name['UpdateScheduledCallbackToCanceled']._loaded_options = None
  _globals['_CBS'].methods_by_name['UpdateScheduledCallbackToCanceled']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0027\"2/api/v0alpha/cbs/updatescheduledcallbacktocanceled:\001*'
  _globals['_CBS'].methods_by_name['GetNextScheduledCallbackWithDetails']._loaded_options = None
  _globals['_CBS'].methods_by_name['GetNextScheduledCallbackWithDetails']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0029\"4/api/v0alpha/cbs/getnextscheduledcallbackwithdetails:\001*'
  _globals['_CBS'].methods_by_name['UpdateScheduledCallbackToClosed']._loaded_options = None
  _globals['_CBS'].methods_by_name['UpdateScheduledCallbackToClosed']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0025\"0/api/v0alpha/cbs/updatescheduledcallbacktoclosed:\001*'
  _globals['_CBS'].methods_by_name['UpdateScheduledCallback']._loaded_options = None
  _globals['_CBS'].methods_by_name['UpdateScheduledCallback']._serialized_options = b'\272\270\221\002\005\n\003\010\220\003\202\323\344\223\002-\"(/api/v0alpha/cbs/updatescheduledcallback:\001*'
  _globals['_CBS'].methods_by_name['GetScheduledCallbackWithDetails']._loaded_options = None
  _globals['_CBS'].methods_by_name['GetScheduledCallbackWithDetails']._serialized_options = b'\272\270\221\002\n\n\003\010\220\003\n\003\010\254\002\202\323\344\223\0025\"0/api/v0alpha/cbs/getscheduledcallbackwithdetails:\001*'
  _globals['_CBS'].methods_by_name['ListScheduledCallbacksWithDetails']._loaded_options = None
  _globals['_CBS'].methods_by_name['ListScheduledCallbacksWithDetails']._serialized_options = b'\272\270\221\002\005\n\003\010\220\003\202\323\344\223\0027\"2/api/v0alpha/cbs/listscheduledcallbackswithdetails:\001*'
  _globals['_CBS'].methods_by_name['ListScheduledCallbacksWithDetailsBySkills']._loaded_options = None
  _globals['_CBS'].methods_by_name['ListScheduledCallbacksWithDetailsBySkills']._serialized_options = b'\272\270\221\002\005\n\003\010\254\002\202\323\344\223\002B\"=/api/v0alpha/cbs/listscheduledcallbackswithdetailsbyskillsreq:\001*'
  _globals['_CREATESERVICEIDREQ']._serialized_start=204
  _globals['_CREATESERVICEIDREQ']._serialized_end=224
  _globals['_CREATESERVICEIDRES']._serialized_start=226
  _globals['_CREATESERVICEIDRES']._serialized_end=277
  _globals['_SCHEDULEDCALLBACK']._serialized_start=280
  _globals['_SCHEDULEDCALLBACK']._serialized_end=859
  _globals['_SCHEDULEDCALLBACKDETAIL']._serialized_start=862
  _globals['_SCHEDULEDCALLBACKDETAIL']._serialized_end=1044
  _globals['_UPDATESCHEDULEDCALLBACKTOREADYREQ']._serialized_start=1047
  _globals['_UPDATESCHEDULEDCALLBACKTOREADYREQ']._serialized_end=1203
  _globals['_UPDATESCHEDULEDCALLBACKTOREADYRES']._serialized_start=1205
  _globals['_UPDATESCHEDULEDCALLBACKTOREADYRES']._serialized_end=1240
  _globals['_UPDATESCHEDULEDCALLBACKTOCANCELEDREQ']._serialized_start=1242
  _globals['_UPDATESCHEDULEDCALLBACKTOCANCELEDREQ']._serialized_end=1363
  _globals['_UPDATESCHEDULEDCALLBACKTOCANCELEDRES']._serialized_start=1365
  _globals['_UPDATESCHEDULEDCALLBACKTOCANCELEDRES']._serialized_end=1403
  _globals['_UPDATESCHEDULEDCALLBACKTOCLOSEDREQ']._serialized_start=1406
  _globals['_UPDATESCHEDULEDCALLBACKTOCLOSEDREQ']._serialized_end=1574
  _globals['_UPDATESCHEDULEDCALLBACKTOCLOSEDRES']._serialized_start=1576
  _globals['_UPDATESCHEDULEDCALLBACKTOCLOSEDRES']._serialized_end=1612
  _globals['_CREATECALLBACKWITHDETAILSREQ']._serialized_start=1615
  _globals['_CREATECALLBACKWITHDETAILSREQ']._serialized_end=2015
  _globals['_CREATECALLBACKWITHDETAILSRES']._serialized_start=2017
  _globals['_CREATECALLBACKWITHDETAILSRES']._serialized_end=2099
  _globals['_UPDATESCHEDULEDCALLBACKREQ']._serialized_start=2102
  _globals['_UPDATESCHEDULEDCALLBACKREQ']._serialized_end=2622
  _globals['_UPDATESCHEDULEDCALLBACKRES']._serialized_start=2624
  _globals['_UPDATESCHEDULEDCALLBACKRES']._serialized_end=2652
  _globals['_SCHEDULEDCALLBACKWITHDETAILS']._serialized_start=2655
  _globals['_SCHEDULEDCALLBACKWITHDETAILS']._serialized_end=3520
  _globals['_GETSCHEDULEDCALLBACKWITHDETAILSREQ']._serialized_start=3522
  _globals['_GETSCHEDULEDCALLBACKWITHDETAILSREQ']._serialized_end=3641
  _globals['_GETSCHEDULEDCALLBACKWITHDETAILSRES']._serialized_start=3643
  _globals['_GETSCHEDULEDCALLBACKWITHDETAILSRES']._serialized_end=3750
  _globals['_LISTSCHEDULEDCALLBACKSWITHDETAILSRES']._serialized_start=3752
  _globals['_LISTSCHEDULEDCALLBACKSWITHDETAILSRES']._serialized_end=3863
  _globals['_GETNEXTSCHEDULEDCALLBACKWITHDETAILSREQ']._serialized_start=3865
  _globals['_GETNEXTSCHEDULEDCALLBACKWITHDETAILSREQ']._serialized_end=3971
  _globals['_GETNEXTSCHEDULEDCALLBACKWITHDETAILSRES']._serialized_start=3974
  _globals['_GETNEXTSCHEDULEDCALLBACKWITHDETAILSRES']._serialized_end=4104
  _globals['_LISTSCHEDULEDCALLBACKSWITHDETAILSREQ']._serialized_start=4107
  _globals['_LISTSCHEDULEDCALLBACKSWITHDETAILSREQ']._serialized_end=4365
  _globals['_LISTSCHEDULEDCALLBACKSWITHDETAILSBYSKILLSREQ']._serialized_start=4367
  _globals['_LISTSCHEDULEDCALLBACKSWITHDETAILSBYSKILLSREQ']._serialized_end=4468
  _globals['_CBS']._serialized_start=4471
  _globals['_CBS']._serialized_end=6466
# @@protoc_insertion_point(module_scope)
