# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/translations/v1alpha1/service.proto
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
    'services/translations/v1alpha1/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from services.translations.v1alpha1 import entities_pb2 as services_dot_translations_dot_v1alpha1_dot_entities__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,services/translations/v1alpha1/service.proto\x12\x1eservices.translations.v1alpha1\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a-services/translations/v1alpha1/entities.proto2\x84\x19\n\x13TranslationsService\x12\xcd\x01\n\x11TranslateTemplate\x12\x38.services.translations.v1alpha1.TranslateTemplateRequest\x1a\x39.services.translations.v1alpha1.TranslateTemplateResponse\"C\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x36\"1/services/translations/v1alpha1/translatetemplate:\x01*\x12\xcc\x01\n\x10ListTranslations\x12\x37.services.translations.v1alpha1.ListTranslationsRequest\x1a\x38.services.translations.v1alpha1.ListTranslationsResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x35\"0/services/translations/v1alpha1/listtranslations:\x01*\x12\xbd\x01\n\rListLanguages\x12\x34.services.translations.v1alpha1.ListLanguagesRequest\x1a\x35.services.translations.v1alpha1.ListLanguagesResponse\"?\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x32\"-/services/translations/v1alpha1/listlanguages:\x01*\x12\xbc\x01\n\x0cListContexts\x12\x33.services.translations.v1alpha1.ListContextsRequest\x1a\x34.services.translations.v1alpha1.ListContextsResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x31\",/services/translations/v1alpha1/listcontexts:\x01*\x12\xd0\x01\n\x11\x43reateTranslation\x12\x38.services.translations.v1alpha1.CreateTranslationRequest\x1a\x39.services.translations.v1alpha1.CreateTranslationResponse\"F\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x36\"1/services/translations/v1alpha1/createtranslation:\x01*\x12\xd0\x01\n\x11UpdateTranslation\x12\x38.services.translations.v1alpha1.UpdateTranslationRequest\x1a\x39.services.translations.v1alpha1.UpdateTranslationResponse\"F\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x36\"1/services/translations/v1alpha1/updatetranslation:\x01*\x12\xe0\x01\n\x15TriggerLLMTranslation\x12<.services.translations.v1alpha1.TriggerLLMTranslationRequest\x1a=.services.translations.v1alpha1.TriggerLLMTranslationResponse\"J\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02:\"5/services/translations/v1alpha1/triggerllmtranslation:\x01*\x12\xe4\x01\n\x16TriggerLLMTranslations\x12=.services.translations.v1alpha1.TriggerLLMTranslationsRequest\x1a>.services.translations.v1alpha1.TriggerLLMTranslationsResponse\"K\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02;\"6/services/translations/v1alpha1/triggerllmtranslations:\x01*\x12\xcc\x01\n\x10SetSystemMessage\x12\x37.services.translations.v1alpha1.SetSystemMessageRequest\x1a\x38.services.translations.v1alpha1.SetSystemMessageResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x35\"0/services/translations/v1alpha1/setsystemmessage:\x01*\x12\xcc\x01\n\x10GetSystemMessage\x12\x37.services.translations.v1alpha1.GetSystemMessageRequest\x1a\x38.services.translations.v1alpha1.GetSystemMessageResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x35\"0/services/translations/v1alpha1/getsystemmessage:\x01*\x12\xd0\x01\n\x11TestSystemMessage\x12\x38.services.translations.v1alpha1.TestSystemMessageRequest\x1a\x39.services.translations.v1alpha1.TestSystemMessageResponse\"F\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x36\"1/services/translations/v1alpha1/testsystemmessage:\x01*\x12\xc0\x01\n\rEnableContext\x12\x34.services.translations.v1alpha1.EnableContextRequest\x1a\x35.services.translations.v1alpha1.EnableContextResponse\"B\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x32\"-/services/translations/v1alpha1/enablecontext:\x01*\x12\xc4\x01\n\x0e\x44isableContext\x12\x35.services.translations.v1alpha1.DisableContextRequest\x1a\x36.services.translations.v1alpha1.DisableContextResponse\"C\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x33\"./services/translations/v1alpha1/disablecontext:\x01*\x12\xfc\x01\n\x1c\x44\x65leteTranslationsByTemplate\x12\x43.services.translations.v1alpha1.DeleteTranslationsByTemplateRequest\x1a\x44.services.translations.v1alpha1.DeleteTranslationsByTemplateResponse\"Q\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x41\"</services/translations/v1alpha1/deletetranslationsbytemplate:\x01*\x12\xe4\x01\n\x16\x42ulkDeleteTranslations\x12=.services.translations.v1alpha1.BulkDeleteTranslationsRequest\x1a>.services.translations.v1alpha1.BulkDeleteTranslationsResponse\"K\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02;\"6/services/translations/v1alpha1/bulkdeletetranslations:\x01*B\xcc\x01\n\"com.services.translations.v1alpha1B\x0cServiceProtoP\x01\xa2\x02\x03STX\xaa\x02\x1eServices.Translations.V1alpha1\xca\x02\x1eServices\\Translations\\V1alpha1\xe2\x02*Services\\Translations\\V1alpha1\\GPBMetadata\xea\x02 Services::Translations::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.translations.v1alpha1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.services.translations.v1alpha1B\014ServiceProtoP\001\242\002\003STX\252\002\036Services.Translations.V1alpha1\312\002\036Services\\Translations\\V1alpha1\342\002*Services\\Translations\\V1alpha1\\GPBMetadata\352\002 Services::Translations::V1alpha1'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['TranslateTemplate']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['TranslateTemplate']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0026\"1/services/translations/v1alpha1/translatetemplate:\001*'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['ListTranslations']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['ListTranslations']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0025\"0/services/translations/v1alpha1/listtranslations:\001*'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['ListLanguages']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['ListLanguages']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0022\"-/services/translations/v1alpha1/listlanguages:\001*'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['ListContexts']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['ListContexts']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0021\",/services/translations/v1alpha1/listcontexts:\001*'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['CreateTranslation']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['CreateTranslation']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0026\"1/services/translations/v1alpha1/createtranslation:\001*'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['UpdateTranslation']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['UpdateTranslation']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0026\"1/services/translations/v1alpha1/updatetranslation:\001*'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['TriggerLLMTranslation']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['TriggerLLMTranslation']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002:\"5/services/translations/v1alpha1/triggerllmtranslation:\001*'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['TriggerLLMTranslations']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['TriggerLLMTranslations']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002;\"6/services/translations/v1alpha1/triggerllmtranslations:\001*'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['SetSystemMessage']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['SetSystemMessage']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0025\"0/services/translations/v1alpha1/setsystemmessage:\001*'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['GetSystemMessage']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['GetSystemMessage']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0025\"0/services/translations/v1alpha1/getsystemmessage:\001*'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['TestSystemMessage']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['TestSystemMessage']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0026\"1/services/translations/v1alpha1/testsystemmessage:\001*'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['EnableContext']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['EnableContext']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0022\"-/services/translations/v1alpha1/enablecontext:\001*'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['DisableContext']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['DisableContext']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0023\"./services/translations/v1alpha1/disablecontext:\001*'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['DeleteTranslationsByTemplate']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['DeleteTranslationsByTemplate']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002A\"</services/translations/v1alpha1/deletetranslationsbytemplate:\001*'
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['BulkDeleteTranslations']._loaded_options = None
  _globals['_TRANSLATIONSSERVICE'].methods_by_name['BulkDeleteTranslations']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002;\"6/services/translations/v1alpha1/bulkdeletetranslations:\001*'
  _globals['_TRANSLATIONSSERVICE']._serialized_start=183
  _globals['_TRANSLATIONSSERVICE']._serialized_end=3387
# @@protoc_insertion_point(module_scope)
