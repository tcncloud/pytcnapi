# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/audit/contactmanager_events.proto
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
    'api/commons/audit/contactmanager_events.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v1alpha1.contactmanager import contactmanager_pb2 as api_dot_v1alpha1_dot_contactmanager_dot_contactmanager__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-api/commons/audit/contactmanager_events.proto\x12\x11\x61pi.commons.audit\x1a\x30\x61pi/v1alpha1/contactmanager/contactmanager.proto\"f\n\x1b\x43ontactManagerEntryAddEvent\x12G\n\x08\x61\x64\x64\x45vent\x18\x01 \x01(\x0b\x32+.api.commons.audit.ContactManagerEntryEventR\x08\x61\x64\x64\x45vent\"k\n\x1e\x43ontactManagerEntryGetEncEvent\x12I\n\tviewEvent\x18\x01 \x01(\x0b\x32+.api.commons.audit.ContactManagerEntryEventR\tviewEvent\"i\n\x1c\x43ontactManagerEntryEditEvent\x12I\n\teditEvent\x18\x01 \x01(\x0b\x32+.api.commons.audit.ContactManagerEntryEventR\teditEvent\"\x1b\n\x19\x43ontactManagerDeleteEvent\"\xc4\x01\n\x18\x43ontactManagerEntryEvent\x12\x32\n\x14\x43ontactManagerListId\x18\x01 \x01(\x03R\x14\x43ontactManagerListId\x12\x34\n\x15\x43ontactManagerEntryId\x18\x02 \x01(\x03R\x15\x43ontactManagerEntryId\x12>\n\x1a\x43ontactManagerEntryListIds\x18\x03 \x03(\x03R\x1a\x43ontactManagerEntryListIds\"\x97\x02\n\x1d\x43ontactManagerListUploadEvent\x12\x32\n\x14\x43ontactManagerListId\x18\x01 \x01(\x03R\x14\x43ontactManagerListId\x12:\n\x18NumberOfContactsUploaded\x18\x02 \x01(\x03R\x18NumberOfContactsUploaded\x12N\n\"NumberOfSuccessfulContactsUploaded\x18\x03 \x01(\x03R\"NumberOfSuccessfulContactsUploaded\x12\x36\n\x16NumberOfFailedContacts\x18\x04 \x01(\x03R\x16NumberOfFailedContacts\"\xd8\x01\n\x16\x43ontactManagerKycEvent\x12\x32\n\x14\x43ontactManagerListId\x18\x01 \x01(\x03R\x14\x43ontactManagerListId\x12\x34\n\x15\x43ontactManagerEntryId\x18\x02 \x01(\x03R\x15\x43ontactManagerEntryId\x12\x14\n\x05types\x18\x03 \x03(\tR\x05types\x12>\n\x1a\x43ontactManagerEntryListIds\x18\x04 \x03(\x03R\x1a\x43ontactManagerEntryListIdsB\x98\x01\n\x15\x63om.api.commons.auditB\x19\x43ontactmanagerEventsProtoP\x01\xa2\x02\x03\x41\x43\x41\xaa\x02\x11\x41pi.Commons.Audit\xca\x02\x11\x41pi\\Commons\\Audit\xe2\x02\x1d\x41pi\\Commons\\Audit\\GPBMetadata\xea\x02\x13\x41pi::Commons::Auditb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.audit.contactmanager_events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.api.commons.auditB\031ContactmanagerEventsProtoP\001\242\002\003ACA\252\002\021Api.Commons.Audit\312\002\021Api\\Commons\\Audit\342\002\035Api\\Commons\\Audit\\GPBMetadata\352\002\023Api::Commons::Audit'
  _globals['_CONTACTMANAGERENTRYADDEVENT']._serialized_start=118
  _globals['_CONTACTMANAGERENTRYADDEVENT']._serialized_end=220
  _globals['_CONTACTMANAGERENTRYGETENCEVENT']._serialized_start=222
  _globals['_CONTACTMANAGERENTRYGETENCEVENT']._serialized_end=329
  _globals['_CONTACTMANAGERENTRYEDITEVENT']._serialized_start=331
  _globals['_CONTACTMANAGERENTRYEDITEVENT']._serialized_end=436
  _globals['_CONTACTMANAGERDELETEEVENT']._serialized_start=438
  _globals['_CONTACTMANAGERDELETEEVENT']._serialized_end=465
  _globals['_CONTACTMANAGERENTRYEVENT']._serialized_start=468
  _globals['_CONTACTMANAGERENTRYEVENT']._serialized_end=664
  _globals['_CONTACTMANAGERLISTUPLOADEVENT']._serialized_start=667
  _globals['_CONTACTMANAGERLISTUPLOADEVENT']._serialized_end=946
  _globals['_CONTACTMANAGERKYCEVENT']._serialized_start=949
  _globals['_CONTACTMANAGERKYCEVENT']._serialized_end=1165
# @@protoc_insertion_point(module_scope)
