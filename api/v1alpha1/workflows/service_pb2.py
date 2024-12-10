# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/workflows/service.proto
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
    'api/v1alpha1/workflows/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$api/v1alpha1/workflows/service.proto\x12\x16\x61pi.v1alpha1.workflows\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbf\x03\n\x1bPersistedWorkflowDefinition\x12,\n\x12\x66low_definition_id\x18\x01 \x01(\tR\x10\x66lowDefinitionId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12 \n\x0b\x61pplication\x18\x03 \x01(\tR\x0b\x61pplication\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12\x16\n\x06labels\x18\t \x03(\tR\x06labels\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12\x1e\n\ndefinition\x18\x06 \x01(\tR\ndefinition\x12;\n\x0b\x63reate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12;\n\x0b\x64\x65lete_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ndeleteTime\x12\x14\n\x05\x65xtra\x18\x64 \x01(\tR\x05\x65xtra\"\x87\x01\n\x1f\x43reateWorkflowDefinitionRequest\x12\x64\n\x13workflow_definition\x18\x01 \x01(\x0b\x32\x33.api.v1alpha1.workflows.PersistedWorkflowDefinitionR\x12workflowDefinition\"\x88\x01\n CreateWorkflowDefinitionResponse\x12\x64\n\x13workflow_definition\x18\x01 \x01(\x0b\x32\x33.api.v1alpha1.workflows.PersistedWorkflowDefinitionR\x12workflowDefinition\"T\n\x1cGetWorkflowDefinitionRequest\x12\x34\n\x16workflow_definition_id\x18\x01 \x01(\tR\x14workflowDefinitionId\"\x85\x01\n\x1dGetWorkflowDefinitionResponse\x12\x64\n\x13workflow_definition\x18\x01 \x01(\x0b\x32\x33.api.v1alpha1.workflows.PersistedWorkflowDefinitionR\x12workflowDefinition\"q\n\x1eListWorkflowDefinitionsRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12 \n\x0b\x61pplication\x18\x02 \x01(\tR\x0b\x61pplication\x12\x16\n\x06labels\x18\x03 \x03(\tR\x06labels\"\x87\x01\n\x1fListWorkflowDefinitionsResponse\x12\x64\n\x13workflow_definition\x18\x01 \x01(\x0b\x32\x33.api.v1alpha1.workflows.PersistedWorkflowDefinitionR\x12workflowDefinition\"\x87\x01\n\x1fUpdateWorkflowDefinitionRequest\x12\x64\n\x13workflow_definition\x18\x01 \x01(\x0b\x32\x33.api.v1alpha1.workflows.PersistedWorkflowDefinitionR\x12workflowDefinition\"\x88\x01\n UpdateWorkflowDefinitionResponse\x12\x64\n\x13workflow_definition\x18\x01 \x01(\x0b\x32\x33.api.v1alpha1.workflows.PersistedWorkflowDefinitionR\x12workflowDefinition\"W\n\x1f\x44\x65leteWorkflowDefinitionRequest\x12\x34\n\x16workflow_definition_id\x18\x01 \x01(\tR\x14workflowDefinitionId\"\x88\x01\n DeleteWorkflowDefinitionResponse\x12\x64\n\x13workflow_definition\x18\x01 \x01(\x0b\x32\x33.api.v1alpha1.workflows.PersistedWorkflowDefinitionR\x12workflowDefinition\"\x89\x01\n!ValidateWorkflowDefinitionRequest\x12\x64\n\x13workflow_definition\x18\x01 \x01(\x0b\x32\x33.api.v1alpha1.workflows.PersistedWorkflowDefinitionR\x12workflowDefinition\"P\n\"ValidateWorkflowDefinitionResponse\x12\x14\n\x05valid\x18\x01 \x01(\x08R\x05valid\x12\x14\n\x05\x65rror\x18\x02 \x01(\tR\x05\x65rror2\xa9\n\n WorkflowDefinitionPersistService\x12\xd4\x01\n\x18\x43reateWorkflowDefinition\x12\x37.api.v1alpha1.workflows.CreateWorkflowDefinitionRequest\x1a\x38.api.v1alpha1.workflows.CreateWorkflowDefinitionResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x1f\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/workflows/createworkflowdefinition:\x01*\x12\xcb\x01\n\x15GetWorkflowDefinition\x12\x34.api.v1alpha1.workflows.GetWorkflowDefinitionRequest\x1a\x35.api.v1alpha1.workflows.GetWorkflowDefinitionResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x1f\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/workflows/createworkflowdefinition:\x01*\x12\xd2\x01\n\x17ListWorkflowDefinitions\x12\x36.api.v1alpha1.workflows.ListWorkflowDefinitionsRequest\x1a\x37.api.v1alpha1.workflows.ListWorkflowDefinitionsResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x1f\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/workflows/listworkflowdefinitions:\x01*0\x01\x12\xd4\x01\n\x18UpdateWorkflowDefinition\x12\x37.api.v1alpha1.workflows.UpdateWorkflowDefinitionRequest\x1a\x38.api.v1alpha1.workflows.UpdateWorkflowDefinitionResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x1f\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/workflows/updateworkflowdefinition:\x01*\x12\xd4\x01\n\x18\x44\x65leteWorkflowDefinition\x12\x37.api.v1alpha1.workflows.DeleteWorkflowDefinitionRequest\x1a\x38.api.v1alpha1.workflows.DeleteWorkflowDefinitionResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x1f\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/workflows/deleteworkflowdefinition:\x01*\x12\xdc\x01\n\x1aValidateWorkflowDefinition\x12\x39.api.v1alpha1.workflows.ValidateWorkflowDefinitionRequest\x1a:.api.v1alpha1.workflows.ValidateWorkflowDefinitionResponse\"G\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x1f\x82\xd3\xe4\x93\x02\x37\"2/api/v1alpha1/workflows/validateworkflowdefinition:\x01*B\xa4\x01\n\x1a\x63om.api.v1alpha1.workflowsB\x0cServiceProtoP\x01\xa2\x02\x03\x41VW\xaa\x02\x16\x41pi.V1alpha1.Workflows\xca\x02\x16\x41pi\\V1alpha1\\Workflows\xe2\x02\"Api\\V1alpha1\\Workflows\\GPBMetadata\xea\x02\x18\x41pi::V1alpha1::Workflowsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.workflows.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.api.v1alpha1.workflowsB\014ServiceProtoP\001\242\002\003AVW\252\002\026Api.V1alpha1.Workflows\312\002\026Api\\V1alpha1\\Workflows\342\002\"Api\\V1alpha1\\Workflows\\GPBMetadata\352\002\030Api::V1alpha1::Workflows'
  _globals['_WORKFLOWDEFINITIONPERSISTSERVICE'].methods_by_name['CreateWorkflowDefinition']._loaded_options = None
  _globals['_WORKFLOWDEFINITIONPERSISTSERVICE'].methods_by_name['CreateWorkflowDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\240\037\202\323\344\223\0025\"0/api/v1alpha1/workflows/createworkflowdefinition:\001*'
  _globals['_WORKFLOWDEFINITIONPERSISTSERVICE'].methods_by_name['GetWorkflowDefinition']._loaded_options = None
  _globals['_WORKFLOWDEFINITIONPERSISTSERVICE'].methods_by_name['GetWorkflowDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\240\037\202\323\344\223\0025\"0/api/v1alpha1/workflows/createworkflowdefinition:\001*'
  _globals['_WORKFLOWDEFINITIONPERSISTSERVICE'].methods_by_name['ListWorkflowDefinitions']._loaded_options = None
  _globals['_WORKFLOWDEFINITIONPERSISTSERVICE'].methods_by_name['ListWorkflowDefinitions']._serialized_options = b'\272\270\221\002\005\n\003\010\240\037\202\323\344\223\0024\"//api/v1alpha1/workflows/listworkflowdefinitions:\001*'
  _globals['_WORKFLOWDEFINITIONPERSISTSERVICE'].methods_by_name['UpdateWorkflowDefinition']._loaded_options = None
  _globals['_WORKFLOWDEFINITIONPERSISTSERVICE'].methods_by_name['UpdateWorkflowDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\240\037\202\323\344\223\0025\"0/api/v1alpha1/workflows/updateworkflowdefinition:\001*'
  _globals['_WORKFLOWDEFINITIONPERSISTSERVICE'].methods_by_name['DeleteWorkflowDefinition']._loaded_options = None
  _globals['_WORKFLOWDEFINITIONPERSISTSERVICE'].methods_by_name['DeleteWorkflowDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\240\037\202\323\344\223\0025\"0/api/v1alpha1/workflows/deleteworkflowdefinition:\001*'
  _globals['_WORKFLOWDEFINITIONPERSISTSERVICE'].methods_by_name['ValidateWorkflowDefinition']._loaded_options = None
  _globals['_WORKFLOWDEFINITIONPERSISTSERVICE'].methods_by_name['ValidateWorkflowDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\240\037\202\323\344\223\0027\"2/api/v1alpha1/workflows/validateworkflowdefinition:\001*'
  _globals['_PERSISTEDWORKFLOWDEFINITION']._serialized_start=153
  _globals['_PERSISTEDWORKFLOWDEFINITION']._serialized_end=600
  _globals['_CREATEWORKFLOWDEFINITIONREQUEST']._serialized_start=603
  _globals['_CREATEWORKFLOWDEFINITIONREQUEST']._serialized_end=738
  _globals['_CREATEWORKFLOWDEFINITIONRESPONSE']._serialized_start=741
  _globals['_CREATEWORKFLOWDEFINITIONRESPONSE']._serialized_end=877
  _globals['_GETWORKFLOWDEFINITIONREQUEST']._serialized_start=879
  _globals['_GETWORKFLOWDEFINITIONREQUEST']._serialized_end=963
  _globals['_GETWORKFLOWDEFINITIONRESPONSE']._serialized_start=966
  _globals['_GETWORKFLOWDEFINITIONRESPONSE']._serialized_end=1099
  _globals['_LISTWORKFLOWDEFINITIONSREQUEST']._serialized_start=1101
  _globals['_LISTWORKFLOWDEFINITIONSREQUEST']._serialized_end=1214
  _globals['_LISTWORKFLOWDEFINITIONSRESPONSE']._serialized_start=1217
  _globals['_LISTWORKFLOWDEFINITIONSRESPONSE']._serialized_end=1352
  _globals['_UPDATEWORKFLOWDEFINITIONREQUEST']._serialized_start=1355
  _globals['_UPDATEWORKFLOWDEFINITIONREQUEST']._serialized_end=1490
  _globals['_UPDATEWORKFLOWDEFINITIONRESPONSE']._serialized_start=1493
  _globals['_UPDATEWORKFLOWDEFINITIONRESPONSE']._serialized_end=1629
  _globals['_DELETEWORKFLOWDEFINITIONREQUEST']._serialized_start=1631
  _globals['_DELETEWORKFLOWDEFINITIONREQUEST']._serialized_end=1718
  _globals['_DELETEWORKFLOWDEFINITIONRESPONSE']._serialized_start=1721
  _globals['_DELETEWORKFLOWDEFINITIONRESPONSE']._serialized_end=1857
  _globals['_VALIDATEWORKFLOWDEFINITIONREQUEST']._serialized_start=1860
  _globals['_VALIDATEWORKFLOWDEFINITIONREQUEST']._serialized_end=1997
  _globals['_VALIDATEWORKFLOWDEFINITIONRESPONSE']._serialized_start=1999
  _globals['_VALIDATEWORKFLOWDEFINITIONRESPONSE']._serialized_end=2079
  _globals['_WORKFLOWDEFINITIONPERSISTSERVICE']._serialized_start=2082
  _globals['_WORKFLOWDEFINITIONPERSISTSERVICE']._serialized_end=3403
# @@protoc_insertion_point(module_scope)
