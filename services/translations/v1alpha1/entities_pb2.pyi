from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
