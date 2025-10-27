import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateCorrectionRequest(_message.Message):
    __slots__ = ()
    CORRECTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    correction: Correction
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, correction: _Optional[_Union[Correction, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCorrectionResponse(_message.Message):
    __slots__ = ()
    CORRECTION_FIELD_NUMBER: _ClassVar[int]
    correction: Correction
    def __init__(self, correction: _Optional[_Union[Correction, _Mapping]] = ...) -> None: ...

class CreateCorrectionRequest(_message.Message):
    __slots__ = ()
    CORRECTION_FIELD_NUMBER: _ClassVar[int]
    correction: Correction
    def __init__(self, correction: _Optional[_Union[Correction, _Mapping]] = ...) -> None: ...

class CreateCorrectionResponse(_message.Message):
    __slots__ = ()
    CORRECTION_FIELD_NUMBER: _ClassVar[int]
    correction: Correction
    def __init__(self, correction: _Optional[_Union[Correction, _Mapping]] = ...) -> None: ...

class GetCorrectionRequest(_message.Message):
    __slots__ = ()
    CORRECTION_SID_FIELD_NUMBER: _ClassVar[int]
    correction_sid: int
    def __init__(self, correction_sid: _Optional[int] = ...) -> None: ...

class ListCorrectionsRequest(_message.Message):
    __slots__ = ()
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    transcript_sid: int
    def __init__(self, transcript_sid: _Optional[int] = ...) -> None: ...

class ListCorrectionsResponse(_message.Message):
    __slots__ = ()
    CORRECTIONS_FIELD_NUMBER: _ClassVar[int]
    corrections: _containers.RepeatedCompositeFieldContainer[Correction]
    def __init__(self, corrections: _Optional[_Iterable[_Union[Correction, _Mapping]]] = ...) -> None: ...

class DeleteCorrectionRequest(_message.Message):
    __slots__ = ()
    CORRECTION_SID_FIELD_NUMBER: _ClassVar[int]
    RETURN_FIELD_NUMBER: _ClassVar[int]
    correction_sid: int
    def __init__(self, correction_sid: _Optional[int] = ..., **kwargs) -> None: ...

class DeleteCorrectionResponse(_message.Message):
    __slots__ = ()
    CORRECTION_FIELD_NUMBER: _ClassVar[int]
    correction: Correction
    def __init__(self, correction: _Optional[_Union[Correction, _Mapping]] = ...) -> None: ...

class Correction(_message.Message):
    __slots__ = ()
    CORRECTION_SID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_TEXT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    correction_sid: int
    transcript_sid: int
    start_offset: _duration_pb2.Duration
    end_offset: _duration_pb2.Duration
    proposed_text: str
    channel: int
    def __init__(self, correction_sid: _Optional[int] = ..., transcript_sid: _Optional[int] = ..., start_offset: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., end_offset: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., proposed_text: _Optional[str] = ..., channel: _Optional[int] = ...) -> None: ...
