# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/org/skill_group.proto
# Protobuf Python Version: 5.27.0
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
    0,
    '',
    'api/commons/org/skill_group.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!api/commons/org/skill_group.proto\x12\x0f\x61pi.commons.org\"\xb9\x01\n\nSkillGroup\x12$\n\x0eskill_group_id\x18\x01 \x01(\tR\x0cskillGroupId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x38\n\nskill_sets\x18\x05 \x03(\x0b\x32\x19.api.commons.org.SkillSetR\tskillSets\"I\n\x08SkillSet\x12 \n\x0bproficiency\x18\x02 \x01(\x05R\x0bproficiency\x12\x1b\n\tskill_sid\x18\x03 \x01(\x03R\x08skillSidB\x84\x01\n\x13\x63om.api.commons.orgB\x0fSkillGroupProtoP\x01\xa2\x02\x03\x41\x43O\xaa\x02\x0f\x41pi.Commons.Org\xca\x02\x0f\x41pi\\Commons\\Org\xe2\x02\x1b\x41pi\\Commons\\Org\\GPBMetadata\xea\x02\x11\x41pi::Commons::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.org.skill_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.api.commons.orgB\017SkillGroupProtoP\001\242\002\003ACO\252\002\017Api.Commons.Org\312\002\017Api\\Commons\\Org\342\002\033Api\\Commons\\Org\\GPBMetadata\352\002\021Api::Commons::Org'
  _globals['_SKILLGROUP']._serialized_start=55
  _globals['_SKILLGROUP']._serialized_end=240
  _globals['_SKILLSET']._serialized_start=242
  _globals['_SKILLSET']._serialized_end=315
# @@protoc_insertion_point(module_scope)
