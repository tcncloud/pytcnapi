# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/audit/contactmanager_events.proto
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
    'api/commons/audit/contactmanager_events.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import classifier_pb2 as api_dot_commons_dot_classifier__pb2
from api.commons import contactmanager_pb2 as api_dot_commons_dot_contactmanager__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-api/commons/audit/contactmanager_events.proto\x12\x11\x61pi.commons.audit\x1a\x1c\x61pi/commons/classifier.proto\x1a api/commons/contactmanager.proto\"f\n\x1b\x43ontactManagerEntryAddEvent\x12G\n\x08\x61\x64\x64\x45vent\x18\x01 \x01(\x0b\x32+.api.commons.audit.ContactManagerEntryEventR\x08\x61\x64\x64\x45vent\"k\n\x1e\x43ontactManagerEntryGetEncEvent\x12I\n\tviewEvent\x18\x01 \x01(\x0b\x32+.api.commons.audit.ContactManagerEntryEventR\tviewEvent\"i\n\x1c\x43ontactManagerEntryEditEvent\x12I\n\teditEvent\x18\x01 \x01(\x0b\x32+.api.commons.audit.ContactManagerEntryEventR\teditEvent\"j\n\x19\x43ontactManagerDeleteEvent\x12M\n\x0b\x64\x65leteEvent\x18\x01 \x01(\x0b\x32+.api.commons.audit.ContactManagerEntryEventR\x0b\x64\x65leteEvent\"\xeb\x02\n\x18\x43ontactManagerEntryEvent\x12\x36\n\x14\x43ontactManagerListId\x18\x01 \x01(\x03\x42\x02\x18\x01R\x14\x43ontactManagerListId\x12\x34\n\x15\x43ontactManagerEntryId\x18\x02 \x01(\x03R\x15\x43ontactManagerEntryId\x12\x42\n\x1a\x43ontactManagerEntryListIds\x18\x03 \x03(\x03\x42\x02\x18\x01R\x1a\x43ontactManagerEntryListIds\x12J\n\x0c\x46ieldChanges\x18\x04 \x03(\x0b\x32&.api.commons.audit.ContactFieldChangesR\x0c\x46ieldChanges\x12\x39\n\x13\x43ontactUpdateTaskId\x18\x05 \x01(\x03\x42\x02\x30\x01H\x00R\x13\x43ontactUpdateTaskId\x88\x01\x01\x42\x16\n\x14_ContactUpdateTaskId\"\x9f\x01\n\x13\x43ontactFieldChanges\x12\x45\n\nfrom_value\x18\x01 \x01(\x0b\x32&.api.commons.audit.AuditedContactFieldR\tfromValue\x12\x41\n\x08to_value\x18\x02 \x01(\x0b\x32&.api.commons.audit.AuditedContactFieldR\x07toValue\"\x8c\x01\n\x13\x41uditedContactField\x12(\n\x10\x63ontact_field_id\x18\x01 \x01(\x03R\x0e\x63ontactFieldId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type\x12\x19\n\x05value\x18\x04 \x01(\tH\x00R\x05value\x88\x01\x01\x42\x08\n\x06_value\"\xc7\x05\n\x1d\x43ontactManagerListUploadEvent\x12\x32\n\x14\x43ontactManagerListId\x18\x01 \x01(\x03R\x14\x43ontactManagerListId\x12:\n\x18NumberOfContactsUploaded\x18\x02 \x01(\x03R\x18NumberOfContactsUploaded\x12N\n\"NumberOfSuccessfulContactsUploaded\x18\x03 \x01(\x03R\"NumberOfSuccessfulContactsUploaded\x12\x36\n\x16NumberOfFailedContacts\x18\x04 \x01(\x03R\x16NumberOfFailedContacts\x12\x30\n\x13NumberOfNewContacts\x18\x05 \x01(\x03R\x13NumberOfNewContacts\x12<\n\x19NumberOfDuplicateContacts\x18\x06 \x01(\x03R\x19NumberOfDuplicateContacts\x12I\n\x0e\x44\x65\x44upFieldType\x18\x07 \x01(\x0e\x32!.api.commons.ClassifierEntityTypeR\x0e\x44\x65\x44upFieldType\x12W\n\x12\x44\x65\x44upMergeStrategy\x18\x08 \x01(\x0e\x32\'.api.commons.DeDuplicationMergeStrategyR\x12\x44\x65\x44upMergeStrategy\x12\x36\n\x16\x43ontactManagerListName\x18\t \x01(\tR\x16\x43ontactManagerListName\x12\x1f\n\x08\x46ileName\x18\n \x01(\tH\x00R\x08\x46ileName\x88\x01\x01\x12\"\n\x0cUpdateTaskId\x18\x0b \x01(\x03R\x0cUpdateTaskId\x12\x10\n\x03Ttl\x18\x0c \x01(\x03R\x03TtlB\x0b\n\t_FileName\"\xd8\x01\n\x16\x43ontactManagerKycEvent\x12\x32\n\x14\x43ontactManagerListId\x18\x01 \x01(\x03R\x14\x43ontactManagerListId\x12\x34\n\x15\x43ontactManagerEntryId\x18\x02 \x01(\x03R\x15\x43ontactManagerEntryId\x12\x14\n\x05types\x18\x03 \x03(\tR\x05types\x12>\n\x1a\x43ontactManagerEntryListIds\x18\x04 \x03(\x03R\x1a\x43ontactManagerEntryListIds\"\xb3\x01\n$ContactManagerEntityAssociationEvent\x12\x37\n\x18\x63ontact_manager_entry_id\x18\x01 \x01(\x03R\x15\x63ontactManagerEntryId\x12\x1b\n\tentity_id\x18\x02 \x01(\tR\x08\x65ntityId\x12\x18\n\x07\x64\x65leted\x18\x03 \x01(\x08R\x07\x64\x65leted\x12\x1b\n\tis_active\x18\x04 \x01(\x08R\x08isActiveB\x98\x01\n\x15\x63om.api.commons.auditB\x19\x43ontactmanagerEventsProtoP\x01\xa2\x02\x03\x41\x43\x41\xaa\x02\x11\x41pi.Commons.Audit\xca\x02\x11\x41pi\\Commons\\Audit\xe2\x02\x1d\x41pi\\Commons\\Audit\\GPBMetadata\xea\x02\x13\x41pi::Commons::Auditb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.audit.contactmanager_events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.api.commons.auditB\031ContactmanagerEventsProtoP\001\242\002\003ACA\252\002\021Api.Commons.Audit\312\002\021Api\\Commons\\Audit\342\002\035Api\\Commons\\Audit\\GPBMetadata\352\002\023Api::Commons::Audit'
  _globals['_CONTACTMANAGERENTRYEVENT'].fields_by_name['ContactManagerListId']._loaded_options = None
  _globals['_CONTACTMANAGERENTRYEVENT'].fields_by_name['ContactManagerListId']._serialized_options = b'\030\001'
  _globals['_CONTACTMANAGERENTRYEVENT'].fields_by_name['ContactManagerEntryListIds']._loaded_options = None
  _globals['_CONTACTMANAGERENTRYEVENT'].fields_by_name['ContactManagerEntryListIds']._serialized_options = b'\030\001'
  _globals['_CONTACTMANAGERENTRYEVENT'].fields_by_name['ContactUpdateTaskId']._loaded_options = None
  _globals['_CONTACTMANAGERENTRYEVENT'].fields_by_name['ContactUpdateTaskId']._serialized_options = b'0\001'
  _globals['_CONTACTMANAGERENTRYADDEVENT']._serialized_start=132
  _globals['_CONTACTMANAGERENTRYADDEVENT']._serialized_end=234
  _globals['_CONTACTMANAGERENTRYGETENCEVENT']._serialized_start=236
  _globals['_CONTACTMANAGERENTRYGETENCEVENT']._serialized_end=343
  _globals['_CONTACTMANAGERENTRYEDITEVENT']._serialized_start=345
  _globals['_CONTACTMANAGERENTRYEDITEVENT']._serialized_end=450
  _globals['_CONTACTMANAGERDELETEEVENT']._serialized_start=452
  _globals['_CONTACTMANAGERDELETEEVENT']._serialized_end=558
  _globals['_CONTACTMANAGERENTRYEVENT']._serialized_start=561
  _globals['_CONTACTMANAGERENTRYEVENT']._serialized_end=924
  _globals['_CONTACTFIELDCHANGES']._serialized_start=927
  _globals['_CONTACTFIELDCHANGES']._serialized_end=1086
  _globals['_AUDITEDCONTACTFIELD']._serialized_start=1089
  _globals['_AUDITEDCONTACTFIELD']._serialized_end=1229
  _globals['_CONTACTMANAGERLISTUPLOADEVENT']._serialized_start=1232
  _globals['_CONTACTMANAGERLISTUPLOADEVENT']._serialized_end=1943
  _globals['_CONTACTMANAGERKYCEVENT']._serialized_start=1946
  _globals['_CONTACTMANAGERKYCEVENT']._serialized_end=2162
  _globals['_CONTACTMANAGERENTITYASSOCIATIONEVENT']._serialized_start=2165
  _globals['_CONTACTMANAGERENTITYASSOCIATIONEVENT']._serialized_end=2344
# @@protoc_insertion_point(module_scope)
