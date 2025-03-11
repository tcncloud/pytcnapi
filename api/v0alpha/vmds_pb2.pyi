from annotations import authz_pb2 as _authz_pb2
from api.commons import acd_pb2 as _acd_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetVoicemailMetadataReq(_message.Message):
    __slots__ = ("mail_boxes",)
    MAIL_BOXES_FIELD_NUMBER: _ClassVar[int]
    mail_boxes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mail_boxes: _Optional[_Iterable[str]] = ...) -> None: ...

class GetVoicemailMetadataRes(_message.Message):
    __slots__ = ("caller_id", "caller_sid", "caller_type", "dialed_number", "duration_seconds", "flag_read", "mail_box", "recording_filename", "recording_start")
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    CALLER_SID_FIELD_NUMBER: _ClassVar[int]
    CALLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    DIALED_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    FLAG_READ_FIELD_NUMBER: _ClassVar[int]
    MAIL_BOX_FIELD_NUMBER: _ClassVar[int]
    RECORDING_FILENAME_FIELD_NUMBER: _ClassVar[int]
    RECORDING_START_FIELD_NUMBER: _ClassVar[int]
    caller_id: str
    caller_sid: str
    caller_type: _acd_pb2.CallType.Enum
    dialed_number: str
    duration_seconds: int
    flag_read: bool
    mail_box: str
    recording_filename: str
    recording_start: int
    def __init__(self, caller_id: _Optional[str] = ..., caller_sid: _Optional[str] = ..., caller_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., dialed_number: _Optional[str] = ..., duration_seconds: _Optional[int] = ..., flag_read: bool = ..., mail_box: _Optional[str] = ..., recording_filename: _Optional[str] = ..., recording_start: _Optional[int] = ...) -> None: ...

class DeleteVoicemailReq(_message.Message):
    __slots__ = ("mail_box", "caller_sid", "caller_type")
    MAIL_BOX_FIELD_NUMBER: _ClassVar[int]
    CALLER_SID_FIELD_NUMBER: _ClassVar[int]
    CALLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    mail_box: str
    caller_sid: str
    caller_type: _acd_pb2.CallType.Enum
    def __init__(self, mail_box: _Optional[str] = ..., caller_sid: _Optional[str] = ..., caller_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class DeleteVoicemailRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteGreetingReq(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class DeleteGreetingRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateUploadNameReq(_message.Message):
    __slots__ = ("current_file_name", "new_file_name")
    CURRENT_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    current_file_name: str
    new_file_name: str
    def __init__(self, current_file_name: _Optional[str] = ..., new_file_name: _Optional[str] = ...) -> None: ...

class UpdateUploadNameRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetVoicemailCountReq(_message.Message):
    __slots__ = ("mail_boxes",)
    MAIL_BOXES_FIELD_NUMBER: _ClassVar[int]
    mail_boxes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mail_boxes: _Optional[_Iterable[str]] = ...) -> None: ...

class GetVoicemailCountRes(_message.Message):
    __slots__ = ("total", "unheard")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    UNHEARD_FIELD_NUMBER: _ClassVar[int]
    total: int
    unheard: int
    def __init__(self, total: _Optional[int] = ..., unheard: _Optional[int] = ...) -> None: ...

class UpdateVoicemailFlagReadReq(_message.Message):
    __slots__ = ("mail_box", "caller_sid", "caller_type", "flag_read")
    MAIL_BOX_FIELD_NUMBER: _ClassVar[int]
    CALLER_SID_FIELD_NUMBER: _ClassVar[int]
    CALLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    FLAG_READ_FIELD_NUMBER: _ClassVar[int]
    mail_box: str
    caller_sid: str
    caller_type: _acd_pb2.CallType.Enum
    flag_read: bool
    def __init__(self, mail_box: _Optional[str] = ..., caller_sid: _Optional[str] = ..., caller_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., flag_read: bool = ...) -> None: ...

class UpdateVoicemailFlagReadRes(_message.Message):
    __slots__ = ("flag_read",)
    FLAG_READ_FIELD_NUMBER: _ClassVar[int]
    flag_read: bool
    def __init__(self, flag_read: bool = ...) -> None: ...

class DownloadMessageReq(_message.Message):
    __slots__ = ("mail_box", "caller_sid", "caller_type")
    MAIL_BOX_FIELD_NUMBER: _ClassVar[int]
    CALLER_SID_FIELD_NUMBER: _ClassVar[int]
    CALLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    mail_box: str
    caller_sid: str
    caller_type: _acd_pb2.CallType.Enum
    def __init__(self, mail_box: _Optional[str] = ..., caller_sid: _Optional[str] = ..., caller_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class DownloadMessageRes(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class GetUploadGreetingUrlReq(_message.Message):
    __slots__ = ("pbx_extension", "filename")
    PBX_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    pbx_extension: str
    filename: str
    def __init__(self, pbx_extension: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...

class GetUploadGreetingUrlRes(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class DownloadMessagesReq(_message.Message):
    __slots__ = ("mail_boxes", "unheard_only")
    MAIL_BOXES_FIELD_NUMBER: _ClassVar[int]
    UNHEARD_ONLY_FIELD_NUMBER: _ClassVar[int]
    mail_boxes: _containers.RepeatedScalarFieldContainer[str]
    unheard_only: bool
    def __init__(self, mail_boxes: _Optional[_Iterable[str]] = ..., unheard_only: bool = ...) -> None: ...

class DownloadMessagesRes(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class DownloadGreetingForExtensionReq(_message.Message):
    __slots__ = ("mail_box",)
    MAIL_BOX_FIELD_NUMBER: _ClassVar[int]
    mail_box: str
    def __init__(self, mail_box: _Optional[str] = ...) -> None: ...

class DownloadGreetingForExtensionRes(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class DownloadGreetingReq(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class DownloadGreetingRes(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class ProcessGreetingUploadReq(_message.Message):
    __slots__ = ("pbx_extension", "filename")
    PBX_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    pbx_extension: str
    filename: str
    def __init__(self, pbx_extension: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...

class ProcessGreetingUploadRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateGreetingForExtensionReq(_message.Message):
    __slots__ = ("pbx_extension", "filename")
    PBX_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    pbx_extension: str
    filename: str
    def __init__(self, pbx_extension: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...

class UpdateGreetingForExtensionRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAvailableGreetingsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAvailableGreetingsRes(_message.Message):
    __slots__ = ("greetings",)
    class FileInfo(_message.Message):
        __slots__ = ("filename", "size")
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        filename: str
        size: int
        def __init__(self, filename: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...
    GREETINGS_FIELD_NUMBER: _ClassVar[int]
    greetings: _containers.RepeatedCompositeFieldContainer[ListAvailableGreetingsRes.FileInfo]
    def __init__(self, greetings: _Optional[_Iterable[_Union[ListAvailableGreetingsRes.FileInfo, _Mapping]]] = ...) -> None: ...
