# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/labels/service.proto
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
    'api/v1alpha1/org/labels/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.org.labels import entities_pb2 as api_dot_v1alpha1_dot_org_dot_labels_dot_entities__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/v1alpha1/org/labels/service.proto\x12\x17\x61pi.v1alpha1.org.labels\x1a\x17\x61nnotations/authz.proto\x1a&api/v1alpha1/org/labels/entities.proto\x1a\x1cgoogle/api/annotations.proto2\x98\r\n\rLabelsService\x12\xa3\x01\n\x0b\x43reateLabel\x12+.api.v1alpha1.org.labels.CreateLabelRequest\x1a,.api.v1alpha1.org.labels.CreateLabelResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\x96\x01\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/org/labels/createlabel:\x01*\x12\x94\x01\n\x08GetLabel\x12(.api.v1alpha1.org.labels.GetLabelRequest\x1a).api.v1alpha1.org.labels.GetLabelResponse\"3\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02&\"!/api/v1alpha1/org/labels/getlabel:\x01*\x12\xa3\x01\n\x0bUpdateLabel\x12+.api.v1alpha1.org.labels.UpdateLabelRequest\x1a,.api.v1alpha1.org.labels.UpdateLabelResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\x96\x01\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/org/labels/updatelabel:\x01*\x12\x9c\x01\n\nListLabels\x12*.api.v1alpha1.org.labels.ListLabelsRequest\x1a+.api.v1alpha1.org.labels.ListLabelsResponse\"5\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/org/labels/listlabels:\x01*\x12\xa3\x01\n\x0b\x44\x65leteLabel\x12+.api.v1alpha1.org.labels.DeleteLabelRequest\x1a,.api.v1alpha1.org.labels.DeleteLabelResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\x96\x01\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/org/labels/deletelabel:\x01*\x12\xa3\x01\n\x0b\x41ttachLabel\x12+.api.v1alpha1.org.labels.AttachLabelRequest\x1a,.api.v1alpha1.org.labels.AttachLabelResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\x97\x01\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/org/labels/attachlabel:\x01*\x12\xa3\x01\n\x0b\x44\x65tachLabel\x12+.api.v1alpha1.org.labels.DetachLabelRequest\x1a,.api.v1alpha1.org.labels.DetachLabelResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\x97\x01\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/org/labels/detachlabel:\x01*\x12\xc0\x01\n\x13GetLabeledEntityMap\x12\x33.api.v1alpha1.org.labels.GetLabeledEntityMapRequest\x1a\x34.api.v1alpha1.org.labels.GetLabeledEntityMapResponse\">\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/org/labels/getlabeledentitymap:\x01*\x12\xa6\x01\n\x0c\x41ssignLabels\x12,.api.v1alpha1.org.labels.AssignLabelsRequest\x1a-.api.v1alpha1.org.labels.AssignLabelsResponse\"9\xba\xb8\x91\x02\x04\n\x02\x08n\x82\xd3\xe4\x93\x02*\"%/api/v1alpha1/org/labels/assignlabels:\x01*\x12\xa6\x01\n\x0cRevokeLabels\x12,.api.v1alpha1.org.labels.RevokeLabelsRequest\x1a-.api.v1alpha1.org.labels.RevokeLabelsResponse\"9\xba\xb8\x91\x02\x04\n\x02\x08n\x82\xd3\xe4\x93\x02*\"%/api/v1alpha1/org/labels/revokelabels:\x01*B\xab\x01\n\x1b\x63om.api.v1alpha1.org.labelsB\x0cServiceProtoP\x01\xa2\x02\x04\x41VOL\xaa\x02\x17\x41pi.V1alpha1.Org.Labels\xca\x02\x17\x41pi\\V1alpha1\\Org\\Labels\xe2\x02#Api\\V1alpha1\\Org\\Labels\\GPBMetadata\xea\x02\x1a\x41pi::V1alpha1::Org::Labelsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.labels.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.org.labelsB\014ServiceProtoP\001\242\002\004AVOL\252\002\027Api.V1alpha1.Org.Labels\312\002\027Api\\V1alpha1\\Org\\Labels\342\002#Api\\V1alpha1\\Org\\Labels\\GPBMetadata\352\002\032Api::V1alpha1::Org::Labels'
  _globals['_LABELSSERVICE'].methods_by_name['CreateLabel']._loaded_options = None
  _globals['_LABELSSERVICE'].methods_by_name['CreateLabel']._serialized_options = b'\272\270\221\002\005\n\003\010\226\001\202\323\344\223\002)\"$/api/v1alpha1/org/labels/createlabel:\001*'
  _globals['_LABELSSERVICE'].methods_by_name['GetLabel']._loaded_options = None
  _globals['_LABELSSERVICE'].methods_by_name['GetLabel']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002&\"!/api/v1alpha1/org/labels/getlabel:\001*'
  _globals['_LABELSSERVICE'].methods_by_name['UpdateLabel']._loaded_options = None
  _globals['_LABELSSERVICE'].methods_by_name['UpdateLabel']._serialized_options = b'\272\270\221\002\005\n\003\010\226\001\202\323\344\223\002)\"$/api/v1alpha1/org/labels/updatelabel:\001*'
  _globals['_LABELSSERVICE'].methods_by_name['ListLabels']._loaded_options = None
  _globals['_LABELSSERVICE'].methods_by_name['ListLabels']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002(\"#/api/v1alpha1/org/labels/listlabels:\001*'
  _globals['_LABELSSERVICE'].methods_by_name['DeleteLabel']._loaded_options = None
  _globals['_LABELSSERVICE'].methods_by_name['DeleteLabel']._serialized_options = b'\272\270\221\002\005\n\003\010\226\001\202\323\344\223\002)\"$/api/v1alpha1/org/labels/deletelabel:\001*'
  _globals['_LABELSSERVICE'].methods_by_name['AttachLabel']._loaded_options = None
  _globals['_LABELSSERVICE'].methods_by_name['AttachLabel']._serialized_options = b'\272\270\221\002\005\n\003\010\227\001\202\323\344\223\002)\"$/api/v1alpha1/org/labels/attachlabel:\001*'
  _globals['_LABELSSERVICE'].methods_by_name['DetachLabel']._loaded_options = None
  _globals['_LABELSSERVICE'].methods_by_name['DetachLabel']._serialized_options = b'\272\270\221\002\005\n\003\010\227\001\202\323\344\223\002)\"$/api/v1alpha1/org/labels/detachlabel:\001*'
  _globals['_LABELSSERVICE'].methods_by_name['GetLabeledEntityMap']._loaded_options = None
  _globals['_LABELSSERVICE'].methods_by_name['GetLabeledEntityMap']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0021\",/api/v1alpha1/org/labels/getlabeledentitymap:\001*'
  _globals['_LABELSSERVICE'].methods_by_name['AssignLabels']._loaded_options = None
  _globals['_LABELSSERVICE'].methods_by_name['AssignLabels']._serialized_options = b'\272\270\221\002\004\n\002\010n\202\323\344\223\002*\"%/api/v1alpha1/org/labels/assignlabels:\001*'
  _globals['_LABELSSERVICE'].methods_by_name['RevokeLabels']._loaded_options = None
  _globals['_LABELSSERVICE'].methods_by_name['RevokeLabels']._serialized_options = b'\272\270\221\002\004\n\002\010n\202\323\344\223\002*\"%/api/v1alpha1/org/labels/revokelabels:\001*'
  _globals['_LABELSSERVICE']._serialized_start=162
  _globals['_LABELSSERVICE']._serialized_end=1850
# @@protoc_insertion_point(module_scope)
