from annotations.perms import license_pb2 as _license_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
OPTIONS_FIELD_NUMBER: _ClassVar[int]
options: _descriptor.FieldDescriptor

class Tcn(_message.Message):
    __slots__ = ["wip", "app", "card", "features"]
    WIP_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    wip: bool
    app: _license_pb2.Application
    card: _license_pb2.Card
    features: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, wip: bool = ..., app: _Optional[_Union[_license_pb2.Application, str]] = ..., card: _Optional[_Union[_license_pb2.Card, str]] = ..., features: _Optional[_Iterable[str]] = ...) -> None: ...
