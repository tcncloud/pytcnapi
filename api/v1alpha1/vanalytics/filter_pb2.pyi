from api.v1alpha1.vanalytics import transcript_pb2 as _transcript_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFilterRequest(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: Filter
    def __init__(self, filter: _Optional[_Union[Filter, _Mapping]] = ...) -> None: ...

class ListFiltersRequest(_message.Message):
    __slots__ = ("page_size", "order_by", "page_token", "conflict", "flag_sid")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_FIELD_NUMBER: _ClassVar[int]
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    order_by: str
    page_token: str
    conflict: Filter
    flag_sid: int
    def __init__(self, page_size: _Optional[int] = ..., order_by: _Optional[str] = ..., page_token: _Optional[str] = ..., conflict: _Optional[_Union[Filter, _Mapping]] = ..., flag_sid: _Optional[int] = ...) -> None: ...

class ListFiltersResponse(_message.Message):
    __slots__ = ("next_page_token", "filters")
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    filters: _containers.RepeatedCompositeFieldContainer[Filter]
    def __init__(self, next_page_token: _Optional[str] = ..., filters: _Optional[_Iterable[_Union[Filter, _Mapping]]] = ...) -> None: ...

class UpdateFilterRequest(_message.Message):
    __slots__ = ("filter", "update_mask", "filter_sid")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    FILTER_SID_FIELD_NUMBER: _ClassVar[int]
    filter: Filter
    update_mask: _field_mask_pb2.FieldMask
    filter_sid: int
    def __init__(self, filter: _Optional[_Union[Filter, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., filter_sid: _Optional[int] = ...) -> None: ...

class DeleteFilterRequest(_message.Message):
    __slots__ = ("filter_sid",)
    FILTER_SID_FIELD_NUMBER: _ClassVar[int]
    RETURN_FIELD_NUMBER: _ClassVar[int]
    filter_sid: int
    def __init__(self, filter_sid: _Optional[int] = ..., **kwargs) -> None: ...

class DeleteFilterResponse(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: Filter
    def __init__(self, filter: _Optional[_Union[Filter, _Mapping]] = ...) -> None: ...

class GetFilterRequest(_message.Message):
    __slots__ = ("search_request", "name", "filter_sid")
    SEARCH_REQUEST_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_SID_FIELD_NUMBER: _ClassVar[int]
    search_request: _transcript_pb2.SearchRequest
    name: str
    filter_sid: int
    def __init__(self, search_request: _Optional[_Union[_transcript_pb2.SearchRequest, _Mapping]] = ..., name: _Optional[str] = ..., filter_sid: _Optional[int] = ...) -> None: ...

class Filter(_message.Message):
    __slots__ = ("filter_sid", "name", "search_request", "create_time", "version")
    FILTER_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEARCH_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    filter_sid: int
    name: str
    search_request: _transcript_pb2.SearchRequest
    create_time: _timestamp_pb2.Timestamp
    version: int
    def __init__(self, filter_sid: _Optional[int] = ..., name: _Optional[str] = ..., search_request: _Optional[_Union[_transcript_pb2.SearchRequest, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...
