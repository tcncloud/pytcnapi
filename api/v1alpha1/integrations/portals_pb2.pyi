from annotations import authz_pb2 as _authz_pb2
from api.commons.integrations import integrations_pb2 as _integrations_pb2
from api.commons import perms_pb2 as _perms_pb2
from api.v1alpha1.integrations import service_pb2 as _service_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpsertPortalConfigReq(_message.Message):
    __slots__ = ("entity", "mask")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalConfig
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalConfig, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpsertPortalConfigRes(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalConfigId
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalConfigId, _Mapping]] = ...) -> None: ...

class GetPortalConfigRes(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalConfig
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalConfig, _Mapping]] = ...) -> None: ...

class DeletePortalConfigRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPortalConfigsRes(_message.Message):
    __slots__ = ("entities", "next_page_token")
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[_service_pb2.PortalConfig]
    next_page_token: str
    def __init__(self, entities: _Optional[_Iterable[_Union[_service_pb2.PortalConfig, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdatePortalConfigLogoReq(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalConfig
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalConfig, _Mapping]] = ...) -> None: ...

class UpdatePortalConfigLogoRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPortalConfigLogoReq(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalConfigId
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalConfigId, _Mapping]] = ...) -> None: ...

class GetPortalConfigLogoRes(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: bytes
    def __init__(self, entity: _Optional[bytes] = ...) -> None: ...

class UpsertPortalReq(_message.Message):
    __slots__ = ("entity", "mask")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.Portal
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[_service_pb2.Portal, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpsertPortalRes(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalId
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalId, _Mapping]] = ...) -> None: ...

class GetPortalReq(_message.Message):
    __slots__ = ("entity", "mask")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalId
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalId, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetPortalRes(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.Portal
    def __init__(self, entity: _Optional[_Union[_service_pb2.Portal, _Mapping]] = ...) -> None: ...

class DeletePortalReq(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalId
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalId, _Mapping]] = ...) -> None: ...

class DeletePortalRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPortalsReq(_message.Message):
    __slots__ = ("entity", "mask", "page_size", "page", "ptypes")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PTYPES_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalId
    mask: _field_mask_pb2.FieldMask
    page_size: int
    page: int
    ptypes: _containers.RepeatedCompositeFieldContainer[_service_pb2.PortalType]
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalId, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., page_size: _Optional[int] = ..., page: _Optional[int] = ..., ptypes: _Optional[_Iterable[_Union[_service_pb2.PortalType, _Mapping]]] = ...) -> None: ...

class ListPortalsRes(_message.Message):
    __slots__ = ("entities",)
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[_service_pb2.Portal]
    def __init__(self, entities: _Optional[_Iterable[_Union[_service_pb2.Portal, _Mapping]]] = ...) -> None: ...

class ListDetailedPortalsReq(_message.Message):
    __slots__ = ("entity", "portal_mask", "portal_config_mask", "plugin_instance_mask", "page_size", "page", "ptypes")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    PORTAL_MASK_FIELD_NUMBER: _ClassVar[int]
    PORTAL_CONFIG_MASK_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_INSTANCE_MASK_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PTYPES_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalId
    portal_mask: _field_mask_pb2.FieldMask
    portal_config_mask: _field_mask_pb2.FieldMask
    plugin_instance_mask: _field_mask_pb2.FieldMask
    page_size: int
    page: int
    ptypes: _containers.RepeatedCompositeFieldContainer[_service_pb2.PortalType]
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalId, _Mapping]] = ..., portal_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., portal_config_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., plugin_instance_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., page_size: _Optional[int] = ..., page: _Optional[int] = ..., ptypes: _Optional[_Iterable[_Union[_service_pb2.PortalType, _Mapping]]] = ...) -> None: ...

