from annotations import authz_pb2 as _authz_pb2
from api.commons import delivery_pb2 as _delivery_pb2
from api.commons import org_pb2 as _org_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTransferConfigReq(_message.Message):
    __slots__ = ["entity", "mask"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: TransferConfig
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[TransferConfig, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateTransferConfigRes(_message.Message):
    __slots__ = ["entity"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: ID
    def __init__(self, entity: _Optional[_Union[ID, _Mapping]] = ...) -> None: ...

class ListTransferConfigsReq(_message.Message):
    __slots__ = ["entity", "mask", "list_req"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    LIST_REQ_FIELD_NUMBER: _ClassVar[int]
    entity: TransferConfig
    mask: _field_mask_pb2.FieldMask
    list_req: ListReq
    def __init__(self, entity: _Optional[_Union[TransferConfig, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., list_req: _Optional[_Union[ListReq, _Mapping]] = ...) -> None: ...

class ListTransferConfigsRes(_message.Message):
    __slots__ = ["entities"]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[TransferConfig]
    def __init__(self, entities: _Optional[_Iterable[_Union[TransferConfig, _Mapping]]] = ...) -> None: ...

class ListTransferConfigsByCredentialIDReq(_message.Message):
    __slots__ = ["entity", "mask", "credential_sid", "list_req"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_SID_FIELD_NUMBER: _ClassVar[int]
    LIST_REQ_FIELD_NUMBER: _ClassVar[int]
    entity: TransferConfig
    mask: _field_mask_pb2.FieldMask
    credential_sid: ID
    list_req: ListReq
    def __init__(self, entity: _Optional[_Union[TransferConfig, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., credential_sid: _Optional[_Union[ID, _Mapping]] = ..., list_req: _Optional[_Union[ListReq, _Mapping]] = ...) -> None: ...

class ListTransferConfigsByCredentialIDRes(_message.Message):
    __slots__ = ["entities"]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[TransferConfig]
    def __init__(self, entities: _Optional[_Iterable[_Union[TransferConfig, _Mapping]]] = ...) -> None: ...

class UpdateTransferConfigReq(_message.Message):
    __slots__ = ["entity", "mask"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: TransferConfig
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[TransferConfig, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateTransferConfigRes(_message.Message):
    __slots__ = ["entity"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: ID
    def __init__(self, entity: _Optional[_Union[ID, _Mapping]] = ...) -> None: ...

class DeleteTransferConfigReq(_message.Message):
    __slots__ = ["entity", "mask"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: TransferConfig
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[TransferConfig, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteTransferConfigRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetTransferConfigReq(_message.Message):
    __slots__ = ["entity", "mask"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: TransferConfig
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[TransferConfig, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetTransferConfigRes(_message.Message):
    __slots__ = ["entity"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: TransferConfig
    def __init__(self, entity: _Optional[_Union[TransferConfig, _Mapping]] = ...) -> None: ...

class GetTransferConfigByNameReq(_message.Message):
    __slots__ = ["name", "mask", "entity"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    mask: _field_mask_pb2.FieldMask
    entity: TransferConfig
    def __init__(self, name: _Optional[str] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., entity: _Optional[_Union[TransferConfig, _Mapping]] = ...) -> None: ...

class GetTransferConfigByNameRes(_message.Message):
    __slots__ = ["entity"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: TransferConfig
    def __init__(self, entity: _Optional[_Union[TransferConfig, _Mapping]] = ...) -> None: ...

class ListHistoryReq(_message.Message):
    __slots__ = ["entity", "mask", "list_req"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    LIST_REQ_FIELD_NUMBER: _ClassVar[int]
    entity: History
    mask: _field_mask_pb2.FieldMask
    list_req: ListReq
    def __init__(self, entity: _Optional[_Union[History, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., list_req: _Optional[_Union[ListReq, _Mapping]] = ...) -> None: ...

class ListHistoryRes(_message.Message):
    __slots__ = ["entities"]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[History]
    def __init__(self, entities: _Optional[_Iterable[_Union[History, _Mapping]]] = ...) -> None: ...

class ListHistoryByTransferConfigReq(_message.Message):
    __slots__ = ["entity", "mask"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: ListByIDReq
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[ListByIDReq, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListHistoryByTransferConfigRes(_message.Message):
    __slots__ = ["entities"]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[History]
    def __init__(self, entities: _Optional[_Iterable[_Union[History, _Mapping]]] = ...) -> None: ...

class CreateHistoryReq(_message.Message):
    __slots__ = ["entity", "mask"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: History
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[History, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateHistoryRes(_message.Message):
    __slots__ = ["entity"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: ID
    def __init__(self, entity: _Optional[_Union[ID, _Mapping]] = ...) -> None: ...

class GetHistoryReq(_message.Message):
    __slots__ = ["entity", "mask"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: ID
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[ID, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetHistoryRes(_message.Message):
    __slots__ = ["entity"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: History
    def __init__(self, entity: _Optional[_Union[History, _Mapping]] = ...) -> None: ...

class TransferConfig(_message.Message):
    __slots__ = ["sid", "name", "description", "ttl", "credential", "destination", "source", "created_on", "last_edited"]
    SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_FIELD_NUMBER: _ClassVar[int]
    sid: int
    name: str
    description: str
    ttl: int
    credential: Credential
    destination: Destination
    source: Source
    created_on: _timestamp_pb2.Timestamp
    last_edited: _timestamp_pb2.Timestamp
    def __init__(self, sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., ttl: _Optional[int] = ..., credential: _Optional[_Union[Credential, _Mapping]] = ..., destination: _Optional[_Union[Destination, _Mapping]] = ..., source: _Optional[_Union[Source, _Mapping]] = ..., created_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_edited: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ID(_message.Message):
    __slots__ = ["sid"]
    SID_FIELD_NUMBER: _ClassVar[int]
    sid: int
    def __init__(self, sid: _Optional[int] = ...) -> None: ...

class ListReq(_message.Message):
    __slots__ = ["before_sid", "limit"]
    BEFORE_SID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    before_sid: int
    limit: int
    def __init__(self, before_sid: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class History(_message.Message):
    __slots__ = ["sid", "transfer_config_name", "transfer_config_sid", "delivery_type", "error", "success", "created_on", "transfer_start", "transfer_complete", "origin", "org_id", "message_payload", "message_payload_len", "status", "is_inbound", "transaction_sid"]
    SID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_CONFIG_SID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_START_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_PAYLOAD_LEN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_INBOUND_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_SID_FIELD_NUMBER: _ClassVar[int]
    sid: int
    transfer_config_name: str
    transfer_config_sid: int
    delivery_type: str
    error: str
    success: bool
    created_on: _timestamp_pb2.Timestamp
    transfer_start: _timestamp_pb2.Timestamp
    transfer_complete: _timestamp_pb2.Timestamp
    origin: _org_pb2.OperatorApplications
    org_id: str
    message_payload: str
    message_payload_len: int
    status: _delivery_pb2.TransferStatus
    is_inbound: bool
    transaction_sid: int
    def __init__(self, sid: _Optional[int] = ..., transfer_config_name: _Optional[str] = ..., transfer_config_sid: _Optional[int] = ..., delivery_type: _Optional[str] = ..., error: _Optional[str] = ..., success: bool = ..., created_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., transfer_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., transfer_complete: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., origin: _Optional[_Union[_org_pb2.OperatorApplications, str]] = ..., org_id: _Optional[str] = ..., message_payload: _Optional[str] = ..., message_payload_len: _Optional[int] = ..., status: _Optional[_Union[_delivery_pb2.TransferStatus, str]] = ..., is_inbound: bool = ..., transaction_sid: _Optional[int] = ...) -> None: ...

class ListByIDReq(_message.Message):
    __slots__ = ["before_sid", "limit", "other_sid"]
    BEFORE_SID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OTHER_SID_FIELD_NUMBER: _ClassVar[int]
    before_sid: int
    limit: int
    other_sid: int
    def __init__(self, before_sid: _Optional[int] = ..., limit: _Optional[int] = ..., other_sid: _Optional[int] = ...) -> None: ...

class Credential(_message.Message):
    __slots__ = ["sid", "name", "description", "data", "created_on", "last_edited"]
    SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_FIELD_NUMBER: _ClassVar[int]
    sid: int
    name: str
    description: str
    data: CredentialData
    created_on: _timestamp_pb2.Timestamp
    last_edited: _timestamp_pb2.Timestamp
    def __init__(self, sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., data: _Optional[_Union[CredentialData, _Mapping]] = ..., created_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_edited: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Destination(_message.Message):
    __slots__ = ["encryption", "email", "room303", "sms", "sftp"]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROOM303_FIELD_NUMBER: _ClassVar[int]
    SMS_FIELD_NUMBER: _ClassVar[int]
    SFTP_FIELD_NUMBER: _ClassVar[int]
    encryption: _delivery_pb2.Encryption
    email: EmailDestination
    room303: Room303Destination
    sms: SmsDestination
    sftp: SftpDestination
    def __init__(self, encryption: _Optional[_Union[_delivery_pb2.Encryption, _Mapping]] = ..., email: _Optional[_Union[EmailDestination, _Mapping]] = ..., room303: _Optional[_Union[Room303Destination, _Mapping]] = ..., sms: _Optional[_Union[SmsDestination, _Mapping]] = ..., sftp: _Optional[_Union[SftpDestination, _Mapping]] = ...) -> None: ...

class SftpDestination(_message.Message):
    __slots__ = ["base_directory", "address", "port"]
    BASE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    base_directory: str
    address: str
    port: int
    def __init__(self, base_directory: _Optional[str] = ..., address: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class Room303Destination(_message.Message):
    __slots__ = ["room", "username", "user_id"]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    room: str
    username: str
    user_id: str
    def __init__(self, room: _Optional[str] = ..., username: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class SmsDestination(_message.Message):
    __slots__ = ["destination_phone", "source_phone"]
    DESTINATION_PHONE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PHONE_FIELD_NUMBER: _ClassVar[int]
    destination_phone: str
    source_phone: str
    def __init__(self, destination_phone: _Optional[str] = ..., source_phone: _Optional[str] = ...) -> None: ...

class EmailDestination(_message.Message):
    __slots__ = ["to_addr", "cc_addrs", "from_addr"]
    TO_ADDR_FIELD_NUMBER: _ClassVar[int]
    CC_ADDRS_FIELD_NUMBER: _ClassVar[int]
    FROM_ADDR_FIELD_NUMBER: _ClassVar[int]
    to_addr: str
    cc_addrs: _containers.RepeatedScalarFieldContainer[str]
    from_addr: str
    def __init__(self, to_addr: _Optional[str] = ..., cc_addrs: _Optional[_Iterable[str]] = ..., from_addr: _Optional[str] = ...) -> None: ...

class CredentialData(_message.Message):
    __slots__ = ["user_password", "password", "ssh_key_pair", "pgp_key_pair", "aes_password"]
    USER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SSH_KEY_PAIR_FIELD_NUMBER: _ClassVar[int]
    PGP_KEY_PAIR_FIELD_NUMBER: _ClassVar[int]
    AES_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    user_password: UserPassword
    password: Password
    ssh_key_pair: SSHKeyPair
    pgp_key_pair: PGPKeyPair
    aes_password: AESPassword
    def __init__(self, user_password: _Optional[_Union[UserPassword, _Mapping]] = ..., password: _Optional[_Union[Password, _Mapping]] = ..., ssh_key_pair: _Optional[_Union[SSHKeyPair, _Mapping]] = ..., pgp_key_pair: _Optional[_Union[PGPKeyPair, _Mapping]] = ..., aes_password: _Optional[_Union[AESPassword, _Mapping]] = ...) -> None: ...

class UserPassword(_message.Message):
    __slots__ = ["username", "password"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class Password(_message.Message):
    __slots__ = ["password"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    password: str
    def __init__(self, password: _Optional[str] = ...) -> None: ...

class SSHKeyPair(_message.Message):
    __slots__ = ["public_key", "private_key"]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: str
    private_key: str
    def __init__(self, public_key: _Optional[str] = ..., private_key: _Optional[str] = ...) -> None: ...

class PGPKeyPair(_message.Message):
    __slots__ = ["public_key", "private_key"]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: str
    private_key: str
    def __init__(self, public_key: _Optional[str] = ..., private_key: _Optional[str] = ...) -> None: ...

class AESPassword(_message.Message):
    __slots__ = ["password"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    password: str
    def __init__(self, password: _Optional[str] = ...) -> None: ...

class Source(_message.Message):
    __slots__ = ["encryption", "sftp"]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    SFTP_FIELD_NUMBER: _ClassVar[int]
    encryption: _delivery_pb2.Encryption
    sftp: SftpSource
    def __init__(self, encryption: _Optional[_Union[_delivery_pb2.Encryption, _Mapping]] = ..., sftp: _Optional[_Union[SftpSource, _Mapping]] = ...) -> None: ...

class SftpSource(_message.Message):
    __slots__ = ["directory"]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    directory: str
    def __init__(self, directory: _Optional[str] = ...) -> None: ...

class GetCredentialReq(_message.Message):
    __slots__ = ["entity", "mask"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: Credential
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[Credential, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetCredentialRes(_message.Message):
    __slots__ = ["credential"]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    credential: Credential
    def __init__(self, credential: _Optional[_Union[Credential, _Mapping]] = ...) -> None: ...

class ListCredentialsReq(_message.Message):
    __slots__ = ["entity", "mask"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: ListReq
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[ListReq, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListCredentialsRes(_message.Message):
    __slots__ = ["credentials"]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    credentials: Credentials
    def __init__(self, credentials: _Optional[_Union[Credentials, _Mapping]] = ...) -> None: ...

class CreateCredentialReq(_message.Message):
    __slots__ = ["entity", "mask"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: Credential
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[Credential, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateCredentialRes(_message.Message):
    __slots__ = ["entity"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: ID
    def __init__(self, entity: _Optional[_Union[ID, _Mapping]] = ...) -> None: ...

class DeleteCredentialReq(_message.Message):
    __slots__ = ["entity", "mask"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: ID
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[ID, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteCredentialRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateCredentialReq(_message.Message):
    __slots__ = ["entity", "mask"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: Credential
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[Credential, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCredentialRes(_message.Message):
    __slots__ = ["entity"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: ID
    def __init__(self, entity: _Optional[_Union[ID, _Mapping]] = ...) -> None: ...

class Credentials(_message.Message):
    __slots__ = ["entities"]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[Credential]
    def __init__(self, entities: _Optional[_Iterable[_Union[Credential, _Mapping]]] = ...) -> None: ...
