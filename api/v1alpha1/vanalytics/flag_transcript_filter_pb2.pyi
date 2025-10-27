from api.v1alpha1.vanalytics import filter_snapshot_pb2 as _filter_snapshot_pb2
from api.v1alpha1.vanalytics import flag_snapshot_pb2 as _flag_snapshot_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListFlagTranscriptFiltersRequest(_message.Message):
    __slots__ = ()
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    FLAG_SNAPSHOT_MASK_FIELD_NUMBER: _ClassVar[int]
    FILTER_SNAPSHOT_MASK_FIELD_NUMBER: _ClassVar[int]
    transcript_sid: int
    flag_snapshot_mask: _field_mask_pb2.FieldMask
    filter_snapshot_mask: _field_mask_pb2.FieldMask
    def __init__(self, transcript_sid: _Optional[int] = ..., flag_snapshot_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., filter_snapshot_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListFlagTranscriptFiltersResponse(_message.Message):
    __slots__ = ()
    FLAG_TRANSCRIPT_FILTERS_FIELD_NUMBER: _ClassVar[int]
    flag_transcript_filters: _containers.RepeatedCompositeFieldContainer[FlagTranscriptFilter]
    def __init__(self, flag_transcript_filters: _Optional[_Iterable[_Union[FlagTranscriptFilter, _Mapping]]] = ...) -> None: ...

class FlagTranscriptFilter(_message.Message):
    __slots__ = ()
    FLAG_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    FILTER_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    flag_snapshot: _flag_snapshot_pb2.FlagSnapshot
    filter_snapshot: _filter_snapshot_pb2.FilterSnapshot
    def __init__(self, flag_snapshot: _Optional[_Union[_flag_snapshot_pb2.FlagSnapshot, _Mapping]] = ..., filter_snapshot: _Optional[_Union[_filter_snapshot_pb2.FilterSnapshot, _Mapping]] = ...) -> None: ...