class ListDetailedPortalsRes(_message.Message):
    __slots__ = ("entities",)
    class Entity(_message.Message):
        __slots__ = ("portal", "portal_config", "plugin_instances")
        PORTAL_FIELD_NUMBER: _ClassVar[int]
        PORTAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
        PLUGIN_INSTANCES_FIELD_NUMBER: _ClassVar[int]
        portal: _service_pb2.Portal
        portal_config: _service_pb2.PortalConfig
        plugin_instances: _containers.RepeatedCompositeFieldContainer[_service_pb2.PluginInstance]
        def __init__(self, portal: _Optional[_Union[_service_pb2.Portal, _Mapping]] = ..., portal_config: _Optional[_Union[_service_pb2.PortalConfig, _Mapping]] = ..., plugin_instances: _Optional[_Iterable[_Union[_service_pb2.PluginInstance, _Mapping]]] = ...) -> None: ...
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[ListDetailedPortalsRes.Entity]
    def __init__(self, entities: _Optional[_Iterable[_Union[ListDetailedPortalsRes.Entity, _Mapping]]] = ...) -> None: ...

class GetDetailedPortalReq(_message.Message):
    __slots__ = ("entity", "portal_mask", "portal_config_mask", "plugin_instance_mask")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    PORTAL_MASK_FIELD_NUMBER: _ClassVar[int]
    PORTAL_CONFIG_MASK_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_INSTANCE_MASK_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalId
    portal_mask: _field_mask_pb2.FieldMask
    portal_config_mask: _field_mask_pb2.FieldMask
    plugin_instance_mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalId, _Mapping]] = ..., portal_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., portal_config_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., plugin_instance_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetDetailedPortalRes(_message.Message):
    __slots__ = ("entity",)
    class Entity(_message.Message):
        __slots__ = ("portal", "portal_config", "plugin_instances")
        PORTAL_FIELD_NUMBER: _ClassVar[int]
        PORTAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
        PLUGIN_INSTANCES_FIELD_NUMBER: _ClassVar[int]
        portal: _service_pb2.Portal
        portal_config: _service_pb2.PortalConfig
        plugin_instances: _containers.RepeatedCompositeFieldContainer[_service_pb2.PluginInstance]
        def __init__(self, portal: _Optional[_Union[_service_pb2.Portal, _Mapping]] = ..., portal_config: _Optional[_Union[_service_pb2.PortalConfig, _Mapping]] = ..., plugin_instances: _Optional[_Iterable[_Union[_service_pb2.PluginInstance, _Mapping]]] = ...) -> None: ...
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: GetDetailedPortalRes.Entity
    def __init__(self, entity: _Optional[_Union[GetDetailedPortalRes.Entity, _Mapping]] = ...) -> None: ...

