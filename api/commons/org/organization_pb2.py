# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/org/organization.proto
# Protobuf Python Version: 5.29.3
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
    3,
    '',
    'api/commons/org/organization.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import org_pb2 as api_dot_commons_dot_org__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/commons/org/organization.proto\x12\x0f\x61pi.commons.org\x1a\x15\x61pi/commons/org.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9c\x05\n\x0cOrganization\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12Z\n\x0f\x65nabled_regions\x18\x02 \x03(\x0b\x32\x31.api.commons.org.Organization.EnabledRegionsEntryR\x0e\x65nabledRegions\x12\x1b\n\tregion_id\x18\x03 \x01(\tR\x08regionId\x12\x1d\n\nbilling_id\x18\x04 \x01(\tR\tbillingId\x12\x1d\n\nclient_sid\x18\x05 \x01(\x03R\tclientSid\x12\x12\n\x04name\x18\x06 \x01(\tR\x04name\x12\x35\n\x08\x61\x64\x64_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x61\x64\x64\x44\x61te\x12\x33\n\x16is_manual_only_account\x18\x08 \x01(\x08R\x13isManualOnlyAccount\x12\x42\n\x10\x62\x61\x63koffice_theme\x18\t \x01(\x0e\x32\x17.api.commons.ClientSkinR\x0f\x62\x61\x63kofficeTheme\x12\x1a\n\x08\x61rchived\x18\n \x01(\x08R\x08\x61rchived\x12\x15\n\x06\x63rm_id\x18\x0b \x01(\tR\x05\x63rmId\x12\x32\n\ttime_zone\x18\x0c \x01(\x0e\x32\x15.api.commons.TimeZoneR\x08timeZone\x12\x30\n\x14\x63\x61llbacks_service_id\x18\r \x01(\tR\x12\x63\x61llbacksServiceId\x12\x1e\n\x0bp3_owner_id\x18\x0e \x01(\tR\tp3OwnerId\x1a\x41\n\x13\x45nabledRegionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value:\x02\x38\x01\"\xa4\x01\n\x13OrganizationDetails\x12\x41\n\x0corganization\x18\x01 \x01(\x0b\x32\x1d.api.commons.org.OrganizationR\x0corganization\x12J\n\x13last_scheduled_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x11lastScheduledDateB\x86\x01\n\x13\x63om.api.commons.orgB\x11OrganizationProtoP\x01\xa2\x02\x03\x41\x43O\xaa\x02\x0f\x41pi.Commons.Org\xca\x02\x0f\x41pi\\Commons\\Org\xe2\x02\x1b\x41pi\\Commons\\Org\\GPBMetadata\xea\x02\x11\x41pi::Commons::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.org.organization_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.api.commons.orgB\021OrganizationProtoP\001\242\002\003ACO\252\002\017Api.Commons.Org\312\002\017Api\\Commons\\Org\342\002\033Api\\Commons\\Org\\GPBMetadata\352\002\021Api::Commons::Org'
  _globals['_ORGANIZATION_ENABLEDREGIONSENTRY']._loaded_options = None
  _globals['_ORGANIZATION_ENABLEDREGIONSENTRY']._serialized_options = b'8\001'
  _globals['_ORGANIZATION']._serialized_start=112
  _globals['_ORGANIZATION']._serialized_end=780
  _globals['_ORGANIZATION_ENABLEDREGIONSENTRY']._serialized_start=715
  _globals['_ORGANIZATION_ENABLEDREGIONSENTRY']._serialized_end=780
  _globals['_ORGANIZATIONDETAILS']._serialized_start=783
  _globals['_ORGANIZATIONDETAILS']._serialized_end=947
# @@protoc_insertion_point(module_scope)
