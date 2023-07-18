# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v0alpha/learn.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61pi/v0alpha/learn.proto\x12\x0b\x61pi.v0alpha\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"4\n\x08\x45xistReq\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\" \n\x08\x45xistRes\x12\x14\n\x05\x65xist\x18\x01 \x01(\x08R\x05\x65xist\"6\n\nContentReq\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\"\xa7\x01\n\nContentRes\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\x12N\n\x15last_edited_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x13lastEditedTimestamp\x12/\n\x06images\x18\x03 \x03(\x0b\x32\x17.api.v0alpha.LearnImageR\x06images\"@\n\x14\x43ontentEditorDataReq\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\"@\n\x14\x43ontentEditorDataRes\x12(\n\x10last_edited_user\x18\x01 \x01(\tR\x0elastEditedUser\"i\n\tUpdateReq\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\x12\x18\n\x07\x63ontent\x18\x03 \x01(\tR\x07\x63ontent\x12\x18\n\x07message\x18\x0c \x01(\tR\x07message\"\x0b\n\tUpdateRes\"S\n\rExportManyReq\x12\x10\n\x03url\x18\x01 \x03(\tR\x03url\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\x12\x18\n\x07\x63ontent\x18\x03 \x01(\tR\x07\x63ontent\".\n\tExportRes\x12!\n\x0c\x64ownload_url\x18\x01 \x01(\tR\x0b\x64ownloadUrl\"D\n\x13StoreStaticImageReq\x12-\n\x05image\x18\x01 \x01(\x0b\x32\x17.api.v0alpha.LearnImageR\x05image\"]\n\nLearnImage\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12\x18\n\x07\x63ontent\x18\x02 \x01(\tR\x07\x63ontent\x12!\n\x0c\x64ownload_url\x18\x03 \x01(\tR\x0b\x64ownloadUrl\"D\n\x13StoreStaticImageRes\x12-\n\x05image\x18\x01 \x01(\x0b\x32\x17.api.v0alpha.LearnImageR\x05image\"\x8c\x01\n\x10SearchContentReq\x12%\n\x0esearch_content\x18\x01 \x01(\tR\rsearchContent\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\x12\x39\n\nfield_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"S\n\tSearchRes\x12\x46\n\x0esearch_details\x18\x01 \x03(\x0b\x32\x1f.api.v0alpha.LearnSearchDetailsR\rsearchDetails\"B\n\x12LearnSearchDetails\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07\x63ontent\x18\x02 \x01(\tR\x07\x63ontent\"\x8c\x01\n\x1aUploadDynamicScreenshotReq\x12\"\n\rdata_learn_id\x18\x01 \x01(\tR\x0b\x64\x61taLearnId\x12\x18\n\x07version\x18\x02 \x01(\x03R\x07version\x12\x16\n\x06locale\x18\x03 \x01(\tR\x06locale\x12\x18\n\x07\x63ontent\x18\x04 \x01(\tR\x07\x63ontent\"c\n\x1aUploadDynamicScreenshotRes\x12\"\n\rdata_learn_id\x18\x01 \x01(\tR\x0b\x64\x61taLearnId\x12!\n\x0c\x64ownload_url\x18\x02 \x01(\tR\x0b\x64ownloadUrl\"\'\n\rStandaloneReq\x12\x16\n\x06locale\x18\x01 \x01(\tR\x06locale\"c\n\rStandaloneRes\x12R\n\x12standalone_details\x18\x01 \x03(\x0b\x32#.api.v0alpha.LearnStandaloneDetailsR\x11standaloneDetails\"\x96\x01\n\x16LearnStandaloneDetails\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07\x63ontent\x18\x02 \x01(\tR\x07\x63ontent\x12N\n\x15last_edited_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x13lastEditedTimestamp\"R\n\x13\x44\x65leteStandaloneReq\x12\x16\n\x06locale\x18\x01 \x01(\tR\x06locale\x12#\n\rarticle_names\x18\x02 \x03(\tR\x0c\x61rticleNames\"\x15\n\x13\x44\x65leteStandaloneRes\"$\n\nSnippetReq\x12\x16\n\x06locale\x18\x01 \x01(\tR\x06locale\"W\n\nSnippetRes\x12I\n\x0fsnippet_details\x18\x01 \x03(\x0b\x32 .api.v0alpha.LearnSnippetDetailsR\x0esnippetDetails\"\x93\x01\n\x13LearnSnippetDetails\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07\x63ontent\x18\x02 \x01(\tR\x07\x63ontent\x12N\n\x15last_edited_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x13lastEditedTimestamp\"?\n\x13\x44\x65leteLearnPagesReq\x12\x16\n\x06locale\x18\x01 \x01(\tR\x06locale\x12\x10\n\x03url\x18\x02 \x03(\tR\x03url\"\x15\n\x13\x44\x65leteLearnPagesRes2\xff\x0b\n\x05Learn\x12\x61\n\x05\x45xist\x12\x15.api.v0alpha.ExistReq\x1a\x15.api.v0alpha.ExistRes\"*\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x1d\"\x18/api/v0alpha/learn/exist:\x01*\x12i\n\x07\x43ontent\x12\x17.api.v0alpha.ContentReq\x1a\x17.api.v0alpha.ContentRes\",\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x1f\"\x1a/api/v0alpha/learn/content:\x01*\x12q\n\nExportMany\x12\x1a.api.v0alpha.ExportManyReq\x1a\x16.api.v0alpha.ExportRes\"/\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\"\"\x1d/api/v0alpha/learn/exportmany:\x01*\x12z\n\rSearchContent\x12\x1d.api.v0alpha.SearchContentReq\x1a\x16.api.v0alpha.SearchRes\"2\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02%\" /api/v0alpha/learn/searchcontent:\x01*\x12u\n\nStandalone\x12\x1a.api.v0alpha.StandaloneReq\x1a\x1a.api.v0alpha.StandaloneRes\"/\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\"\"\x1d/api/v0alpha/learn/standalone:\x01*\x12\x93\x01\n\x11\x43ontentEditorData\x12!.api.v0alpha.ContentEditorDataReq\x1a!.api.v0alpha.ContentEditorDataRes\"8\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02)\"$/api/v0alpha/learn/contenteditordata:\x01*\x12g\n\x06Update\x12\x16.api.v0alpha.UpdateReq\x1a\x16.api.v0alpha.UpdateRes\"-\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02\x1e\"\x19/api/v0alpha/learn/update:\x01*\x12\x8f\x01\n\x10StoreStaticImage\x12 .api.v0alpha.StoreStaticImageReq\x1a .api.v0alpha.StoreStaticImageRes\"7\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02(\"#/api/v0alpha/learn/storestaticimage:\x01*\x12\xa1\x01\n\x17UploadDynamicScreenshot\x12\'.api.v0alpha.UploadDynamicScreenshotReq\x1a\'.api.v0alpha.UploadDynamicScreenshotRes\"4\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02%\" /api/v0alpha/learn/uploaddynamic:\x01*\x12\x8f\x01\n\x10\x44\x65leteStandalone\x12 .api.v0alpha.DeleteStandaloneReq\x1a .api.v0alpha.DeleteStandaloneRes\"7\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02(\"#/api/v0alpha/learn/deletestandalone:\x01*\x12i\n\x07Snippet\x12\x17.api.v0alpha.SnippetReq\x1a\x17.api.v0alpha.SnippetRes\",\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x1f\"\x1a/api/v0alpha/learn/snippet:\x01*\x12\x8f\x01\n\x10\x44\x65leteLearnPages\x12 .api.v0alpha.DeleteLearnPagesReq\x1a .api.v0alpha.DeleteLearnPagesRes\"7\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02(\"#/api/v0alpha/learn/deletelearnpages:\x01*Bj\n\x0f\x63om.api.v0alphaB\nLearnProtoP\x01\xa2\x02\x03\x41VX\xaa\x02\x0b\x41pi.V0alpha\xca\x02\x0b\x41pi\\V0alpha\xe2\x02\x17\x41pi\\V0alpha\\GPBMetadata\xea\x02\x0c\x41pi::V0alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v0alpha.learn_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.api.v0alphaB\nLearnProtoP\001\242\002\003AVX\252\002\013Api.V0alpha\312\002\013Api\\V0alpha\342\002\027Api\\V0alpha\\GPBMetadata\352\002\014Api::V0alpha'
  _LEARN.methods_by_name['Exist']._options = None
  _LEARN.methods_by_name['Exist']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\035\"\030/api/v0alpha/learn/exist:\001*'
  _LEARN.methods_by_name['Content']._options = None
  _LEARN.methods_by_name['Content']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\037\"\032/api/v0alpha/learn/content:\001*'
  _LEARN.methods_by_name['ExportMany']._options = None
  _LEARN.methods_by_name['ExportMany']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\"\"\035/api/v0alpha/learn/exportmany:\001*'
  _LEARN.methods_by_name['SearchContent']._options = None
  _LEARN.methods_by_name['SearchContent']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002%\" /api/v0alpha/learn/searchcontent:\001*'
  _LEARN.methods_by_name['Standalone']._options = None
  _LEARN.methods_by_name['Standalone']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\"\"\035/api/v0alpha/learn/standalone:\001*'
  _LEARN.methods_by_name['ContentEditorData']._options = None
  _LEARN.methods_by_name['ContentEditorData']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002)\"$/api/v0alpha/learn/contenteditordata:\001*'
  _LEARN.methods_by_name['Update']._options = None
  _LEARN.methods_by_name['Update']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002\036\"\031/api/v0alpha/learn/update:\001*'
  _LEARN.methods_by_name['StoreStaticImage']._options = None
  _LEARN.methods_by_name['StoreStaticImage']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002(\"#/api/v0alpha/learn/storestaticimage:\001*'
  _LEARN.methods_by_name['UploadDynamicScreenshot']._options = None
  _LEARN.methods_by_name['UploadDynamicScreenshot']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002%\" /api/v0alpha/learn/uploaddynamic:\001*'
  _LEARN.methods_by_name['DeleteStandalone']._options = None
  _LEARN.methods_by_name['DeleteStandalone']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002(\"#/api/v0alpha/learn/deletestandalone:\001*'
  _LEARN.methods_by_name['Snippet']._options = None
  _LEARN.methods_by_name['Snippet']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\037\"\032/api/v0alpha/learn/snippet:\001*'
  _LEARN.methods_by_name['DeleteLearnPages']._options = None
  _LEARN.methods_by_name['DeleteLearnPages']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002(\"#/api/v0alpha/learn/deletelearnpages:\001*'
  _globals['_EXISTREQ']._serialized_start=162
  _globals['_EXISTREQ']._serialized_end=214
  _globals['_EXISTRES']._serialized_start=216
  _globals['_EXISTRES']._serialized_end=248
  _globals['_CONTENTREQ']._serialized_start=250
  _globals['_CONTENTREQ']._serialized_end=304
  _globals['_CONTENTRES']._serialized_start=307
  _globals['_CONTENTRES']._serialized_end=474
  _globals['_CONTENTEDITORDATAREQ']._serialized_start=476
  _globals['_CONTENTEDITORDATAREQ']._serialized_end=540
  _globals['_CONTENTEDITORDATARES']._serialized_start=542
  _globals['_CONTENTEDITORDATARES']._serialized_end=606
  _globals['_UPDATEREQ']._serialized_start=608
  _globals['_UPDATEREQ']._serialized_end=713
  _globals['_UPDATERES']._serialized_start=715
  _globals['_UPDATERES']._serialized_end=726
  _globals['_EXPORTMANYREQ']._serialized_start=728
  _globals['_EXPORTMANYREQ']._serialized_end=811
  _globals['_EXPORTRES']._serialized_start=813
  _globals['_EXPORTRES']._serialized_end=859
  _globals['_STORESTATICIMAGEREQ']._serialized_start=861
  _globals['_STORESTATICIMAGEREQ']._serialized_end=929
  _globals['_LEARNIMAGE']._serialized_start=931
  _globals['_LEARNIMAGE']._serialized_end=1024
  _globals['_STORESTATICIMAGERES']._serialized_start=1026
  _globals['_STORESTATICIMAGERES']._serialized_end=1094
  _globals['_SEARCHCONTENTREQ']._serialized_start=1097
  _globals['_SEARCHCONTENTREQ']._serialized_end=1237
  _globals['_SEARCHRES']._serialized_start=1239
  _globals['_SEARCHRES']._serialized_end=1322
  _globals['_LEARNSEARCHDETAILS']._serialized_start=1324
  _globals['_LEARNSEARCHDETAILS']._serialized_end=1390
  _globals['_UPLOADDYNAMICSCREENSHOTREQ']._serialized_start=1393
  _globals['_UPLOADDYNAMICSCREENSHOTREQ']._serialized_end=1533
  _globals['_UPLOADDYNAMICSCREENSHOTRES']._serialized_start=1535
  _globals['_UPLOADDYNAMICSCREENSHOTRES']._serialized_end=1634
  _globals['_STANDALONEREQ']._serialized_start=1636
  _globals['_STANDALONEREQ']._serialized_end=1675
  _globals['_STANDALONERES']._serialized_start=1677
  _globals['_STANDALONERES']._serialized_end=1776
  _globals['_LEARNSTANDALONEDETAILS']._serialized_start=1779
  _globals['_LEARNSTANDALONEDETAILS']._serialized_end=1929
  _globals['_DELETESTANDALONEREQ']._serialized_start=1931
  _globals['_DELETESTANDALONEREQ']._serialized_end=2013
  _globals['_DELETESTANDALONERES']._serialized_start=2015
  _globals['_DELETESTANDALONERES']._serialized_end=2036
  _globals['_SNIPPETREQ']._serialized_start=2038
  _globals['_SNIPPETREQ']._serialized_end=2074
  _globals['_SNIPPETRES']._serialized_start=2076
  _globals['_SNIPPETRES']._serialized_end=2163
  _globals['_LEARNSNIPPETDETAILS']._serialized_start=2166
  _globals['_LEARNSNIPPETDETAILS']._serialized_end=2313
  _globals['_DELETELEARNPAGESREQ']._serialized_start=2315
  _globals['_DELETELEARNPAGESREQ']._serialized_end=2378
  _globals['_DELETELEARNPAGESRES']._serialized_start=2380
  _globals['_DELETELEARNPAGESRES']._serialized_end=2401
  _globals['_LEARN']._serialized_start=2404
  _globals['_LEARN']._serialized_end=3939
# @@protoc_insertion_point(module_scope)
