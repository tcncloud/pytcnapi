# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/vanalytics/dncl_list.proto
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
    'api/v1alpha1/vanalytics/dncl_list.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import compliance_pb2 as api_dot_commons_dot_compliance__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'api/v1alpha1/vanalytics/dncl_list.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a\x1c\x61pi/commons/compliance.proto\"\x83\x02\n\x08\x44nclList\x12\x17\n\x07list_id\x18\x02 \x01(\tR\x06listId\x12;\n\x0c\x63ontent_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ContentTypeR\x0b\x63ontentType\x12N\n\rexpire_period\x18\x04 \x01(\x0e\x32).api.v1alpha1.vanalytics.DnclExpirePeriodR\x0c\x65xpirePeriod\x12#\n\rexpire_offset\x18\x05 \x01(\x04R\x0c\x65xpireOffset\x12,\n\x12\x61gent_response_key\x18\x06 \x01(\tR\x10\x61gentResponseKey*\xa4\x01\n\x10\x44nclExpirePeriod\x12\x1b\n\x17\x44NCL_EXPIRE_PERIOD_HOUR\x10\x00\x12\x1a\n\x16\x44NCL_EXPIRE_PERIOD_DAY\x10\x01\x12\x1b\n\x17\x44NCL_EXPIRE_PERIOD_WEEK\x10\x02\x12\x1c\n\x18\x44NCL_EXPIRE_PERIOD_NEVER\x10\x03\x12\x1c\n\x18\x44NCL_EXPIRE_PERIOD_MONTH\x10\x04\x42\xaa\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\rDnclListProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.dncl_list_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\rDnclListProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_DNCLEXPIREPERIOD']._serialized_start=361
  _globals['_DNCLEXPIREPERIOD']._serialized_end=525
  _globals['_DNCLLIST']._serialized_start=99
  _globals['_DNCLLIST']._serialized_end=358
# @@protoc_insertion_point(module_scope)
