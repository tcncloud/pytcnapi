from api.commons import org_pb2 as _org_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SoundboardDetails(_message.Message):
    __slots__ = ("soundboard_id", "file_name", "file_type", "title", "description", "date_created", "last_modified", "file_size", "recording_length")
    SOUNDBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    RECORDING_LENGTH_FIELD_NUMBER: _ClassVar[int]
    soundboard_id: int
    file_name: str
    file_type: _org_pb2.RecordingFileType
    title: str
    description: str
    date_created: _timestamp_pb2.Timestamp
    last_modified: _timestamp_pb2.Timestamp
    file_size: int
    recording_length: int
    def __init__(self, soundboard_id: _Optional[int] = ..., file_name: _Optional[str] = ..., file_type: _Optional[_Union[_org_pb2.RecordingFileType, str]] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_modified: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., file_size: _Optional[int] = ..., recording_length: _Optional[int] = ...) -> None: ...

class GetSoundboardFileReq(_message.Message):
    __slots__ = ("soundboard_id",)
    SOUNDBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    soundboard_id: int
    def __init__(self, soundboard_id: _Optional[int] = ...) -> None: ...

class GetSoundboardFileRes(_message.Message):
    __slots__ = ("soundboard_file",)
    SOUNDBOARD_FILE_FIELD_NUMBER: _ClassVar[int]
    soundboard_file: bytes
    def __init__(self, soundboard_file: _Optional[bytes] = ...) -> None: ...

class GetSoundboardReq(_message.Message):
    __slots__ = ("soundboard_id",)
    SOUNDBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    soundboard_id: int
    def __init__(self, soundboard_id: _Optional[int] = ...) -> None: ...

class GetSoundboardRes(_message.Message):
    __slots__ = ("soundboard",)
    SOUNDBOARD_FIELD_NUMBER: _ClassVar[int]
    soundboard: SoundboardDetails
    def __init__(self, soundboard: _Optional[_Union[SoundboardDetails, _Mapping]] = ...) -> None: ...

class CreateSoundboardReq(_message.Message):
    __slots__ = ("soundboard", "fts_id")
    SOUNDBOARD_FIELD_NUMBER: _ClassVar[int]
    FTS_ID_FIELD_NUMBER: _ClassVar[int]
    soundboard: SoundboardDetails
    fts_id: str
    def __init__(self, soundboard: _Optional[_Union[SoundboardDetails, _Mapping]] = ..., fts_id: _Optional[str] = ...) -> None: ...

class CreateSoundboardRes(_message.Message):
    __slots__ = ("soundboard_id", "fts_id")
    SOUNDBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    FTS_ID_FIELD_NUMBER: _ClassVar[int]
    soundboard_id: int
    fts_id: str
    def __init__(self, soundboard_id: _Optional[int] = ..., fts_id: _Optional[str] = ...) -> None: ...

class ListSoundboardsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSoundboardsRes(_message.Message):
    __slots__ = ("soundboards",)
    SOUNDBOARDS_FIELD_NUMBER: _ClassVar[int]
    soundboards: _containers.RepeatedCompositeFieldContainer[SoundboardDetails]
    def __init__(self, soundboards: _Optional[_Iterable[_Union[SoundboardDetails, _Mapping]]] = ...) -> None: ...

class UpdateSoundboardReq(_message.Message):
    __slots__ = ("soundboard",)
    SOUNDBOARD_FIELD_NUMBER: _ClassVar[int]
    soundboard: SoundboardDetails
    def __init__(self, soundboard: _Optional[_Union[SoundboardDetails, _Mapping]] = ...) -> None: ...

class UpdateSoundboardRes(_message.Message):
    __slots__ = ("soundboard_id",)
    SOUNDBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    soundboard_id: int
    def __init__(self, soundboard_id: _Optional[int] = ...) -> None: ...

class DeleteSoundboardReq(_message.Message):
    __slots__ = ("soundboard_id",)
    SOUNDBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    soundboard_id: int
    def __init__(self, soundboard_id: _Optional[int] = ...) -> None: ...

class DeleteSoundboardRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
