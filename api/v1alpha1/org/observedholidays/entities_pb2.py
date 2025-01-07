# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/observedholidays/entities.proto
# Protobuf Python Version: 5.29.2
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
    2,
    '',
    'api/v1alpha1/org/observedholidays/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import org_pb2 as api_dot_commons_dot_org__pb2
from api.commons.org import preferences_pb2 as api_dot_commons_dot_org_dot_preferences__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0api/v1alpha1/org/observedholidays/entities.proto\x12!api.v1alpha1.org.observedholidays\x1a\x15\x61pi/commons/org.proto\x1a!api/commons/org/preferences.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x1d\n\x1bListObservedHolidaysRequest\"n\n\x1cListObservedHolidaysResponse\x12N\n\x11observed_holidays\x18\x01 \x03(\x0b\x32!.api.commons.org.ObservedHolidaysR\x10observedHolidays\"N\n\x1aGetObservedHolidaysRequest\x12\x30\n\x14observed_holidays_id\x18\x01 \x01(\tR\x12observedHolidaysId\"m\n\x1bGetObservedHolidaysResponse\x12N\n\x11observed_holidays\x18\x01 \x01(\x0b\x32!.api.commons.org.ObservedHolidaysR\x10observedHolidays\"\xdd\x01\n\x1aSetObservedHolidaysRequest\x12\x34\n\x16observed_holidays_name\x18\x01 \x01(\tR\x14observedHolidaysName\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x31\n\x08timezone\x18\x03 \x01(\x0e\x32\x15.api.commons.TimeZoneR\x08timezone\x12\x34\n\x04\x64\x61ys\x18\x04 \x03(\x0b\x32 .api.commons.org.ObservedHolidayR\x04\x64\x61ys\"O\n\x1bSetObservedHolidaysResponse\x12\x30\n\x14observed_holidays_id\x18\x01 \x01(\tR\x12observedHolidaysId\"\x84\x01\n\x1c\x41\x64\x64ToObservedHolidaysRequest\x12\x30\n\x14observed_holidays_id\x18\x01 \x01(\tR\x12observedHolidaysId\x12\x32\n\x03\x64\x61y\x18\x02 \x01(\x0b\x32 .api.commons.org.ObservedHolidayR\x03\x64\x61y\"\x1f\n\x1d\x41\x64\x64ToObservedHolidaysResponse\"\x89\x01\n!RemoveFromObservedHolidaysRequest\x12\x30\n\x14observed_holidays_id\x18\x01 \x01(\tR\x12observedHolidaysId\x12\x32\n\x03\x64\x61y\x18\x02 \x01(\x0b\x32 .api.commons.org.ObservedHolidayR\x03\x64\x61y\"$\n\"RemoveFromObservedHolidaysResponse\"\x9b\x02\n!UpdateObservedHolidaysInfoRequest\x12\x30\n\x14observed_holidays_id\x18\x01 \x01(\tR\x12observedHolidaysId\x12\x34\n\x16observed_holidays_name\x18\x02 \x01(\tR\x14observedHolidaysName\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x31\n\x08timezone\x18\x04 \x01(\x0e\x32\x15.api.commons.TimeZoneR\x08timezone\x12\x39\n\nfield_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"$\n\"UpdateObservedHolidaysInfoResponse\"Q\n\x1d\x44\x65leteObservedHolidaysRequest\x12\x30\n\x14observed_holidays_id\x18\x01 \x01(\tR\x12observedHolidaysId\"R\n\x1e\x44\x65leteObservedHolidaysResponse\x12\x30\n\x14observed_holidays_id\x18\x01 \x01(\tR\x12observedHolidaysId\"S\n\x1f\x45valuateObservedHolidaysRequest\x12\x30\n\x14observed_holidays_id\x18\x01 \x01(\tR\x12observedHolidaysId\"\x8e\x01\n EvaluateObservedHolidaysResponse\x12!\n\x0c\x64\x61te_matched\x18\x01 \x01(\x08R\x0b\x64\x61teMatched\x12G\n\x11result_expiration\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x10resultExpirationB\xde\x01\n%com.api.v1alpha1.org.observedholidaysB\rEntitiesProtoP\x01\xa2\x02\x04\x41VOO\xaa\x02!Api.V1alpha1.Org.Observedholidays\xca\x02!Api\\V1alpha1\\Org\\Observedholidays\xe2\x02-Api\\V1alpha1\\Org\\Observedholidays\\GPBMetadata\xea\x02$Api::V1alpha1::Org::Observedholidaysb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.observedholidays.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%com.api.v1alpha1.org.observedholidaysB\rEntitiesProtoP\001\242\002\004AVOO\252\002!Api.V1alpha1.Org.Observedholidays\312\002!Api\\V1alpha1\\Org\\Observedholidays\342\002-Api\\V1alpha1\\Org\\Observedholidays\\GPBMetadata\352\002$Api::V1alpha1::Org::Observedholidays'
  _globals['_LISTOBSERVEDHOLIDAYSREQUEST']._serialized_start=212
  _globals['_LISTOBSERVEDHOLIDAYSREQUEST']._serialized_end=241
  _globals['_LISTOBSERVEDHOLIDAYSRESPONSE']._serialized_start=243
  _globals['_LISTOBSERVEDHOLIDAYSRESPONSE']._serialized_end=353
  _globals['_GETOBSERVEDHOLIDAYSREQUEST']._serialized_start=355
  _globals['_GETOBSERVEDHOLIDAYSREQUEST']._serialized_end=433
  _globals['_GETOBSERVEDHOLIDAYSRESPONSE']._serialized_start=435
  _globals['_GETOBSERVEDHOLIDAYSRESPONSE']._serialized_end=544
  _globals['_SETOBSERVEDHOLIDAYSREQUEST']._serialized_start=547
  _globals['_SETOBSERVEDHOLIDAYSREQUEST']._serialized_end=768
  _globals['_SETOBSERVEDHOLIDAYSRESPONSE']._serialized_start=770
  _globals['_SETOBSERVEDHOLIDAYSRESPONSE']._serialized_end=849
  _globals['_ADDTOOBSERVEDHOLIDAYSREQUEST']._serialized_start=852
  _globals['_ADDTOOBSERVEDHOLIDAYSREQUEST']._serialized_end=984
  _globals['_ADDTOOBSERVEDHOLIDAYSRESPONSE']._serialized_start=986
  _globals['_ADDTOOBSERVEDHOLIDAYSRESPONSE']._serialized_end=1017
  _globals['_REMOVEFROMOBSERVEDHOLIDAYSREQUEST']._serialized_start=1020
  _globals['_REMOVEFROMOBSERVEDHOLIDAYSREQUEST']._serialized_end=1157
  _globals['_REMOVEFROMOBSERVEDHOLIDAYSRESPONSE']._serialized_start=1159
  _globals['_REMOVEFROMOBSERVEDHOLIDAYSRESPONSE']._serialized_end=1195
  _globals['_UPDATEOBSERVEDHOLIDAYSINFOREQUEST']._serialized_start=1198
  _globals['_UPDATEOBSERVEDHOLIDAYSINFOREQUEST']._serialized_end=1481
  _globals['_UPDATEOBSERVEDHOLIDAYSINFORESPONSE']._serialized_start=1483
  _globals['_UPDATEOBSERVEDHOLIDAYSINFORESPONSE']._serialized_end=1519
  _globals['_DELETEOBSERVEDHOLIDAYSREQUEST']._serialized_start=1521
  _globals['_DELETEOBSERVEDHOLIDAYSREQUEST']._serialized_end=1602
  _globals['_DELETEOBSERVEDHOLIDAYSRESPONSE']._serialized_start=1604
  _globals['_DELETEOBSERVEDHOLIDAYSRESPONSE']._serialized_end=1686
  _globals['_EVALUATEOBSERVEDHOLIDAYSREQUEST']._serialized_start=1688
  _globals['_EVALUATEOBSERVEDHOLIDAYSREQUEST']._serialized_end=1771
  _globals['_EVALUATEOBSERVEDHOLIDAYSRESPONSE']._serialized_start=1774
  _globals['_EVALUATEOBSERVEDHOLIDAYSRESPONSE']._serialized_end=1916
# @@protoc_insertion_point(module_scope)
