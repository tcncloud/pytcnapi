# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/newsroom/entities.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import newsroom_pb2 as api_dot_commons_dot_newsroom__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$api/v1alpha1/newsroom/entities.proto\x12\x15\x61pi.v1alpha1.newsroom\x1a\x1a\x61pi/commons/newsroom.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"J\n\x18\x43reateNewsArticleRequest\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12\x18\n\x07\x63ontent\x18\x02 \x01(\tR\x07\x63ontent\"o\n\x19\x43reateNewsArticleResponse\x12R\n\x0f\x61rticle_details\x18\x01 \x01(\x0b\x32).api.v1alpha1.newsroom.NewsArticleDetailsR\x0e\x61rticleDetails\"\x8c\x01\n\x17ListNewsArticlesRequest\x12\x36\n\x08statuses\x18\x01 \x03(\x0e\x32\x1a.api.commons.ArticleStatusR\x08statuses\x12\x39\n\nfield_mask\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"n\n\x18ListNewsArticlesResponse\x12R\n\x0f\x61rticle_details\x18\x01 \x03(\x0b\x32).api.v1alpha1.newsroom.NewsArticleDetailsR\x0e\x61rticleDetails\"G\n\x19GetNewsArticleByIdRequest\x12*\n\x0fnew_article_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\rnewArticleSid\"p\n\x1aGetNewsArticleByIdResponse\x12R\n\x0f\x61rticle_details\x18\x01 \x01(\x0b\x32).api.v1alpha1.newsroom.NewsArticleDetailsR\x0e\x61rticleDetails\"\xa9\x01\n\x18UpdateNewsArticleRequest\x12R\n\x0f\x61rticle_details\x18\x01 \x01(\x0b\x32).api.v1alpha1.newsroom.NewsArticleDetailsR\x0e\x61rticleDetails\x12\x39\n\nfield_mask\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"o\n\x19UpdateNewsArticleResponse\x12R\n\x0f\x61rticle_details\x18\x01 \x01(\x0b\x32).api.v1alpha1.newsroom.NewsArticleDetailsR\x0e\x61rticleDetails\"\xa0\x02\n\x12NewsArticleDetails\x12*\n\x0fnew_article_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\rnewArticleSid\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12\x18\n\x07\x63ontent\x18\x03 \x01(\tR\x07\x63ontent\x12\x32\n\x06status\x18\x04 \x01(\x0e\x32\x1a.api.commons.ArticleStatusR\x06status\x12=\n\x0c\x64\x61te_created\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64\x61teCreated\x12;\n\x0blast_edited\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nlastEdited\"\x99\x02\n\x17PublishedArticleDetails\x12\x36\n\x15published_article_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x13publishedArticleSid\x12[\n\x14news_article_details\x18\x02 \x01(\x0b\x32).api.v1alpha1.newsroom.NewsArticleDetailsR\x12newsArticleDetails\x12\x41\n\x0e\x64\x61te_published\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rdatePublished\x12&\n\x0f\x64isplay_to_user\x18\x04 \x01(\x08R\rdisplayToUser\"o\n\x1d\x43reatePublishedArticleRequest\x12&\n\x0fnew_article_sid\x18\x01 \x01(\x03R\rnewArticleSid\x12&\n\x0f\x64isplay_to_user\x18\x02 \x01(\x08R\rdisplayToUser\"\x8c\x01\n\x1e\x43reatePublishedArticleResponse\x12j\n\x19published_article_details\x18\x01 \x01(\x0b\x32..api.v1alpha1.newsroom.PublishedArticleDetailsR\x17publishedArticleDetails\"\x1e\n\x1cListPublishedArticlesRequest\"\x8b\x01\n\x1dListPublishedArticlesResponse\x12j\n\x19published_article_details\x18\x01 \x03(\x0b\x32..api.v1alpha1.newsroom.PublishedArticleDetailsR\x17publishedArticleDetails\"L\n\x1eGetPublishedArticleByIdRequest\x12*\n\x0fnew_article_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\rnewArticleSid\"\x8d\x01\n\x1fGetPublishedArticleByIdResponse\x12j\n\x19published_article_details\x18\x01 \x01(\x0b\x32..api.v1alpha1.newsroom.PublishedArticleDetailsR\x17publishedArticleDetailsB\xa0\x01\n\x19\x63om.api.v1alpha1.newsroomB\rEntitiesProtoP\x01\xa2\x02\x03\x41VN\xaa\x02\x15\x41pi.V1alpha1.Newsroom\xca\x02\x15\x41pi\\V1alpha1\\Newsroom\xe2\x02!Api\\V1alpha1\\Newsroom\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Newsroomb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.newsroom.entities_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.api.v1alpha1.newsroomB\rEntitiesProtoP\001\242\002\003AVN\252\002\025Api.V1alpha1.Newsroom\312\002\025Api\\V1alpha1\\Newsroom\342\002!Api\\V1alpha1\\Newsroom\\GPBMetadata\352\002\027Api::V1alpha1::Newsroom'
  _GETNEWSARTICLEBYIDREQUEST.fields_by_name['new_article_sid']._options = None
  _GETNEWSARTICLEBYIDREQUEST.fields_by_name['new_article_sid']._serialized_options = b'0\001'
  _NEWSARTICLEDETAILS.fields_by_name['new_article_sid']._options = None
  _NEWSARTICLEDETAILS.fields_by_name['new_article_sid']._serialized_options = b'0\001'
  _PUBLISHEDARTICLEDETAILS.fields_by_name['published_article_sid']._options = None
  _PUBLISHEDARTICLEDETAILS.fields_by_name['published_article_sid']._serialized_options = b'0\001'
  _GETPUBLISHEDARTICLEBYIDREQUEST.fields_by_name['new_article_sid']._options = None
  _GETPUBLISHEDARTICLEBYIDREQUEST.fields_by_name['new_article_sid']._serialized_options = b'0\001'
  _globals['_CREATENEWSARTICLEREQUEST']._serialized_start=158
  _globals['_CREATENEWSARTICLEREQUEST']._serialized_end=232
  _globals['_CREATENEWSARTICLERESPONSE']._serialized_start=234
  _globals['_CREATENEWSARTICLERESPONSE']._serialized_end=345
  _globals['_LISTNEWSARTICLESREQUEST']._serialized_start=348
  _globals['_LISTNEWSARTICLESREQUEST']._serialized_end=488
  _globals['_LISTNEWSARTICLESRESPONSE']._serialized_start=490
  _globals['_LISTNEWSARTICLESRESPONSE']._serialized_end=600
  _globals['_GETNEWSARTICLEBYIDREQUEST']._serialized_start=602
  _globals['_GETNEWSARTICLEBYIDREQUEST']._serialized_end=673
  _globals['_GETNEWSARTICLEBYIDRESPONSE']._serialized_start=675
  _globals['_GETNEWSARTICLEBYIDRESPONSE']._serialized_end=787
  _globals['_UPDATENEWSARTICLEREQUEST']._serialized_start=790
  _globals['_UPDATENEWSARTICLEREQUEST']._serialized_end=959
  _globals['_UPDATENEWSARTICLERESPONSE']._serialized_start=961
  _globals['_UPDATENEWSARTICLERESPONSE']._serialized_end=1072
  _globals['_NEWSARTICLEDETAILS']._serialized_start=1075
  _globals['_NEWSARTICLEDETAILS']._serialized_end=1363
  _globals['_PUBLISHEDARTICLEDETAILS']._serialized_start=1366
  _globals['_PUBLISHEDARTICLEDETAILS']._serialized_end=1647
  _globals['_CREATEPUBLISHEDARTICLEREQUEST']._serialized_start=1649
  _globals['_CREATEPUBLISHEDARTICLEREQUEST']._serialized_end=1760
  _globals['_CREATEPUBLISHEDARTICLERESPONSE']._serialized_start=1763
  _globals['_CREATEPUBLISHEDARTICLERESPONSE']._serialized_end=1903
  _globals['_LISTPUBLISHEDARTICLESREQUEST']._serialized_start=1905
  _globals['_LISTPUBLISHEDARTICLESREQUEST']._serialized_end=1935
  _globals['_LISTPUBLISHEDARTICLESRESPONSE']._serialized_start=1938
  _globals['_LISTPUBLISHEDARTICLESRESPONSE']._serialized_end=2077
  _globals['_GETPUBLISHEDARTICLEBYIDREQUEST']._serialized_start=2079
  _globals['_GETPUBLISHEDARTICLEBYIDREQUEST']._serialized_end=2155
  _globals['_GETPUBLISHEDARTICLEBYIDRESPONSE']._serialized_start=2158
  _globals['_GETPUBLISHEDARTICLEBYIDRESPONSE']._serialized_end=2299
# @@protoc_insertion_point(module_scope)
