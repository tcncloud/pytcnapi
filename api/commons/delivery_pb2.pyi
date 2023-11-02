from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TransferStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSFER_STATUS_WAITING: _ClassVar[TransferStatus]
    TRANSFER_STATUS_RUNNING: _ClassVar[TransferStatus]
    TRANSFER_STATUS_DONE_SUCCESS: _ClassVar[TransferStatus]
    TRANSFER_STATUS_DONE_PARTIAL_FAILURE: _ClassVar[TransferStatus]
    TRANSFER_STATUS_DONE_TOTAL_FAILURE: _ClassVar[TransferStatus]
TRANSFER_STATUS_WAITING: TransferStatus
TRANSFER_STATUS_RUNNING: TransferStatus
TRANSFER_STATUS_DONE_SUCCESS: TransferStatus
TRANSFER_STATUS_DONE_PARTIAL_FAILURE: TransferStatus
TRANSFER_STATUS_DONE_TOTAL_FAILURE: TransferStatus

class Encryption(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
