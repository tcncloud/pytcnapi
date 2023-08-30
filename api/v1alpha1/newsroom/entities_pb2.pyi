from api.commons import newsroom_pb2 as _newsroom_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateNewsArticleRequest(_message.Message):
    __slots__ = ["title", "content"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    title: str
    content: str
    def __init__(self, title: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class CreateNewsArticleResponse(_message.Message):
    __slots__ = ["article_details"]
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    article_details: NewsArticleDetails
    def __init__(self, article_details: _Optional[_Union[NewsArticleDetails, _Mapping]] = ...) -> None: ...

class ListNewsArticlesRequest(_message.Message):
    __slots__ = ["statuses", "field_mask"]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    statuses: _containers.RepeatedScalarFieldContainer[_newsroom_pb2.ArticleStatus]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, statuses: _Optional[_Iterable[_Union[_newsroom_pb2.ArticleStatus, str]]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListNewsArticlesResponse(_message.Message):
    __slots__ = ["article_details"]
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    article_details: _containers.RepeatedCompositeFieldContainer[NewsArticleDetails]
    def __init__(self, article_details: _Optional[_Iterable[_Union[NewsArticleDetails, _Mapping]]] = ...) -> None: ...

class GetNewsArticleByIdRequest(_message.Message):
    __slots__ = ["new_article_sid"]
    NEW_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    new_article_sid: int
    def __init__(self, new_article_sid: _Optional[int] = ...) -> None: ...

class GetNewsArticleByIdResponse(_message.Message):
    __slots__ = ["article_details"]
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    article_details: NewsArticleDetails
    def __init__(self, article_details: _Optional[_Union[NewsArticleDetails, _Mapping]] = ...) -> None: ...

class UpdateNewsArticleRequest(_message.Message):
    __slots__ = ["article_details", "field_mask"]
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    article_details: NewsArticleDetails
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, article_details: _Optional[_Union[NewsArticleDetails, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateNewsArticleResponse(_message.Message):
    __slots__ = ["article_details"]
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    article_details: NewsArticleDetails
    def __init__(self, article_details: _Optional[_Union[NewsArticleDetails, _Mapping]] = ...) -> None: ...

class NewsArticleDetails(_message.Message):
    __slots__ = ["new_article_sid", "title", "content", "status", "date_created", "last_edited"]
    NEW_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_FIELD_NUMBER: _ClassVar[int]
    new_article_sid: int
    title: str
    content: str
    status: _newsroom_pb2.ArticleStatus
    date_created: _timestamp_pb2.Timestamp
    last_edited: _timestamp_pb2.Timestamp
    def __init__(self, new_article_sid: _Optional[int] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., status: _Optional[_Union[_newsroom_pb2.ArticleStatus, str]] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_edited: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
