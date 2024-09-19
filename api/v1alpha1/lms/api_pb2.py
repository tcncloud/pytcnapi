# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/lms/api.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'api/v1alpha1/lms/api.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.lms import entities_pb2 as api_dot_v1alpha1_dot_lms_dot_entities__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x61pi/v1alpha1/lms/api.proto\x12\x10\x61pi.v1alpha1.lms\x1a\x17\x61nnotations/authz.proto\x1a\x1f\x61pi/v1alpha1/lms/entities.proto\x1a\x1cgoogle/api/annotations.proto\"b\n\x19\x44\x65leteFileTemplateRequest\x12\x45\n\rfile_template\x18\x01 \x01(\x0b\x32 .api.v1alpha1.lms.FileTemplateV2R\x0c\x66ileTemplate\"c\n\x1a\x44\x65leteFileTemplateResponse\x12\x45\n\rfile_template\x18\x01 \x01(\x0b\x32 .api.v1alpha1.lms.FileTemplateV2R\x0c\x66ileTemplate\"_\n\x16GetFileTemplateRequest\x12\x45\n\rfile_template\x18\x01 \x01(\x0b\x32 .api.v1alpha1.lms.FileTemplateV2R\x0c\x66ileTemplate\"`\n\x17GetFileTemplateResponse\x12\x45\n\rfile_template\x18\x01 \x01(\x0b\x32 .api.v1alpha1.lms.FileTemplateV2R\x0c\x66ileTemplate\"\x88\x01\n\x18ListFileTemplatesRequest\x12\x36\n\x05value\x18\x01 \x01(\x0b\x32 .api.v1alpha1.lms.FileTemplateV2R\x05value\x12\x17\n\x07last_id\x18\x02 \x01(\tR\x06lastId\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\"d\n\x19ListFileTemplatesResponse\x12G\n\x0e\x66ile_templates\x18\x01 \x03(\x0b\x32 .api.v1alpha1.lms.FileTemplateV2R\rfileTemplates\"\xc0\x01\n\x18ParseFileTemplateRequest\x12\x42\n\x0cnew_template\x18\x01 \x01(\x0b\x32\x1d.api.v1alpha1.lms.NewTemplateH\x00R\x0bnewTemplate\x12Q\n\x11\x65xisting_template\x18\x02 \x01(\x0b\x32\".api.v1alpha1.lms.ExistingTemplateH\x00R\x10\x65xistingTemplateB\r\n\x0bretrieve_by\"\x19\n\x17ParseFileTemplateResult\"b\n\x19UpdateFileTemplateRequest\x12\x45\n\rfile_template\x18\x01 \x01(\x0b\x32 .api.v1alpha1.lms.FileTemplateV2R\x0c\x66ileTemplate\"c\n\x1aUpdateFileTemplateResponse\x12\x45\n\rfile_template\x18\x01 \x01(\x0b\x32 .api.v1alpha1.lms.FileTemplateV2R\x0c\x66ileTemplate2\xd0\x06\n\x03LMS\x12\xaa\x01\n\x12\x44\x65leteFileTemplate\x12+.api.v1alpha1.lms.DeleteFileTemplateRequest\x1a,.api.v1alpha1.lms.DeleteFileTemplateResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\xe9\x07\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/lms/deletefiletemplate:\x01*\x12\x9e\x01\n\x0fGetFileTemplate\x12(.api.v1alpha1.lms.GetFileTemplateRequest\x1a).api.v1alpha1.lms.GetFileTemplateResponse\"6\xba\xb8\x91\x02\x05\n\x03\x08\xe8\x07\x82\xd3\xe4\x93\x02&\"!/api/v1alpha1/lms/getfiletemplate:\x01*\x12\xa6\x01\n\x11ListFileTemplates\x12*.api.v1alpha1.lms.ListFileTemplatesRequest\x1a+.api.v1alpha1.lms.ListFileTemplatesResponse\"8\xba\xb8\x91\x02\x05\n\x03\x08\xe8\x07\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/lms/listfiletemplates:\x01*\x12\xa4\x01\n\x11ParseFileTemplate\x12*.api.v1alpha1.lms.ParseFileTemplateRequest\x1a).api.v1alpha1.lms.ParseFileTemplateResult\"8\xba\xb8\x91\x02\x05\n\x03\x08\xe9\x07\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/lms/parsefiletemplate:\x01*\x12\xaa\x01\n\x12UpdateFileTemplate\x12+.api.v1alpha1.lms.UpdateFileTemplateRequest\x1a,.api.v1alpha1.lms.UpdateFileTemplateResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\xe9\x07\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/lms/updatefiletemplate:\x01*B\x82\x01\n\x14\x63om.api.v1alpha1.lmsB\x08\x41piProtoP\x01\xa2\x02\x03\x41VL\xaa\x02\x10\x41pi.V1alpha1.Lms\xca\x02\x10\x41pi\\V1alpha1\\Lms\xe2\x02\x1c\x41pi\\V1alpha1\\Lms\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Lmsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.lms.api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.lmsB\010ApiProtoP\001\242\002\003AVL\252\002\020Api.V1alpha1.Lms\312\002\020Api\\V1alpha1\\Lms\342\002\034Api\\V1alpha1\\Lms\\GPBMetadata\352\002\022Api::V1alpha1::Lms'
  _globals['_LMS'].methods_by_name['DeleteFileTemplate']._loaded_options = None
  _globals['_LMS'].methods_by_name['DeleteFileTemplate']._serialized_options = b'\272\270\221\002\005\n\003\010\351\007\202\323\344\223\002)\"$/api/v1alpha1/lms/deletefiletemplate:\001*'
  _globals['_LMS'].methods_by_name['GetFileTemplate']._loaded_options = None
  _globals['_LMS'].methods_by_name['GetFileTemplate']._serialized_options = b'\272\270\221\002\005\n\003\010\350\007\202\323\344\223\002&\"!/api/v1alpha1/lms/getfiletemplate:\001*'
  _globals['_LMS'].methods_by_name['ListFileTemplates']._loaded_options = None
  _globals['_LMS'].methods_by_name['ListFileTemplates']._serialized_options = b'\272\270\221\002\005\n\003\010\350\007\202\323\344\223\002(\"#/api/v1alpha1/lms/listfiletemplates:\001*'
  _globals['_LMS'].methods_by_name['ParseFileTemplate']._loaded_options = None
  _globals['_LMS'].methods_by_name['ParseFileTemplate']._serialized_options = b'\272\270\221\002\005\n\003\010\351\007\202\323\344\223\002(\"#/api/v1alpha1/lms/parsefiletemplate:\001*'
  _globals['_LMS'].methods_by_name['UpdateFileTemplate']._loaded_options = None
  _globals['_LMS'].methods_by_name['UpdateFileTemplate']._serialized_options = b'\272\270\221\002\005\n\003\010\351\007\202\323\344\223\002)\"$/api/v1alpha1/lms/updatefiletemplate:\001*'
  _globals['_DELETEFILETEMPLATEREQUEST']._serialized_start=136
  _globals['_DELETEFILETEMPLATEREQUEST']._serialized_end=234
  _globals['_DELETEFILETEMPLATERESPONSE']._serialized_start=236
  _globals['_DELETEFILETEMPLATERESPONSE']._serialized_end=335
  _globals['_GETFILETEMPLATEREQUEST']._serialized_start=337
  _globals['_GETFILETEMPLATEREQUEST']._serialized_end=432
  _globals['_GETFILETEMPLATERESPONSE']._serialized_start=434
  _globals['_GETFILETEMPLATERESPONSE']._serialized_end=530
  _globals['_LISTFILETEMPLATESREQUEST']._serialized_start=533
  _globals['_LISTFILETEMPLATESREQUEST']._serialized_end=669
  _globals['_LISTFILETEMPLATESRESPONSE']._serialized_start=671
  _globals['_LISTFILETEMPLATESRESPONSE']._serialized_end=771
  _globals['_PARSEFILETEMPLATEREQUEST']._serialized_start=774
  _globals['_PARSEFILETEMPLATEREQUEST']._serialized_end=966
  _globals['_PARSEFILETEMPLATERESULT']._serialized_start=968
  _globals['_PARSEFILETEMPLATERESULT']._serialized_end=993
  _globals['_UPDATEFILETEMPLATEREQUEST']._serialized_start=995
  _globals['_UPDATEFILETEMPLATEREQUEST']._serialized_end=1093
  _globals['_UPDATEFILETEMPLATERESPONSE']._serialized_start=1095
  _globals['_UPDATEFILETEMPLATERESPONSE']._serialized_end=1194
  _globals['_LMS']._serialized_start=1197
  _globals['_LMS']._serialized_end=2045
# @@protoc_insertion_point(module_scope)
