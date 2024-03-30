# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/newsroom/entities.proto
# Protobuf Python Version: 5.26.1
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$api/v1alpha1/newsroom/entities.proto\x12\x15\x61pi.v1alpha1.newsroom\x1a\x1a\x61pi/commons/newsroom.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x90\x01\n\x18\x43reateNewsArticleRequest\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12\x18\n\x07\x63ontent\x18\x02 \x01(\tR\x07\x63ontent\x12\x16\n\x06\x61uthor\x18\x03 \x01(\tR\x06\x61uthor\x12,\n\x12image_reference_id\x18\x04 \x01(\tR\x10imageReferenceId\"o\n\x19\x43reateNewsArticleResponse\x12R\n\x0f\x61rticle_details\x18\x01 \x01(\x0b\x32).api.v1alpha1.newsroom.NewsArticleDetailsR\x0e\x61rticleDetails\"\x8c\x01\n\x17ListNewsArticlesRequest\x12\x36\n\x08statuses\x18\x01 \x03(\x0e\x32\x1a.api.commons.ArticleStatusR\x08statuses\x12\x39\n\nfield_mask\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"n\n\x18ListNewsArticlesResponse\x12R\n\x0f\x61rticle_details\x18\x01 \x03(\x0b\x32).api.v1alpha1.newsroom.NewsArticleDetailsR\x0e\x61rticleDetails\"G\n\x19GetNewsArticleByIdRequest\x12*\n\x0fnew_article_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\rnewArticleSid\"p\n\x1aGetNewsArticleByIdResponse\x12R\n\x0f\x61rticle_details\x18\x01 \x01(\x0b\x32).api.v1alpha1.newsroom.NewsArticleDetailsR\x0e\x61rticleDetails\"\xa9\x01\n\x18UpdateNewsArticleRequest\x12R\n\x0f\x61rticle_details\x18\x01 \x01(\x0b\x32).api.v1alpha1.newsroom.NewsArticleDetailsR\x0e\x61rticleDetails\x12\x39\n\nfield_mask\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"o\n\x19UpdateNewsArticleResponse\x12R\n\x0f\x61rticle_details\x18\x01 \x01(\x0b\x32).api.v1alpha1.newsroom.NewsArticleDetailsR\x0e\x61rticleDetails\"\xe6\x02\n\x12NewsArticleDetails\x12*\n\x0fnew_article_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\rnewArticleSid\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12\x18\n\x07\x63ontent\x18\x03 \x01(\tR\x07\x63ontent\x12\x32\n\x06status\x18\x04 \x01(\x0e\x32\x1a.api.commons.ArticleStatusR\x06status\x12=\n\x0c\x64\x61te_created\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64\x61teCreated\x12;\n\x0blast_edited\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nlastEdited\x12\x16\n\x06\x61uthor\x18\x07 \x01(\tR\x06\x61uthor\x12,\n\x12image_reference_id\x18\x08 \x01(\tR\x10imageReferenceId\"\x99\x02\n\x17PublishedArticleDetails\x12\x36\n\x15published_article_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x13publishedArticleSid\x12[\n\x14news_article_details\x18\x02 \x01(\x0b\x32).api.v1alpha1.newsroom.NewsArticleDetailsR\x12newsArticleDetails\x12\x41\n\x0e\x64\x61te_published\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rdatePublished\x12&\n\x0f\x64isplay_to_user\x18\x04 \x01(\x08R\rdisplayToUser\"\xc0\x02\n\x0cUserActivity\x12\x35\n\x15user_activity_log_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x12userActivityLogSid\x12=\n\x0c\x64\x61te_created\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64\x61teCreated\x12k\n\x15user_activity_details\x18\x03 \x01(\x0b\x32\x37.api.v1alpha1.newsroom.UserActivity.UserActivityDetailsR\x13userActivityDetails\x1aM\n\x13UserActivityDetails\x12\x36\n\x15published_article_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x13publishedArticleSid\"\x96\x01\n\x1d\x43reatePublishedArticleRequest\x12*\n\x0fnew_article_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\rnewArticleSid\x12&\n\x0f\x64isplay_to_user\x18\x02 \x01(\x08R\rdisplayToUser\x12!\n\x0c\x61rticle_link\x18\x03 \x01(\tR\x0b\x61rticleLink\"\x8c\x01\n\x1e\x43reatePublishedArticleResponse\x12j\n\x19published_article_details\x18\x01 \x01(\x0b\x32..api.v1alpha1.newsroom.PublishedArticleDetailsR\x17publishedArticleDetails\"\x1e\n\x1cListPublishedArticlesRequest\"\x8b\x01\n\x1dListPublishedArticlesResponse\x12j\n\x19published_article_details\x18\x01 \x03(\x0b\x32..api.v1alpha1.newsroom.PublishedArticleDetailsR\x17publishedArticleDetails\"\x84\x01\n\x1eGetPublishedArticleByIdRequest\x12*\n\x0fnew_article_sid\x18\x01 \x01(\x03\x42\x02\x18\x01R\rnewArticleSid\x12\x36\n\x15published_article_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x13publishedArticleSid\"\x8d\x01\n\x1fGetPublishedArticleByIdResponse\x12j\n\x19published_article_details\x18\x01 \x01(\x0b\x32..api.v1alpha1.newsroom.PublishedArticleDetailsR\x17publishedArticleDetails\"M\n\x13UserActivityRequest\x12\x36\n\x15published_article_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x13publishedArticleSid\"`\n\x14UserActivityResponse\x12H\n\ruser_activity\x18\x01 \x01(\x0b\x32#.api.v1alpha1.newsroom.UserActivityR\x0cuserActivity\"\x17\n\x15GetNewsForUserRequest\"\x84\x01\n\x16GetNewsForUserResponse\x12j\n\x19published_article_details\x18\x01 \x03(\x0b\x32..api.v1alpha1.newsroom.PublishedArticleDetailsR\x17publishedArticleDetails\"]\n\x1cStoreNewsArticleImageRequest\x12=\n\x05image\x18\x01 \x01(\x0b\x32\'.api.v1alpha1.newsroom.NewsArticleImageR\x05image\"\xdc\x01\n\x10NewsArticleImage\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12*\n\x0fnew_article_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\rnewArticleSid\x12\x18\n\x07\x63ontent\x18\x03 \x01(\tR\x07\x63ontent\x12!\n\x0c\x64ownload_url\x18\x04 \x01(\tR\x0b\x64ownloadUrl\x12,\n\x12image_reference_id\x18\x05 \x01(\tR\x10imageReferenceId\x12\x1d\n\nimage_type\x18\x06 \x01(\tR\timageType\"^\n\x1dStoreNewsArticleImageResponse\x12=\n\x05image\x18\x01 \x01(\x0b\x32\'.api.v1alpha1.newsroom.NewsArticleImageR\x05image\"M\n\x1fListImagesForNewsArticleRequest\x12*\n\x0fnew_article_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\rnewArticleSid\"{\n ListImagesForNewsArticleResponse\x12W\n\x13news_article_images\x18\x01 \x03(\x0b\x32\'.api.v1alpha1.newsroom.NewsArticleImageR\x11newsArticleImagesB\xa0\x01\n\x19\x63om.api.v1alpha1.newsroomB\rEntitiesProtoP\x01\xa2\x02\x03\x41VN\xaa\x02\x15\x41pi.V1alpha1.Newsroom\xca\x02\x15\x41pi\\V1alpha1\\Newsroom\xe2\x02!Api\\V1alpha1\\Newsroom\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Newsroomb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.newsroom.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.api.v1alpha1.newsroomB\rEntitiesProtoP\001\242\002\003AVN\252\002\025Api.V1alpha1.Newsroom\312\002\025Api\\V1alpha1\\Newsroom\342\002!Api\\V1alpha1\\Newsroom\\GPBMetadata\352\002\027Api::V1alpha1::Newsroom'
  _globals['_GETNEWSARTICLEBYIDREQUEST'].fields_by_name['new_article_sid']._loaded_options = None
  _globals['_GETNEWSARTICLEBYIDREQUEST'].fields_by_name['new_article_sid']._serialized_options = b'0\001'
  _globals['_NEWSARTICLEDETAILS'].fields_by_name['new_article_sid']._loaded_options = None
  _globals['_NEWSARTICLEDETAILS'].fields_by_name['new_article_sid']._serialized_options = b'0\001'
  _globals['_PUBLISHEDARTICLEDETAILS'].fields_by_name['published_article_sid']._loaded_options = None
  _globals['_PUBLISHEDARTICLEDETAILS'].fields_by_name['published_article_sid']._serialized_options = b'0\001'
  _globals['_USERACTIVITY_USERACTIVITYDETAILS'].fields_by_name['published_article_sid']._loaded_options = None
  _globals['_USERACTIVITY_USERACTIVITYDETAILS'].fields_by_name['published_article_sid']._serialized_options = b'0\001'
  _globals['_USERACTIVITY'].fields_by_name['user_activity_log_sid']._loaded_options = None
  _globals['_USERACTIVITY'].fields_by_name['user_activity_log_sid']._serialized_options = b'0\001'
  _globals['_CREATEPUBLISHEDARTICLEREQUEST'].fields_by_name['new_article_sid']._loaded_options = None
  _globals['_CREATEPUBLISHEDARTICLEREQUEST'].fields_by_name['new_article_sid']._serialized_options = b'0\001'
  _globals['_GETPUBLISHEDARTICLEBYIDREQUEST'].fields_by_name['new_article_sid']._loaded_options = None
  _globals['_GETPUBLISHEDARTICLEBYIDREQUEST'].fields_by_name['new_article_sid']._serialized_options = b'\030\001'
  _globals['_GETPUBLISHEDARTICLEBYIDREQUEST'].fields_by_name['published_article_sid']._loaded_options = None
  _globals['_GETPUBLISHEDARTICLEBYIDREQUEST'].fields_by_name['published_article_sid']._serialized_options = b'0\001'
  _globals['_USERACTIVITYREQUEST'].fields_by_name['published_article_sid']._loaded_options = None
  _globals['_USERACTIVITYREQUEST'].fields_by_name['published_article_sid']._serialized_options = b'0\001'
  _globals['_NEWSARTICLEIMAGE'].fields_by_name['new_article_sid']._loaded_options = None
  _globals['_NEWSARTICLEIMAGE'].fields_by_name['new_article_sid']._serialized_options = b'0\001'
  _globals['_LISTIMAGESFORNEWSARTICLEREQUEST'].fields_by_name['new_article_sid']._loaded_options = None
  _globals['_LISTIMAGESFORNEWSARTICLEREQUEST'].fields_by_name['new_article_sid']._serialized_options = b'0\001'
  _globals['_CREATENEWSARTICLEREQUEST']._serialized_start=159
  _globals['_CREATENEWSARTICLEREQUEST']._serialized_end=303
  _globals['_CREATENEWSARTICLERESPONSE']._serialized_start=305
  _globals['_CREATENEWSARTICLERESPONSE']._serialized_end=416
  _globals['_LISTNEWSARTICLESREQUEST']._serialized_start=419
  _globals['_LISTNEWSARTICLESREQUEST']._serialized_end=559
  _globals['_LISTNEWSARTICLESRESPONSE']._serialized_start=561
  _globals['_LISTNEWSARTICLESRESPONSE']._serialized_end=671
  _globals['_GETNEWSARTICLEBYIDREQUEST']._serialized_start=673
  _globals['_GETNEWSARTICLEBYIDREQUEST']._serialized_end=744
  _globals['_GETNEWSARTICLEBYIDRESPONSE']._serialized_start=746
  _globals['_GETNEWSARTICLEBYIDRESPONSE']._serialized_end=858
  _globals['_UPDATENEWSARTICLEREQUEST']._serialized_start=861
  _globals['_UPDATENEWSARTICLEREQUEST']._serialized_end=1030
  _globals['_UPDATENEWSARTICLERESPONSE']._serialized_start=1032
  _globals['_UPDATENEWSARTICLERESPONSE']._serialized_end=1143
  _globals['_NEWSARTICLEDETAILS']._serialized_start=1146
  _globals['_NEWSARTICLEDETAILS']._serialized_end=1504
  _globals['_PUBLISHEDARTICLEDETAILS']._serialized_start=1507
  _globals['_PUBLISHEDARTICLEDETAILS']._serialized_end=1788
  _globals['_USERACTIVITY']._serialized_start=1791
  _globals['_USERACTIVITY']._serialized_end=2111
  _globals['_USERACTIVITY_USERACTIVITYDETAILS']._serialized_start=2034
  _globals['_USERACTIVITY_USERACTIVITYDETAILS']._serialized_end=2111
  _globals['_CREATEPUBLISHEDARTICLEREQUEST']._serialized_start=2114
  _globals['_CREATEPUBLISHEDARTICLEREQUEST']._serialized_end=2264
  _globals['_CREATEPUBLISHEDARTICLERESPONSE']._serialized_start=2267
  _globals['_CREATEPUBLISHEDARTICLERESPONSE']._serialized_end=2407
  _globals['_LISTPUBLISHEDARTICLESREQUEST']._serialized_start=2409
  _globals['_LISTPUBLISHEDARTICLESREQUEST']._serialized_end=2439
  _globals['_LISTPUBLISHEDARTICLESRESPONSE']._serialized_start=2442
  _globals['_LISTPUBLISHEDARTICLESRESPONSE']._serialized_end=2581
  _globals['_GETPUBLISHEDARTICLEBYIDREQUEST']._serialized_start=2584
  _globals['_GETPUBLISHEDARTICLEBYIDREQUEST']._serialized_end=2716
  _globals['_GETPUBLISHEDARTICLEBYIDRESPONSE']._serialized_start=2719
  _globals['_GETPUBLISHEDARTICLEBYIDRESPONSE']._serialized_end=2860
  _globals['_USERACTIVITYREQUEST']._serialized_start=2862
  _globals['_USERACTIVITYREQUEST']._serialized_end=2939
  _globals['_USERACTIVITYRESPONSE']._serialized_start=2941
  _globals['_USERACTIVITYRESPONSE']._serialized_end=3037
  _globals['_GETNEWSFORUSERREQUEST']._serialized_start=3039
  _globals['_GETNEWSFORUSERREQUEST']._serialized_end=3062
  _globals['_GETNEWSFORUSERRESPONSE']._serialized_start=3065
  _globals['_GETNEWSFORUSERRESPONSE']._serialized_end=3197
  _globals['_STORENEWSARTICLEIMAGEREQUEST']._serialized_start=3199
  _globals['_STORENEWSARTICLEIMAGEREQUEST']._serialized_end=3292
  _globals['_NEWSARTICLEIMAGE']._serialized_start=3295
  _globals['_NEWSARTICLEIMAGE']._serialized_end=3515
  _globals['_STORENEWSARTICLEIMAGERESPONSE']._serialized_start=3517
  _globals['_STORENEWSARTICLEIMAGERESPONSE']._serialized_end=3611
  _globals['_LISTIMAGESFORNEWSARTICLEREQUEST']._serialized_start=3613
  _globals['_LISTIMAGESFORNEWSARTICLEREQUEST']._serialized_end=3690
  _globals['_LISTIMAGESFORNEWSARTICLERESPONSE']._serialized_start=3692
  _globals['_LISTIMAGESFORNEWSARTICLERESPONSE']._serialized_end=3815
# @@protoc_insertion_point(module_scope)
