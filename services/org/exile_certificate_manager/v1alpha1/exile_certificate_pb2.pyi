from google.protobuf import field_mask_pb2 as _field_mask_pb2
from services.org.exile_certificate_manager.v1alpha1 import entities_pb2 as _entities_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateExileCertificateRequest(_message.Message):
    __slots__ = ("name", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CreateExileCertificateResponse(_message.Message):
    __slots__ = ("encoded_exile_certificate", "exile_certificate")
    ENCODED_EXILE_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    EXILE_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    encoded_exile_certificate: str
    exile_certificate: _entities_pb2.ExileCertificate
    def __init__(self, encoded_exile_certificate: _Optional[str] = ..., exile_certificate: _Optional[_Union[_entities_pb2.ExileCertificate, _Mapping]] = ...) -> None: ...

class RevokeExileCertificateRequest(_message.Message):
    __slots__ = ("exile_certificate_id",)
    EXILE_CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    exile_certificate_id: str
    def __init__(self, exile_certificate_id: _Optional[str] = ...) -> None: ...

class RevokeExileCertificateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignExileConfigurationRequest(_message.Message):
    __slots__ = ("exile_certificate_id", "exile_configuration_id")
    EXILE_CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    EXILE_CONFIGURATION_ID_FIELD_NUMBER: _ClassVar[int]
    exile_certificate_id: str
    exile_configuration_id: str
    def __init__(self, exile_certificate_id: _Optional[str] = ..., exile_configuration_id: _Optional[str] = ...) -> None: ...

class AssignExileConfigurationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnassignExileConfigurationRequest(_message.Message):
    __slots__ = ("exile_certificate_id",)
    EXILE_CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    exile_certificate_id: str
    def __init__(self, exile_certificate_id: _Optional[str] = ...) -> None: ...

class UnassignExileConfigurationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListExileCertificatesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListExileCertificatesResponse(_message.Message):
    __slots__ = ("exile_certificates",)
    EXILE_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    exile_certificates: _containers.RepeatedCompositeFieldContainer[_entities_pb2.ExileCertificate]
    def __init__(self, exile_certificates: _Optional[_Iterable[_Union[_entities_pb2.ExileCertificate, _Mapping]]] = ...) -> None: ...
