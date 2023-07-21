from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Application(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    APPLICATION_UNSPECIFIED: _ClassVar[Application]
    APPLICATION_AGENT: _ClassVar[Application]
    APPLICATION_BUSINESS_INTELLIGENCE: _ClassVar[Application]
    APPLICATION_DELIVERY_SERVICE: _ClassVar[Application]
    APPLICATION_DEV_TOOLS: _ClassVar[Application]
    APPLICATION_INTEGRATIONS: _ClassVar[Application]
    APPLICATION_LIST_MANAGEMENT_SERVICES: _ClassVar[Application]
    APPLICATION_NATURAL_LANGUAGE_COMPLIANCE: _ClassVar[Application]
    APPLICATION_OMNI_BOSS: _ClassVar[Application]
    APPLICATION_ORGANIZATION: _ClassVar[Application]
    APPLICATION_ROOM_303: _ClassVar[Application]
    APPLICATION_SCORECARDS: _ClassVar[Application]
    APPLICATION_SCRIPTS: _ClassVar[Application]
    APPLICATION_TICKETS: _ClassVar[Application]
    APPLICATION_VOICE_ANALYTICS: _ClassVar[Application]
    APPLICATION_WORK_FORCE_MANAGEMENT: _ClassVar[Application]
    APPLICATION_WORKFLOWS: _ClassVar[Application]

class Card(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CARD_UNSPECIFIED: _ClassVar[Card]
    CARD_ORGANIZATION: _ClassVar[Card]
    CARD_USERS: _ClassVar[Card]
    CARD_AGENTS: _ClassVar[Card]
    CARD_PERMISSION_GROUPS: _ClassVar[Card]
    CARD_LABELS: _ClassVar[Card]
    CARD_TRUSTS: _ClassVar[Card]
    CARD_HUNT_GROUPS: _ClassVar[Card]
    CARD_SOUNDBOARD: _ClassVar[Card]
    CARD_SUBSCRIPTIONS: _ClassVar[Card]
APPLICATION_UNSPECIFIED: Application
APPLICATION_AGENT: Application
APPLICATION_BUSINESS_INTELLIGENCE: Application
APPLICATION_DELIVERY_SERVICE: Application
APPLICATION_DEV_TOOLS: Application
APPLICATION_INTEGRATIONS: Application
APPLICATION_LIST_MANAGEMENT_SERVICES: Application
APPLICATION_NATURAL_LANGUAGE_COMPLIANCE: Application
APPLICATION_OMNI_BOSS: Application
APPLICATION_ORGANIZATION: Application
APPLICATION_ROOM_303: Application
APPLICATION_SCORECARDS: Application
APPLICATION_SCRIPTS: Application
APPLICATION_TICKETS: Application
APPLICATION_VOICE_ANALYTICS: Application
APPLICATION_WORK_FORCE_MANAGEMENT: Application
APPLICATION_WORKFLOWS: Application
CARD_UNSPECIFIED: Card
CARD_ORGANIZATION: Card
CARD_USERS: Card
CARD_AGENTS: Card
CARD_PERMISSION_GROUPS: Card
CARD_LABELS: Card
CARD_TRUSTS: Card
CARD_HUNT_GROUPS: Card
CARD_SOUNDBOARD: Card
CARD_SUBSCRIPTIONS: Card
