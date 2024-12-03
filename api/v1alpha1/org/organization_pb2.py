# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/organization.proto
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
    'api/v1alpha1/org/organization.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import country_pb2 as api_dot_commons_dot_country__pb2
from api.commons import org_pb2 as api_dot_commons_dot_org__pb2
from api.commons.org import organization_pb2 as api_dot_commons_dot_org_dot_organization__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/v1alpha1/org/organization.proto\x12\x10\x61pi.v1alpha1.org\x1a\x19\x61pi/commons/country.proto\x1a\x15\x61pi/commons/org.proto\x1a\"api/commons/org/organization.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe2\x02\n\x19\x43reateOrganizationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x15\n\x06\x63rm_id\x18\x02 \x01(\tR\x05\x63rmId\x12\x32\n\ttime_zone\x18\x03 \x01(\x0e\x32\x15.api.commons.TimeZoneR\x08timeZone\x12\x33\n\x16is_manual_only_account\x18\x04 \x01(\x08R\x13isManualOnlyAccount\x12\x42\n\x10\x62\x61\x63koffice_theme\x18\x05 \x01(\x0e\x32\x17.api.commons.ClientSkinR\x0f\x62\x61\x63kofficeTheme\x12\x41\n\x11\x61llowed_countries\x18\x06 \x03(\x0e\x32\x14.api.commons.CountryR\x10\x61llowedCountries\x12*\n\x11p3_parent_account\x18\x07 \x01(\tR\x0fp3ParentAccount\"3\n\x1a\x43reateOrganizationResponse\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\"\x18\n\x16GetOrganizationRequest\"\\\n\x17GetOrganizationResponse\x12\x41\n\x0corganization\x18\x01 \x01(\x0b\x32\x1d.api.commons.org.OrganizationR\x0corganization\"3\n\x1aGetOrganizationByIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\"`\n\x1bGetOrganizationByIdResponse\x12\x41\n\x0corganization\x18\x01 \x01(\x0b\x32\x1d.api.commons.org.OrganizationR\x0corganization\"}\n\x18ListOrganizationsRequest\x12\x18\n\x06global\x18\x01 \x01(\x08H\x00R\x06global\x12\x1d\n\tregion_id\x18\x02 \x01(\tH\x00R\x08regionId\x12\x1a\n\x08\x61rchived\x18\x03 \x01(\x08R\x08\x61rchivedB\x0c\n\nidentifier\"u\n\x19ListOrganizationsResponse\x12X\n\x14organization_details\x18\x01 \x03(\x0b\x32%.api.v1alpha1.org.OrganizationDetailsR\x13organizationDetails\"\xa4\x01\n\x13OrganizationDetails\x12\x41\n\x0corganization\x18\x01 \x01(\x0b\x32\x1d.api.commons.org.OrganizationR\x0corganization\x12J\n\x13last_scheduled_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x11lastScheduledDate\"2\n\x19\x43onvertOrgToManualRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\"\x1c\n\x1a\x43onvertOrgToManualResponse\"\x16\n\x14ListOwnedOrgsRequest\"q\n\x15ListOwnedOrgsResponse\x12X\n\x14organization_details\x18\x01 \x03(\x0b\x32%.api.v1alpha1.org.OrganizationDetailsR\x13organizationDetails\"\xf4\x01\n\x19UpdateOrganizationRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x32\n\ttime_zone\x18\x02 \x01(\x0e\x32\x15.api.commons.TimeZoneR\x08timeZone\x12\x1d\n\nbilling_id\x18\x03 \x01(\tR\tbillingId\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12\x1e\n\x0bp3_owner_id\x18\x05 \x01(\tR\tp3OwnerId\x12\x1a\n\x08\x61rchived\x18\x06 \x01(\x08R\x08\x61rchived\x12\x1d\n\nfield_mask\x18\n \x03(\tR\tfieldMask\"_\n\x1aUpdateOrganizationResponse\x12\x41\n\x0corganization\x18\x01 \x01(\x0b\x32\x1d.api.commons.org.OrganizationR\x0corganization\"3\n\x1a\x41rchiveOrganizationRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\"\x1d\n\x1b\x41rchiveOrganizationResponse\"5\n\x1cUnArchiveOrganizationRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\"\x1f\n\x1dUnArchiveOrganizationResponse\"%\n#ListAllOrganizationsGloballyRequest\"\xe2\x03\n$ListAllOrganizationsGloballyResponse\x12}\n\x14organization_details\x18\x01 \x03(\x0b\x32J.api.v1alpha1.org.ListAllOrganizationsGloballyResponse.OrganizationDetailsR\x13organizationDetails\x1a\xba\x02\n\x13OrganizationDetails\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1d\n\nclient_sid\x18\x03 \x01(\x03R\tclientSid\x12\x1d\n\nbilling_id\x18\x04 \x01(\tR\tbillingId\x12\x1b\n\tregion_id\x18\x05 \x01(\tR\x08regionId\x12\x35\n\x08\x61\x64\x64_date\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x61\x64\x64\x44\x61te\x12J\n\x13last_scheduled_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x11lastScheduledDate\x12\x1a\n\x08\x61rchived\x18\x08 \x01(\x08R\x08\x61rchived\"?\n ListOrganizationsByRegionRequest\x12\x1b\n\tregion_id\x18\x01 \x01(\tR\x08regionId\"\xc0\x03\n!ListOrganizationsByRegionResponse\x12z\n\x14organization_details\x18\x01 \x03(\x0b\x32G.api.v1alpha1.org.ListOrganizationsByRegionResponse.OrganizationDetailsR\x13organizationDetails\x1a\x9e\x02\n\x13OrganizationDetails\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1d\n\nclient_sid\x18\x03 \x01(\x03R\tclientSid\x12\x1d\n\nbilling_id\x18\x04 \x01(\tR\tbillingId\x12\x1b\n\tregion_id\x18\x05 \x01(\tR\x08regionId\x12\x35\n\x08\x61\x64\x64_date\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x61\x64\x64\x44\x61te\x12J\n\x13last_scheduled_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x11lastScheduledDate\"\"\n ListArchivedOrganizationsRequest\"\xc0\x03\n!ListArchivedOrganizationsResponse\x12z\n\x14organization_details\x18\x01 \x03(\x0b\x32G.api.v1alpha1.org.ListArchivedOrganizationsResponse.OrganizationDetailsR\x13organizationDetails\x1a\x9e\x02\n\x13OrganizationDetails\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1d\n\nbilling_id\x18\x03 \x01(\tR\tbillingId\x12\x35\n\x08\x61\x64\x64_date\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x61\x64\x64\x44\x61te\x12J\n\x13last_scheduled_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x11lastScheduledDate\x12\x1d\n\nclient_sid\x18\x06 \x01(\x03R\tclientSid\x12\x1b\n\tregion_id\x18\x07 \x01(\tR\x08regionIdB\x8b\x01\n\x14\x63om.api.v1alpha1.orgB\x11OrganizationProtoP\x01\xa2\x02\x03\x41VO\xaa\x02\x10\x41pi.V1alpha1.Org\xca\x02\x10\x41pi\\V1alpha1\\Org\xe2\x02\x1c\x41pi\\V1alpha1\\Org\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.organization_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.orgB\021OrganizationProtoP\001\242\002\003AVO\252\002\020Api.V1alpha1.Org\312\002\020Api\\V1alpha1\\Org\342\002\034Api\\V1alpha1\\Org\\GPBMetadata\352\002\022Api::V1alpha1::Org'
  _globals['_CREATEORGANIZATIONREQUEST']._serialized_start=177
  _globals['_CREATEORGANIZATIONREQUEST']._serialized_end=531
  _globals['_CREATEORGANIZATIONRESPONSE']._serialized_start=533
  _globals['_CREATEORGANIZATIONRESPONSE']._serialized_end=584
  _globals['_GETORGANIZATIONREQUEST']._serialized_start=586
  _globals['_GETORGANIZATIONREQUEST']._serialized_end=610
  _globals['_GETORGANIZATIONRESPONSE']._serialized_start=612
  _globals['_GETORGANIZATIONRESPONSE']._serialized_end=704
  _globals['_GETORGANIZATIONBYIDREQUEST']._serialized_start=706
  _globals['_GETORGANIZATIONBYIDREQUEST']._serialized_end=757
  _globals['_GETORGANIZATIONBYIDRESPONSE']._serialized_start=759
  _globals['_GETORGANIZATIONBYIDRESPONSE']._serialized_end=855
  _globals['_LISTORGANIZATIONSREQUEST']._serialized_start=857
  _globals['_LISTORGANIZATIONSREQUEST']._serialized_end=982
  _globals['_LISTORGANIZATIONSRESPONSE']._serialized_start=984
  _globals['_LISTORGANIZATIONSRESPONSE']._serialized_end=1101
  _globals['_ORGANIZATIONDETAILS']._serialized_start=1104
  _globals['_ORGANIZATIONDETAILS']._serialized_end=1268
  _globals['_CONVERTORGTOMANUALREQUEST']._serialized_start=1270
  _globals['_CONVERTORGTOMANUALREQUEST']._serialized_end=1320
  _globals['_CONVERTORGTOMANUALRESPONSE']._serialized_start=1322
  _globals['_CONVERTORGTOMANUALRESPONSE']._serialized_end=1350
  _globals['_LISTOWNEDORGSREQUEST']._serialized_start=1352
  _globals['_LISTOWNEDORGSREQUEST']._serialized_end=1374
  _globals['_LISTOWNEDORGSRESPONSE']._serialized_start=1376
  _globals['_LISTOWNEDORGSRESPONSE']._serialized_end=1489
  _globals['_UPDATEORGANIZATIONREQUEST']._serialized_start=1492
  _globals['_UPDATEORGANIZATIONREQUEST']._serialized_end=1736
  _globals['_UPDATEORGANIZATIONRESPONSE']._serialized_start=1738
  _globals['_UPDATEORGANIZATIONRESPONSE']._serialized_end=1833
  _globals['_ARCHIVEORGANIZATIONREQUEST']._serialized_start=1835
  _globals['_ARCHIVEORGANIZATIONREQUEST']._serialized_end=1886
  _globals['_ARCHIVEORGANIZATIONRESPONSE']._serialized_start=1888
  _globals['_ARCHIVEORGANIZATIONRESPONSE']._serialized_end=1917
  _globals['_UNARCHIVEORGANIZATIONREQUEST']._serialized_start=1919
  _globals['_UNARCHIVEORGANIZATIONREQUEST']._serialized_end=1972
  _globals['_UNARCHIVEORGANIZATIONRESPONSE']._serialized_start=1974
  _globals['_UNARCHIVEORGANIZATIONRESPONSE']._serialized_end=2005
  _globals['_LISTALLORGANIZATIONSGLOBALLYREQUEST']._serialized_start=2007
  _globals['_LISTALLORGANIZATIONSGLOBALLYREQUEST']._serialized_end=2044
  _globals['_LISTALLORGANIZATIONSGLOBALLYRESPONSE']._serialized_start=2047
  _globals['_LISTALLORGANIZATIONSGLOBALLYRESPONSE']._serialized_end=2529
  _globals['_LISTALLORGANIZATIONSGLOBALLYRESPONSE_ORGANIZATIONDETAILS']._serialized_start=2215
  _globals['_LISTALLORGANIZATIONSGLOBALLYRESPONSE_ORGANIZATIONDETAILS']._serialized_end=2529
  _globals['_LISTORGANIZATIONSBYREGIONREQUEST']._serialized_start=2531
  _globals['_LISTORGANIZATIONSBYREGIONREQUEST']._serialized_end=2594
  _globals['_LISTORGANIZATIONSBYREGIONRESPONSE']._serialized_start=2597
  _globals['_LISTORGANIZATIONSBYREGIONRESPONSE']._serialized_end=3045
  _globals['_LISTORGANIZATIONSBYREGIONRESPONSE_ORGANIZATIONDETAILS']._serialized_start=2215
  _globals['_LISTORGANIZATIONSBYREGIONRESPONSE_ORGANIZATIONDETAILS']._serialized_end=2501
  _globals['_LISTARCHIVEDORGANIZATIONSREQUEST']._serialized_start=3047
  _globals['_LISTARCHIVEDORGANIZATIONSREQUEST']._serialized_end=3081
  _globals['_LISTARCHIVEDORGANIZATIONSRESPONSE']._serialized_start=3084
  _globals['_LISTARCHIVEDORGANIZATIONSRESPONSE']._serialized_end=3532
  _globals['_LISTARCHIVEDORGANIZATIONSRESPONSE_ORGANIZATIONDETAILS']._serialized_start=3246
  _globals['_LISTARCHIVEDORGANIZATIONSRESPONSE_ORGANIZATIONDETAILS']._serialized_end=3532
# @@protoc_insertion_point(module_scope)
