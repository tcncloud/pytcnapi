# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/workflows/entities.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.workflows import entities_pb2 as api_dot_commons_dot_workflows_dot_entities__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/v1alpha1/workflows/entities.proto\x12\x16\x61pi.v1alpha1.workflows\x1a$api/commons/workflows/entities.proto\x1a google/protobuf/field_mask.proto\"4\n\x1aListFlowDefinitionsRequest\x12\x16\n\x06\x66ilter\x18\x01 \x01(\tR\x06\x66ilter\"o\n\x1bListFlowDefinitionsResponse\x12P\n\x10\x66low_definitions\x18\x01 \x03(\x0b\x32%.api.commons.workflows.FlowDefinitionR\x0f\x66lowDefinitions\"\xa8\x01\n\x19SaveFlowDefinitionRequest\x12N\n\x0f\x66low_definition\x18\x01 \x01(\x0b\x32%.api.commons.workflows.FlowDefinitionR\x0e\x66lowDefinition\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"\x9a\x01\n\x1aSaveFlowDefinitionResponse\x12,\n\x12\x66low_definition_id\x18\x01 \x01(\tR\x10\x66lowDefinitionId\x12N\n\x0f\x66low_definition\x18\x02 \x01(\x0b\x32%.api.commons.workflows.FlowDefinitionR\x0e\x66lowDefinition\"H\n\x18GetFlowDefinitionRequest\x12,\n\x12\x66low_definition_id\x18\x01 \x01(\tR\x10\x66lowDefinitionId\"k\n\x19GetFlowDefinitionResponse\x12N\n\x0f\x66low_definition\x18\x01 \x01(\x0b\x32%.api.commons.workflows.FlowDefinitionR\x0e\x66lowDefinition\"K\n\x1b\x44\x65leteFlowDefinitionRequest\x12,\n\x12\x66low_definition_id\x18\x01 \x01(\tR\x10\x66lowDefinitionId\"6\n\x1c\x44\x65leteFlowDefinitionResponse\x12\x16\n\x06result\x18\x01 \x01(\x08R\x06resultB\xa5\x01\n\x1a\x63om.api.v1alpha1.workflowsB\rEntitiesProtoP\x01\xa2\x02\x03\x41VW\xaa\x02\x16\x41pi.V1alpha1.Workflows\xca\x02\x16\x41pi\\V1alpha1\\Workflows\xe2\x02\"Api\\V1alpha1\\Workflows\\GPBMetadata\xea\x02\x18\x41pi::V1alpha1::Workflowsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.workflows.entities_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.api.v1alpha1.workflowsB\rEntitiesProtoP\001\242\002\003AVW\252\002\026Api.V1alpha1.Workflows\312\002\026Api\\V1alpha1\\Workflows\342\002\"Api\\V1alpha1\\Workflows\\GPBMetadata\352\002\030Api::V1alpha1::Workflows'
  _globals['_LISTFLOWDEFINITIONSREQUEST']._serialized_start=137
  _globals['_LISTFLOWDEFINITIONSREQUEST']._serialized_end=189
  _globals['_LISTFLOWDEFINITIONSRESPONSE']._serialized_start=191
  _globals['_LISTFLOWDEFINITIONSRESPONSE']._serialized_end=302
  _globals['_SAVEFLOWDEFINITIONREQUEST']._serialized_start=305
  _globals['_SAVEFLOWDEFINITIONREQUEST']._serialized_end=473
  _globals['_SAVEFLOWDEFINITIONRESPONSE']._serialized_start=476
  _globals['_SAVEFLOWDEFINITIONRESPONSE']._serialized_end=630
  _globals['_GETFLOWDEFINITIONREQUEST']._serialized_start=632
  _globals['_GETFLOWDEFINITIONREQUEST']._serialized_end=704
  _globals['_GETFLOWDEFINITIONRESPONSE']._serialized_start=706
  _globals['_GETFLOWDEFINITIONRESPONSE']._serialized_end=813
  _globals['_DELETEFLOWDEFINITIONREQUEST']._serialized_start=815
  _globals['_DELETEFLOWDEFINITIONREQUEST']._serialized_end=890
  _globals['_DELETEFLOWDEFINITIONRESPONSE']._serialized_start=892
  _globals['_DELETEFLOWDEFINITIONRESPONSE']._serialized_end=946
# @@protoc_insertion_point(module_scope)
