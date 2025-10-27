from api.commons.auth import perms_pb2 as _perms_pb2
from api.commons.org import labels_pb2 as _labels_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PENDING: _ClassVar[Status]
    REJECTED: _ClassVar[Status]
    ACCEPTED: _ClassVar[Status]
PENDING: Status
REJECTED: Status
ACCEPTED: Status

class Trust(_message.Message):
    __slots__ = ()
    TRUST_ID_FIELD_NUMBER: _ClassVar[int]
    GRANTOR_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    trust_id: str
    grantor: str
    grantee: str
    name: str
    description: str
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    labels: _containers.RepeatedCompositeFieldContainer[_labels_pb2.Label]
    status: Status
    deleted: bool
    def __init__(self, trust_id: _Optional[str] = ..., grantor: _Optional[str] = ..., grantee: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ..., labels: _Optional[_Iterable[_Union[_labels_pb2.Label, _Mapping]]] = ..., status: _Optional[_Union[Status, str]] = ..., deleted: _Optional[bool] = ...) -> None: ...

class TrustGroup(_message.Message):
    __slots__ = ()
    class LabeledPermissions(_message.Message):
        __slots__ = ()
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
        labels: _containers.RepeatedCompositeFieldContainer[_labels_pb2.Label]
        def __init__(self, permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ..., labels: _Optional[_Iterable[_Union[_labels_pb2.Label, _Mapping]]] = ...) -> None: ...
    GRANTOR_FIELD_NUMBER: _ClassVar[int]
    LABELED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    grantor: str
    labeled_permissions: _containers.RepeatedCompositeFieldContainer[TrustGroup.LabeledPermissions]
    def __init__(self, grantor: _Optional[str] = ..., labeled_permissions: _Optional[_Iterable[_Union[TrustGroup.LabeledPermissions, _Mapping]]] = ...) -> None: ...

class TrustFilter(_message.Message):
    __slots__ = ()
    class StatusFilter(_message.Message):
        __slots__ = ()
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[Status]
        def __init__(self, values: _Optional[_Iterable[_Union[Status, str]]] = ...) -> None: ...
    GRANTOR_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FILTER_FIELD_NUMBER: _ClassVar[int]
    grantor: _wrappers_pb2.StringValue
    grantee: _wrappers_pb2.StringValue
    status_filter: TrustFilter.StatusFilter
    def __init__(self, grantor: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., grantee: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., status_filter: _Optional[_Union[TrustFilter.StatusFilter, _Mapping]] = ...) -> None: ...