class UpsertPluginInstanceReq(_message.Message):
    __slots__ = ("entity", "mask")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PluginInstance
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[_service_pb2.PluginInstance, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpsertPluginInstanceRes(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PluginInstanceId
    def __init__(self, entity: _Optional[_Union[_service_pb2.PluginInstanceId, _Mapping]] = ...) -> None: ...

class GetPluginInstanceReq(_message.Message):
    __slots__ = ("entity", "mask")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PluginInstanceId
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[_service_pb2.PluginInstanceId, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetPluginInstanceRes(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PluginInstance
    def __init__(self, entity: _Optional[_Union[_service_pb2.PluginInstance, _Mapping]] = ...) -> None: ...

class DeletePluginInstanceReq(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PluginInstanceId
    def __init__(self, entity: _Optional[_Union[_service_pb2.PluginInstanceId, _Mapping]] = ...) -> None: ...

class DeletePluginInstanceRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPluginInstanceReq(_message.Message):
    __slots__ = ("entity", "mask", "page_size", "page")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PluginInstance
    mask: _field_mask_pb2.FieldMask
    page_size: int
    page: int
    def __init__(self, entity: _Optional[_Union[_service_pb2.PluginInstance, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., page_size: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class ListPluginInstanceRes(_message.Message):
    __slots__ = ("entities",)
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[_service_pb2.PluginInstance]
    def __init__(self, entities: _Optional[_Iterable[_Union[_service_pb2.PluginInstance, _Mapping]]] = ...) -> None: ...

class ListPluginsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPluginsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPortalLinksReq(_message.Message):
    __slots__ = ("entity", "mask", "page_size", "page")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalLinkId
    mask: _field_mask_pb2.FieldMask
    page_size: int
    page: int
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalLinkId, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., page_size: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class ListPortalLinksRes(_message.Message):
    __slots__ = ("entities",)
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[_service_pb2.PortalLink]
    def __init__(self, entities: _Optional[_Iterable[_Union[_service_pb2.PortalLink, _Mapping]]] = ...) -> None: ...

class GetPortalLinkReq(_message.Message):
    __slots__ = ("entity", "mask")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalLinkId
    mask: _field_mask_pb2.FieldMask
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalLinkId, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetPortalLinkRes(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalLink
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalLink, _Mapping]] = ...) -> None: ...

class DeletePortalLinkReq(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalLinkId
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalLinkId, _Mapping]] = ...) -> None: ...

class DeletePortalLinkRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreatePortalLinksReq(_message.Message):
    __slots__ = ("entity", "link_datas")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    LINK_DATAS_FIELD_NUMBER: _ClassVar[int]
    entity: _service_pb2.PortalId
    link_datas: _containers.RepeatedCompositeFieldContainer[_service_pb2.Task]
    def __init__(self, entity: _Optional[_Union[_service_pb2.PortalId, _Mapping]] = ..., link_datas: _Optional[_Iterable[_Union[_service_pb2.Task, _Mapping]]] = ...) -> None: ...

class CreatePortalLinksRes(_message.Message):
    __slots__ = ("urls",)
    URLS_FIELD_NUMBER: _ClassVar[int]
    urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, urls: _Optional[_Iterable[str]] = ...) -> None: ...

class ListFlowFieldNamesReq(_message.Message):
    __slots__ = ("entity",)
    class Entity(_message.Message):
        __slots__ = ("flow", "loc")
        FLOW_FIELD_NUMBER: _ClassVar[int]
        LOC_FIELD_NUMBER: _ClassVar[int]
        flow: _integrations_pb2.Flow
        loc: _integrations_pb2.FlowFieldLoc
        def __init__(self, flow: _Optional[_Union[_integrations_pb2.Flow, _Mapping]] = ..., loc: _Optional[_Union[_integrations_pb2.FlowFieldLoc, str]] = ...) -> None: ...
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: ListFlowFieldNamesReq.Entity
    def __init__(self, entity: _Optional[_Union[ListFlowFieldNamesReq.Entity, _Mapping]] = ...) -> None: ...

class ListFlowFieldNamesRes(_message.Message):
    __slots__ = ("field_names",)
    FIELD_NAMES_FIELD_NUMBER: _ClassVar[int]
    field_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, field_names: _Optional[_Iterable[str]] = ...) -> None: ...

class ListAvailableVerificationFieldsReq(_message.Message):
    __slots__ = ("verification",)
    VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    verification: _integrations_pb2.VerificationFlow
    def __init__(self, verification: _Optional[_Union[_integrations_pb2.VerificationFlow, _Mapping]] = ...) -> None: ...

class ListAvailableVerificationFieldsRes(_message.Message):
    __slots__ = ("verification_fields",)
    VERIFICATION_FIELDS_FIELD_NUMBER: _ClassVar[int]
    verification_fields: _containers.RepeatedCompositeFieldContainer[_integrations_pb2.FieldDefinition]
    def __init__(self, verification_fields: _Optional[_Iterable[_Union[_integrations_pb2.FieldDefinition, _Mapping]]] = ...) -> None: ...

class ListAvailablePaymentFieldsReq(_message.Message):
    __slots__ = ("payment",)
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    payment: _integrations_pb2.PaymentFlow
    def __init__(self, payment: _Optional[_Union[_integrations_pb2.PaymentFlow, _Mapping]] = ...) -> None: ...

class ListAvailablePaymentFieldsRes(_message.Message):
    __slots__ = ("payment_fields",)
    PAYMENT_FIELDS_FIELD_NUMBER: _ClassVar[int]
    payment_fields: _containers.RepeatedCompositeFieldContainer[_integrations_pb2.FieldDefinition]
    def __init__(self, payment_fields: _Optional[_Iterable[_Union[_integrations_pb2.FieldDefinition, _Mapping]]] = ...) -> None: ...
