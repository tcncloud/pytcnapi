# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/trusts.proto
# Protobuf Python Version: 5.29.3
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
    3,
    '',
    'api/v1alpha1/org/trusts.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.auth import perms_pb2 as api_dot_commons_dot_auth_dot_perms__pb2
from api.commons.org import trusts_pb2 as api_dot_commons_dot_org_dot_trusts__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61pi/v1alpha1/org/trusts.proto\x12\x10\x61pi.v1alpha1.org\x1a\x1c\x61pi/commons/auth/perms.proto\x1a\x1c\x61pi/commons/org/trusts.proto\"\xc1\x01\n\x12\x43reateTrustRequest\x12\x18\n\x07grantee\x18\x01 \x01(\tR\x07grantee\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12>\n\x0bpermissions\x18\x04 \x03(\x0e\x32\x1c.api.commons.auth.PermissionR\x0bpermissions\x12\x1b\n\tlabel_ids\x18\x05 \x03(\tR\x08labelIds\"0\n\x13\x43reateTrustResponse\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\"/\n\x12\x41\x63\x63\x65ptTrustRequest\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\"\x15\n\x13\x41\x63\x63\x65ptTrustResponse\"/\n\x12RejectTrustRequest\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\"\x15\n\x13RejectTrustResponse\",\n\x0fGetTrustRequest\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\"\x86\x01\n\x10GetTrustResponse\x12,\n\x05trust\x18\x01 \x01(\x0b\x32\x16.api.commons.org.TrustR\x05trust\x12!\n\x0cgrantor_name\x18\x02 \x01(\tR\x0bgrantorName\x12!\n\x0cgrantee_name\x18\x03 \x01(\tR\x0bgranteeName\"\x1b\n\x19ListIncomingTrustsRequest\"\xe9\x01\n\x1aListIncomingTrustsResponse\x12L\n\x06trusts\x18\x01 \x03(\x0b\x32\x34.api.v1alpha1.org.ListIncomingTrustsResponse.PayloadR\x06trusts\x1a}\n\x07Payload\x12,\n\x05trust\x18\x01 \x01(\x0b\x32\x16.api.commons.org.TrustR\x05trust\x12!\n\x0cgrantor_name\x18\x02 \x01(\tR\x0bgrantorName\x12!\n\x0cgrantee_name\x18\x03 \x01(\tR\x0bgranteeName\"\x18\n\x16ListGivenTrustsRequest\"\xe3\x01\n\x17ListGivenTrustsResponse\x12I\n\x06trusts\x18\x01 \x03(\x0b\x32\x31.api.v1alpha1.org.ListGivenTrustsResponse.PayloadR\x06trusts\x1a}\n\x07Payload\x12,\n\x05trust\x18\x01 \x01(\x0b\x32\x16.api.commons.org.TrustR\x05trust\x12!\n\x0cgrantor_name\x18\x02 \x01(\tR\x0bgrantorName\x12!\n\x0cgrantee_name\x18\x03 \x01(\tR\x0bgranteeName\"\x1d\n\x1bListAssignableTrustsRequest\"\xed\x01\n\x1cListAssignableTrustsResponse\x12N\n\x06trusts\x18\x01 \x03(\x0b\x32\x36.api.v1alpha1.org.ListAssignableTrustsResponse.PayloadR\x06trusts\x1a}\n\x07Payload\x12,\n\x05trust\x18\x01 \x01(\x0b\x32\x16.api.commons.org.TrustR\x05trust\x12!\n\x0cgrantor_name\x18\x02 \x01(\tR\x0bgrantorName\x12!\n\x0cgrantee_name\x18\x03 \x01(\tR\x0bgranteeName\"/\n\x12\x44\x65leteTrustRequest\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\"\x15\n\x13\x44\x65leteTrustResponse\"J\n\x12\x41ssignTrustRequest\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\x12\x19\n\x08user_ids\x18\x02 \x03(\tR\x07userIds\"\x15\n\x13\x41ssignTrustResponse\"J\n\x14UnassignTrustRequest\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"\x17\n\x15UnassignTrustResponseB\x85\x01\n\x14\x63om.api.v1alpha1.orgB\x0bTrustsProtoP\x01\xa2\x02\x03\x41VO\xaa\x02\x10\x41pi.V1alpha1.Org\xca\x02\x10\x41pi\\V1alpha1\\Org\xe2\x02\x1c\x41pi\\V1alpha1\\Org\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.trusts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.orgB\013TrustsProtoP\001\242\002\003AVO\252\002\020Api.V1alpha1.Org\312\002\020Api\\V1alpha1\\Org\342\002\034Api\\V1alpha1\\Org\\GPBMetadata\352\002\022Api::V1alpha1::Org'
  _globals['_CREATETRUSTREQUEST']._serialized_start=112
  _globals['_CREATETRUSTREQUEST']._serialized_end=305
  _globals['_CREATETRUSTRESPONSE']._serialized_start=307
  _globals['_CREATETRUSTRESPONSE']._serialized_end=355
  _globals['_ACCEPTTRUSTREQUEST']._serialized_start=357
  _globals['_ACCEPTTRUSTREQUEST']._serialized_end=404
  _globals['_ACCEPTTRUSTRESPONSE']._serialized_start=406
  _globals['_ACCEPTTRUSTRESPONSE']._serialized_end=427
  _globals['_REJECTTRUSTREQUEST']._serialized_start=429
  _globals['_REJECTTRUSTREQUEST']._serialized_end=476
  _globals['_REJECTTRUSTRESPONSE']._serialized_start=478
  _globals['_REJECTTRUSTRESPONSE']._serialized_end=499
  _globals['_GETTRUSTREQUEST']._serialized_start=501
  _globals['_GETTRUSTREQUEST']._serialized_end=545
  _globals['_GETTRUSTRESPONSE']._serialized_start=548
  _globals['_GETTRUSTRESPONSE']._serialized_end=682
  _globals['_LISTINCOMINGTRUSTSREQUEST']._serialized_start=684
  _globals['_LISTINCOMINGTRUSTSREQUEST']._serialized_end=711
  _globals['_LISTINCOMINGTRUSTSRESPONSE']._serialized_start=714
  _globals['_LISTINCOMINGTRUSTSRESPONSE']._serialized_end=947
  _globals['_LISTINCOMINGTRUSTSRESPONSE_PAYLOAD']._serialized_start=822
  _globals['_LISTINCOMINGTRUSTSRESPONSE_PAYLOAD']._serialized_end=947
  _globals['_LISTGIVENTRUSTSREQUEST']._serialized_start=949
  _globals['_LISTGIVENTRUSTSREQUEST']._serialized_end=973
  _globals['_LISTGIVENTRUSTSRESPONSE']._serialized_start=976
  _globals['_LISTGIVENTRUSTSRESPONSE']._serialized_end=1203
  _globals['_LISTGIVENTRUSTSRESPONSE_PAYLOAD']._serialized_start=822
  _globals['_LISTGIVENTRUSTSRESPONSE_PAYLOAD']._serialized_end=947
  _globals['_LISTASSIGNABLETRUSTSREQUEST']._serialized_start=1205
  _globals['_LISTASSIGNABLETRUSTSREQUEST']._serialized_end=1234
  _globals['_LISTASSIGNABLETRUSTSRESPONSE']._serialized_start=1237
  _globals['_LISTASSIGNABLETRUSTSRESPONSE']._serialized_end=1474
  _globals['_LISTASSIGNABLETRUSTSRESPONSE_PAYLOAD']._serialized_start=822
  _globals['_LISTASSIGNABLETRUSTSRESPONSE_PAYLOAD']._serialized_end=947
  _globals['_DELETETRUSTREQUEST']._serialized_start=1476
  _globals['_DELETETRUSTREQUEST']._serialized_end=1523
  _globals['_DELETETRUSTRESPONSE']._serialized_start=1525
  _globals['_DELETETRUSTRESPONSE']._serialized_end=1546
  _globals['_ASSIGNTRUSTREQUEST']._serialized_start=1548
  _globals['_ASSIGNTRUSTREQUEST']._serialized_end=1622
  _globals['_ASSIGNTRUSTRESPONSE']._serialized_start=1624
  _globals['_ASSIGNTRUSTRESPONSE']._serialized_end=1645
  _globals['_UNASSIGNTRUSTREQUEST']._serialized_start=1647
  _globals['_UNASSIGNTRUSTREQUEST']._serialized_end=1721
  _globals['_UNASSIGNTRUSTRESPONSE']._serialized_start=1723
  _globals['_UNASSIGNTRUSTRESPONSE']._serialized_end=1746
# @@protoc_insertion_point(module_scope)
