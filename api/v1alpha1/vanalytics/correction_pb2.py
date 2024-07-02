# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/vanalytics/correction.proto
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
    'api/v1alpha1/vanalytics/correction.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(api/v1alpha1/vanalytics/correction.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\"\x9b\x01\n\x17UpdateCorrectionRequest\x12\x43\n\ncorrection\x18\x01 \x01(\x0b\x32#.api.v1alpha1.vanalytics.CorrectionR\ncorrection\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"_\n\x18UpdateCorrectionResponse\x12\x43\n\ncorrection\x18\x01 \x01(\x0b\x32#.api.v1alpha1.vanalytics.CorrectionR\ncorrection\"^\n\x17\x43reateCorrectionRequest\x12\x43\n\ncorrection\x18\x01 \x01(\x0b\x32#.api.v1alpha1.vanalytics.CorrectionR\ncorrection\"_\n\x18\x43reateCorrectionResponse\x12\x43\n\ncorrection\x18\x01 \x01(\x0b\x32#.api.v1alpha1.vanalytics.CorrectionR\ncorrection\"=\n\x14GetCorrectionRequest\x12%\n\x0e\x63orrection_sid\x18\x02 \x01(\x03R\rcorrectionSid\"?\n\x16ListCorrectionsRequest\x12%\n\x0etranscript_sid\x18\x02 \x01(\x03R\rtranscriptSid\"`\n\x17ListCorrectionsResponse\x12\x45\n\x0b\x63orrections\x18\x01 \x03(\x0b\x32#.api.v1alpha1.vanalytics.CorrectionR\x0b\x63orrections\"X\n\x17\x44\x65leteCorrectionRequest\x12%\n\x0e\x63orrection_sid\x18\x01 \x01(\x03R\rcorrectionSid\x12\x16\n\x06return\x18\x03 \x01(\x08R\x06return\"_\n\x18\x44\x65leteCorrectionResponse\x12\x43\n\ncorrection\x18\x01 \x01(\x0b\x32#.api.v1alpha1.vanalytics.CorrectionR\ncorrection\"\x91\x02\n\nCorrection\x12%\n\x0e\x63orrection_sid\x18\x01 \x01(\x03R\rcorrectionSid\x12%\n\x0etranscript_sid\x18\x03 \x01(\x03R\rtranscriptSid\x12<\n\x0cstart_offset\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0bstartOffset\x12\x38\n\nend_offset\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationR\tendOffset\x12#\n\rproposed_text\x18\x06 \x01(\tR\x0cproposedText\x12\x18\n\x07\x63hannel\x18\x07 \x01(\rR\x07\x63hannelB\xac\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\x0f\x43orrectionProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.correction_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\017CorrectionProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_UPDATECORRECTIONREQUEST']._serialized_start=136
  _globals['_UPDATECORRECTIONREQUEST']._serialized_end=291
  _globals['_UPDATECORRECTIONRESPONSE']._serialized_start=293
  _globals['_UPDATECORRECTIONRESPONSE']._serialized_end=388
  _globals['_CREATECORRECTIONREQUEST']._serialized_start=390
  _globals['_CREATECORRECTIONREQUEST']._serialized_end=484
  _globals['_CREATECORRECTIONRESPONSE']._serialized_start=486
  _globals['_CREATECORRECTIONRESPONSE']._serialized_end=581
  _globals['_GETCORRECTIONREQUEST']._serialized_start=583
  _globals['_GETCORRECTIONREQUEST']._serialized_end=644
  _globals['_LISTCORRECTIONSREQUEST']._serialized_start=646
  _globals['_LISTCORRECTIONSREQUEST']._serialized_end=709
  _globals['_LISTCORRECTIONSRESPONSE']._serialized_start=711
  _globals['_LISTCORRECTIONSRESPONSE']._serialized_end=807
  _globals['_DELETECORRECTIONREQUEST']._serialized_start=809
  _globals['_DELETECORRECTIONREQUEST']._serialized_end=897
  _globals['_DELETECORRECTIONRESPONSE']._serialized_start=899
  _globals['_DELETECORRECTIONRESPONSE']._serialized_end=994
  _globals['_CORRECTION']._serialized_start=997
  _globals['_CORRECTION']._serialized_end=1270
# @@protoc_insertion_point(module_scope)
