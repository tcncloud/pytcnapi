# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/exile/station/finvi/v1/service.proto
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
    'api/v1alpha1/exile/station/finvi/v1/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1api/v1alpha1/exile/station/finvi/v1/service.proto\x12#api.v1alpha1.exile.station.finvi.v1\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\"\xac\x01\n\rPopAccountReq\x12\x1b\n\trecord_id\x18\n \x01(\tR\x08recordId\x12\x17\n\x07user_id\x18\x0b \x01(\tR\x06userId\x12!\n\x0c\x61lternate_id\x18\x0c \x01(\tR\x0b\x61lternateId\x12\x19\n\x08\x63\x61ll_sid\x18\r \x01(\x03R\x07\x63\x61llSid\x12\x1b\n\tcall_type\x18\x0e \x01(\tR\x08\x63\x61llTypeJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03\"<\n\rPopAccountRes\x12\x15\n\x06job_id\x18\x01 \x01(\x03R\x05jobId\x12\x14\n\x05\x61sync\x18\x02 \x01(\x08R\x05\x61sync2\xe6\x01\n\x13GenericFinviService\x12\xce\x01\n\nPopAccount\x12\x32.api.v1alpha1.exile.station.finvi.v1.PopAccountReq\x1a\x32.api.v1alpha1.exile.station.finvi.v1.PopAccountRes\"X\xba\xb8\x91\x02\x05\n\x03\x08\xac\x02\x82\xd3\xe4\x93\x02H\"C/api/v1alpha1/exile/station/finvi/v1/genericfinviservice/popaccount:\x01*B\xea\x01\n\'com.api.v1alpha1.exile.station.finvi.v1B\x0cServiceProtoP\x01\xa2\x02\x05\x41VESF\xaa\x02#Api.V1alpha1.Exile.Station.Finvi.V1\xca\x02#Api\\V1alpha1\\Exile\\Station\\Finvi\\V1\xe2\x02/Api\\V1alpha1\\Exile\\Station\\Finvi\\V1\\GPBMetadata\xea\x02(Api::V1alpha1::Exile::Station::Finvi::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.exile.station.finvi.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.api.v1alpha1.exile.station.finvi.v1B\014ServiceProtoP\001\242\002\005AVESF\252\002#Api.V1alpha1.Exile.Station.Finvi.V1\312\002#Api\\V1alpha1\\Exile\\Station\\Finvi\\V1\342\002/Api\\V1alpha1\\Exile\\Station\\Finvi\\V1\\GPBMetadata\352\002(Api::V1alpha1::Exile::Station::Finvi::V1'
  _globals['_GENERICFINVISERVICE'].methods_by_name['PopAccount']._loaded_options = None
  _globals['_GENERICFINVISERVICE'].methods_by_name['PopAccount']._serialized_options = b'\272\270\221\002\005\n\003\010\254\002\202\323\344\223\002H\"C/api/v1alpha1/exile/station/finvi/v1/genericfinviservice/popaccount:\001*'
  _globals['_POPACCOUNTREQ']._serialized_start=178
  _globals['_POPACCOUNTREQ']._serialized_end=350
  _globals['_POPACCOUNTRES']._serialized_start=352
  _globals['_POPACCOUNTRES']._serialized_end=412
  _globals['_GENERICFINVISERVICE']._serialized_start=415
  _globals['_GENERICFINVISERVICE']._serialized_end=645
# @@protoc_insertion_point(module_scope)
