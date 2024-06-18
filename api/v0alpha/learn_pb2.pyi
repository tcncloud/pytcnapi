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
    __slots__ = ("content", "last_edited_timestamp", "images", "title", "total_view_count", "last_edited_user")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_USER_FIELD_NUMBER: _ClassVar[int]
    content: str
    last_edited_timestamp: _timestamp_pb2.Timestamp
    images: _containers.RepeatedCompositeFieldContainer[LearnImage]
    title: str
    total_view_count: int
    last_edited_user: str
    def __init__(self, content: _Optional[str] = ..., last_edited_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., images: _Optional[_Iterable[_Union[LearnImage, _Mapping]]] = ..., title: _Optional[str] = ..., total_view_count: _Optional[int] = ..., last_edited_user: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("locale", "category", "version")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    locale: str
    category: str
    version: str
    def __init__(self, locale: _Optional[str] = ..., category: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("locale", "article_names", "version")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    ARTICLE_NAMES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    locale: str
    article_names: _containers.RepeatedScalarFieldContainer[str]
    version: str
    def __init__(self, locale: _Optional[str] = ..., article_names: _Optional[_Iterable[str]] = ..., version: _Optional[str] = ...) -> None: ...

class DeleteStandaloneRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SnippetReq(_message.Message):
    __slots__ = ("locale", "version")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    locale: str
    version: str
    def __init__(self, locale: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("locale", "url", "version")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    locale: str
    url: _containers.RepeatedScalarFieldContainer[str]
    version: str
    def __init__(self, locale: _Optional[str] = ..., url: _Optional[_Iterable[str]] = ..., version: _Optional[str] = ...) -> None: ...

class DeleteLearnPagesRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateEditVersionReq(_message.Message):
    __slots__ = ("src_version", "dest_version", "dest_version_name")
    SRC_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEST_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEST_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    src_version: str
    dest_version: str
    dest_version_name: str
    def __init__(self, src_version: _Optional[str] = ..., dest_version: _Optional[str] = ..., dest_version_name: _Optional[str] = ...) -> None: ...

class CreateEditVersionRes(_message.Message):
    __slots__ = ("version_details",)
    VERSION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    version_details: VersionDetails
    def __init__(self, version_details: _Optional[_Union[VersionDetails, _Mapping]] = ...) -> None: ...

class PublishVersionReq(_message.Message):
    __slots__ = ("publish_version",)
    PUBLISH_VERSION_FIELD_NUMBER: _ClassVar[int]
    publish_version: str
    def __init__(self, publish_version: _Optional[str] = ...) -> None: ...

class PublishVersionRes(_message.Message):
    __slots__ = ("version_details",)
    VERSION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    version_details: VersionDetails
    def __init__(self, version_details: _Optional[_Union[VersionDetails, _Mapping]] = ...) -> None: ...

class ContentByVersionReq(_message.Message):
    __slots__ = ("url", "locale", "version")
    URL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    url: str
    locale: str
    version: str
    def __init__(self, url: _Optional[str] = ..., locale: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class UpdateByVersionReq(_message.Message):
    __slots__ = ("url", "locale", "content", "version", "message", "title")
    URL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    url: str
    locale: str
    content: str
    version: str
    message: str
    title: str
    def __init__(self, url: _Optional[str] = ..., locale: _Optional[str] = ..., content: _Optional[str] = ..., version: _Optional[str] = ..., message: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class SearchContentByVersionReq(_message.Message):
    __slots__ = ("search_content", "locale", "field_mask", "version")
    SEARCH_CONTENT_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    search_content: str
    locale: str
    field_mask: _field_mask_pb2.FieldMask
    version: str
    def __init__(self, search_content: _Optional[str] = ..., locale: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., version: _Optional[str] = ...) -> None: ...

class ReviewFileVersionsReq(_message.Message):
    __slots__ = ("url", "version", "locale")
    URL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    url: str
    version: str
    locale: str
    def __init__(self, url: _Optional[str] = ..., version: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class ReviewFileVersionsRes(_message.Message):
    __slots__ = ("content", "diff_content", "images")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DIFF_CONTENT_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    content: str
    diff_content: str
    images: _containers.RepeatedCompositeFieldContainer[LearnImage]
    def __init__(self, content: _Optional[str] = ..., diff_content: _Optional[str] = ..., images: _Optional[_Iterable[_Union[LearnImage, _Mapping]]] = ...) -> None: ...

class ReviewVersionReq(_message.Message):
    __slots__ = ("version", "locale")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    version: str
    locale: str
    def __init__(self, version: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class ReviewVersionRes(_message.Message):
    __slots__ = ("diff_urls", "diff_file_names", "src_content", "dest_content")
    DIFF_URLS_FIELD_NUMBER: _ClassVar[int]
    DIFF_FILE_NAMES_FIELD_NUMBER: _ClassVar[int]
    SRC_CONTENT_FIELD_NUMBER: _ClassVar[int]
    DEST_CONTENT_FIELD_NUMBER: _ClassVar[int]
    diff_urls: str
    diff_file_names: str
    src_content: str
    dest_content: str
    def __init__(self, diff_urls: _Optional[str] = ..., diff_file_names: _Optional[str] = ..., src_content: _Optional[str] = ..., dest_content: _Optional[str] = ...) -> None: ...

class ListVersionsReq(_message.Message):
    __slots__ = ("locale",)
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    locale: str
    def __init__(self, locale: _Optional[str] = ...) -> None: ...

class ListVersionsRes(_message.Message):
    __slots__ = ("versions", "version_details")
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    VERSION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    versions: _containers.RepeatedScalarFieldContainer[str]
    version_details: _containers.RepeatedCompositeFieldContainer[VersionDetails]
    def __init__(self, versions: _Optional[_Iterable[str]] = ..., version_details: _Optional[_Iterable[_Union[VersionDetails, _Mapping]]] = ...) -> None: ...

class VersionDetails(_message.Message):
    __slots__ = ("version", "version_name", "date_created", "date_published", "status")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    version: str
    version_name: str
    date_created: _timestamp_pb2.Timestamp
    date_published: _timestamp_pb2.Timestamp
    status: str
    def __init__(self, version: _Optional[str] = ..., version_name: _Optional[str] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., date_published: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[str] = ...) -> None: ...

class DeleteVersionReq(_message.Message):
    __slots__ = ("locale", "version")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    locale: str
    version: str
    def __init__(self, locale: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class DeleteVersionRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
