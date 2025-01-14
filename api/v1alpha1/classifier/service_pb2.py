# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/classifier/service.proto
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
    'api/v1alpha1/classifier/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons import classifier_pb2 as api_dot_commons_dot_classifier__pb2
from api.v1alpha1.classifier import entities_pb2 as api_dot_v1alpha1_dot_classifier_dot_entities__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/v1alpha1/classifier/service.proto\x12\x17\x61pi.v1alpha1.classifier\x1a\x17\x61nnotations/authz.proto\x1a\x1c\x61pi/commons/classifier.proto\x1a&api/v1alpha1/classifier/entities.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9c\x04\n\x10ParseFileRequest\x12\x1b\n\x08raw_data\x18\x03 \x01(\x0cH\x00R\x07rawData\x12Z\n\x0creparse_file\x18\x04 \x01(\x0b\x32\x35.api.v1alpha1.classifier.ParseFileRequest.ReParseFileH\x00R\x0breparseFile\x12\x64\n\x10parse_with_hints\x18\x06 \x01(\x0b\x32\x38.api.v1alpha1.classifier.ParseFileRequest.ParseWithHintsH\x00R\x0eparseWithHints\x12\x12\n\x04name\x18\x05 \x01(\tR\x04name\x1a\xad\x01\n\x0bReParseFile\x12,\n\x10\x66ile_template_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0e\x66ileTemplateId\x12=\n\x05hints\x18\x02 \x01(\x0b\x32#.api.v1alpha1.classifier.ParseHintsB\x02\x18\x01R\x05hints\x12\x31\n\x04opts\x18\x03 \x01(\x0b\x32\x1d.api.v1alpha1.classifier.OptsR\x04opts\x1a^\n\x0eParseWithHints\x12\x19\n\x08raw_data\x18\x07 \x01(\x0cR\x07rawData\x12\x31\n\x04opts\x18\x08 \x01(\x0b\x32\x1d.api.v1alpha1.classifier.OptsR\x04optsB\x05\n\x03opt\"_\n\x11ParseFileResponse\x12J\n\rfile_template\x18\x01 \x01(\x0b\x32%.api.v1alpha1.classifier.FileTemplateR\x0c\x66ileTemplate\"g\n\x19UpdateFileTemplateRequest\x12J\n\rfile_template\x18\x01 \x01(\x0b\x32%.api.v1alpha1.classifier.FileTemplateR\x0c\x66ileTemplate\"\x1c\n\x1aUpdateFileTemplateResponse\"D\n\x19\x44\x65leteFileTemplateRequest\x12\'\n\rfile_template\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0c\x66ileTemplate\"\x1c\n\x1a\x44\x65leteFileTemplateResponse\"f\n\x18ListFileTemplatesRequest\x12\x1b\n\x07prev_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x06prevId\x12\x10\n\x03\x61sc\x18\x02 \x01(\x08R\x03\x61sc\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\"i\n\x19ListFileTemplatesResponse\x12L\n\x0e\x66ile_templates\x18\x01 \x03(\x0b\x32%.api.v1alpha1.classifier.FileTemplateR\rfileTemplates\"F\n\x16GetFileTemplateRequest\x12,\n\x10\x66ile_template_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0e\x66ileTemplateId\"e\n\x17GetFileTemplateResponse\x12J\n\rfile_template\x18\x01 \x01(\x0b\x32%.api.v1alpha1.classifier.FileTemplateR\x0c\x66ileTemplate\"\xf3\x01\n\x11ListEventsRequest\x12\x1d\n\nelement_id\x18\x01 \x01(\tR\telementId\x12\x30\n\x05\x62\x65gin\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05\x62\x65gin\x12,\n\x03\x65nd\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03\x65nd\x12\x1d\n\ntime_range\x18\x04 \x01(\tR\ttimeRange\x12#\n\rentrypoint_id\x18\x05 \x01(\tR\x0c\x65ntrypointId\x12\x1b\n\tparent_id\x18\x06 \x01(\tR\x08parentId\"\xe5\x05\n\x12ListEventsResponse\x12\x43\n\x04rows\x18\x01 \x03(\x0b\x32/.api.v1alpha1.classifier.ListEventsResponse.RowR\x04rows\x1a\x89\x05\n\x03Row\x12,\n\x12input_record_count\x18\x01 \x01(\x03R\x10inputRecordCount\x12.\n\x13output_record_count\x18\x02 \x01(\x03R\x11outputRecordCount\x12\x34\n\x16\x64iscarded_record_count\x18\x03 \x01(\x03R\x14\x64iscardedRecordCount\x12\x30\n\x05\x62\x65gin\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05\x62\x65gin\x12,\n\x03\x65nd\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03\x65nd\x12\x1d\n\nelement_id\x18\x06 \x01(\tR\telementId\x12 \n\x0b\x65ntrypoints\x18\x07 \x03(\tR\x0b\x65ntrypoints\x12\x1d\n\nparent_ids\x18\x08 \x03(\tR\tparentIds\x12\x18\n\x07\x63olumns\x18\t \x03(\tR\x07\x63olumns\x12;\n\x18total_queue_wait_seconds\x18\n \x01(\x03\x42\x02\x18\x01R\x15totalQueueWaitSeconds\x12<\n\x18total_processing_seconds\x18\x0b \x01(\x03\x42\x02\x18\x01R\x16totalProcessingSeconds\x12\x41\n\x1dtotal_queue_wait_milliseconds\x18\r \x01(\x03R\x1atotalQueueWaitMilliseconds\x12\x42\n\x1dtotal_processing_milliseconds\x18\x0e \x01(\x03R\x1btotalProcessingMilliseconds\x12\x12\n\x04msgs\x18\x0c \x03(\tR\x04msgs\"\x82\x03\n\x0fPeekListRequest\x12\x30\n\x05\x62\x65gin\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05\x62\x65gin\x12,\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03\x65nd\x12!\n\x0c\x65xternal_tag\x18\x03 \x01(\tR\x0b\x65xternalTag\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x10\n\x03\x61sc\x18\x05 \x01(\x08R\x03\x61sc\x12\x1b\n\tpage_size\x18\x06 \x01(\x05R\x08pageSize\x12\x1d\n\nelement_id\x18\x07 \x01(\tR\telementId\x12\x18\n\x07\x63olumns\x18\x08 \x03(\tR\x07\x63olumns\x12#\n\rentrypoint_id\x18\t \x01(\tR\x0c\x65ntrypointId\x12\x1b\n\tparent_id\x18\n \x01(\tR\x08parentId\x12#\n\rview_discards\x18\x0b \x01(\x08R\x0cviewDiscards\"T\n\x10PeekListResponse\x12!\n\x0cjson_records\x18\x01 \x03(\tR\x0bjsonRecords\x12\x1d\n\npage_token\x18\x02 \x01(\tR\tpageToken2\x88\n\n\x17\x43lassifierFileTemplates\x12\xa6\x01\n\tParseFile\x12).api.v1alpha1.classifier.ParseFileRequest\x1a*.api.v1alpha1.classifier.ParseFileResponse\"B\xba\xb8\x91\x02\x05\n\x03\x08\xe9\x07\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/classifier/file_templates/parse:\x01*\x12\xa0\x01\n\nListEvents\x12*.api.v1alpha1.classifier.ListEventsRequest\x1a+.api.v1alpha1.classifier.ListEventsResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\xe9\x07\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/classifier/events/list:\x01*\x12\x9d\x01\n\x08PeekList\x12(.api.v1alpha1.classifier.PeekListRequest\x1a).api.v1alpha1.classifier.PeekListResponse\"<\xba\xb8\x91\x02\x05\n\x03\x08\xe9\x07\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/classifier/events/preview:\x01*\x12\xc2\x01\n\x12UpdateFileTemplate\x12\x32.api.v1alpha1.classifier.UpdateFileTemplateRequest\x1a\x33.api.v1alpha1.classifier.UpdateFileTemplateResponse\"C\xba\xb8\x91\x02\x05\n\x03\x08\xe9\x07\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/classifier/file_templates/update:\x01*\x12\xc2\x01\n\x12\x44\x65leteFileTemplate\x12\x32.api.v1alpha1.classifier.DeleteFileTemplateRequest\x1a\x33.api.v1alpha1.classifier.DeleteFileTemplateResponse\"C\xba\xb8\x91\x02\x05\n\x03\x08\xe9\x07\x82\xd3\xe4\x93\x02\x33*./api/v1alpha1/classifier/file_templates/delete:\x01*\x12\xbd\x01\n\x11ListFileTemplates\x12\x31.api.v1alpha1.classifier.ListFileTemplatesRequest\x1a\x32.api.v1alpha1.classifier.ListFileTemplatesResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xe9\x07\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/classifier/file_templates/list:\x01*\x12\xb6\x01\n\x0fGetFileTemplate\x12/.api.v1alpha1.classifier.GetFileTemplateRequest\x1a\x30.api.v1alpha1.classifier.GetFileTemplateResponse\"@\xba\xb8\x91\x02\x05\n\x03\x08\xe9\x07\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/classifier/file_templates/get:\x01*B\xa9\x01\n\x1b\x63om.api.v1alpha1.classifierB\x0cServiceProtoP\x01\xa2\x02\x03\x41VC\xaa\x02\x17\x41pi.V1alpha1.Classifier\xca\x02\x17\x41pi\\V1alpha1\\Classifier\xe2\x02#Api\\V1alpha1\\Classifier\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Classifierb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.classifier.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.classifierB\014ServiceProtoP\001\242\002\003AVC\252\002\027Api.V1alpha1.Classifier\312\002\027Api\\V1alpha1\\Classifier\342\002#Api\\V1alpha1\\Classifier\\GPBMetadata\352\002\031Api::V1alpha1::Classifier'
  _globals['_PARSEFILEREQUEST_REPARSEFILE'].fields_by_name['file_template_id']._loaded_options = None
  _globals['_PARSEFILEREQUEST_REPARSEFILE'].fields_by_name['file_template_id']._serialized_options = b'0\001'
  _globals['_PARSEFILEREQUEST_REPARSEFILE'].fields_by_name['hints']._loaded_options = None
  _globals['_PARSEFILEREQUEST_REPARSEFILE'].fields_by_name['hints']._serialized_options = b'\030\001'
  _globals['_DELETEFILETEMPLATEREQUEST'].fields_by_name['file_template']._loaded_options = None
  _globals['_DELETEFILETEMPLATEREQUEST'].fields_by_name['file_template']._serialized_options = b'0\001'
  _globals['_LISTFILETEMPLATESREQUEST'].fields_by_name['prev_id']._loaded_options = None
  _globals['_LISTFILETEMPLATESREQUEST'].fields_by_name['prev_id']._serialized_options = b'0\001'
  _globals['_GETFILETEMPLATEREQUEST'].fields_by_name['file_template_id']._loaded_options = None
  _globals['_GETFILETEMPLATEREQUEST'].fields_by_name['file_template_id']._serialized_options = b'0\001'
  _globals['_LISTEVENTSRESPONSE_ROW'].fields_by_name['total_queue_wait_seconds']._loaded_options = None
  _globals['_LISTEVENTSRESPONSE_ROW'].fields_by_name['total_queue_wait_seconds']._serialized_options = b'\030\001'
  _globals['_LISTEVENTSRESPONSE_ROW'].fields_by_name['total_processing_seconds']._loaded_options = None
  _globals['_LISTEVENTSRESPONSE_ROW'].fields_by_name['total_processing_seconds']._serialized_options = b'\030\001'
  _globals['_CLASSIFIERFILETEMPLATES'].methods_by_name['ParseFile']._loaded_options = None
  _globals['_CLASSIFIERFILETEMPLATES'].methods_by_name['ParseFile']._serialized_options = b'\272\270\221\002\005\n\003\010\351\007\202\323\344\223\0022\"-/api/v1alpha1/classifier/file_templates/parse:\001*'
  _globals['_CLASSIFIERFILETEMPLATES'].methods_by_name['ListEvents']._loaded_options = None
  _globals['_CLASSIFIERFILETEMPLATES'].methods_by_name['ListEvents']._serialized_options = b'\272\270\221\002\005\n\003\010\351\007\202\323\344\223\002)\"$/api/v1alpha1/classifier/events/list:\001*'
  _globals['_CLASSIFIERFILETEMPLATES'].methods_by_name['PeekList']._loaded_options = None
  _globals['_CLASSIFIERFILETEMPLATES'].methods_by_name['PeekList']._serialized_options = b'\272\270\221\002\005\n\003\010\351\007\202\323\344\223\002,\"\'/api/v1alpha1/classifier/events/preview:\001*'
  _globals['_CLASSIFIERFILETEMPLATES'].methods_by_name['UpdateFileTemplate']._loaded_options = None
  _globals['_CLASSIFIERFILETEMPLATES'].methods_by_name['UpdateFileTemplate']._serialized_options = b'\272\270\221\002\005\n\003\010\351\007\202\323\344\223\0023\"./api/v1alpha1/classifier/file_templates/update:\001*'
  _globals['_CLASSIFIERFILETEMPLATES'].methods_by_name['DeleteFileTemplate']._loaded_options = None
  _globals['_CLASSIFIERFILETEMPLATES'].methods_by_name['DeleteFileTemplate']._serialized_options = b'\272\270\221\002\005\n\003\010\351\007\202\323\344\223\0023*./api/v1alpha1/classifier/file_templates/delete:\001*'
  _globals['_CLASSIFIERFILETEMPLATES'].methods_by_name['ListFileTemplates']._loaded_options = None
  _globals['_CLASSIFIERFILETEMPLATES'].methods_by_name['ListFileTemplates']._serialized_options = b'\272\270\221\002\005\n\003\010\351\007\202\323\344\223\0021\",/api/v1alpha1/classifier/file_templates/list:\001*'
  _globals['_CLASSIFIERFILETEMPLATES'].methods_by_name['GetFileTemplate']._loaded_options = None
  _globals['_CLASSIFIERFILETEMPLATES'].methods_by_name['GetFileTemplate']._serialized_options = b'\272\270\221\002\005\n\003\010\351\007\202\323\344\223\0020\"+/api/v1alpha1/classifier/file_templates/get:\001*'
  _globals['_PARSEFILEREQUEST']._serialized_start=225
  _globals['_PARSEFILEREQUEST']._serialized_end=765
  _globals['_PARSEFILEREQUEST_REPARSEFILE']._serialized_start=489
  _globals['_PARSEFILEREQUEST_REPARSEFILE']._serialized_end=662
  _globals['_PARSEFILEREQUEST_PARSEWITHHINTS']._serialized_start=664
  _globals['_PARSEFILEREQUEST_PARSEWITHHINTS']._serialized_end=758
  _globals['_PARSEFILERESPONSE']._serialized_start=767
  _globals['_PARSEFILERESPONSE']._serialized_end=862
  _globals['_UPDATEFILETEMPLATEREQUEST']._serialized_start=864
  _globals['_UPDATEFILETEMPLATEREQUEST']._serialized_end=967
  _globals['_UPDATEFILETEMPLATERESPONSE']._serialized_start=969
  _globals['_UPDATEFILETEMPLATERESPONSE']._serialized_end=997
  _globals['_DELETEFILETEMPLATEREQUEST']._serialized_start=999
  _globals['_DELETEFILETEMPLATEREQUEST']._serialized_end=1067
  _globals['_DELETEFILETEMPLATERESPONSE']._serialized_start=1069
  _globals['_DELETEFILETEMPLATERESPONSE']._serialized_end=1097
  _globals['_LISTFILETEMPLATESREQUEST']._serialized_start=1099
  _globals['_LISTFILETEMPLATESREQUEST']._serialized_end=1201
  _globals['_LISTFILETEMPLATESRESPONSE']._serialized_start=1203
  _globals['_LISTFILETEMPLATESRESPONSE']._serialized_end=1308
  _globals['_GETFILETEMPLATEREQUEST']._serialized_start=1310
  _globals['_GETFILETEMPLATEREQUEST']._serialized_end=1380
  _globals['_GETFILETEMPLATERESPONSE']._serialized_start=1382
  _globals['_GETFILETEMPLATERESPONSE']._serialized_end=1483
  _globals['_LISTEVENTSREQUEST']._serialized_start=1486
  _globals['_LISTEVENTSREQUEST']._serialized_end=1729
  _globals['_LISTEVENTSRESPONSE']._serialized_start=1732
  _globals['_LISTEVENTSRESPONSE']._serialized_end=2473
  _globals['_LISTEVENTSRESPONSE_ROW']._serialized_start=1824
  _globals['_LISTEVENTSRESPONSE_ROW']._serialized_end=2473
  _globals['_PEEKLISTREQUEST']._serialized_start=2476
  _globals['_PEEKLISTREQUEST']._serialized_end=2862
  _globals['_PEEKLISTRESPONSE']._serialized_start=2864
  _globals['_PEEKLISTRESPONSE']._serialized_end=2948
  _globals['_CLASSIFIERFILETEMPLATES']._serialized_start=2951
  _globals['_CLASSIFIERFILETEMPLATES']._serialized_end=4239
# @@protoc_insertion_point(module_scope)
