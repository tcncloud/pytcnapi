from api.v1alpha1.vanalytics import filter_pb2 as _filter_pb2
from api.v1alpha1.vanalytics import flag_pb2 as _flag_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFlagFilterRequest(_message.Message):
    __slots__ = ("flag_filter",)
    FLAG_FILTER_FIELD_NUMBER: _ClassVar[int]
    flag_filter: FlagFilter
    def __init__(self, flag_filter: _Optional[_Union[FlagFilter, _Mapping]] = ...) -> None: ...

class ListFlagFiltersRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "flag_mask", "filter_mask", "flag_sids")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FLAG_MASK_FIELD_NUMBER: _ClassVar[int]
    FILTER_MASK_FIELD_NUMBER: _ClassVar[int]
    FLAG_SIDS_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    flag_mask: _field_mask_pb2.FieldMask
    filter_mask: _field_mask_pb2.FieldMask
    flag_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., flag_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., filter_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., flag_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class ListFlagFiltersResponse(_message.Message):
    __slots__ = ("next_page_token", "flag_filters")
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FLAG_FILTERS_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    flag_filters: _containers.RepeatedCompositeFieldContainer[FlagFilter]
    def __init__(self, next_page_token: _Optional[str] = ..., flag_filters: _Optional[_Iterable[_Union[FlagFilter, _Mapping]]] = ...) -> None: ...

class DeleteFlagFilterRequest(_message.Message):
    __slots__ = ("flag_sid", "filter_sid", "all")
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    FILTER_SID_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    flag_sid: int
    filter_sid: int
    all: bool
    def __init__(self, flag_sid: _Optional[int] = ..., filter_sid: _Optional[int] = ..., all: bool = ...) -> None: ...

class DeleteFlagFilterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FlagFilter(_message.Message):
    __slots__ = ("flag_filter_sid", "filter_sid", "flag_sid", "flag", "filter")
    FLAG_FILTER_SID_FIELD_NUMBER: _ClassVar[int]
    FILTER_SID_FIELD_NUMBER: _ClassVar[int]
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    flag_filter_sid: int
    filter_sid: int
    flag_sid: int
    flag: _flag_pb2.Flag
    filter: _filter_pb2.Filter
    def __init__(self, flag_filter_sid: _Optional[int] = ..., filter_sid: _Optional[int] = ..., flag_sid: _Optional[int] = ..., flag: _Optional[_Union[_flag_pb2.Flag, _Mapping]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...
