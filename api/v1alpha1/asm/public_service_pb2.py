# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/asm/public_service.proto
# Protobuf Python Version: 5.27.3
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
    3,
    '',
    'api/v1alpha1/asm/public_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from api.commons import asm_pb2 as api_dot_commons_dot_asm__pb2
from api.commons import omnichannel_pb2 as api_dot_commons_dot_omnichannel__pb2
from api.v1alpha1.asm import service_pb2 as api_dot_v1alpha1_dot_asm_dot_service__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/v1alpha1/asm/public_service.proto\x12\x10\x61pi.v1alpha1.asm\x1a\x17\x61nnotations/authz.proto\x1a\x15\x61pi/commons/acd.proto\x1a\x15\x61pi/commons/asm.proto\x1a\x1d\x61pi/commons/omnichannel.proto\x1a\x1e\x61pi/v1alpha1/asm/service.proto\x1a\x1cgoogle/api/annotations.proto2\xf6\x0f\n\x03\x41sm\x12\x9a\x01\n\x10StreamAgentState\x12%.api.v1alpha1.asm.StreamAgentStateReq\x1a .api.commons.StreamAgentStateRes\";\xba\xb8\x91\x02\x05\n\x03\x08\xac\x02\x82\xd3\xe4\x93\x02+\"&/api/v1alpha1/asm/asm/streamagentstate:\x01*0\x01\x12\xb6\x01\n\x17ManagerStreamAgentState\x12,.api.v1alpha1.asm.ManagerStreamAgentStateReq\x1a\'.api.commons.ManagerStreamAgentStateRes\"B\xba\xb8\x91\x02\x05\n\x03\x08\x90\x03\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/asm/asm/managerstreamagentstate:\x01*0\x01\x12\x85\x01\n\nPushEvents\x12\x1f.api.v1alpha1.asm.PushEventsReq\x1a\x1f.api.v1alpha1.asm.PushEventsRes\"5\xba\xb8\x91\x02\x05\n\x03\x08\xac\x02\x82\xd3\xe4\x93\x02%\" /api/v1alpha1/asm/asm/pushevents:\x01*\x12\x8e\x01\n\rCreateSession\x12\".api.v1alpha1.asm.CreateSessionReq\x1a\".api.v1alpha1.asm.CreateSessionRes\"5\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/asm/asm/createsession:\x01*\x12\x82\x01\n\nEndSession\x12\x1f.api.v1alpha1.asm.EndSessionReq\x1a\x1f.api.v1alpha1.asm.EndSessionRes\"2\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02%\" /api/v1alpha1/asm/asm/endsession:\x01*\x12\x94\x01\n\x11GetCurrentSession\x12&.api.v1alpha1.asm.GetCurrentSessionReq\x1a\x1c.api.v1alpha1.asm.AsmSession\"9\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/asm/asm/getcurrentsession:\x01*\x12\x86\x01\n\x0b\x45nableVoice\x12 .api.v1alpha1.asm.EnableVoiceReq\x1a .api.v1alpha1.asm.EnableVoiceRes\"3\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02&\"!/api/v1alpha1/asm/asm/enablevoice:\x01*\x12\x8a\x01\n\x0c\x44isableVoice\x12!.api.v1alpha1.asm.DisableVoiceReq\x1a!.api.v1alpha1.asm.DisableVoiceRes\"4\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\'\"\"/api/v1alpha1/asm/asm/disablevoice:\x01*\x12\xa1\x01\n\x11ListConversations\x12&.api.v1alpha1.asm.ListConversationsReq\x1a&.api.v1alpha1.asm.ListConversationsRes\"<\xba\xb8\x91\x02\x05\n\x03\x08\xac\x02\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/asm/asm/listconversations:\x01*\x12\xb1\x01\n\x15\x41ssignNewConversation\x12*.api.v1alpha1.asm.AssignNewConversationReq\x1a*.api.v1alpha1.asm.AssignNewConversationRes\"@\xba\xb8\x91\x02\x05\n\x03\x08\xac\x02\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/asm/asm/assignnewconversation:\x01*\x12\x85\x01\n\nListAgents\x12\x1f.api.v1alpha1.asm.ListAgentsReq\x1a\x1f.api.v1alpha1.asm.ListAgentsRes\"5\xba\xb8\x91\x02\x05\n\x03\x08\xb0\t\x82\xd3\xe4\x93\x02%\" /api/v1alpha1/asm/asm/listagents:\x01*\x12\xd2\x01\n\x1cSetConversationCollectedData\x12\x31.api.v1alpha1.asm.SetConversationCollectedDataReq\x1a\x31.api.v1alpha1.asm.SetConversationCollectedDataRes\"L\xba\xb8\x91\x02\n\n\x03\x08\xac\x02\n\x03\x08\xb0\t\x82\xd3\xe4\x93\x02\x37\"2/api/v1alpha1/asm/asm/setconversationcollecteddata:\x01*\x12\x98\x01\n\x10GetQueuesDetails\x12%.api.v1alpha1.asm.GetQueuesDetailsReq\x1a .api.commons.GetQueuesDetailsRes\";\xba\xb8\x91\x02\x05\n\x03\x08\xac\x02\x82\xd3\xe4\x93\x02+\"&/api/v1alpha1/asm/asm/getqueuesdetails:\x01*B\x8c\x01\n\x14\x63om.api.v1alpha1.asmB\x12PublicServiceProtoP\x01\xa2\x02\x03\x41VA\xaa\x02\x10\x41pi.V1alpha1.Asm\xca\x02\x10\x41pi\\V1alpha1\\Asm\xe2\x02\x1c\x41pi\\V1alpha1\\Asm\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Asmb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.asm.public_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.asmB\022PublicServiceProtoP\001\242\002\003AVA\252\002\020Api.V1alpha1.Asm\312\002\020Api\\V1alpha1\\Asm\342\002\034Api\\V1alpha1\\Asm\\GPBMetadata\352\002\022Api::V1alpha1::Asm'
  _globals['_ASM'].methods_by_name['StreamAgentState']._loaded_options = None
  _globals['_ASM'].methods_by_name['StreamAgentState']._serialized_options = b'\272\270\221\002\005\n\003\010\254\002\202\323\344\223\002+\"&/api/v1alpha1/asm/asm/streamagentstate:\001*'
  _globals['_ASM'].methods_by_name['ManagerStreamAgentState']._loaded_options = None
  _globals['_ASM'].methods_by_name['ManagerStreamAgentState']._serialized_options = b'\272\270\221\002\005\n\003\010\220\003\202\323\344\223\0022\"-/api/v1alpha1/asm/asm/managerstreamagentstate:\001*'
  _globals['_ASM'].methods_by_name['PushEvents']._loaded_options = None
  _globals['_ASM'].methods_by_name['PushEvents']._serialized_options = b'\272\270\221\002\005\n\003\010\254\002\202\323\344\223\002%\" /api/v1alpha1/asm/asm/pushevents:\001*'
  _globals['_ASM'].methods_by_name['CreateSession']._loaded_options = None
  _globals['_ASM'].methods_by_name['CreateSession']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002(\"#/api/v1alpha1/asm/asm/createsession:\001*'
  _globals['_ASM'].methods_by_name['EndSession']._loaded_options = None
  _globals['_ASM'].methods_by_name['EndSession']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002%\" /api/v1alpha1/asm/asm/endsession:\001*'
  _globals['_ASM'].methods_by_name['GetCurrentSession']._loaded_options = None
  _globals['_ASM'].methods_by_name['GetCurrentSession']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002,\"\'/api/v1alpha1/asm/asm/getcurrentsession:\001*'
  _globals['_ASM'].methods_by_name['EnableVoice']._loaded_options = None
  _globals['_ASM'].methods_by_name['EnableVoice']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002&\"!/api/v1alpha1/asm/asm/enablevoice:\001*'
  _globals['_ASM'].methods_by_name['DisableVoice']._loaded_options = None
  _globals['_ASM'].methods_by_name['DisableVoice']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\'\"\"/api/v1alpha1/asm/asm/disablevoice:\001*'
  _globals['_ASM'].methods_by_name['ListConversations']._loaded_options = None
  _globals['_ASM'].methods_by_name['ListConversations']._serialized_options = b'\272\270\221\002\005\n\003\010\254\002\202\323\344\223\002,\"\'/api/v1alpha1/asm/asm/listconversations:\001*'
  _globals['_ASM'].methods_by_name['AssignNewConversation']._loaded_options = None
  _globals['_ASM'].methods_by_name['AssignNewConversation']._serialized_options = b'\272\270\221\002\005\n\003\010\254\002\202\323\344\223\0020\"+/api/v1alpha1/asm/asm/assignnewconversation:\001*'
  _globals['_ASM'].methods_by_name['ListAgents']._loaded_options = None
  _globals['_ASM'].methods_by_name['ListAgents']._serialized_options = b'\272\270\221\002\005\n\003\010\260\t\202\323\344\223\002%\" /api/v1alpha1/asm/asm/listagents:\001*'
  _globals['_ASM'].methods_by_name['SetConversationCollectedData']._loaded_options = None
  _globals['_ASM'].methods_by_name['SetConversationCollectedData']._serialized_options = b'\272\270\221\002\n\n\003\010\254\002\n\003\010\260\t\202\323\344\223\0027\"2/api/v1alpha1/asm/asm/setconversationcollecteddata:\001*'
  _globals['_ASM'].methods_by_name['GetQueuesDetails']._loaded_options = None
  _globals['_ASM'].methods_by_name['GetQueuesDetails']._serialized_options = b'\272\270\221\002\005\n\003\010\254\002\202\323\344\223\002+\"&/api/v1alpha1/asm/asm/getqueuesdetails:\001*'
  _globals['_ASM']._serialized_start=224
  _globals['_ASM']._serialized_end=2262
# @@protoc_insertion_point(module_scope)
