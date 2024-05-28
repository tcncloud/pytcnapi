# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/bireportgenerator/service.proto
# Protobuf Python Version: 5.27.0
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
    0,
    '',
    'api/v1alpha1/bireportgenerator/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.bireportgenerator import entities_pb2 as api_dot_v1alpha1_dot_bireportgenerator_dot_entities__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,api/v1alpha1/bireportgenerator/service.proto\x12\x1e\x61pi.v1alpha1.bireportgenerator\x1a\x17\x61nnotations/authz.proto\x1a-api/v1alpha1/bireportgenerator/entities.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"b\n\x16\x43reateReportJobRequest\x12H\n\nreport_job\x18\x01 \x01(\x0b\x32).api.v1alpha1.bireportgenerator.ReportJobR\treportJob\"c\n\x17\x43reateReportJobResponse\x12H\n\nreport_job\x18\x01 \x01(\x0b\x32).api.v1alpha1.bireportgenerator.ReportJobR\treportJob\"\x17\n\x15ListReportJobsRequest\"d\n\x16ListReportJobsResponse\x12J\n\x0breport_jobs\x18\x01 \x03(\x0b\x32).api.v1alpha1.bireportgenerator.ReportJobR\nreportJobs\"\x9f\x01\n\x16UpdateReportJobRequest\x12H\n\nreport_job\x18\x01 \x01(\x0b\x32).api.v1alpha1.bireportgenerator.ReportJobR\treportJob\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"c\n\x17UpdateReportJobResponse\x12H\n\nreport_job\x18\x01 \x01(\x0b\x32).api.v1alpha1.bireportgenerator.ReportJobR\treportJob\"<\n\x16\x44\x65leteReportJobRequest\x12\"\n\rreport_job_id\x18\x01 \x01(\tR\x0breportJobId\"\x19\n\x17\x44\x65leteReportJobResponse\"9\n\x13GetReportJobRequest\x12\"\n\rreport_job_id\x18\x01 \x01(\tR\x0breportJobId\"`\n\x14GetReportJobResponse\x12H\n\nreport_job\x18\x01 \x01(\x0b\x32).api.v1alpha1.bireportgenerator.ReportJobR\treportJob\"\xa4\x01\n\x15GenerateReportRequest\x12H\n\nreport_job\x18\x01 \x01(\x0b\x32).api.v1alpha1.bireportgenerator.ReportJobR\treportJob\x12\x41\n\x0fsend_as_of_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0csendAsOfDate\"\x18\n\x16GenerateReportResponse2\x9c\n\n\x18\x42IReportGeneratorService\x12\xd6\x01\n\x0f\x43reateReportJob\x12\x36.api.v1alpha1.bireportgenerator.CreateReportJobRequest\x1a\x37.api.v1alpha1.bireportgenerator.CreateReportJobResponse\"R\xba\xb8\x91\x02\x05\n\x03\x08\xe1\x04\x82\xd3\xe4\x93\x02\x42\"=/api/v1alpha1/reportgenerator/reportgenerator/createreportjob:\x01*\x12\xd2\x01\n\x0eListReportJobs\x12\x35.api.v1alpha1.bireportgenerator.ListReportJobsRequest\x1a\x36.api.v1alpha1.bireportgenerator.ListReportJobsResponse\"Q\xba\xb8\x91\x02\x05\n\x03\x08\xe1\x04\x82\xd3\xe4\x93\x02\x41\"</api/v1alpha1/reportgenerator/reportgenerator/listreportjobs:\x01*\x12\xd6\x01\n\x0fUpdateReportJob\x12\x36.api.v1alpha1.bireportgenerator.UpdateReportJobRequest\x1a\x37.api.v1alpha1.bireportgenerator.UpdateReportJobResponse\"R\xba\xb8\x91\x02\x05\n\x03\x08\xe1\x04\x82\xd3\xe4\x93\x02\x42\"=/api/v1alpha1/reportgenerator/reportgenerator/updatereportjob:\x01*\x12\xd6\x01\n\x0f\x44\x65leteReportJob\x12\x36.api.v1alpha1.bireportgenerator.DeleteReportJobRequest\x1a\x37.api.v1alpha1.bireportgenerator.DeleteReportJobResponse\"R\xba\xb8\x91\x02\x05\n\x03\x08\xe1\x04\x82\xd3\xe4\x93\x02\x42\"=/api/v1alpha1/reportgenerator/reportgenerator/deletereportjob:\x01*\x12\xca\x01\n\x0cGetReportJob\x12\x33.api.v1alpha1.bireportgenerator.GetReportJobRequest\x1a\x34.api.v1alpha1.bireportgenerator.GetReportJobResponse\"O\xba\xb8\x91\x02\x05\n\x03\x08\xe1\x04\x82\xd3\xe4\x93\x02?\":/api/v1alpha1/reportgenerator/reportgenerator/getreportjob:\x01*\x12\xd2\x01\n\x0eGenerateReport\x12\x35.api.v1alpha1.bireportgenerator.GenerateReportRequest\x1a\x36.api.v1alpha1.bireportgenerator.GenerateReportResponse\"Q\xba\xb8\x91\x02\x05\n\x03\x08\xe1\x04\x82\xd3\xe4\x93\x02\x41\"</api/v1alpha1/reportgenerator/reportgenerator/generatereport:\x01*B\xcc\x01\n\"com.api.v1alpha1.bireportgeneratorB\x0cServiceProtoP\x01\xa2\x02\x03\x41VB\xaa\x02\x1e\x41pi.V1alpha1.Bireportgenerator\xca\x02\x1e\x41pi\\V1alpha1\\Bireportgenerator\xe2\x02*Api\\V1alpha1\\Bireportgenerator\\GPBMetadata\xea\x02 Api::V1alpha1::Bireportgeneratorb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.bireportgenerator.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.api.v1alpha1.bireportgeneratorB\014ServiceProtoP\001\242\002\003AVB\252\002\036Api.V1alpha1.Bireportgenerator\312\002\036Api\\V1alpha1\\Bireportgenerator\342\002*Api\\V1alpha1\\Bireportgenerator\\GPBMetadata\352\002 Api::V1alpha1::Bireportgenerator'
  _globals['_BIREPORTGENERATORSERVICE'].methods_by_name['CreateReportJob']._loaded_options = None
  _globals['_BIREPORTGENERATORSERVICE'].methods_by_name['CreateReportJob']._serialized_options = b'\272\270\221\002\005\n\003\010\341\004\202\323\344\223\002B\"=/api/v1alpha1/reportgenerator/reportgenerator/createreportjob:\001*'
  _globals['_BIREPORTGENERATORSERVICE'].methods_by_name['ListReportJobs']._loaded_options = None
  _globals['_BIREPORTGENERATORSERVICE'].methods_by_name['ListReportJobs']._serialized_options = b'\272\270\221\002\005\n\003\010\341\004\202\323\344\223\002A\"</api/v1alpha1/reportgenerator/reportgenerator/listreportjobs:\001*'
  _globals['_BIREPORTGENERATORSERVICE'].methods_by_name['UpdateReportJob']._loaded_options = None
  _globals['_BIREPORTGENERATORSERVICE'].methods_by_name['UpdateReportJob']._serialized_options = b'\272\270\221\002\005\n\003\010\341\004\202\323\344\223\002B\"=/api/v1alpha1/reportgenerator/reportgenerator/updatereportjob:\001*'
  _globals['_BIREPORTGENERATORSERVICE'].methods_by_name['DeleteReportJob']._loaded_options = None
  _globals['_BIREPORTGENERATORSERVICE'].methods_by_name['DeleteReportJob']._serialized_options = b'\272\270\221\002\005\n\003\010\341\004\202\323\344\223\002B\"=/api/v1alpha1/reportgenerator/reportgenerator/deletereportjob:\001*'
  _globals['_BIREPORTGENERATORSERVICE'].methods_by_name['GetReportJob']._loaded_options = None
  _globals['_BIREPORTGENERATORSERVICE'].methods_by_name['GetReportJob']._serialized_options = b'\272\270\221\002\005\n\003\010\341\004\202\323\344\223\002?\":/api/v1alpha1/reportgenerator/reportgenerator/getreportjob:\001*'
  _globals['_BIREPORTGENERATORSERVICE'].methods_by_name['GenerateReport']._loaded_options = None
  _globals['_BIREPORTGENERATORSERVICE'].methods_by_name['GenerateReport']._serialized_options = b'\272\270\221\002\005\n\003\010\341\004\202\323\344\223\002A\"</api/v1alpha1/reportgenerator/reportgenerator/generatereport:\001*'
  _globals['_CREATEREPORTJOBREQUEST']._serialized_start=249
  _globals['_CREATEREPORTJOBREQUEST']._serialized_end=347
  _globals['_CREATEREPORTJOBRESPONSE']._serialized_start=349
  _globals['_CREATEREPORTJOBRESPONSE']._serialized_end=448
  _globals['_LISTREPORTJOBSREQUEST']._serialized_start=450
  _globals['_LISTREPORTJOBSREQUEST']._serialized_end=473
  _globals['_LISTREPORTJOBSRESPONSE']._serialized_start=475
  _globals['_LISTREPORTJOBSRESPONSE']._serialized_end=575
  _globals['_UPDATEREPORTJOBREQUEST']._serialized_start=578
  _globals['_UPDATEREPORTJOBREQUEST']._serialized_end=737
  _globals['_UPDATEREPORTJOBRESPONSE']._serialized_start=739
  _globals['_UPDATEREPORTJOBRESPONSE']._serialized_end=838
  _globals['_DELETEREPORTJOBREQUEST']._serialized_start=840
  _globals['_DELETEREPORTJOBREQUEST']._serialized_end=900
  _globals['_DELETEREPORTJOBRESPONSE']._serialized_start=902
  _globals['_DELETEREPORTJOBRESPONSE']._serialized_end=927
  _globals['_GETREPORTJOBREQUEST']._serialized_start=929
  _globals['_GETREPORTJOBREQUEST']._serialized_end=986
  _globals['_GETREPORTJOBRESPONSE']._serialized_start=988
  _globals['_GETREPORTJOBRESPONSE']._serialized_end=1084
  _globals['_GENERATEREPORTREQUEST']._serialized_start=1087
  _globals['_GENERATEREPORTREQUEST']._serialized_end=1251
  _globals['_GENERATEREPORTRESPONSE']._serialized_start=1253
  _globals['_GENERATEREPORTRESPONSE']._serialized_end=1277
  _globals['_BIREPORTGENERATORSERVICE']._serialized_start=1280
  _globals['_BIREPORTGENERATORSERVICE']._serialized_end=2588
# @@protoc_insertion_point(module_scope)
