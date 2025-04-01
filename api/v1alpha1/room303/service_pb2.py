# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/room303/service.proto
# Protobuf Python Version: 6.30.2
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
    2,
    '',
    'api/v1alpha1/room303/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons import room303_pb2 as api_dot_commons_dot_room303__pb2
from api.v1alpha1.room303 import member_pb2 as api_dot_v1alpha1_dot_room303_dot_member__pb2
from api.v1alpha1.room303 import message_pb2 as api_dot_v1alpha1_dot_room303_dot_message__pb2
from api.v1alpha1.room303 import room_pb2 as api_dot_v1alpha1_dot_room303_dot_room__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/v1alpha1/room303/service.proto\x12\x14\x61pi.v1alpha1.room303\x1a\x17\x61nnotations/authz.proto\x1a\x19\x61pi/commons/room303.proto\x1a!api/v1alpha1/room303/member.proto\x1a\"api/v1alpha1/room303/message.proto\x1a\x1f\x61pi/v1alpha1/room303/room.proto\x1a\x1cgoogle/api/annotations.proto2\xe0!\n\nRoom303API\x12\x95\x01\n\rAddRoomMember\x12*.api.v1alpha1.room303.AddRoomMemberRequest\x1a\x13.api.commons.Member\"C\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/room303/room303api/addroommember:\x01*\x12\xb9\x01\n\x10RemoveRoomMember\x12-.api.v1alpha1.room303.RemoveRoomMemberRequest\x1a..api.v1alpha1.room303.RemoveRoomMemberResponse\"F\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x36\"1/api/v1alpha1/room303/room303api/removeroommember:\x01*\x12\xb5\x01\n\x0fListRoomMembers\x12,.api.v1alpha1.room303.ListRoomMembersRequest\x1a-.api.v1alpha1.room303.ListRoomMembersResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/room303/room303api/listroommembers:\x01*\x12\xcd\x01\n\x15SetAdminForRoomMember\x12\x32.api.v1alpha1.room303.SetAdminForRoomMemberRequest\x1a\x33.api.v1alpha1.room303.SetAdminForRoomMemberResponse\"K\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02;\"6/api/v1alpha1/room303/room303api/setadminforroommember:\x01*\x12\x84\x01\n\x08JoinRoom\x12%.api.v1alpha1.room303.JoinRoomRequest\x1a\x11.api.commons.Room\">\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/room303/room303api/joinroom:\x01*\x12\x95\x01\n\rGetRoomMember\x12*.api.v1alpha1.room303.GetRoomMemberRequest\x1a\x13.api.commons.Member\"C\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/room303/room303api/getroommember:\x01*\x12\xad\x01\n\rCreateMessage\x12*.api.v1alpha1.room303.CreateMessageRequest\x1a+.api.v1alpha1.room303.CreateMessageResponse\"C\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/room303/room303api/createmessage:\x01*\x12\xa5\x01\n\x0b\x45\x64itMessage\x12(.api.v1alpha1.room303.EditMessageRequest\x1a).api.v1alpha1.room303.EditMessageResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/room303/room303api/editmessage:\x01*\x12\xad\x01\n\rDeleteMessage\x12*.api.v1alpha1.room303.DeleteMessageRequest\x1a+.api.v1alpha1.room303.DeleteMessageResponse\"C\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/room303/room303api/deletemessage:\x01*\x12\xa5\x01\n\x0bGetMessages\x12(.api.v1alpha1.room303.GetMessagesRequest\x1a).api.v1alpha1.room303.GetMessagesResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/room303/room303api/getmessages:\x01*\x12\xcb\x01\n\x14StreamMessageUpdates\x12\x31.api.v1alpha1.room303.StreamMessageUpdatesRequest\x1a\x32.api.v1alpha1.room303.StreamMessageUpdatesResponse\"J\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02:\"5/api/v1alpha1/room303/room303api/streammessageupdates:\x01*0\x01\x12\xb1\x01\n\x0eGetUnreadStats\x12+.api.v1alpha1.room303.GetUnreadStatsRequest\x1a,.api.v1alpha1.room303.GetUnreadStatsResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/room303/room303api/getunreadstats:\x01*\x12\xb5\x01\n\x0fMarkMessageRead\x12,.api.v1alpha1.room303.MarkMessageReadRequest\x1a-.api.v1alpha1.room303.MarkMessageReadResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/room303/room303api/markmessageread:\x01*\x12\xc5\x01\n\x13MarkAllMessagesRead\x12\x30.api.v1alpha1.room303.MarkAllMessagesReadRequest\x1a\x31.api.v1alpha1.room303.MarkAllMessagesReadResponse\"I\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/room303/room303api/markallmessagesread:\x01*\x12\xc5\x01\n\x13\x42ulkMarkMessageRead\x12\x30.api.v1alpha1.room303.BulkMarkMessageReadRequest\x1a\x31.api.v1alpha1.room303.BulkMarkMessageReadResponse\"I\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/room303/room303api/bulkmarkmessageread:\x01*\x12\x8a\x01\n\nCreateRoom\x12\'.api.v1alpha1.room303.CreateRoomRequest\x1a\x11.api.commons.Room\"@\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/room303/room303api/createroom:\x01*\x12\x81\x01\n\x07GetRoom\x12$.api.v1alpha1.room303.GetRoomRequest\x1a\x11.api.commons.Room\"=\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/room303/room303api/getroom:\x01*\x12\xa6\x01\n\x0cListAllRooms\x12).api.v1alpha1.room303.ListAllRoomsRequest\x1a\'.api.v1alpha1.room303.ListRoomsResponse\"B\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/room303/room303api/listallrooms:\x01*\x12\xb8\x01\n\x12ListRoomsForMember\x12/.api.v1alpha1.room303.ListRoomsForMemberRequest\x1a\'.api.v1alpha1.room303.ListRoomsResponse\"H\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x38\"3/api/v1alpha1/room303/room303api/listroomsformember:\x01*\x12\x89\x01\n\x0b\x41rchiveRoom\x12(.api.v1alpha1.room303.ArchiveRoomRequest\x1a\x11.api.commons.Room\"=\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/room303/room303api/archive:\x01*\x12\xb3\x01\n\x0eListUsersNames\x12+.api.v1alpha1.room303.ListUsersNamesRequest\x1a,.api.v1alpha1.room303.ListUsersNamesResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/room303/room303api/listusersnames:\x01*0\x01\x12\x9c\x01\n\x10UpdateRoomConfig\x12-.api.v1alpha1.room303.UpdateRoomConfigRequest\x1a\x11.api.commons.Room\"F\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x36\"1/api/v1alpha1/room303/room303api/updateroomconfig:\x01*\x12\xc1\x01\n\x12UpdateGlobalConfig\x12/.api.v1alpha1.room303.UpdateGlobalConfigRequest\x1a\x30.api.v1alpha1.room303.UpdateGlobalConfigResponse\"H\xba\xb8\x91\x02\x05\n\x03\x08\xbe\x05\x82\xd3\xe4\x93\x02\x38\"3/api/v1alpha1/room303/room303api/updateglobalconfig:\x01*\x12\xb5\x01\n\x0fGetGlobalConfig\x12,.api.v1alpha1.room303.GetGlobalConfigRequest\x1a-.api.v1alpha1.room303.GetGlobalConfigResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/room303/room303api/getglobalconfig:\x01*\x12\x8a\x01\n\nUpdateRoom\x12\'.api.v1alpha1.room303.UpdateRoomRequest\x1a\x11.api.commons.Room\"@\xba\xb8\x91\x02\x05\n\x03\x08\xbc\x05\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/room303/room303api/updateroom:\x01*B\x9a\x01\n\x18\x63om.api.v1alpha1.room303B\x0cServiceProtoP\x01\xa2\x02\x03\x41VR\xaa\x02\x14\x41pi.V1alpha1.Room303\xca\x02\x14\x41pi\\V1alpha1\\Room303\xe2\x02 Api\\V1alpha1\\Room303\\GPBMetadata\xea\x02\x16\x41pi::V1alpha1::Room303b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.room303.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.api.v1alpha1.room303B\014ServiceProtoP\001\242\002\003AVR\252\002\024Api.V1alpha1.Room303\312\002\024Api\\V1alpha1\\Room303\342\002 Api\\V1alpha1\\Room303\\GPBMetadata\352\002\026Api::V1alpha1::Room303'
  _globals['_ROOM303API'].methods_by_name['AddRoomMember']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['AddRoomMember']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0023\"./api/v1alpha1/room303/room303api/addroommember:\001*'
  _globals['_ROOM303API'].methods_by_name['RemoveRoomMember']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['RemoveRoomMember']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0026\"1/api/v1alpha1/room303/room303api/removeroommember:\001*'
  _globals['_ROOM303API'].methods_by_name['ListRoomMembers']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['ListRoomMembers']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0025\"0/api/v1alpha1/room303/room303api/listroommembers:\001*'
  _globals['_ROOM303API'].methods_by_name['SetAdminForRoomMember']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['SetAdminForRoomMember']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\002;\"6/api/v1alpha1/room303/room303api/setadminforroommember:\001*'
  _globals['_ROOM303API'].methods_by_name['JoinRoom']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['JoinRoom']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\002.\")/api/v1alpha1/room303/room303api/joinroom:\001*'
  _globals['_ROOM303API'].methods_by_name['GetRoomMember']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['GetRoomMember']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0023\"./api/v1alpha1/room303/room303api/getroommember:\001*'
  _globals['_ROOM303API'].methods_by_name['CreateMessage']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['CreateMessage']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0023\"./api/v1alpha1/room303/room303api/createmessage:\001*'
  _globals['_ROOM303API'].methods_by_name['EditMessage']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['EditMessage']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0021\",/api/v1alpha1/room303/room303api/editmessage:\001*'
  _globals['_ROOM303API'].methods_by_name['DeleteMessage']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['DeleteMessage']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0023\"./api/v1alpha1/room303/room303api/deletemessage:\001*'
  _globals['_ROOM303API'].methods_by_name['GetMessages']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['GetMessages']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0021\",/api/v1alpha1/room303/room303api/getmessages:\001*'
  _globals['_ROOM303API'].methods_by_name['StreamMessageUpdates']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['StreamMessageUpdates']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\002:\"5/api/v1alpha1/room303/room303api/streammessageupdates:\001*'
  _globals['_ROOM303API'].methods_by_name['GetUnreadStats']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['GetUnreadStats']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0024\"//api/v1alpha1/room303/room303api/getunreadstats:\001*'
  _globals['_ROOM303API'].methods_by_name['MarkMessageRead']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['MarkMessageRead']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0025\"0/api/v1alpha1/room303/room303api/markmessageread:\001*'
  _globals['_ROOM303API'].methods_by_name['MarkAllMessagesRead']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['MarkAllMessagesRead']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0029\"4/api/v1alpha1/room303/room303api/markallmessagesread:\001*'
  _globals['_ROOM303API'].methods_by_name['BulkMarkMessageRead']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['BulkMarkMessageRead']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0029\"4/api/v1alpha1/room303/room303api/bulkmarkmessageread:\001*'
  _globals['_ROOM303API'].methods_by_name['CreateRoom']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['CreateRoom']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0020\"+/api/v1alpha1/room303/room303api/createroom:\001*'
  _globals['_ROOM303API'].methods_by_name['GetRoom']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['GetRoom']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\002-\"(/api/v1alpha1/room303/room303api/getroom:\001*'
  _globals['_ROOM303API'].methods_by_name['ListAllRooms']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['ListAllRooms']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0022\"-/api/v1alpha1/room303/room303api/listallrooms:\001*'
  _globals['_ROOM303API'].methods_by_name['ListRoomsForMember']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['ListRoomsForMember']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0028\"3/api/v1alpha1/room303/room303api/listroomsformember:\001*'
  _globals['_ROOM303API'].methods_by_name['ArchiveRoom']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['ArchiveRoom']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\002-\"(/api/v1alpha1/room303/room303api/archive:\001*'
  _globals['_ROOM303API'].methods_by_name['ListUsersNames']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['ListUsersNames']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0024\"//api/v1alpha1/room303/room303api/listusersnames:\001*'
  _globals['_ROOM303API'].methods_by_name['UpdateRoomConfig']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['UpdateRoomConfig']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0026\"1/api/v1alpha1/room303/room303api/updateroomconfig:\001*'
  _globals['_ROOM303API'].methods_by_name['UpdateGlobalConfig']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['UpdateGlobalConfig']._serialized_options = b'\272\270\221\002\005\n\003\010\276\005\202\323\344\223\0028\"3/api/v1alpha1/room303/room303api/updateglobalconfig:\001*'
  _globals['_ROOM303API'].methods_by_name['GetGlobalConfig']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['GetGlobalConfig']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0025\"0/api/v1alpha1/room303/room303api/getglobalconfig:\001*'
  _globals['_ROOM303API'].methods_by_name['UpdateRoom']._loaded_options = None
  _globals['_ROOM303API'].methods_by_name['UpdateRoom']._serialized_options = b'\272\270\221\002\005\n\003\010\274\005\202\323\344\223\0020\"+/api/v1alpha1/room303/room303api/updateroom:\001*'
  _globals['_ROOM303API']._serialized_start=247
  _globals['_ROOM303API']._serialized_end=4567
# @@protoc_insertion_point(module_scope)
