# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/org/hunt_groups/v1alpha1/entities.proto
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
    'services/org/hunt_groups/v1alpha1/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.org import huntgroup_pb2 as api_dot_commons_dot_org_dot_huntgroup__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0services/org/hunt_groups/v1alpha1/entities.proto\x12!services.org.hunt_groups.v1alpha1\x1a\x1f\x61pi/commons/org/huntgroup.proto\"\xce\x02\n\tExileLink\x12#\n\rparameter_sid\x18\x01 \x01(\x03R\x0cparameterSid\x12$\n\x0ehunt_group_sid\x18\x02 \x01(\x03R\x0chuntGroupSid\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x14\n\x05order\x18\x05 \x01(\x03R\x05order\x12S\n\x0cinbound_data\x18\x06 \x01(\x0b\x32\x30.services.org.hunt_groups.v1alpha1.ExileLinkDataR\x0binboundData\x12U\n\routbound_data\x18\x07 \x01(\x0b\x32\x30.services.org.hunt_groups.v1alpha1.ExileLinkDataR\x0coutboundData\"\xbd\x01\n\rExileLinkData\x12R\n\trecord_id\x18\x01 \x01(\x0b\x32\x35.services.org.hunt_groups.v1alpha1.ExileLinkParameterR\x08recordId\x12X\n\x0c\x61lternate_id\x18\x02 \x01(\x0b\x32\x35.services.org.hunt_groups.v1alpha1.ExileLinkParameterR\x0b\x61lternateId\"\xbd\x01\n\x12\x45xileLinkParameter\x12*\n\x11\x63ontact_field_sid\x18\x01 \x01(\x03R\x0f\x63ontactFieldSid\x12!\n\x0chelper_value\x18\x02 \x01(\tR\x0bhelperValue\x12X\n\x15parameter_source_type\x18\x03 \x01(\x0e\x32$.api.commons.org.ParameterSourceTypeR\x13parameterSourceType\"F\n\x1eListHuntGroupExileLinksRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\"p\n\x1fListHuntGroupExileLinksResponse\x12M\n\x0b\x65xile_links\x18\x01 \x03(\x0b\x32,.services.org.hunt_groups.v1alpha1.ExileLinkR\nexileLinksB\xd9\x01\n%com.services.org.hunt_groups.v1alpha1B\rEntitiesProtoP\x01\xa2\x02\x03SOH\xaa\x02 Services.Org.HuntGroups.V1alpha1\xca\x02 Services\\Org\\HuntGroups\\V1alpha1\xe2\x02,Services\\Org\\HuntGroups\\V1alpha1\\GPBMetadata\xea\x02#Services::Org::HuntGroups::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.org.hunt_groups.v1alpha1.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%com.services.org.hunt_groups.v1alpha1B\rEntitiesProtoP\001\242\002\003SOH\252\002 Services.Org.HuntGroups.V1alpha1\312\002 Services\\Org\\HuntGroups\\V1alpha1\342\002,Services\\Org\\HuntGroups\\V1alpha1\\GPBMetadata\352\002#Services::Org::HuntGroups::V1alpha1'
  _globals['_EXILELINK']._serialized_start=121
  _globals['_EXILELINK']._serialized_end=455
  _globals['_EXILELINKDATA']._serialized_start=458
  _globals['_EXILELINKDATA']._serialized_end=647
  _globals['_EXILELINKPARAMETER']._serialized_start=650
  _globals['_EXILELINKPARAMETER']._serialized_end=839
  _globals['_LISTHUNTGROUPEXILELINKSREQUEST']._serialized_start=841
  _globals['_LISTHUNTGROUPEXILELINKSREQUEST']._serialized_end=911
  _globals['_LISTHUNTGROUPEXILELINKSRESPONSE']._serialized_start=913
  _globals['_LISTHUNTGROUPEXILELINKSRESPONSE']._serialized_end=1025
# @@protoc_insertion_point(module_scope)
