# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/scorecards/smart_evaluation.proto
# Protobuf Python Version: 6.30.0
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
    0,
    '',
    'api/v1alpha1/scorecards/smart_evaluation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import scorecards_pb2 as api_dot_commons_dot_scorecards__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.api/v1alpha1/scorecards/smart_evaluation.proto\x12\x17\x61pi.v1alpha1.scorecards\x1a\x1c\x61pi/commons/scorecards.proto\x1a google/protobuf/field_mask.proto\"g\n\x1c\x43reateSmartEvaluationRequest\x12G\n\x10smart_evaluation\x18\x01 \x01(\x0b\x32\x1c.api.commons.SmartEvaluationR\x0fsmartEvaluation\"h\n\x1d\x43reateSmartEvaluationResponse\x12G\n\x10smart_evaluation\x18\x01 \x01(\x0b\x32\x1c.api.commons.SmartEvaluationR\x0fsmartEvaluation\"\xcd\x01\n\x1bListSmartEvaluationsRequest\x12\x19\n\x08order_by\x18\x02 \x01(\tR\x07orderBy\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12?\n\rreturn_fields\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0creturnFields\x12\x16\n\x06\x66ilter\x18\x06 \x01(\tR\x06\x66ilter\"\x91\x01\n\x1cListSmartEvaluationsResponse\x12I\n\x11smart_evaluations\x18\x01 \x03(\x0b\x32\x1c.api.commons.SmartEvaluationR\x10smartEvaluations\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\xa4\x01\n\x1cUpdateSmartEvaluationRequest\x12G\n\x10smart_evaluation\x18\x01 \x01(\x0b\x32\x1c.api.commons.SmartEvaluationR\x0fsmartEvaluation\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"h\n\x1dUpdateSmartEvaluationResponse\x12G\n\x10smart_evaluation\x18\x01 \x01(\x0b\x32\x1c.api.commons.SmartEvaluationR\x0fsmartEvaluation\"N\n\x1c\x44\x65leteSmartEvaluationRequest\x12.\n\x13smart_evaluation_id\x18\x02 \x01(\x03R\x11smartEvaluationId\"\x1f\n\x1d\x44\x65leteSmartEvaluationResponse\"K\n\x19GetSmartEvaluationRequest\x12.\n\x13smart_evaluation_id\x18\x02 \x01(\x03R\x11smartEvaluationId\"e\n\x1aGetSmartEvaluationResponse\x12G\n\x10smart_evaluation\x18\x01 \x01(\x0b\x32\x1c.api.commons.SmartEvaluationR\x0fsmartEvaluationB\xb1\x01\n\x1b\x63om.api.v1alpha1.scorecardsB\x14SmartEvaluationProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Scorecards\xca\x02\x17\x41pi\\V1alpha1\\Scorecards\xe2\x02#Api\\V1alpha1\\Scorecards\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Scorecardsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.scorecards.smart_evaluation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.scorecardsB\024SmartEvaluationProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Scorecards\312\002\027Api\\V1alpha1\\Scorecards\342\002#Api\\V1alpha1\\Scorecards\\GPBMetadata\352\002\031Api::V1alpha1::Scorecards'
  _globals['_CREATESMARTEVALUATIONREQUEST']._serialized_start=139
  _globals['_CREATESMARTEVALUATIONREQUEST']._serialized_end=242
  _globals['_CREATESMARTEVALUATIONRESPONSE']._serialized_start=244
  _globals['_CREATESMARTEVALUATIONRESPONSE']._serialized_end=348
  _globals['_LISTSMARTEVALUATIONSREQUEST']._serialized_start=351
  _globals['_LISTSMARTEVALUATIONSREQUEST']._serialized_end=556
  _globals['_LISTSMARTEVALUATIONSRESPONSE']._serialized_start=559
  _globals['_LISTSMARTEVALUATIONSRESPONSE']._serialized_end=704
  _globals['_UPDATESMARTEVALUATIONREQUEST']._serialized_start=707
  _globals['_UPDATESMARTEVALUATIONREQUEST']._serialized_end=871
  _globals['_UPDATESMARTEVALUATIONRESPONSE']._serialized_start=873
  _globals['_UPDATESMARTEVALUATIONRESPONSE']._serialized_end=977
  _globals['_DELETESMARTEVALUATIONREQUEST']._serialized_start=979
  _globals['_DELETESMARTEVALUATIONREQUEST']._serialized_end=1057
  _globals['_DELETESMARTEVALUATIONRESPONSE']._serialized_start=1059
  _globals['_DELETESMARTEVALUATIONRESPONSE']._serialized_end=1090
  _globals['_GETSMARTEVALUATIONREQUEST']._serialized_start=1092
  _globals['_GETSMARTEVALUATIONREQUEST']._serialized_end=1167
  _globals['_GETSMARTEVALUATIONRESPONSE']._serialized_start=1169
  _globals['_GETSMARTEVALUATIONRESPONSE']._serialized_end=1270
# @@protoc_insertion_point(module_scope)
