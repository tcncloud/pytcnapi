# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/v1alpha4/tag.proto
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
    'services/billing/v1alpha4/tag.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from services.billing.entities.v1alpha4 import tags_pb2 as services_dot_billing_dot_entities_dot_v1alpha4_dot_tags__pb2
from services.billing.v1alpha4 import core_pb2 as services_dot_billing_dot_v1alpha4_dot_core__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#services/billing/v1alpha4/tag.proto\x12\x19services.billing.v1alpha4\x1a google/protobuf/field_mask.proto\x1a-services/billing/entities/v1alpha4/tags.proto\x1a$services/billing/v1alpha4/core.proto\"\x90\x01\n\x17\x43reateBillingTagRequest\x12$\n\x0e\x62illing_tag_id\x18\x01 \x01(\tR\x0c\x62illingTagId\x12O\n\x0b\x62illing_tag\x18\x02 \x01(\x0b\x32..services.billing.entities.v1alpha4.BillingTagR\nbillingTag\"@\n\x18\x43reateBillingTagResponse\x12$\n\x0e\x62illing_tag_id\x18\x01 \x01(\tR\x0c\x62illingTagId\"?\n\x17\x44\x65leteBillingTagRequest\x12$\n\x0e\x62illing_tag_id\x18\x01 \x01(\tR\x0c\x62illingTagId\"\x1a\n\x18\x44\x65leteBillingTagResponse\"<\n\x14GetBillingTagRequest\x12$\n\x0e\x62illing_tag_id\x18\x01 \x01(\tR\x0c\x62illingTagId\"h\n\x15GetBillingTagResponse\x12O\n\x0b\x62illing_tag\x18\x01 \x01(\x0b\x32..services.billing.entities.v1alpha4.BillingTagR\nbillingTag\"\xf4\x01\n\x16ListBillingTagsRequest\x12$\n\x0e\x62illing_tag_id\x18\x01 \x01(\tR\x0c\x62illingTagId\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x32\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x06\x66ields\x12\x33\n\x04sort\x18\x04 \x03(\x0b\x32\x1f.services.billing.v1alpha4.SortR\x04sort\x12\x33\n\x04page\x18\x05 \x01(\x0b\x32\x1f.services.billing.v1alpha4.PageR\x04page\"\x82\x01\n\x17ListBillingTagsResponse\x12Q\n\x0c\x62illing_tags\x18\x01 \x03(\x0b\x32..services.billing.entities.v1alpha4.BillingTagR\x0b\x62illingTags\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"\xcd\x01\n\x17UpdateBillingTagRequest\x12$\n\x0e\x62illing_tag_id\x18\x01 \x01(\tR\x0c\x62illingTagId\x12O\n\x0b\x62illing_tag\x18\x02 \x01(\x0b\x32..services.billing.entities.v1alpha4.BillingTagR\nbillingTag\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"\x1a\n\x18UpdateBillingTagResponseB\xaf\x01\n\x1d\x63om.services.billing.v1alpha4B\x08TagProtoP\x01\xa2\x02\x03SBX\xaa\x02\x19Services.Billing.V1alpha4\xca\x02\x19Services\\Billing\\V1alpha4\xe2\x02%Services\\Billing\\V1alpha4\\GPBMetadata\xea\x02\x1bServices::Billing::V1alpha4b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.v1alpha4.tag_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.services.billing.v1alpha4B\010TagProtoP\001\242\002\003SBX\252\002\031Services.Billing.V1alpha4\312\002\031Services\\Billing\\V1alpha4\342\002%Services\\Billing\\V1alpha4\\GPBMetadata\352\002\033Services::Billing::V1alpha4'
  _globals['_CREATEBILLINGTAGREQUEST']._serialized_start=186
  _globals['_CREATEBILLINGTAGREQUEST']._serialized_end=330
  _globals['_CREATEBILLINGTAGRESPONSE']._serialized_start=332
  _globals['_CREATEBILLINGTAGRESPONSE']._serialized_end=396
  _globals['_DELETEBILLINGTAGREQUEST']._serialized_start=398
  _globals['_DELETEBILLINGTAGREQUEST']._serialized_end=461
  _globals['_DELETEBILLINGTAGRESPONSE']._serialized_start=463
  _globals['_DELETEBILLINGTAGRESPONSE']._serialized_end=489
  _globals['_GETBILLINGTAGREQUEST']._serialized_start=491
  _globals['_GETBILLINGTAGREQUEST']._serialized_end=551
  _globals['_GETBILLINGTAGRESPONSE']._serialized_start=553
  _globals['_GETBILLINGTAGRESPONSE']._serialized_end=657
  _globals['_LISTBILLINGTAGSREQUEST']._serialized_start=660
  _globals['_LISTBILLINGTAGSREQUEST']._serialized_end=904
  _globals['_LISTBILLINGTAGSRESPONSE']._serialized_start=907
  _globals['_LISTBILLINGTAGSRESPONSE']._serialized_end=1037
  _globals['_UPDATEBILLINGTAGREQUEST']._serialized_start=1040
  _globals['_UPDATEBILLINGTAGREQUEST']._serialized_end=1245
  _globals['_UPDATEBILLINGTAGRESPONSE']._serialized_start=1247
  _globals['_UPDATEBILLINGTAGRESPONSE']._serialized_end=1273
# @@protoc_insertion_point(module_scope)
