# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/contactmanager.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'api/commons/contactmanager.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n api/commons/contactmanager.proto\x12\x0b\x61pi.commons\x1a\x1fgoogle/protobuf/timestamp.proto\"\x97\x02\n\x13\x43ontactManagerEntry\x12;\n\x18\x63ontact_manager_entry_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x15\x63ontactManagerEntryId\x12\x44\n\x1d\x63ontact_manager_entry_list_id\x18\x02 \x01(\x03\x42\x02\x30\x01R\x19\x63ontactManagerEntryListId\x12\x10\n\x03key\x18\x03 \x01(\tR\x03key\x12\x14\n\x05value\x18\x04 \x01(\tR\x05value\x12\x12\n\x04type\x18\x05 \x01(\tR\x04type\x12=\n\x0c\x64\x61te_created\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64\x61teCreated:\x02\x18\x01\"\xc4\x02\n\x12\x43ontactManagerList\x12\x39\n\x17\x63ontact_manager_list_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x14\x63ontactManagerListId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12!\n\nproject_id\x18\x03 \x01(\x03\x42\x02\x30\x01R\tprojectId\x12\x1b\n\tfile_name\x18\x04 \x01(\tR\x08\x66ileName\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12!\n\x0clist_details\x18\x06 \x03(\tR\x0blistDetails\x12\x14\n\x03ttl\x18\x07 \x01(\x03\x42\x02\x30\x01R\x03ttl\x12=\n\x0c\x64\x61te_created\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64\x61teCreated:\x02\x18\x01\"F\n\x16\x43ontactManagerEntryVal\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x18\x01*O\n\x1a\x44\x65\x44uplicationMergeStrategy\x12\x16\n\x12KEEP_EXISTING_LIST\x10\x00\x12\x19\n\x15REPLACE_EXISTING_LIST\x10\x01*0\n\x11\x43ontactListStatus\x12\x1b\n\x17\x43ONTACT_LIST_STATUS_NEW\x10\x00*\xb4\x01\n\x12\x43ontactEntryStatus\x12\x1c\n\x18\x43ONTACT_ENTRY_STATUS_NEW\x10\x00\x12\x1e\n\x1a\x43ONTACT_ENTRY_STATUS_INUSE\x10\x01\x12\x1f\n\x1b\x43ONTACT_ENTRY_STATUS_NOTREF\x10\x02\x12\x1d\n\x19\x43ONTACT_ENTRY_STATUS_DONE\x10\x03\x12 \n\x1c\x43ONTACT_ENTRY_STATUS_EXPIRED\x10\x04\x42s\n\x0f\x63om.api.commonsB\x13\x43ontactmanagerProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.contactmanager_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\023ContactmanagerProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_CONTACTMANAGERENTRY'].fields_by_name['contact_manager_entry_id']._loaded_options = None
  _globals['_CONTACTMANAGERENTRY'].fields_by_name['contact_manager_entry_id']._serialized_options = b'0\001'
  _globals['_CONTACTMANAGERENTRY'].fields_by_name['contact_manager_entry_list_id']._loaded_options = None
  _globals['_CONTACTMANAGERENTRY'].fields_by_name['contact_manager_entry_list_id']._serialized_options = b'0\001'
  _globals['_CONTACTMANAGERENTRY']._loaded_options = None
  _globals['_CONTACTMANAGERENTRY']._serialized_options = b'\030\001'
  _globals['_CONTACTMANAGERLIST'].fields_by_name['contact_manager_list_id']._loaded_options = None
  _globals['_CONTACTMANAGERLIST'].fields_by_name['contact_manager_list_id']._serialized_options = b'0\001'
  _globals['_CONTACTMANAGERLIST'].fields_by_name['project_id']._loaded_options = None
  _globals['_CONTACTMANAGERLIST'].fields_by_name['project_id']._serialized_options = b'0\001'
  _globals['_CONTACTMANAGERLIST'].fields_by_name['ttl']._loaded_options = None
  _globals['_CONTACTMANAGERLIST'].fields_by_name['ttl']._serialized_options = b'0\001'
  _globals['_CONTACTMANAGERLIST']._loaded_options = None
  _globals['_CONTACTMANAGERLIST']._serialized_options = b'\030\001'
  _globals['_CONTACTMANAGERENTRYVAL']._loaded_options = None
  _globals['_CONTACTMANAGERENTRYVAL']._serialized_options = b'\030\001'
  _globals['_DEDUPLICATIONMERGESTRATEGY']._serialized_start=763
  _globals['_DEDUPLICATIONMERGESTRATEGY']._serialized_end=842
  _globals['_CONTACTLISTSTATUS']._serialized_start=844
  _globals['_CONTACTLISTSTATUS']._serialized_end=892
  _globals['_CONTACTENTRYSTATUS']._serialized_start=895
  _globals['_CONTACTENTRYSTATUS']._serialized_end=1075
  _globals['_CONTACTMANAGERENTRY']._serialized_start=83
  _globals['_CONTACTMANAGERENTRY']._serialized_end=362
  _globals['_CONTACTMANAGERLIST']._serialized_start=365
  _globals['_CONTACTMANAGERLIST']._serialized_end=689
  _globals['_CONTACTMANAGERENTRYVAL']._serialized_start=691
  _globals['_CONTACTMANAGERENTRYVAL']._serialized_end=761
# @@protoc_insertion_point(module_scope)
