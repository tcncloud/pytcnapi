from wfo.vanalytics.v2 import flag_pb2 as _flag_pb2
from wfo.vanalytics.v2 import transcript_pb2 as _transcript_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFlagTranscriptRequest(_message.Message):
    __slots__ = ("transcript_sids", "flag")
    TRANSCRIPT_SIDS_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    transcript_sids: _containers.RepeatedScalarFieldContainer[int]
    flag: _flag_pb2.Flag
    def __init__(self, transcript_sids: _Optional[_Iterable[int]] = ..., flag: _Optional[_Union[_flag_pb2.Flag, _Mapping]] = ...) -> None: ...

class CreateFlagTranscriptResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
