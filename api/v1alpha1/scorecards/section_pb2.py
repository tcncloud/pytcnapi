# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/scorecards/section.proto
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
    'api/v1alpha1/scorecards/section.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import scorecards_pb2 as api_dot_commons_dot_scorecards__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/v1alpha1/scorecards/section.proto\x12\x17\x61pi.v1alpha1.scorecards\x1a\x1c\x61pi/commons/scorecards.proto\x1a google/protobuf/field_mask.proto\"F\n\x14\x43reateSectionRequest\x12.\n\x07section\x18\x01 \x01(\x0b\x32\x14.api.commons.SectionR\x07section\"G\n\x15\x43reateSectionResponse\x12.\n\x07section\x18\x01 \x01(\x0b\x32\x14.api.commons.SectionR\x07section\"8\n\x13ListSectionsRequest\x12!\n\x0cscorecard_id\x18\x02 \x01(\x03R\x0bscorecardId\"H\n\x14ListSectionsResponse\x12\x30\n\x08sections\x18\x01 \x03(\x0b\x32\x14.api.commons.SectionR\x08sections\"\x83\x01\n\x14UpdateSectionRequest\x12.\n\x07section\x18\x01 \x01(\x0b\x32\x14.api.commons.SectionR\x07section\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"G\n\x15UpdateSectionResponse\x12.\n\x07section\x18\x01 \x01(\x0b\x32\x14.api.commons.SectionR\x07section\"5\n\x14\x44\x65leteSectionRequest\x12\x1d\n\nsection_id\x18\x02 \x01(\x03R\tsectionId\"G\n\x15\x44\x65leteSectionResponse\x12.\n\x07section\x18\x01 \x01(\x0b\x32\x14.api.commons.SectionR\x07section\"2\n\x11GetSectionRequest\x12\x1d\n\nsection_id\x18\x02 \x01(\x03R\tsectionId\"D\n\x12GetSectionResponse\x12.\n\x07section\x18\x01 \x01(\x0b\x32\x14.api.commons.SectionR\x07sectionB\xa9\x01\n\x1b\x63om.api.v1alpha1.scorecardsB\x0cSectionProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Scorecards\xca\x02\x17\x41pi\\V1alpha1\\Scorecards\xe2\x02#Api\\V1alpha1\\Scorecards\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Scorecardsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.scorecards.section_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.scorecardsB\014SectionProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Scorecards\312\002\027Api\\V1alpha1\\Scorecards\342\002#Api\\V1alpha1\\Scorecards\\GPBMetadata\352\002\031Api::V1alpha1::Scorecards'
  _globals['_CREATESECTIONREQUEST']._serialized_start=130
  _globals['_CREATESECTIONREQUEST']._serialized_end=200
  _globals['_CREATESECTIONRESPONSE']._serialized_start=202
  _globals['_CREATESECTIONRESPONSE']._serialized_end=273
  _globals['_LISTSECTIONSREQUEST']._serialized_start=275
  _globals['_LISTSECTIONSREQUEST']._serialized_end=331
  _globals['_LISTSECTIONSRESPONSE']._serialized_start=333
  _globals['_LISTSECTIONSRESPONSE']._serialized_end=405
  _globals['_UPDATESECTIONREQUEST']._serialized_start=408
  _globals['_UPDATESECTIONREQUEST']._serialized_end=539
  _globals['_UPDATESECTIONRESPONSE']._serialized_start=541
  _globals['_UPDATESECTIONRESPONSE']._serialized_end=612
  _globals['_DELETESECTIONREQUEST']._serialized_start=614
  _globals['_DELETESECTIONREQUEST']._serialized_end=667
  _globals['_DELETESECTIONRESPONSE']._serialized_start=669
  _globals['_DELETESECTIONRESPONSE']._serialized_end=740
  _globals['_GETSECTIONREQUEST']._serialized_start=742
  _globals['_GETSECTIONREQUEST']._serialized_end=792
  _globals['_GETSECTIONRESPONSE']._serialized_start=794
  _globals['_GETSECTIONRESPONSE']._serialized_end=862
# @@protoc_insertion_point(module_scope)
