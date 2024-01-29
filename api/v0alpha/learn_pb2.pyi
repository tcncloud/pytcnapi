from annotations import authz_pb2 as _authz_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExistReq(_message.Message):
    __slots__ = ("url", "locale")
    URL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    url: str
    locale: str
    def __init__(self, url: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class ExistRes(_message.Message):
    __slots__ = ("exist",)
    EXIST_FIELD_NUMBER: _ClassVar[int]
    exist: bool
    def __init__(self, exist: bool = ...) -> None: ...

class ContentReq(_message.Message):
    __slots__ = ("url", "locale")
    URL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    url: str
    locale: str
    def __init__(self, url: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class ContentRes(_message.Message):
    __slots__ = ("content", "last_edited_timestamp", "images", "title", "total_view_count")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    content: str
    last_edited_timestamp: _timestamp_pb2.Timestamp
    images: _containers.RepeatedCompositeFieldContainer[LearnImage]
    title: str
    total_view_count: int
    def __init__(self, content: _Optional[str] = ..., last_edited_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., images: _Optional[_Iterable[_Union[LearnImage, _Mapping]]] = ..., title: _Optional[str] = ..., total_view_count: _Optional[int] = ...) -> None: ...

class ContentEditorDataReq(_message.Message):
    __slots__ = ("url", "locale")
    URL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    url: str
    locale: str
    def __init__(self, url: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class ContentEditorDataRes(_message.Message):
    __slots__ = ("last_edited_user",)
    LAST_EDITED_USER_FIELD_NUMBER: _ClassVar[int]
    last_edited_user: str
    def __init__(self, last_edited_user: _Optional[str] = ...) -> None: ...

class UpdateReq(_message.Message):
    __slots__ = ("url", "locale", "content", "message", "title")
    URL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    url: str
    locale: str
    content: str
    message: str
    title: str
    def __init__(self, url: _Optional[str] = ..., locale: _Optional[str] = ..., content: _Optional[str] = ..., message: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class UpdateRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExportManyReq(_message.Message):
    __slots__ = ("url", "locale", "content")
    URL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    url: _containers.RepeatedScalarFieldContainer[str]
    locale: str
    content: str
    def __init__(self, url: _Optional[_Iterable[str]] = ..., locale: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class ExportRes(_message.Message):
    __slots__ = ("download_url",)
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    download_url: str
    def __init__(self, download_url: _Optional[str] = ...) -> None: ...

class StoreStaticImageReq(_message.Message):
    __slots__ = ("image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: LearnImage
    def __init__(self, image: _Optional[_Union[LearnImage, _Mapping]] = ...) -> None: ...

class LearnImage(_message.Message):
    __slots__ = ("uuid", "content", "download_url")
    UUID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    content: str
    download_url: str
    def __init__(self, uuid: _Optional[str] = ..., content: _Optional[str] = ..., download_url: _Optional[str] = ...) -> None: ...

class StoreStaticImageRes(_message.Message):
    __slots__ = ("image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: LearnImage
    def __init__(self, image: _Optional[_Union[LearnImage, _Mapping]] = ...) -> None: ...

class SearchContentReq(_message.Message):
    __slots__ = ("search_content", "locale", "field_mask")
    SEARCH_CONTENT_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    search_content: str
    locale: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, search_content: _Optional[str] = ..., locale: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class SearchRes(_message.Message):
    __slots__ = ("search_details",)
    SEARCH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    search_details: _containers.RepeatedCompositeFieldContainer[LearnSearchDetails]
    def __init__(self, search_details: _Optional[_Iterable[_Union[LearnSearchDetails, _Mapping]]] = ...) -> None: ...

class LearnSearchDetails(_message.Message):
    __slots__ = ("name", "content")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    content: str
    def __init__(self, name: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class UploadDynamicScreenshotReq(_message.Message):
    __slots__ = ("data_learn_id", "version", "locale", "content")
    DATA_LEARN_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    data_learn_id: str
    version: int
    locale: str
    content: str
    def __init__(self, data_learn_id: _Optional[str] = ..., version: _Optional[int] = ..., locale: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class UploadDynamicScreenshotRes(_message.Message):
    __slots__ = ("data_learn_id", "download_url")
    DATA_LEARN_ID_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    data_learn_id: str
    download_url: str
    def __init__(self, data_learn_id: _Optional[str] = ..., download_url: _Optional[str] = ...) -> None: ...

class StandaloneReq(_message.Message):
    __slots__ = ("locale", "category")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    locale: str
    category: str
    def __init__(self, locale: _Optional[str] = ..., category: _Optional[str] = ...) -> None: ...

class StandaloneRes(_message.Message):
    __slots__ = ("standalone_details",)
    STANDALONE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    standalone_details: _containers.RepeatedCompositeFieldContainer[LearnStandaloneDetails]
    def __init__(self, standalone_details: _Optional[_Iterable[_Union[LearnStandaloneDetails, _Mapping]]] = ...) -> None: ...

class LearnStandaloneDetails(_message.Message):
    __slots__ = ("name", "content", "last_edited_timestamp", "title")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    content: str
    last_edited_timestamp: _timestamp_pb2.Timestamp
    title: str
    def __init__(self, name: _Optional[str] = ..., content: _Optional[str] = ..., last_edited_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., title: _Optional[str] = ...) -> None: ...

class DeleteStandaloneReq(_message.Message):
    __slots__ = ("locale", "article_names")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    ARTICLE_NAMES_FIELD_NUMBER: _ClassVar[int]
    locale: str
    article_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, locale: _Optional[str] = ..., article_names: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteStandaloneRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SnippetReq(_message.Message):
    __slots__ = ("locale",)
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    locale: str
    def __init__(self, locale: _Optional[str] = ...) -> None: ...

class SnippetRes(_message.Message):
    __slots__ = ("snippet_details",)
    SNIPPET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    snippet_details: _containers.RepeatedCompositeFieldContainer[LearnSnippetDetails]
    def __init__(self, snippet_details: _Optional[_Iterable[_Union[LearnSnippetDetails, _Mapping]]] = ...) -> None: ...

class LearnSnippetDetails(_message.Message):
    __slots__ = ("name", "content", "last_edited_timestamp", "title")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    content: str
    last_edited_timestamp: _timestamp_pb2.Timestamp
    title: str
    def __init__(self, name: _Optional[str] = ..., content: _Optional[str] = ..., last_edited_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., title: _Optional[str] = ...) -> None: ...

class DeleteLearnPagesReq(_message.Message):
    __slots__ = ("locale", "url")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    locale: str
    url: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, locale: _Optional[str] = ..., url: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteLearnPagesRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
