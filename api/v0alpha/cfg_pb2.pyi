from annotations import authz_pb2 as _authz_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetConfigReq(_message.Message):
    __slots__ = ("region_id",)
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    region_id: str
    def __init__(self, region_id: _Optional[str] = ...) -> None: ...

class WebAgent(_message.Message):
    __slots__ = ("open_sips", "engine_priority", "log_level", "use_stun", "use_fast_stun", "use_fast_ice", "ice_timeout", "set_final_codec", "use_rport", "server", "base_url", "stun_server_address")
    class OpenSips(_message.Message):
        __slots__ = ("address",)
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        address: str
        def __init__(self, address: _Optional[str] = ...) -> None: ...
    class EnginePriority(_message.Message):
        __slots__ = ("java", "webrtc", "ns", "flash", "app", "p2p", "access_num", "native")
        JAVA_FIELD_NUMBER: _ClassVar[int]
        WEBRTC_FIELD_NUMBER: _ClassVar[int]
        NS_FIELD_NUMBER: _ClassVar[int]
        FLASH_FIELD_NUMBER: _ClassVar[int]
        APP_FIELD_NUMBER: _ClassVar[int]
        P2P_FIELD_NUMBER: _ClassVar[int]
        ACCESS_NUM_FIELD_NUMBER: _ClassVar[int]
        NATIVE_FIELD_NUMBER: _ClassVar[int]
        java: int
        webrtc: int
        ns: int
        flash: int
        app: int
        p2p: int
        access_num: int
        native: int
        def __init__(self, java: _Optional[int] = ..., webrtc: _Optional[int] = ..., ns: _Optional[int] = ..., flash: _Optional[int] = ..., app: _Optional[int] = ..., p2p: _Optional[int] = ..., access_num: _Optional[int] = ..., native: _Optional[int] = ...) -> None: ...
    class Server(_message.Message):
        __slots__ = ("sip", "webrtc")
        SIP_FIELD_NUMBER: _ClassVar[int]
        WEBRTC_FIELD_NUMBER: _ClassVar[int]
        sip: str
        webrtc: str
        def __init__(self, sip: _Optional[str] = ..., webrtc: _Optional[str] = ...) -> None: ...
    OPEN_SIPS_FIELD_NUMBER: _ClassVar[int]
    ENGINE_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    USE_STUN_FIELD_NUMBER: _ClassVar[int]
    USE_FAST_STUN_FIELD_NUMBER: _ClassVar[int]
    USE_FAST_ICE_FIELD_NUMBER: _ClassVar[int]
    ICE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SET_FINAL_CODEC_FIELD_NUMBER: _ClassVar[int]
    USE_RPORT_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    BASE_URL_FIELD_NUMBER: _ClassVar[int]
    STUN_SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    open_sips: WebAgent.OpenSips
    engine_priority: WebAgent.EnginePriority
    log_level: int
    use_stun: int
    use_fast_stun: int
    use_fast_ice: int
    ice_timeout: int
    set_final_codec: int
    use_rport: int
    server: WebAgent.Server
    base_url: str
    stun_server_address: str
    def __init__(self, open_sips: _Optional[_Union[WebAgent.OpenSips, _Mapping]] = ..., engine_priority: _Optional[_Union[WebAgent.EnginePriority, _Mapping]] = ..., log_level: _Optional[int] = ..., use_stun: _Optional[int] = ..., use_fast_stun: _Optional[int] = ..., use_fast_ice: _Optional[int] = ..., ice_timeout: _Optional[int] = ..., set_final_codec: _Optional[int] = ..., use_rport: _Optional[int] = ..., server: _Optional[_Union[WebAgent.Server, _Mapping]] = ..., base_url: _Optional[str] = ..., stun_server_address: _Optional[str] = ...) -> None: ...
