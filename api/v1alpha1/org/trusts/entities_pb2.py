# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/trusts/entities.proto
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
    'api/v1alpha1/org/trusts/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.auth import perms_pb2 as api_dot_commons_dot_auth_dot_perms__pb2
from api.commons.org import trusts_pb2 as api_dot_commons_dot_org_dot_trusts__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&api/v1alpha1/org/trusts/entities.proto\x12\x17\x61pi.v1alpha1.org.trusts\x1a\x1c\x61pi/commons/auth/perms.proto\x1a\x1c\x61pi/commons/org/trusts.proto\"\xc1\x01\n\x12\x43reateTrustRequest\x12\x18\n\x07grantee\x18\x01 \x01(\tR\x07grantee\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12>\n\x0bpermissions\x18\x04 \x03(\x0e\x32\x1c.api.commons.auth.PermissionR\x0bpermissions\x12\x1b\n\tlabel_ids\x18\x05 \x03(\tR\x08labelIds\"0\n\x13\x43reateTrustResponse\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\"/\n\x12\x41\x63\x63\x65ptTrustRequest\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\"\x15\n\x13\x41\x63\x63\x65ptTrustResponse\"/\n\x12RejectTrustRequest\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\"\x15\n\x13RejectTrustResponse\",\n\x0fGetTrustRequest\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\"\x86\x01\n\x10GetTrustResponse\x12,\n\x05trust\x18\x01 \x01(\x0b\x32\x16.api.commons.org.TrustR\x05trust\x12!\n\x0cgrantor_name\x18\x02 \x01(\tR\x0bgrantorName\x12!\n\x0cgrantee_name\x18\x03 \x01(\tR\x0bgranteeName\"\x8f\x01\n\x19ListTrustsResponsePayload\x12,\n\x05trust\x18\x01 \x01(\x0b\x32\x16.api.commons.org.TrustR\x05trust\x12!\n\x0cgrantor_name\x18\x02 \x01(\tR\x0bgrantorName\x12!\n\x0cgrantee_name\x18\x03 \x01(\tR\x0bgranteeName\"\x1b\n\x19ListIncomingTrustsRequest\"h\n\x1aListIncomingTrustsResponse\x12J\n\x06trusts\x18\x01 \x03(\x0b\x32\x32.api.v1alpha1.org.trusts.ListTrustsResponsePayloadR\x06trusts\"\x18\n\x16ListGivenTrustsRequest\"e\n\x17ListGivenTrustsResponse\x12J\n\x06trusts\x18\x01 \x03(\x0b\x32\x32.api.v1alpha1.org.trusts.ListTrustsResponsePayloadR\x06trusts\"\x1d\n\x1bListAssignableTrustsRequest\"j\n\x1cListAssignableTrustsResponse\x12J\n\x06trusts\x18\x01 \x03(\x0b\x32\x32.api.v1alpha1.org.trusts.ListTrustsResponsePayloadR\x06trusts\"/\n\x12\x44\x65leteTrustRequest\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\"\x15\n\x13\x44\x65leteTrustResponse\"J\n\x12\x41ssignTrustRequest\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\x12\x19\n\x08user_ids\x18\x02 \x03(\tR\x07userIds\"\x15\n\x13\x41ssignTrustResponse\"J\n\x14UnassignTrustRequest\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"\x17\n\x15UnassignTrustResponseB\xac\x01\n\x1b\x63om.api.v1alpha1.org.trustsB\rEntitiesProtoP\x01\xa2\x02\x04\x41VOT\xaa\x02\x17\x41pi.V1alpha1.Org.Trusts\xca\x02\x17\x41pi\\V1alpha1\\Org\\Trusts\xe2\x02#Api\\V1alpha1\\Org\\Trusts\\GPBMetadata\xea\x02\x1a\x41pi::V1alpha1::Org::Trustsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.trusts.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.org.trustsB\rEntitiesProtoP\001\242\002\004AVOT\252\002\027Api.V1alpha1.Org.Trusts\312\002\027Api\\V1alpha1\\Org\\Trusts\342\002#Api\\V1alpha1\\Org\\Trusts\\GPBMetadata\352\002\032Api::V1alpha1::Org::Trusts'
  _globals['_CREATETRUSTREQUEST']._serialized_start=128
  _globals['_CREATETRUSTREQUEST']._serialized_end=321
  _globals['_CREATETRUSTRESPONSE']._serialized_start=323
  _globals['_CREATETRUSTRESPONSE']._serialized_end=371
  _globals['_ACCEPTTRUSTREQUEST']._serialized_start=373
  _globals['_ACCEPTTRUSTREQUEST']._serialized_end=420
  _globals['_ACCEPTTRUSTRESPONSE']._serialized_start=422
  _globals['_ACCEPTTRUSTRESPONSE']._serialized_end=443
  _globals['_REJECTTRUSTREQUEST']._serialized_start=445
  _globals['_REJECTTRUSTREQUEST']._serialized_end=492
  _globals['_REJECTTRUSTRESPONSE']._serialized_start=494
  _globals['_REJECTTRUSTRESPONSE']._serialized_end=515
  _globals['_GETTRUSTREQUEST']._serialized_start=517
  _globals['_GETTRUSTREQUEST']._serialized_end=561
  _globals['_GETTRUSTRESPONSE']._serialized_start=564
  _globals['_GETTRUSTRESPONSE']._serialized_end=698
  _globals['_LISTTRUSTSRESPONSEPAYLOAD']._serialized_start=701
  _globals['_LISTTRUSTSRESPONSEPAYLOAD']._serialized_end=844
  _globals['_LISTINCOMINGTRUSTSREQUEST']._serialized_start=846
  _globals['_LISTINCOMINGTRUSTSREQUEST']._serialized_end=873
  _globals['_LISTINCOMINGTRUSTSRESPONSE']._serialized_start=875
  _globals['_LISTINCOMINGTRUSTSRESPONSE']._serialized_end=979
  _globals['_LISTGIVENTRUSTSREQUEST']._serialized_start=981
  _globals['_LISTGIVENTRUSTSREQUEST']._serialized_end=1005
  _globals['_LISTGIVENTRUSTSRESPONSE']._serialized_start=1007
  _globals['_LISTGIVENTRUSTSRESPONSE']._serialized_end=1108
  _globals['_LISTASSIGNABLETRUSTSREQUEST']._serialized_start=1110
  _globals['_LISTASSIGNABLETRUSTSREQUEST']._serialized_end=1139
  _globals['_LISTASSIGNABLETRUSTSRESPONSE']._serialized_start=1141
  _globals['_LISTASSIGNABLETRUSTSRESPONSE']._serialized_end=1247
  _globals['_DELETETRUSTREQUEST']._serialized_start=1249
  _globals['_DELETETRUSTREQUEST']._serialized_end=1296
  _globals['_DELETETRUSTRESPONSE']._serialized_start=1298
  _globals['_DELETETRUSTRESPONSE']._serialized_end=1319
  _globals['_ASSIGNTRUSTREQUEST']._serialized_start=1321
  _globals['_ASSIGNTRUSTREQUEST']._serialized_end=1395
  _globals['_ASSIGNTRUSTRESPONSE']._serialized_start=1397
  _globals['_ASSIGNTRUSTRESPONSE']._serialized_end=1418
  _globals['_UNASSIGNTRUSTREQUEST']._serialized_start=1420
  _globals['_UNASSIGNTRUSTREQUEST']._serialized_end=1494
  _globals['_UNASSIGNTRUSTRESPONSE']._serialized_start=1496
  _globals['_UNASSIGNTRUSTRESPONSE']._serialized_end=1519
# @@protoc_insertion_point(module_scope)
