# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v0alpha/learn.proto
# Protobuf Python Version: 5.28.1
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
    1,
    '',
    'api/v0alpha/learn.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61pi/v0alpha/learn.proto\x12\x0b\x61pi.v0alpha\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"4\n\x08\x45xistReq\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\" \n\x08\x45xistRes\x12\x14\n\x05\x65xist\x18\x01 \x01(\x08R\x05\x65xist\"6\n\nContentReq\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\"\x91\x02\n\nContentRes\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\x12N\n\x15last_edited_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x13lastEditedTimestamp\x12/\n\x06images\x18\x03 \x03(\x0b\x32\x17.api.v0alpha.LearnImageR\x06images\x12\x14\n\x05title\x18\x04 \x01(\tR\x05title\x12(\n\x10total_view_count\x18\x05 \x01(\x03R\x0etotalViewCount\x12(\n\x10last_edited_user\x18\x06 \x01(\tR\x0elastEditedUser\"@\n\x14\x43ontentEditorDataReq\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\"@\n\x14\x43ontentEditorDataRes\x12(\n\x10last_edited_user\x18\x01 \x01(\tR\x0elastEditedUser\"\x7f\n\tUpdateReq\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\x12\x18\n\x07\x63ontent\x18\x03 \x01(\tR\x07\x63ontent\x12\x18\n\x07message\x18\x0c \x01(\tR\x07message\x12\x14\n\x05title\x18\r \x01(\tR\x05title\"\x0b\n\tUpdateRes\"S\n\rExportManyReq\x12\x10\n\x03url\x18\x01 \x03(\tR\x03url\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\x12\x18\n\x07\x63ontent\x18\x03 \x01(\tR\x07\x63ontent\".\n\tExportRes\x12!\n\x0c\x64ownload_url\x18\x01 \x01(\tR\x0b\x64ownloadUrl\"D\n\x13StoreStaticImageReq\x12-\n\x05image\x18\x01 \x01(\x0b\x32\x17.api.v0alpha.LearnImageR\x05image\"\x94\x01\n\nLearnImage\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12\x18\n\x07\x63ontent\x18\x02 \x01(\tR\x07\x63ontent\x12!\n\x0c\x64ownload_url\x18\x03 \x01(\tR\x0b\x64ownloadUrl\x12\x35\n\x07temp_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x06tempId\"D\n\x13StoreStaticImageRes\x12-\n\x05image\x18\x01 \x01(\x0b\x32\x17.api.v0alpha.LearnImageR\x05image\"\x8c\x01\n\x10SearchContentReq\x12%\n\x0esearch_content\x18\x01 \x01(\tR\rsearchContent\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\x12\x39\n\nfield_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"S\n\tSearchRes\x12\x46\n\x0esearch_details\x18\x01 \x03(\x0b\x32\x1f.api.v0alpha.LearnSearchDetailsR\rsearchDetails\"B\n\x12LearnSearchDetails\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07\x63ontent\x18\x02 \x01(\tR\x07\x63ontent\"\x8c\x01\n\x1aUploadDynamicScreenshotReq\x12\"\n\rdata_learn_id\x18\x01 \x01(\tR\x0b\x64\x61taLearnId\x12\x18\n\x07version\x18\x02 \x01(\x03R\x07version\x12\x16\n\x06locale\x18\x03 \x01(\tR\x06locale\x12\x18\n\x07\x63ontent\x18\x04 \x01(\tR\x07\x63ontent\"c\n\x1aUploadDynamicScreenshotRes\x12\"\n\rdata_learn_id\x18\x01 \x01(\tR\x0b\x64\x61taLearnId\x12!\n\x0c\x64ownload_url\x18\x02 \x01(\tR\x0b\x64ownloadUrl\"]\n\rStandaloneReq\x12\x16\n\x06locale\x18\x01 \x01(\tR\x06locale\x12\x1a\n\x08\x63\x61tegory\x18\x02 \x01(\tR\x08\x63\x61tegory\x12\x18\n\x07version\x18\x03 \x01(\tR\x07version\"c\n\rStandaloneRes\x12R\n\x12standalone_details\x18\x01 \x03(\x0b\x32#.api.v0alpha.LearnStandaloneDetailsR\x11standaloneDetails\"\xb4\x01\n\x16LearnStandaloneDetails\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1c\n\x07\x63ontent\x18\x02 \x01(\tB\x02\x18\x01R\x07\x63ontent\x12R\n\x15last_edited_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\x13lastEditedTimestamp\x12\x14\n\x05title\x18\x04 \x01(\tR\x05title\"l\n\x13\x44\x65leteStandaloneReq\x12\x16\n\x06locale\x18\x01 \x01(\tR\x06locale\x12#\n\rarticle_names\x18\x02 \x03(\tR\x0c\x61rticleNames\x12\x18\n\x07version\x18\x03 \x01(\tR\x07version\"\x15\n\x13\x44\x65leteStandaloneRes\">\n\nSnippetReq\x12\x16\n\x06locale\x18\x01 \x01(\tR\x06locale\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\"W\n\nSnippetRes\x12I\n\x0fsnippet_details\x18\x01 \x03(\x0b\x32 .api.v0alpha.LearnSnippetDetailsR\x0esnippetDetails\"\xa9\x01\n\x13LearnSnippetDetails\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07\x63ontent\x18\x02 \x01(\tR\x07\x63ontent\x12N\n\x15last_edited_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x13lastEditedTimestamp\x12\x14\n\x05title\x18\x04 \x01(\tR\x05title\"Y\n\x13\x44\x65leteLearnPagesReq\x12\x16\n\x06locale\x18\x01 \x01(\tR\x06locale\x12\x10\n\x03url\x18\x02 \x03(\tR\x03url\x12\x18\n\x07version\x18\x03 \x01(\tR\x07version\"\x15\n\x13\x44\x65leteLearnPagesRes\"\x86\x01\n\x14\x43reateEditVersionReq\x12\x1f\n\x0bsrc_version\x18\x01 \x01(\tR\nsrcVersion\x12!\n\x0c\x64\x65st_version\x18\x02 \x01(\tR\x0b\x64\x65stVersion\x12*\n\x11\x64\x65st_version_name\x18\x03 \x01(\tR\x0f\x64\x65stVersionName\"\\\n\x14\x43reateEditVersionRes\x12\x44\n\x0fversion_details\x18\x01 \x01(\x0b\x32\x1b.api.v0alpha.VersionDetailsR\x0eversionDetails\"<\n\x11PublishVersionReq\x12\'\n\x0fpublish_version\x18\x01 \x01(\tR\x0epublishVersion\"Y\n\x11PublishVersionRes\x12\x44\n\x0fversion_details\x18\x01 \x01(\x0b\x32\x1b.api.v0alpha.VersionDetailsR\x0eversionDetails\"Y\n\x13\x43ontentByVersionReq\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\x12\x18\n\x07version\x18\x03 \x01(\tR\x07version\"\xa2\x01\n\x12UpdateByVersionReq\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\x12\x18\n\x07\x63ontent\x18\x03 \x01(\tR\x07\x63ontent\x12\x18\n\x07version\x18\x04 \x01(\tR\x07version\x12\x18\n\x07message\x18\x0c \x01(\tR\x07message\x12\x14\n\x05title\x18\r \x01(\tR\x05title\"\xaf\x01\n\x19SearchContentByVersionReq\x12%\n\x0esearch_content\x18\x01 \x01(\tR\rsearchContent\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\x12\x39\n\nfield_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\x12\x18\n\x07version\x18\x06 \x01(\tR\x07version\"[\n\x15ReviewFileVersionsReq\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12\x16\n\x06locale\x18\x03 \x01(\tR\x06locale\"\x85\x01\n\x15ReviewFileVersionsRes\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\x12!\n\x0c\x64iff_content\x18\x02 \x01(\tR\x0b\x64iffContent\x12/\n\x06images\x18\x03 \x03(\x0b\x32\x17.api.v0alpha.LearnImageR\x06images\"D\n\x10ReviewVersionReq\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\x12\x16\n\x06locale\x18\x02 \x01(\tR\x06locale\"\x9b\x01\n\x10ReviewVersionRes\x12\x1b\n\tdiff_urls\x18\x01 \x01(\tR\x08\x64iffUrls\x12&\n\x0f\x64iff_file_names\x18\x02 \x01(\tR\rdiffFileNames\x12\x1f\n\x0bsrc_content\x18\x03 \x01(\tR\nsrcContent\x12!\n\x0c\x64\x65st_content\x18\x04 \x01(\tR\x0b\x64\x65stContent\")\n\x0fListVersionsReq\x12\x16\n\x06locale\x18\x01 \x01(\tR\x06locale\"s\n\x0fListVersionsRes\x12\x1a\n\x08versions\x18\x01 \x03(\tR\x08versions\x12\x44\n\x0fversion_details\x18\x02 \x03(\x0b\x32\x1b.api.v0alpha.VersionDetailsR\x0eversionDetails\"\xe7\x01\n\x0eVersionDetails\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\x12!\n\x0cversion_name\x18\x02 \x01(\tR\x0bversionName\x12=\n\x0c\x64\x61te_created\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64\x61teCreated\x12\x41\n\x0e\x64\x61te_published\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rdatePublished\x12\x16\n\x06status\x18\x05 \x01(\tR\x06status\"D\n\x10\x44\x65leteVersionReq\x12\x16\n\x06locale\x18\x01 \x01(\tR\x06locale\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\"\x12\n\x10\x44\x65leteVersionRes\"E\n\x14UploadStaticImageReq\x12-\n\x05image\x18\x01 \x01(\x0b\x32\x17.api.v0alpha.LearnImageR\x05image\"E\n\x14UploadStaticImageRes\x12-\n\x05image\x18\x01 \x01(\x0b\x32\x17.api.v0alpha.LearnImageR\x05image2\xaa\x1a\n\x05Learn\x12\x61\n\x05\x45xist\x12\x15.api.v0alpha.ExistReq\x1a\x15.api.v0alpha.ExistRes\"*\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x1d\"\x18/api/v0alpha/learn/exist:\x01*\x12i\n\x07\x43ontent\x12\x17.api.v0alpha.ContentReq\x1a\x17.api.v0alpha.ContentRes\",\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x1f\"\x1a/api/v0alpha/learn/content:\x01*\x12q\n\nExportMany\x12\x1a.api.v0alpha.ExportManyReq\x1a\x16.api.v0alpha.ExportRes\"/\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\"\"\x1d/api/v0alpha/learn/exportmany:\x01*\x12z\n\rSearchContent\x12\x1d.api.v0alpha.SearchContentReq\x1a\x16.api.v0alpha.SearchRes\"2\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02%\" /api/v0alpha/learn/searchcontent:\x01*\x12\x84\x01\n\x11ListSearchResults\x12\x1d.api.v0alpha.SearchContentReq\x1a\x16.api.v0alpha.SearchRes\"6\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02)\"$/api/v0alpha/learn/listsearchresults:\x01*0\x01\x12u\n\nStandalone\x12\x1a.api.v0alpha.StandaloneReq\x1a\x1a.api.v0alpha.StandaloneRes\"/\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\"\"\x1d/api/v0alpha/learn/standalone:\x01*\x12\x93\x01\n\x11\x43ontentEditorData\x12!.api.v0alpha.ContentEditorDataReq\x1a!.api.v0alpha.ContentEditorDataRes\"8\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02)\"$/api/v0alpha/learn/contenteditordata:\x01*\x12g\n\x06Update\x12\x16.api.v0alpha.UpdateReq\x1a\x16.api.v0alpha.UpdateRes\"-\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02\x1e\"\x19/api/v0alpha/learn/update:\x01*\x12\x8f\x01\n\x10StoreStaticImage\x12 .api.v0alpha.StoreStaticImageReq\x1a .api.v0alpha.StoreStaticImageRes\"7\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02(\"#/api/v0alpha/learn/storestaticimage:\x01*\x12\xa1\x01\n\x17UploadDynamicScreenshot\x12\'.api.v0alpha.UploadDynamicScreenshotReq\x1a\'.api.v0alpha.UploadDynamicScreenshotRes\"4\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02%\" /api/v0alpha/learn/uploaddynamic:\x01*\x12\x8f\x01\n\x10\x44\x65leteStandalone\x12 .api.v0alpha.DeleteStandaloneReq\x1a .api.v0alpha.DeleteStandaloneRes\"7\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02(\"#/api/v0alpha/learn/deletestandalone:\x01*\x12i\n\x07Snippet\x12\x17.api.v0alpha.SnippetReq\x1a\x17.api.v0alpha.SnippetRes\",\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x1f\"\x1a/api/v0alpha/learn/snippet:\x01*\x12\x8f\x01\n\x10\x44\x65leteLearnPages\x12 .api.v0alpha.DeleteLearnPagesReq\x1a .api.v0alpha.DeleteLearnPagesRes\"7\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02(\"#/api/v0alpha/learn/deletelearnpages:\x01*\x12\x93\x01\n\x11\x43reateEditVersion\x12!.api.v0alpha.CreateEditVersionReq\x1a!.api.v0alpha.CreateEditVersionRes\"8\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02)\"$/api/v0alpha/learn/createeditversion:\x01*\x12\x87\x01\n\x0ePublishVersion\x12\x1e.api.v0alpha.PublishVersionReq\x1a\x1e.api.v0alpha.PublishVersionRes\"5\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02&\"!/api/v0alpha/learn/publishversion:\x01*\x12\x86\x01\n\x10\x43ontentByVersion\x12 .api.v0alpha.ContentByVersionReq\x1a\x17.api.v0alpha.ContentRes\"7\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02(\"#/api/v0alpha/learn/contentbyversion:\x01*\x12\x82\x01\n\x0fUpdateByVersion\x12\x1f.api.v0alpha.UpdateByVersionReq\x1a\x16.api.v0alpha.UpdateRes\"6\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02\'\"\"/api/v0alpha/learn/updatebyversion:\x01*\x12\xa1\x01\n\x1aListSearchResultsByVersion\x12&.api.v0alpha.SearchContentByVersionReq\x1a\x16.api.v0alpha.SearchRes\"A\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02\x32\"-/api/v0alpha/learn/listsearchresultsbyversion:\x01*0\x01\x12\x97\x01\n\x12ReviewFileVersions\x12\".api.v0alpha.ReviewFileVersionsReq\x1a\".api.v0alpha.ReviewFileVersionsRes\"9\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02*\"%/api/v0alpha/learn/reviewfileversions:\x01*\x12\x83\x01\n\rReviewVersion\x12\x1d.api.v0alpha.ReviewVersionReq\x1a\x1d.api.v0alpha.ReviewVersionRes\"4\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02%\" /api/v0alpha/learn/reviewversion:\x01*\x12\x7f\n\x10\x45xportManyStream\x12\x1a.api.v0alpha.ExportManyReq\x1a\x16.api.v0alpha.ExportRes\"5\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02(\"#/api/v0alpha/learn/exportmanystream:\x01*0\x01\x12\x7f\n\x0cListVersions\x12\x1c.api.v0alpha.ListVersionsReq\x1a\x1c.api.v0alpha.ListVersionsRes\"3\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02$\"\x1f/api/v0alpha/learn/listversions:\x01*\x12\x91\x01\n\x13ReviewVersionStream\x12\x1d.api.v0alpha.ReviewVersionReq\x1a\x1d.api.v0alpha.ReviewVersionRes\":\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02+\"&/api/v0alpha/learn/reviewversionstream:\x01*0\x01\x12\x83\x01\n\rDeleteVersion\x12\x1d.api.v0alpha.DeleteVersionReq\x1a\x1d.api.v0alpha.DeleteVersionRes\"4\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02%\" /api/v0alpha/learn/deleteversion:\x01*\x12\x93\x01\n\x11UploadStaticImage\x12!.api.v0alpha.UploadStaticImageReq\x1a!.api.v0alpha.UploadStaticImageRes\"8\xba\xb8\x91\x02\x04\n\x02\x08\n\x82\xd3\xe4\x93\x02)\"$/api/v0alpha/learn/uploadstaticimage:\x01*Bj\n\x0f\x63om.api.v0alphaB\nLearnProtoP\x01\xa2\x02\x03\x41VX\xaa\x02\x0b\x41pi.V0alpha\xca\x02\x0b\x41pi\\V0alpha\xe2\x02\x17\x41pi\\V0alpha\\GPBMetadata\xea\x02\x0c\x41pi::V0alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v0alpha.learn_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.v0alphaB\nLearnProtoP\001\242\002\003AVX\252\002\013Api.V0alpha\312\002\013Api\\V0alpha\342\002\027Api\\V0alpha\\GPBMetadata\352\002\014Api::V0alpha'
  _globals['_LEARNSTANDALONEDETAILS'].fields_by_name['content']._loaded_options = None
  _globals['_LEARNSTANDALONEDETAILS'].fields_by_name['content']._serialized_options = b'\030\001'
  _globals['_LEARNSTANDALONEDETAILS'].fields_by_name['last_edited_timestamp']._loaded_options = None
  _globals['_LEARNSTANDALONEDETAILS'].fields_by_name['last_edited_timestamp']._serialized_options = b'\030\001'
  _globals['_LEARN'].methods_by_name['Exist']._loaded_options = None
  _globals['_LEARN'].methods_by_name['Exist']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\035\"\030/api/v0alpha/learn/exist:\001*'
  _globals['_LEARN'].methods_by_name['Content']._loaded_options = None
  _globals['_LEARN'].methods_by_name['Content']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\037\"\032/api/v0alpha/learn/content:\001*'
  _globals['_LEARN'].methods_by_name['ExportMany']._loaded_options = None
  _globals['_LEARN'].methods_by_name['ExportMany']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\"\"\035/api/v0alpha/learn/exportmany:\001*'
  _globals['_LEARN'].methods_by_name['SearchContent']._loaded_options = None
  _globals['_LEARN'].methods_by_name['SearchContent']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002%\" /api/v0alpha/learn/searchcontent:\001*'
  _globals['_LEARN'].methods_by_name['ListSearchResults']._loaded_options = None
  _globals['_LEARN'].methods_by_name['ListSearchResults']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002)\"$/api/v0alpha/learn/listsearchresults:\001*'
  _globals['_LEARN'].methods_by_name['Standalone']._loaded_options = None
  _globals['_LEARN'].methods_by_name['Standalone']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\"\"\035/api/v0alpha/learn/standalone:\001*'
  _globals['_LEARN'].methods_by_name['ContentEditorData']._loaded_options = None
  _globals['_LEARN'].methods_by_name['ContentEditorData']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002)\"$/api/v0alpha/learn/contenteditordata:\001*'
  _globals['_LEARN'].methods_by_name['Update']._loaded_options = None
  _globals['_LEARN'].methods_by_name['Update']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002\036\"\031/api/v0alpha/learn/update:\001*'
  _globals['_LEARN'].methods_by_name['StoreStaticImage']._loaded_options = None
  _globals['_LEARN'].methods_by_name['StoreStaticImage']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002(\"#/api/v0alpha/learn/storestaticimage:\001*'
  _globals['_LEARN'].methods_by_name['UploadDynamicScreenshot']._loaded_options = None
  _globals['_LEARN'].methods_by_name['UploadDynamicScreenshot']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002%\" /api/v0alpha/learn/uploaddynamic:\001*'
  _globals['_LEARN'].methods_by_name['DeleteStandalone']._loaded_options = None
  _globals['_LEARN'].methods_by_name['DeleteStandalone']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002(\"#/api/v0alpha/learn/deletestandalone:\001*'
  _globals['_LEARN'].methods_by_name['Snippet']._loaded_options = None
  _globals['_LEARN'].methods_by_name['Snippet']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\037\"\032/api/v0alpha/learn/snippet:\001*'
  _globals['_LEARN'].methods_by_name['DeleteLearnPages']._loaded_options = None
  _globals['_LEARN'].methods_by_name['DeleteLearnPages']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002(\"#/api/v0alpha/learn/deletelearnpages:\001*'
  _globals['_LEARN'].methods_by_name['CreateEditVersion']._loaded_options = None
  _globals['_LEARN'].methods_by_name['CreateEditVersion']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002)\"$/api/v0alpha/learn/createeditversion:\001*'
  _globals['_LEARN'].methods_by_name['PublishVersion']._loaded_options = None
  _globals['_LEARN'].methods_by_name['PublishVersion']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002&\"!/api/v0alpha/learn/publishversion:\001*'
  _globals['_LEARN'].methods_by_name['ContentByVersion']._loaded_options = None
  _globals['_LEARN'].methods_by_name['ContentByVersion']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002(\"#/api/v0alpha/learn/contentbyversion:\001*'
  _globals['_LEARN'].methods_by_name['UpdateByVersion']._loaded_options = None
  _globals['_LEARN'].methods_by_name['UpdateByVersion']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002\'\"\"/api/v0alpha/learn/updatebyversion:\001*'
  _globals['_LEARN'].methods_by_name['ListSearchResultsByVersion']._loaded_options = None
  _globals['_LEARN'].methods_by_name['ListSearchResultsByVersion']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\0022\"-/api/v0alpha/learn/listsearchresultsbyversion:\001*'
  _globals['_LEARN'].methods_by_name['ReviewFileVersions']._loaded_options = None
  _globals['_LEARN'].methods_by_name['ReviewFileVersions']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002*\"%/api/v0alpha/learn/reviewfileversions:\001*'
  _globals['_LEARN'].methods_by_name['ReviewVersion']._loaded_options = None
  _globals['_LEARN'].methods_by_name['ReviewVersion']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002%\" /api/v0alpha/learn/reviewversion:\001*'
  _globals['_LEARN'].methods_by_name['ExportManyStream']._loaded_options = None
  _globals['_LEARN'].methods_by_name['ExportManyStream']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002(\"#/api/v0alpha/learn/exportmanystream:\001*'
  _globals['_LEARN'].methods_by_name['ListVersions']._loaded_options = None
  _globals['_LEARN'].methods_by_name['ListVersions']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002$\"\037/api/v0alpha/learn/listversions:\001*'
  _globals['_LEARN'].methods_by_name['ReviewVersionStream']._loaded_options = None
  _globals['_LEARN'].methods_by_name['ReviewVersionStream']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002+\"&/api/v0alpha/learn/reviewversionstream:\001*'
  _globals['_LEARN'].methods_by_name['DeleteVersion']._loaded_options = None
  _globals['_LEARN'].methods_by_name['DeleteVersion']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002%\" /api/v0alpha/learn/deleteversion:\001*'
  _globals['_LEARN'].methods_by_name['UploadStaticImage']._loaded_options = None
  _globals['_LEARN'].methods_by_name['UploadStaticImage']._serialized_options = b'\272\270\221\002\004\n\002\010\n\202\323\344\223\002)\"$/api/v0alpha/learn/uploadstaticimage:\001*'
  _globals['_EXISTREQ']._serialized_start=194
  _globals['_EXISTREQ']._serialized_end=246
  _globals['_EXISTRES']._serialized_start=248
  _globals['_EXISTRES']._serialized_end=280
  _globals['_CONTENTREQ']._serialized_start=282
  _globals['_CONTENTREQ']._serialized_end=336
  _globals['_CONTENTRES']._serialized_start=339
  _globals['_CONTENTRES']._serialized_end=612
  _globals['_CONTENTEDITORDATAREQ']._serialized_start=614
  _globals['_CONTENTEDITORDATAREQ']._serialized_end=678
  _globals['_CONTENTEDITORDATARES']._serialized_start=680
  _globals['_CONTENTEDITORDATARES']._serialized_end=744
  _globals['_UPDATEREQ']._serialized_start=746
  _globals['_UPDATEREQ']._serialized_end=873
  _globals['_UPDATERES']._serialized_start=875
  _globals['_UPDATERES']._serialized_end=886
  _globals['_EXPORTMANYREQ']._serialized_start=888
  _globals['_EXPORTMANYREQ']._serialized_end=971
  _globals['_EXPORTRES']._serialized_start=973
  _globals['_EXPORTRES']._serialized_end=1019
  _globals['_STORESTATICIMAGEREQ']._serialized_start=1021
  _globals['_STORESTATICIMAGEREQ']._serialized_end=1089
  _globals['_LEARNIMAGE']._serialized_start=1092
  _globals['_LEARNIMAGE']._serialized_end=1240
  _globals['_STORESTATICIMAGERES']._serialized_start=1242
  _globals['_STORESTATICIMAGERES']._serialized_end=1310
  _globals['_SEARCHCONTENTREQ']._serialized_start=1313
  _globals['_SEARCHCONTENTREQ']._serialized_end=1453
  _globals['_SEARCHRES']._serialized_start=1455
  _globals['_SEARCHRES']._serialized_end=1538
  _globals['_LEARNSEARCHDETAILS']._serialized_start=1540
  _globals['_LEARNSEARCHDETAILS']._serialized_end=1606
  _globals['_UPLOADDYNAMICSCREENSHOTREQ']._serialized_start=1609
  _globals['_UPLOADDYNAMICSCREENSHOTREQ']._serialized_end=1749
  _globals['_UPLOADDYNAMICSCREENSHOTRES']._serialized_start=1751
  _globals['_UPLOADDYNAMICSCREENSHOTRES']._serialized_end=1850
  _globals['_STANDALONEREQ']._serialized_start=1852
  _globals['_STANDALONEREQ']._serialized_end=1945
  _globals['_STANDALONERES']._serialized_start=1947
  _globals['_STANDALONERES']._serialized_end=2046
  _globals['_LEARNSTANDALONEDETAILS']._serialized_start=2049
  _globals['_LEARNSTANDALONEDETAILS']._serialized_end=2229
  _globals['_DELETESTANDALONEREQ']._serialized_start=2231
  _globals['_DELETESTANDALONEREQ']._serialized_end=2339
  _globals['_DELETESTANDALONERES']._serialized_start=2341
  _globals['_DELETESTANDALONERES']._serialized_end=2362
  _globals['_SNIPPETREQ']._serialized_start=2364
  _globals['_SNIPPETREQ']._serialized_end=2426
  _globals['_SNIPPETRES']._serialized_start=2428
  _globals['_SNIPPETRES']._serialized_end=2515
  _globals['_LEARNSNIPPETDETAILS']._serialized_start=2518
  _globals['_LEARNSNIPPETDETAILS']._serialized_end=2687
  _globals['_DELETELEARNPAGESREQ']._serialized_start=2689
  _globals['_DELETELEARNPAGESREQ']._serialized_end=2778
  _globals['_DELETELEARNPAGESRES']._serialized_start=2780
  _globals['_DELETELEARNPAGESRES']._serialized_end=2801
  _globals['_CREATEEDITVERSIONREQ']._serialized_start=2804
  _globals['_CREATEEDITVERSIONREQ']._serialized_end=2938
  _globals['_CREATEEDITVERSIONRES']._serialized_start=2940
  _globals['_CREATEEDITVERSIONRES']._serialized_end=3032
  _globals['_PUBLISHVERSIONREQ']._serialized_start=3034
  _globals['_PUBLISHVERSIONREQ']._serialized_end=3094
  _globals['_PUBLISHVERSIONRES']._serialized_start=3096
  _globals['_PUBLISHVERSIONRES']._serialized_end=3185
  _globals['_CONTENTBYVERSIONREQ']._serialized_start=3187
  _globals['_CONTENTBYVERSIONREQ']._serialized_end=3276
  _globals['_UPDATEBYVERSIONREQ']._serialized_start=3279
  _globals['_UPDATEBYVERSIONREQ']._serialized_end=3441
  _globals['_SEARCHCONTENTBYVERSIONREQ']._serialized_start=3444
  _globals['_SEARCHCONTENTBYVERSIONREQ']._serialized_end=3619
  _globals['_REVIEWFILEVERSIONSREQ']._serialized_start=3621
  _globals['_REVIEWFILEVERSIONSREQ']._serialized_end=3712
  _globals['_REVIEWFILEVERSIONSRES']._serialized_start=3715
  _globals['_REVIEWFILEVERSIONSRES']._serialized_end=3848
  _globals['_REVIEWVERSIONREQ']._serialized_start=3850
  _globals['_REVIEWVERSIONREQ']._serialized_end=3918
  _globals['_REVIEWVERSIONRES']._serialized_start=3921
  _globals['_REVIEWVERSIONRES']._serialized_end=4076
  _globals['_LISTVERSIONSREQ']._serialized_start=4078
  _globals['_LISTVERSIONSREQ']._serialized_end=4119
  _globals['_LISTVERSIONSRES']._serialized_start=4121
  _globals['_LISTVERSIONSRES']._serialized_end=4236
  _globals['_VERSIONDETAILS']._serialized_start=4239
  _globals['_VERSIONDETAILS']._serialized_end=4470
  _globals['_DELETEVERSIONREQ']._serialized_start=4472
  _globals['_DELETEVERSIONREQ']._serialized_end=4540
  _globals['_DELETEVERSIONRES']._serialized_start=4542
  _globals['_DELETEVERSIONRES']._serialized_end=4560
  _globals['_UPLOADSTATICIMAGEREQ']._serialized_start=4562
  _globals['_UPLOADSTATICIMAGEREQ']._serialized_end=4631
  _globals['_UPLOADSTATICIMAGERES']._serialized_start=4633
  _globals['_UPLOADSTATICIMAGERES']._serialized_end=4702
  _globals['_LEARN']._serialized_start=4705
  _globals['_LEARN']._serialized_end=8075
# @@protoc_insertion_point(module_scope)
