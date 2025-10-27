import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExileConfigurationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXILE_CONFIGURATION_TYPE_UNSPECIFIED: _ClassVar[ExileConfigurationType]
    EXILE_CONFIGURATION_TYPE_NONE: _ClassVar[ExileConfigurationType]
    EXILE_CONFIGURATION_TYPE_ARTIVA_HCX: _ClassVar[ExileConfigurationType]
    EXILE_CONFIGURATION_TYPE_ARTIVA_RM: _ClassVar[ExileConfigurationType]
    EXILE_CONFIGURATION_TYPE_FACS: _ClassVar[ExileConfigurationType]
    EXILE_CONFIGURATION_TYPE_VELOSIDY: _ClassVar[ExileConfigurationType]
    EXILE_CONFIGURATION_TYPE_LATITUDE_CLASSIC: _ClassVar[ExileConfigurationType]
    EXILE_CONFIGURATION_TYPE_LATITUDE_LIQUID: _ClassVar[ExileConfigurationType]
EXILE_CONFIGURATION_TYPE_UNSPECIFIED: ExileConfigurationType
EXILE_CONFIGURATION_TYPE_NONE: ExileConfigurationType
EXILE_CONFIGURATION_TYPE_ARTIVA_HCX: ExileConfigurationType
EXILE_CONFIGURATION_TYPE_ARTIVA_RM: ExileConfigurationType
EXILE_CONFIGURATION_TYPE_FACS: ExileConfigurationType
EXILE_CONFIGURATION_TYPE_VELOSIDY: ExileConfigurationType
EXILE_CONFIGURATION_TYPE_LATITUDE_CLASSIC: ExileConfigurationType
EXILE_CONFIGURATION_TYPE_LATITUDE_LIQUID: ExileConfigurationType

class ExileCertificate(_message.Message):
    __slots__ = ()
    EXILE_CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BY_FIELD_NUMBER: _ClassVar[int]
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    EXILE_CONFIGURATION_ID_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    exile_certificate_id: str
    org_id: str
    name: str
    description: str
    hash: str
    expiration_date: _timestamp_pb2.Timestamp
    creation_date: _timestamp_pb2.Timestamp
    request_by: str
    revoked: bool
    exile_configuration_id: str
    renewal_instance: int
    def __init__(self, exile_certificate_id: _Optional[str] = ..., org_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., hash: _Optional[str] = ..., expiration_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., creation_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., request_by: _Optional[str] = ..., revoked: _Optional[bool] = ..., exile_configuration_id: _Optional[str] = ..., renewal_instance: _Optional[int] = ...) -> None: ...

class ExileConfiguration(_message.Message):
    __slots__ = ()
    EXILE_CONFIGURATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    exile_configuration_id: str
    org_id: str
    name: str
    description: str
    type: ExileConfigurationType
    parameters: str
    def __init__(self, exile_configuration_id: _Optional[str] = ..., org_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[ExileConfigurationType, str]] = ..., parameters: _Optional[str] = ...) -> None: ...
