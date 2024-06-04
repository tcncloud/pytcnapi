from api.commons.auth import perms_pb2 as _perms_pb2
from api.commons.org import trusts_pb2 as _trusts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTrustRequest(_message.Message):
    __slots__ = ("grantee", "name", "description", "permissions", "label_ids")
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    LABEL_IDS_FIELD_NUMBER: _ClassVar[int]
    grantee: str
    name: str
    description: str
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    label_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, grantee: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ..., label_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateTrustResponse(_message.Message):
    __slots__ = ("trust_id",)
    TRUST_ID_FIELD_NUMBER: _ClassVar[int]
    trust_id: str
    def __init__(self, trust_id: _Optional[str] = ...) -> None: ...

class AcceptTrustRequest(_message.Message):
    __slots__ = ("trust_id",)
    TRUST_ID_FIELD_NUMBER: _ClassVar[int]
    trust_id: str
    def __init__(self, trust_id: _Optional[str] = ...) -> None: ...

class AcceptTrustResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RejectTrustRequest(_message.Message):
    __slots__ = ("trust_id",)
    TRUST_ID_FIELD_NUMBER: _ClassVar[int]
    trust_id: str
    def __init__(self, trust_id: _Optional[str] = ...) -> None: ...

class RejectTrustResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetTrustRequest(_message.Message):
    __slots__ = ("trust_id",)
    TRUST_ID_FIELD_NUMBER: _ClassVar[int]
    trust_id: str
    def __init__(self, trust_id: _Optional[str] = ...) -> None: ...

class GetTrustResponse(_message.Message):
    __slots__ = ("trust", "grantor_name", "grantee_name")
    TRUST_FIELD_NUMBER: _ClassVar[int]
    GRANTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_NAME_FIELD_NUMBER: _ClassVar[int]
    trust: _trusts_pb2.Trust
    grantor_name: str
    grantee_name: str
    def __init__(self, trust: _Optional[_Union[_trusts_pb2.Trust, _Mapping]] = ..., grantor_name: _Optional[str] = ..., grantee_name: _Optional[str] = ...) -> None: ...

class ListTrustsResponsePayload(_message.Message):
    __slots__ = ("trust", "grantor_name", "grantee_name")
    TRUST_FIELD_NUMBER: _ClassVar[int]
    GRANTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_NAME_FIELD_NUMBER: _ClassVar[int]
    trust: _trusts_pb2.Trust
    grantor_name: str
    grantee_name: str
    def __init__(self, trust: _Optional[_Union[_trusts_pb2.Trust, _Mapping]] = ..., grantor_name: _Optional[str] = ..., grantee_name: _Optional[str] = ...) -> None: ...

class ListIncomingTrustsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListIncomingTrustsResponse(_message.Message):
    __slots__ = ("trusts",)
    TRUSTS_FIELD_NUMBER: _ClassVar[int]
    trusts: _containers.RepeatedCompositeFieldContainer[ListTrustsResponsePayload]
    def __init__(self, trusts: _Optional[_Iterable[_Union[ListTrustsResponsePayload, _Mapping]]] = ...) -> None: ...

class ListGivenTrustsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListGivenTrustsResponse(_message.Message):
    __slots__ = ("trusts",)
    TRUSTS_FIELD_NUMBER: _ClassVar[int]
    trusts: _containers.RepeatedCompositeFieldContainer[ListTrustsResponsePayload]
    def __init__(self, trusts: _Optional[_Iterable[_Union[ListTrustsResponsePayload, _Mapping]]] = ...) -> None: ...

class ListAssignableTrustsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAssignableTrustsResponse(_message.Message):
    __slots__ = ("trusts",)
    TRUSTS_FIELD_NUMBER: _ClassVar[int]
    trusts: _containers.RepeatedCompositeFieldContainer[ListTrustsResponsePayload]
    def __init__(self, trusts: _Optional[_Iterable[_Union[ListTrustsResponsePayload, _Mapping]]] = ...) -> None: ...

class DeleteTrustRequest(_message.Message):
    __slots__ = ("trust_id",)
    TRUST_ID_FIELD_NUMBER: _ClassVar[int]
    trust_id: str
    def __init__(self, trust_id: _Optional[str] = ...) -> None: ...

class DeleteTrustResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignTrustRequest(_message.Message):
    __slots__ = ("trust_id", "user_ids")
    TRUST_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    trust_id: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, trust_id: _Optional[str] = ..., user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class AssignTrustResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnassignTrustRequest(_message.Message):
    __slots__ = ("trust_id", "user_id")
    TRUST_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    trust_id: str
    user_id: str
    def __init__(self, trust_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UnassignTrustResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
