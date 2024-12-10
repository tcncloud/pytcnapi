# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/labels.proto
# Protobuf Python Version: 5.29.1
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
    1,
    '',
    'api/v1alpha1/org/labels.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.auth import perms_pb2 as api_dot_commons_dot_auth_dot_perms__pb2
from api.commons import labels_pb2 as api_dot_commons_dot_labels__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61pi/v1alpha1/org/labels.proto\x12\x10\x61pi.v1alpha1.org\x1a\x1c\x61pi/commons/auth/perms.proto\x1a\x18\x61pi/commons/labels.proto\"\x94\x01\n\x05Label\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scription\x12\x14\n\x05\x63olor\x18\x07 \x01(\tR\x05\x63olor\x12\x19\n\x08label_id\x18\x08 \x01(\tR\x07labelId\x12\x18\n\x07\x64\x65leted\x18\t \x01(\x08R\x07\x64\x65letedJ\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06\"C\n\x12\x43reateLabelRequest\x12-\n\x05label\x18\x01 \x01(\x0b\x32\x17.api.v1alpha1.org.LabelR\x05label\"0\n\x13\x43reateLabelResponse\x12\x19\n\x08label_id\x18\x01 \x01(\tR\x07labelId\"5\n\x12\x44\x65leteLabelRequest\x12\x19\n\x08label_id\x18\x02 \x01(\tR\x07labelIdJ\x04\x08\x01\x10\x02\"\x15\n\x13\x44\x65leteLabelResponse\"\x19\n\x11ListLabelsRequestJ\x04\x08\x02\x10\x03\"E\n\x12ListLabelsResponse\x12/\n\x06labels\x18\x01 \x03(\x0b\x32\x17.api.v1alpha1.org.LabelR\x06labels\"2\n\x0fGetLabelRequest\x12\x19\n\x08label_id\x18\x02 \x01(\tR\x07labelIdJ\x04\x08\x01\x10\x02\"A\n\x10GetLabelResponse\x12-\n\x05label\x18\x01 \x01(\x0b\x32\x17.api.v1alpha1.org.LabelR\x05label\"C\n\x12UpdateLabelRequest\x12-\n\x05label\x18\x01 \x01(\x0b\x32\x17.api.v1alpha1.org.LabelR\x05label\"\x15\n\x13UpdateLabelResponse\"\xab\x01\n\x0fLabelAssignment\x12\x19\n\x08label_id\x18\x01 \x01(\tR\x07labelId\x12+\n\x04type\x18\x02 \x01(\x0e\x32\x17.api.commons.EntityTypeR\x04type\x12\x1b\n\tentity_id\x18\x03 \x01(\tR\x08\x65ntityId\x12-\n\x05label\x18\x05 \x01(\x0b\x32\x17.api.v1alpha1.org.LabelR\x05labelJ\x04\x08\x04\x10\x05\"_\n\x12\x41ssignLabelRequest\x12\x43\n\x0b\x61ssignments\x18\x02 \x03(\x0b\x32!.api.v1alpha1.org.LabelAssignmentR\x0b\x61ssignmentsJ\x04\x08\x01\x10\x02\"\x15\n\x13\x41ssignLabelResponse\"a\n\x14UnassignLabelRequest\x12\x43\n\x0b\x61ssignments\x18\x02 \x03(\x0b\x32!.api.v1alpha1.org.LabelAssignmentR\x0b\x61ssignmentsJ\x04\x08\x01\x10\x02\"\x17\n\x15UnassignLabelResponse\"7\n\x1aGetAssignmentCountsRequest\x12\x19\n\x08label_id\x18\x01 \x01(\tR\x07labelId\"\xab\x01\n\x1bGetAssignmentCountsResponse\x12Q\n\x06\x63ounts\x18\x01 \x03(\x0b\x32\x39.api.v1alpha1.org.GetAssignmentCountsResponse.CountsEntryR\x06\x63ounts\x1a\x39\n\x0b\x43ountsEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value:\x02\x38\x01\"Z\n\x1aGetAssignableLabelsRequest\x12<\n\npermission\x18\x01 \x01(\x0e\x32\x1c.api.commons.auth.PermissionR\npermission\"N\n\x1bGetAssignableLabelsResponse\x12/\n\x06labels\x18\x01 \x03(\x0b\x32\x17.api.v1alpha1.org.LabelR\x06labelsB\x85\x01\n\x14\x63om.api.v1alpha1.orgB\x0bLabelsProtoP\x01\xa2\x02\x03\x41VO\xaa\x02\x10\x41pi.V1alpha1.Org\xca\x02\x10\x41pi\\V1alpha1\\Org\xe2\x02\x1c\x41pi\\V1alpha1\\Org\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.labels_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.orgB\013LabelsProtoP\001\242\002\003AVO\252\002\020Api.V1alpha1.Org\312\002\020Api\\V1alpha1\\Org\342\002\034Api\\V1alpha1\\Org\\GPBMetadata\352\002\022Api::V1alpha1::Org'
  _globals['_GETASSIGNMENTCOUNTSRESPONSE_COUNTSENTRY']._loaded_options = None
  _globals['_GETASSIGNMENTCOUNTSRESPONSE_COUNTSENTRY']._serialized_options = b'8\001'
  _globals['_LABEL']._serialized_start=108
  _globals['_LABEL']._serialized_end=256
  _globals['_CREATELABELREQUEST']._serialized_start=258
  _globals['_CREATELABELREQUEST']._serialized_end=325
  _globals['_CREATELABELRESPONSE']._serialized_start=327
  _globals['_CREATELABELRESPONSE']._serialized_end=375
  _globals['_DELETELABELREQUEST']._serialized_start=377
  _globals['_DELETELABELREQUEST']._serialized_end=430
  _globals['_DELETELABELRESPONSE']._serialized_start=432
  _globals['_DELETELABELRESPONSE']._serialized_end=453
  _globals['_LISTLABELSREQUEST']._serialized_start=455
  _globals['_LISTLABELSREQUEST']._serialized_end=480
  _globals['_LISTLABELSRESPONSE']._serialized_start=482
  _globals['_LISTLABELSRESPONSE']._serialized_end=551
  _globals['_GETLABELREQUEST']._serialized_start=553
  _globals['_GETLABELREQUEST']._serialized_end=603
  _globals['_GETLABELRESPONSE']._serialized_start=605
  _globals['_GETLABELRESPONSE']._serialized_end=670
  _globals['_UPDATELABELREQUEST']._serialized_start=672
  _globals['_UPDATELABELREQUEST']._serialized_end=739
  _globals['_UPDATELABELRESPONSE']._serialized_start=741
  _globals['_UPDATELABELRESPONSE']._serialized_end=762
  _globals['_LABELASSIGNMENT']._serialized_start=765
  _globals['_LABELASSIGNMENT']._serialized_end=936
  _globals['_ASSIGNLABELREQUEST']._serialized_start=938
  _globals['_ASSIGNLABELREQUEST']._serialized_end=1033
  _globals['_ASSIGNLABELRESPONSE']._serialized_start=1035
  _globals['_ASSIGNLABELRESPONSE']._serialized_end=1056
  _globals['_UNASSIGNLABELREQUEST']._serialized_start=1058
  _globals['_UNASSIGNLABELREQUEST']._serialized_end=1155
  _globals['_UNASSIGNLABELRESPONSE']._serialized_start=1157
  _globals['_UNASSIGNLABELRESPONSE']._serialized_end=1180
  _globals['_GETASSIGNMENTCOUNTSREQUEST']._serialized_start=1182
  _globals['_GETASSIGNMENTCOUNTSREQUEST']._serialized_end=1237
  _globals['_GETASSIGNMENTCOUNTSRESPONSE']._serialized_start=1240
  _globals['_GETASSIGNMENTCOUNTSRESPONSE']._serialized_end=1411
  _globals['_GETASSIGNMENTCOUNTSRESPONSE_COUNTSENTRY']._serialized_start=1354
  _globals['_GETASSIGNMENTCOUNTSRESPONSE_COUNTSENTRY']._serialized_end=1411
  _globals['_GETASSIGNABLELABELSREQUEST']._serialized_start=1413
  _globals['_GETASSIGNABLELABELSREQUEST']._serialized_end=1503
  _globals['_GETASSIGNABLELABELSRESPONSE']._serialized_start=1505
  _globals['_GETASSIGNABLELABELSRESPONSE']._serialized_end=1583
# @@protoc_insertion_point(module_scope)
