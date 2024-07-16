from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Translation(_message.Message):
    __slots__ = ("translation_id", "template", "context", "language_tag", "llm_translation", "manual_translation")
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    LLM_TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    MANUAL_TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    translation_id: str
    template: str
    context: str
    language_tag: str
    llm_translation: str
    manual_translation: str
    def __init__(self, translation_id: _Optional[str] = ..., template: _Optional[str] = ..., context: _Optional[str] = ..., language_tag: _Optional[str] = ..., llm_translation: _Optional[str] = ..., manual_translation: _Optional[str] = ...) -> None: ...

class TranslateTemplateRequest(_message.Message):
    __slots__ = ("template", "context")
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    template: str
    context: str
    def __init__(self, template: _Optional[str] = ..., context: _Optional[str] = ...) -> None: ...

class TranslateTemplateResponse(_message.Message):
    __slots__ = ("translations",)
    TRANSLATIONS_FIELD_NUMBER: _ClassVar[int]
    translations: _containers.RepeatedCompositeFieldContainer[Translation]
    def __init__(self, translations: _Optional[_Iterable[_Union[Translation, _Mapping]]] = ...) -> None: ...

class ListTranslationsRequest(_message.Message):
    __slots__ = ("context", "language_tag")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    context: str
    language_tag: str
    def __init__(self, context: _Optional[str] = ..., language_tag: _Optional[str] = ...) -> None: ...

class ListTranslationsResponse(_message.Message):
    __slots__ = ("translations",)
    TRANSLATIONS_FIELD_NUMBER: _ClassVar[int]
    translations: _containers.RepeatedCompositeFieldContainer[Translation]
    def __init__(self, translations: _Optional[_Iterable[_Union[Translation, _Mapping]]] = ...) -> None: ...

class UpdateTranslationRequest(_message.Message):
    __slots__ = ("translation_id", "translation")
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    translation_id: str
    translation: str
    def __init__(self, translation_id: _Optional[str] = ..., translation: _Optional[str] = ...) -> None: ...

class UpdateTranslationResponse(_message.Message):
    __slots__ = ("translation",)
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    translation: Translation
    def __init__(self, translation: _Optional[_Union[Translation, _Mapping]] = ...) -> None: ...

class TriggerLLMTranslationRequest(_message.Message):
    __slots__ = ("translation_id",)
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    translation_id: str
    def __init__(self, translation_id: _Optional[str] = ...) -> None: ...

class TriggerLLMTranslationResponse(_message.Message):
    __slots__ = ("translation",)
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    translation: Translation
    def __init__(self, translation: _Optional[_Union[Translation, _Mapping]] = ...) -> None: ...

class SetSystemMessageRequest(_message.Message):
    __slots__ = ("context", "system_message")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    context: str
    system_message: str
    def __init__(self, context: _Optional[str] = ..., system_message: _Optional[str] = ...) -> None: ...

class SetSystemMessageResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSystemMessageRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: str
    def __init__(self, context: _Optional[str] = ...) -> None: ...

class GetSystemMessageResponse(_message.Message):
    __slots__ = ("system_message",)
    SYSTEM_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    system_message: str
    def __init__(self, system_message: _Optional[str] = ...) -> None: ...

class TestSystemMessageRequest(_message.Message):
    __slots__ = ("system_message", "template", "language_tag")
    SYSTEM_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    system_message: str
    template: str
    language_tag: str
    def __init__(self, system_message: _Optional[str] = ..., template: _Optional[str] = ..., language_tag: _Optional[str] = ...) -> None: ...

class TestSystemMessageResponse(_message.Message):
    __slots__ = ("translation",)
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    translation: str
    def __init__(self, translation: _Optional[str] = ...) -> None: ...

class TriggerLLMTranslationsRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: str
    def __init__(self, context: _Optional[str] = ...) -> None: ...

class TriggerLLMTranslationsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLanguagesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLanguagesResponse(_message.Message):
    __slots__ = ("languages",)
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    languages: _containers.RepeatedCompositeFieldContainer[LocalizationLanguage]
    def __init__(self, languages: _Optional[_Iterable[_Union[LocalizationLanguage, _Mapping]]] = ...) -> None: ...

class LocalizationLanguage(_message.Message):
    __slots__ = ("language_tag", "english_name")
    LANGUAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    ENGLISH_NAME_FIELD_NUMBER: _ClassVar[int]
    language_tag: str
    english_name: str
    def __init__(self, language_tag: _Optional[str] = ..., english_name: _Optional[str] = ...) -> None: ...
