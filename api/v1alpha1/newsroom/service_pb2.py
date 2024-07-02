# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/newsroom/service.proto
# Protobuf Python Version: 5.27.2
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
    2,
    '',
    'api/v1alpha1/newsroom/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.newsroom import entities_pb2 as api_dot_v1alpha1_dot_newsroom_dot_entities__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/v1alpha1/newsroom/service.proto\x12\x15\x61pi.v1alpha1.newsroom\x1a\x17\x61nnotations/authz.proto\x1a$api/v1alpha1/newsroom/entities.proto\x1a\x1cgoogle/api/annotations.proto2\xbd\x10\n\x0bNewsroomAPI\x12\xb5\x01\n\x11\x43reateNewsArticle\x12/.api.v1alpha1.newsroom.CreateNewsArticleRequest\x1a\x30.api.v1alpha1.newsroom.CreateNewsArticleResponse\"=\xba\xb8\x91\x02\x05\n\x03\x08\xe8 \x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/newsroom/createnewsarticle:\x01*\x12\xb1\x01\n\x10ListNewsArticles\x12..api.v1alpha1.newsroom.ListNewsArticlesRequest\x1a/.api.v1alpha1.newsroom.ListNewsArticlesResponse\"<\xba\xb8\x91\x02\x05\n\x03\x08\xe7 \x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/newsroom/listnewsarticles:\x01*\x12\xb9\x01\n\x12GetNewsArticleById\x12\x30.api.v1alpha1.newsroom.GetNewsArticleByIdRequest\x1a\x31.api.v1alpha1.newsroom.GetNewsArticleByIdResponse\">\xba\xb8\x91\x02\x05\n\x03\x08\xe7 \x82\xd3\xe4\x93\x02.\")/api/v1alpha1/newsroom/getnewsarticlebyid:\x01*\x12\xb5\x01\n\x11UpdateNewsArticle\x12/.api.v1alpha1.newsroom.UpdateNewsArticleRequest\x1a\x30.api.v1alpha1.newsroom.UpdateNewsArticleResponse\"=\xba\xb8\x91\x02\x05\n\x03\x08\xe8 \x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/newsroom/updatenewsarticle:\x01*\x12\xc9\x01\n\x16\x43reatePublishedArticle\x12\x34.api.v1alpha1.newsroom.CreatePublishedArticleRequest\x1a\x35.api.v1alpha1.newsroom.CreatePublishedArticleResponse\"B\xba\xb8\x91\x02\x05\n\x03\x08\xe9 \x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/newsroom/createpublishedarticle:\x01*\x12\xc5\x01\n\x15ListPublishedArticles\x12\x33.api.v1alpha1.newsroom.ListPublishedArticlesRequest\x1a\x34.api.v1alpha1.newsroom.ListPublishedArticlesResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xe7 \x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/newsroom/listpublishedarticles:\x01*\x12\xcd\x01\n\x17GetPublishedArticleById\x12\x35.api.v1alpha1.newsroom.GetPublishedArticleByIdRequest\x1a\x36.api.v1alpha1.newsroom.GetPublishedArticleByIdResponse\"C\xba\xb8\x91\x02\x05\n\x03\x08\xe7 \x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/newsroom/getpublishedarticlebyid:\x01*\x12\xa1\x01\n\x0cUserActivity\x12*.api.v1alpha1.newsroom.UserActivityRequest\x1a+.api.v1alpha1.newsroom.UserActivityResponse\"8\xba\xb8\x91\x02\x05\n\x03\x08\xe7 \x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/newsroom/useractivity:\x01*\x12\xa9\x01\n\x0eGetNewsForUser\x12,.api.v1alpha1.newsroom.GetNewsForUserRequest\x1a-.api.v1alpha1.newsroom.GetNewsForUserResponse\":\xba\xb8\x91\x02\x05\n\x03\x08\xe7 \x82\xd3\xe4\x93\x02*\"%/api/v1alpha1/newsroom/getnewsforuser:\x01*\x12\xc5\x01\n\x15StoreNewsArticleImage\x12\x33.api.v1alpha1.newsroom.StoreNewsArticleImageRequest\x1a\x34.api.v1alpha1.newsroom.StoreNewsArticleImageResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xe8 \x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/newsroom/storenewsarticleimage:\x01*\x12\xd1\x01\n\x18ListImagesForNewsArticle\x12\x36.api.v1alpha1.newsroom.ListImagesForNewsArticleRequest\x1a\x37.api.v1alpha1.newsroom.ListImagesForNewsArticleResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xe7 \x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/newsroom/listimagesfornewsarticle:\x01*B\x9f\x01\n\x19\x63om.api.v1alpha1.newsroomB\x0cServiceProtoP\x01\xa2\x02\x03\x41VN\xaa\x02\x15\x41pi.V1alpha1.Newsroom\xca\x02\x15\x41pi\\V1alpha1\\Newsroom\xe2\x02!Api\\V1alpha1\\Newsroom\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Newsroomb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.newsroom.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.api.v1alpha1.newsroomB\014ServiceProtoP\001\242\002\003AVN\252\002\025Api.V1alpha1.Newsroom\312\002\025Api\\V1alpha1\\Newsroom\342\002!Api\\V1alpha1\\Newsroom\\GPBMetadata\352\002\027Api::V1alpha1::Newsroom'
  _globals['_NEWSROOMAPI'].methods_by_name['CreateNewsArticle']._loaded_options = None
  _globals['_NEWSROOMAPI'].methods_by_name['CreateNewsArticle']._serialized_options = b'\272\270\221\002\005\n\003\010\350 \202\323\344\223\002-\"(/api/v1alpha1/newsroom/createnewsarticle:\001*'
  _globals['_NEWSROOMAPI'].methods_by_name['ListNewsArticles']._loaded_options = None
  _globals['_NEWSROOMAPI'].methods_by_name['ListNewsArticles']._serialized_options = b'\272\270\221\002\005\n\003\010\347 \202\323\344\223\002,\"\'/api/v1alpha1/newsroom/listnewsarticles:\001*'
  _globals['_NEWSROOMAPI'].methods_by_name['GetNewsArticleById']._loaded_options = None
  _globals['_NEWSROOMAPI'].methods_by_name['GetNewsArticleById']._serialized_options = b'\272\270\221\002\005\n\003\010\347 \202\323\344\223\002.\")/api/v1alpha1/newsroom/getnewsarticlebyid:\001*'
  _globals['_NEWSROOMAPI'].methods_by_name['UpdateNewsArticle']._loaded_options = None
  _globals['_NEWSROOMAPI'].methods_by_name['UpdateNewsArticle']._serialized_options = b'\272\270\221\002\005\n\003\010\350 \202\323\344\223\002-\"(/api/v1alpha1/newsroom/updatenewsarticle:\001*'
  _globals['_NEWSROOMAPI'].methods_by_name['CreatePublishedArticle']._loaded_options = None
  _globals['_NEWSROOMAPI'].methods_by_name['CreatePublishedArticle']._serialized_options = b'\272\270\221\002\005\n\003\010\351 \202\323\344\223\0022\"-/api/v1alpha1/newsroom/createpublishedarticle:\001*'
  _globals['_NEWSROOMAPI'].methods_by_name['ListPublishedArticles']._loaded_options = None
  _globals['_NEWSROOMAPI'].methods_by_name['ListPublishedArticles']._serialized_options = b'\272\270\221\002\005\n\003\010\347 \202\323\344\223\0021\",/api/v1alpha1/newsroom/listpublishedarticles:\001*'
  _globals['_NEWSROOMAPI'].methods_by_name['GetPublishedArticleById']._loaded_options = None
  _globals['_NEWSROOMAPI'].methods_by_name['GetPublishedArticleById']._serialized_options = b'\272\270\221\002\005\n\003\010\347 \202\323\344\223\0023\"./api/v1alpha1/newsroom/getpublishedarticlebyid:\001*'
  _globals['_NEWSROOMAPI'].methods_by_name['UserActivity']._loaded_options = None
  _globals['_NEWSROOMAPI'].methods_by_name['UserActivity']._serialized_options = b'\272\270\221\002\005\n\003\010\347 \202\323\344\223\002(\"#/api/v1alpha1/newsroom/useractivity:\001*'
  _globals['_NEWSROOMAPI'].methods_by_name['GetNewsForUser']._loaded_options = None
  _globals['_NEWSROOMAPI'].methods_by_name['GetNewsForUser']._serialized_options = b'\272\270\221\002\005\n\003\010\347 \202\323\344\223\002*\"%/api/v1alpha1/newsroom/getnewsforuser:\001*'
  _globals['_NEWSROOMAPI'].methods_by_name['StoreNewsArticleImage']._loaded_options = None
  _globals['_NEWSROOMAPI'].methods_by_name['StoreNewsArticleImage']._serialized_options = b'\272\270\221\002\005\n\003\010\350 \202\323\344\223\0021\",/api/v1alpha1/newsroom/storenewsarticleimage:\001*'
  _globals['_NEWSROOMAPI'].methods_by_name['ListImagesForNewsArticle']._loaded_options = None
  _globals['_NEWSROOMAPI'].methods_by_name['ListImagesForNewsArticle']._serialized_options = b'\272\270\221\002\005\n\003\010\347 \202\323\344\223\0024\"//api/v1alpha1/newsroom/listimagesfornewsarticle:\001*'
  _globals['_NEWSROOMAPI']._serialized_start=156
  _globals['_NEWSROOMAPI']._serialized_end=2265
# @@protoc_insertion_point(module_scope)
