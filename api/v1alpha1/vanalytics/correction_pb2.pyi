from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCorrectionRequest(_message.Message):
    __slots__ = ["correction"]
    CORRECTION_FIELD_NUMBER: _ClassVar[int]
    correction: Correction
    def __init__(self, correction: _Optional[_Union[Correction, _Mapping]] = ...) -> None: ...

class CreateCorrectionResponse(_message.Message):
    __slots__ = ["correction"]
    CORRECTION_FIELD_NUMBER: _ClassVar[int]
    correction: Correction
    def __init__(self, correction: _Optional[_Union[Correction, _Mapping]] = ...) -> None: ...

class Correction(_message.Message):
    __slots__ = ["correction_sid", "transcript_sid", "start_offset", "end_offset", "proposed_text", "channel"]
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
    def __init__(self, correction_sid: _Optional[int] = ..., transcript_sid: _Optional[int] = ..., start_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., end_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., proposed_text: _Optional[str] = ..., channel: _Optional[int] = ...) -> None: ...
