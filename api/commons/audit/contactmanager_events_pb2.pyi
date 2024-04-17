from api.v1alpha1.contactmanager import contactmanager_pb2 as _contactmanager_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ContactManagerEntryAddEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ContactManagerEntryGetEncEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ContactManagerDeleteEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ContactManagerKycEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
