# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/org/labels.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import labels_pb2 as api_dot_commons_dot_labels__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/commons/org/labels.proto\x12\x0f\x61pi.commons.org\x1a\x18\x61pi/commons/labels.proto\"\xab\x01\n\x05Label\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scription\x12\x14\n\x05\x63olor\x18\x07 \x01(\tR\x05\x63olor\x12\x19\n\x08label_id\x18\x08 \x01(\tR\x07labelId\x12\x18\n\x07\x64\x65leted\x18\t \x01(\x08R\x07\x64\x65letedJ\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06\"\xbb\x01\n\x0fLabelAssignment\x12\x19\n\x08label_id\x18\x01 \x01(\tR\x07labelId\x12+\n\x04type\x18\x02 \x01(\x0e\x32\x17.api.commons.EntityTypeR\x04type\x12\x1b\n\tentity_id\x18\x03 \x01(\tR\x08\x65ntityId\x12\x15\n\x06org_id\x18\x04 \x01(\tR\x05orgId\x12,\n\x05label\x18\x05 \x01(\x0b\x32\x16.api.commons.org.LabelR\x05labelB\x80\x01\n\x13\x63om.api.commons.orgB\x0bLabelsProtoP\x01\xa2\x02\x03\x41\x43O\xaa\x02\x0f\x41pi.Commons.Org\xca\x02\x0f\x41pi\\Commons\\Org\xe2\x02\x1b\x41pi\\Commons\\Org\\GPBMetadata\xea\x02\x11\x41pi::Commons::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.org.labels_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.api.commons.orgB\013LabelsProtoP\001\242\002\003ACO\252\002\017Api.Commons.Org\312\002\017Api\\Commons\\Org\342\002\033Api\\Commons\\Org\\GPBMetadata\352\002\021Api::Commons::Org'
  _globals['_LABEL']._serialized_start=76
  _globals['_LABEL']._serialized_end=247
  _globals['_LABELASSIGNMENT']._serialized_start=250
  _globals['_LABELASSIGNMENT']._serialized_end=437
# @@protoc_insertion_point(module_scope)
