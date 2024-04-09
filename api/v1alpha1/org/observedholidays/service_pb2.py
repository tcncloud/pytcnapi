# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/org/observedholidays/service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.org.observedholidays import entities_pb2 as api_dot_v1alpha1_dot_org_dot_observedholidays_dot_entities__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/api/v1alpha1/org/observedholidays/service.proto\x12!api.v1alpha1.org.observedholidays\x1a\x17\x61nnotations/authz.proto\x1a\x30\x61pi/v1alpha1/org/observedholidays/entities.proto\x1a\x1cgoogle/api/annotations.proto2\x8b\x0e\n\x17ObservedHolidaysService\x12\xd4\x01\n\x14ListObservedHolidays\x12>.api.v1alpha1.org.observedholidays.ListObservedHolidaysRequest\x1a?.api.v1alpha1.org.observedholidays.ListObservedHolidaysResponse\";\xba\xb8\x91\x02\x04\n\x02\x08\x65\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/org/observedholidays/list:\x01*\x12\xd0\x01\n\x13GetObservedHolidays\x12=.api.v1alpha1.org.observedholidays.GetObservedHolidaysRequest\x1a>.api.v1alpha1.org.observedholidays.GetObservedHolidaysResponse\":\xba\xb8\x91\x02\x04\n\x02\x08\x65\x82\xd3\xe4\x93\x02+\"&/api/v1alpha1/org/observedholidays/get:\x01*\x12\xd0\x01\n\x13SetObservedHolidays\x12=.api.v1alpha1.org.observedholidays.SetObservedHolidaysRequest\x1a>.api.v1alpha1.org.observedholidays.SetObservedHolidaysResponse\":\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02+\"&/api/v1alpha1/org/observedholidays/set:\x01*\x12\xd6\x01\n\x15\x41\x64\x64ToObservedHolidays\x12?.api.v1alpha1.org.observedholidays.AddToObservedHolidaysRequest\x1a@.api.v1alpha1.org.observedholidays.AddToObservedHolidaysResponse\":\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02+\"&/api/v1alpha1/org/observedholidays/add:\x01*\x12\xe4\x01\n\x16RemoveObservedHolidays\x12\x44.api.v1alpha1.org.observedholidays.RemoveFromObservedHolidaysRequest\x1a\x45.api.v1alpha1.org.observedholidays.RemoveFromObservedHolidaysResponse\"=\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/org/observedholidays/remove:\x01*\x12\xec\x01\n\x1aUpdateObservedHolidaysInfo\x12\x44.api.v1alpha1.org.observedholidays.UpdateObservedHolidaysInfoRequest\x1a\x45.api.v1alpha1.org.observedholidays.UpdateObservedHolidaysInfoResponse\"A\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/org/observedholidays/updateinfo:\x01*\x12\xdc\x01\n\x16\x44\x65leteObservedHolidays\x12@.api.v1alpha1.org.observedholidays.DeleteObservedHolidaysRequest\x1a\x41.api.v1alpha1.org.observedholidays.DeleteObservedHolidaysResponse\"=\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/org/observedholidays/delete:\x01*\x12\xe4\x01\n\x18\x45valuateObservedHolidays\x12\x42.api.v1alpha1.org.observedholidays.EvaluateObservedHolidaysRequest\x1a\x43.api.v1alpha1.org.observedholidays.EvaluateObservedHolidaysResponse\"?\xba\xb8\x91\x02\x04\n\x02\x08\x65\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/org/observedholidays/evaluate:\x01*B\xdd\x01\n%com.api.v1alpha1.org.observedholidaysB\x0cServiceProtoP\x01\xa2\x02\x04\x41VOO\xaa\x02!Api.V1alpha1.Org.Observedholidays\xca\x02!Api\\V1alpha1\\Org\\Observedholidays\xe2\x02-Api\\V1alpha1\\Org\\Observedholidays\\GPBMetadata\xea\x02$Api::V1alpha1::Org::Observedholidaysb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.observedholidays.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%com.api.v1alpha1.org.observedholidaysB\014ServiceProtoP\001\242\002\004AVOO\252\002!Api.V1alpha1.Org.Observedholidays\312\002!Api\\V1alpha1\\Org\\Observedholidays\342\002-Api\\V1alpha1\\Org\\Observedholidays\\GPBMetadata\352\002$Api::V1alpha1::Org::Observedholidays'
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['ListObservedHolidays']._loaded_options = None
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['ListObservedHolidays']._serialized_options = b'\272\270\221\002\004\n\002\010e\202\323\344\223\002,\"\'/api/v1alpha1/org/observedholidays/list:\001*'
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['GetObservedHolidays']._loaded_options = None
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['GetObservedHolidays']._serialized_options = b'\272\270\221\002\004\n\002\010e\202\323\344\223\002+\"&/api/v1alpha1/org/observedholidays/get:\001*'
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['SetObservedHolidays']._loaded_options = None
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['SetObservedHolidays']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\002+\"&/api/v1alpha1/org/observedholidays/set:\001*'
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['AddToObservedHolidays']._loaded_options = None
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['AddToObservedHolidays']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\002+\"&/api/v1alpha1/org/observedholidays/add:\001*'
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['RemoveObservedHolidays']._loaded_options = None
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['RemoveObservedHolidays']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\002.\")/api/v1alpha1/org/observedholidays/remove:\001*'
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['UpdateObservedHolidaysInfo']._loaded_options = None
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['UpdateObservedHolidaysInfo']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\0022\"-/api/v1alpha1/org/observedholidays/updateinfo:\001*'
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['DeleteObservedHolidays']._loaded_options = None
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['DeleteObservedHolidays']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\002.\")/api/v1alpha1/org/observedholidays/delete:\001*'
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['EvaluateObservedHolidays']._loaded_options = None
  _globals['_OBSERVEDHOLIDAYSSERVICE'].methods_by_name['EvaluateObservedHolidays']._serialized_options = b'\272\270\221\002\004\n\002\010e\202\323\344\223\0020\"+/api/v1alpha1/org/observedholidays/evaluate:\001*'
  _globals['_OBSERVEDHOLIDAYSSERVICE']._serialized_start=192
  _globals['_OBSERVEDHOLIDAYSSERVICE']._serialized_end=1995
# @@protoc_insertion_point(module_scope)