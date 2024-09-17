# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/org/hunt_groups/v1alpha1/service.proto
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
    'services/org/hunt_groups/v1alpha1/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from services.org.hunt_groups.v1alpha1 import entities_pb2 as services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/services/org/hunt_groups/v1alpha1/service.proto\x12!services.org.hunt_groups.v1alpha1\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x30services/org/hunt_groups/v1alpha1/entities.proto2\xf1\x0b\n\x11HuntGroupsService\x12\xf0\x01\n\x17ListHuntGroupExileLinks\x12\x41.services.org.hunt_groups.v1alpha1.ListHuntGroupExileLinksRequest\x1a\x42.services.org.hunt_groups.v1alpha1.ListHuntGroupExileLinksResponse\"N\xba\xb8\x91\x02\x05\n\x03\x08\xec\x0e\x82\xd3\xe4\x93\x02>\"9/services/org/huntgroups/v1alpha1/listhuntgroupexilelinks:\x01*\x12\xec\x01\n\x16\x43opyHuntGroupExileLink\x12@.services.org.hunt_groups.v1alpha1.CopyHuntGroupExileLinkRequest\x1a\x41.services.org.hunt_groups.v1alpha1.CopyHuntGroupExileLinkResponse\"M\xba\xb8\x91\x02\x05\n\x03\x08\xed\x0e\x82\xd3\xe4\x93\x02=\"8/services/org/huntgroups/v1alpha1/copyhuntgroupexilelink:\x01*\x12\xf8\x01\n\x19UpdateHuntGroupExileLinks\x12\x43.services.org.hunt_groups.v1alpha1.UpdateHuntGroupExileLinksRequest\x1a\x44.services.org.hunt_groups.v1alpha1.UpdateHuntGroupExileLinksResponse\"P\xba\xb8\x91\x02\x05\n\x03\x08\xed\x0e\x82\xd3\xe4\x93\x02@\";/services/org/huntgroups/v1alpha1/updatehuntgroupexilelinks:\x01*\x12\xfc\x01\n\x1aListHuntGroupAgentTriggers\x12\x44.services.org.hunt_groups.v1alpha1.ListHuntGroupAgentTriggersRequest\x1a\x45.services.org.hunt_groups.v1alpha1.ListHuntGroupAgentTriggersResponse\"Q\xba\xb8\x91\x02\x05\n\x03\x08\xec\x0e\x82\xd3\xe4\x93\x02\x41\"</services/org/huntgroups/v1alpha1/listhuntgroupagenttriggers:\x01*\x12\xf8\x01\n\x19\x43opyHuntGroupAgentTrigger\x12\x43.services.org.hunt_groups.v1alpha1.CopyHuntGroupAgentTriggerRequest\x1a\x44.services.org.hunt_groups.v1alpha1.CopyHuntGroupAgentTriggerResponse\"P\xba\xb8\x91\x02\x05\n\x03\x08\xed\x0e\x82\xd3\xe4\x93\x02@\";/services/org/huntgroups/v1alpha1/copyhuntgroupagenttrigger:\x01*\x12\x84\x02\n\x1cUpdateHuntGroupAgentTriggers\x12\x46.services.org.hunt_groups.v1alpha1.UpdateHuntGroupAgentTriggersRequest\x1aG.services.org.hunt_groups.v1alpha1.UpdateHuntGroupAgentTriggersResponse\"S\xba\xb8\x91\x02\x05\n\x03\x08\xed\x0e\x82\xd3\xe4\x93\x02\x43\">/services/org/huntgroups/v1alpha1/updatehuntgroupagenttriggers:\x01*B\xd8\x01\n%com.services.org.hunt_groups.v1alpha1B\x0cServiceProtoP\x01\xa2\x02\x03SOH\xaa\x02 Services.Org.HuntGroups.V1alpha1\xca\x02 Services\\Org\\HuntGroups\\V1alpha1\xe2\x02,Services\\Org\\HuntGroups\\V1alpha1\\GPBMetadata\xea\x02#Services::Org::HuntGroups::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.org.hunt_groups.v1alpha1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%com.services.org.hunt_groups.v1alpha1B\014ServiceProtoP\001\242\002\003SOH\252\002 Services.Org.HuntGroups.V1alpha1\312\002 Services\\Org\\HuntGroups\\V1alpha1\342\002,Services\\Org\\HuntGroups\\V1alpha1\\GPBMetadata\352\002#Services::Org::HuntGroups::V1alpha1'
  _globals['_HUNTGROUPSSERVICE'].methods_by_name['ListHuntGroupExileLinks']._loaded_options = None
  _globals['_HUNTGROUPSSERVICE'].methods_by_name['ListHuntGroupExileLinks']._serialized_options = b'\272\270\221\002\005\n\003\010\354\016\202\323\344\223\002>\"9/services/org/huntgroups/v1alpha1/listhuntgroupexilelinks:\001*'
  _globals['_HUNTGROUPSSERVICE'].methods_by_name['CopyHuntGroupExileLink']._loaded_options = None
  _globals['_HUNTGROUPSSERVICE'].methods_by_name['CopyHuntGroupExileLink']._serialized_options = b'\272\270\221\002\005\n\003\010\355\016\202\323\344\223\002=\"8/services/org/huntgroups/v1alpha1/copyhuntgroupexilelink:\001*'
  _globals['_HUNTGROUPSSERVICE'].methods_by_name['UpdateHuntGroupExileLinks']._loaded_options = None
  _globals['_HUNTGROUPSSERVICE'].methods_by_name['UpdateHuntGroupExileLinks']._serialized_options = b'\272\270\221\002\005\n\003\010\355\016\202\323\344\223\002@\";/services/org/huntgroups/v1alpha1/updatehuntgroupexilelinks:\001*'
  _globals['_HUNTGROUPSSERVICE'].methods_by_name['ListHuntGroupAgentTriggers']._loaded_options = None
  _globals['_HUNTGROUPSSERVICE'].methods_by_name['ListHuntGroupAgentTriggers']._serialized_options = b'\272\270\221\002\005\n\003\010\354\016\202\323\344\223\002A\"</services/org/huntgroups/v1alpha1/listhuntgroupagenttriggers:\001*'
  _globals['_HUNTGROUPSSERVICE'].methods_by_name['CopyHuntGroupAgentTrigger']._loaded_options = None
  _globals['_HUNTGROUPSSERVICE'].methods_by_name['CopyHuntGroupAgentTrigger']._serialized_options = b'\272\270\221\002\005\n\003\010\355\016\202\323\344\223\002@\";/services/org/huntgroups/v1alpha1/copyhuntgroupagenttrigger:\001*'
  _globals['_HUNTGROUPSSERVICE'].methods_by_name['UpdateHuntGroupAgentTriggers']._loaded_options = None
  _globals['_HUNTGROUPSSERVICE'].methods_by_name['UpdateHuntGroupAgentTriggers']._serialized_options = b'\272\270\221\002\005\n\003\010\355\016\202\323\344\223\002C\">/services/org/huntgroups/v1alpha1/updatehuntgroupagenttriggers:\001*'
  _globals['_HUNTGROUPSSERVICE']._serialized_start=192
  _globals['_HUNTGROUPSSERVICE']._serialized_end=1713
# @@protoc_insertion_point(module_scope)
