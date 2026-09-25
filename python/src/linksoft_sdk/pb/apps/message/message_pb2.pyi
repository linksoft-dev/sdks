import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESSAGE_TYPE_UNSPECIFIED: _ClassVar[MessageType]
    MESSAGE_TYPE_CHAT: _ClassVar[MessageType]
    MESSAGE_TYPE_TICKET: _ClassVar[MessageType]
    MESSAGE_TYPE_ARTICLE: _ClassVar[MessageType]
    MESSAGE_TYPE_KNOWLEDGE_BASE: _ClassVar[MessageType]
    MESSAGE_TYPE_TRANSACTIONAL: _ClassVar[MessageType]
    MESSAGE_TYPE_NOTIFICATION: _ClassVar[MessageType]
    MESSAGE_TYPE_DEAL: _ClassVar[MessageType]
    MESSAGE_TYPE_CAMPAIGN: _ClassVar[MessageType]

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_UNSPECIFIED: _ClassVar[Status]
    STATUS_OPEN: _ClassVar[Status]
    STATUS_CLOSED: _ClassVar[Status]
    STATUS_PENDING: _ClassVar[Status]
    STATUS_RESOLVED: _ClassVar[Status]
    STATUS_DRAFT: _ClassVar[Status]
    STATUS_PUBLISHED: _ClassVar[Status]
    STATUS_ARCHIVED: _ClassVar[Status]
    STATUS_SENT: _ClassVar[Status]
    STATUS_DELIVERED: _ClassVar[Status]
    STATUS_READ: _ClassVar[Status]
    STATUS_CLICKED: _ClassVar[Status]
    STATUS_FAILED: _ClassVar[Status]

class TrackingEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACKING_EVENT_TYPE_UNSPECIFIED: _ClassVar[TrackingEventType]
    TRACKING_EVENT_TYPE_SENT: _ClassVar[TrackingEventType]
    TRACKING_EVENT_TYPE_DELIVERED: _ClassVar[TrackingEventType]
    TRACKING_EVENT_TYPE_OPENED: _ClassVar[TrackingEventType]
    TRACKING_EVENT_TYPE_READ: _ClassVar[TrackingEventType]
    TRACKING_EVENT_TYPE_CLICKED: _ClassVar[TrackingEventType]
    TRACKING_EVENT_TYPE_BOUNCED: _ClassVar[TrackingEventType]
    TRACKING_EVENT_TYPE_COMPLAINED: _ClassVar[TrackingEventType]
    TRACKING_EVENT_TYPE_FAILED: _ClassVar[TrackingEventType]

class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRIORITY_UNSPECIFIED: _ClassVar[Priority]
    PRIORITY_LOW: _ClassVar[Priority]
    PRIORITY_MEDIUM: _ClassVar[Priority]
    PRIORITY_HIGH: _ClassVar[Priority]
    PRIORITY_URGENT: _ClassVar[Priority]

class AccessLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCESS_LEVEL_UNSPECIFIED: _ClassVar[AccessLevel]
    ACCESS_LEVEL_NO_ACCESS: _ClassVar[AccessLevel]
    ACCESS_LEVEL_READ: _ClassVar[AccessLevel]
    ACCESS_LEVEL_WRITE: _ClassVar[AccessLevel]
    ACCESS_LEVEL_ADMIN: _ClassVar[AccessLevel]

class DealOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEAL_OUTCOME_UNSPECIFIED: _ClassVar[DealOutcome]
    DEAL_OUTCOME_OPEN: _ClassVar[DealOutcome]
    DEAL_OUTCOME_CONCLUDED: _ClassVar[DealOutcome]
    DEAL_OUTCOME_LOST: _ClassVar[DealOutcome]

class ChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHANGE_TYPE_UNSPECIFIED: _ClassVar[ChangeType]
    CHANGE_TYPE_FIELD_UPDATED: _ClassVar[ChangeType]
    CHANGE_TYPE_STATUS_CHANGED: _ClassVar[ChangeType]
    CHANGE_TYPE_PRIORITY_CHANGED: _ClassVar[ChangeType]
    CHANGE_TYPE_ASSIGNMENT_CHANGED: _ClassVar[ChangeType]
    CHANGE_TYPE_TAG_ADDED: _ClassVar[ChangeType]
    CHANGE_TYPE_TAG_REMOVED: _ClassVar[ChangeType]
    CHANGE_TYPE_PARTICIPANT_ADDED: _ClassVar[ChangeType]
    CHANGE_TYPE_PARTICIPANT_REMOVED: _ClassVar[ChangeType]

class Channel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHANNEL_UNSPECIFIED: _ClassVar[Channel]
    CHANNEL_WHATSAPP: _ClassVar[Channel]
    CHANNEL_TELEGRAM: _ClassVar[Channel]
    CHANNEL_WEB: _ClassVar[Channel]
    CHANNEL_EMAIL: _ClassVar[Channel]
    CHANNEL_PHONE: _ClassVar[Channel]
    CHANNEL_SMS: _ClassVar[Channel]
    CHANNEL_FACEBOOK: _ClassVar[Channel]
    CHANNEL_INSTAGRAM: _ClassVar[Channel]
    CHANNEL_X: _ClassVar[Channel]
    CHANNEL_SYSTEM: _ClassVar[Channel]
MESSAGE_TYPE_UNSPECIFIED: MessageType
MESSAGE_TYPE_CHAT: MessageType
MESSAGE_TYPE_TICKET: MessageType
MESSAGE_TYPE_ARTICLE: MessageType
MESSAGE_TYPE_KNOWLEDGE_BASE: MessageType
MESSAGE_TYPE_TRANSACTIONAL: MessageType
MESSAGE_TYPE_NOTIFICATION: MessageType
MESSAGE_TYPE_DEAL: MessageType
MESSAGE_TYPE_CAMPAIGN: MessageType
STATUS_UNSPECIFIED: Status
STATUS_OPEN: Status
STATUS_CLOSED: Status
STATUS_PENDING: Status
STATUS_RESOLVED: Status
STATUS_DRAFT: Status
STATUS_PUBLISHED: Status
STATUS_ARCHIVED: Status
STATUS_SENT: Status
STATUS_DELIVERED: Status
STATUS_READ: Status
STATUS_CLICKED: Status
STATUS_FAILED: Status
TRACKING_EVENT_TYPE_UNSPECIFIED: TrackingEventType
TRACKING_EVENT_TYPE_SENT: TrackingEventType
TRACKING_EVENT_TYPE_DELIVERED: TrackingEventType
TRACKING_EVENT_TYPE_OPENED: TrackingEventType
TRACKING_EVENT_TYPE_READ: TrackingEventType
TRACKING_EVENT_TYPE_CLICKED: TrackingEventType
TRACKING_EVENT_TYPE_BOUNCED: TrackingEventType
TRACKING_EVENT_TYPE_COMPLAINED: TrackingEventType
TRACKING_EVENT_TYPE_FAILED: TrackingEventType
PRIORITY_UNSPECIFIED: Priority
PRIORITY_LOW: Priority
PRIORITY_MEDIUM: Priority
PRIORITY_HIGH: Priority
PRIORITY_URGENT: Priority
ACCESS_LEVEL_UNSPECIFIED: AccessLevel
ACCESS_LEVEL_NO_ACCESS: AccessLevel
ACCESS_LEVEL_READ: AccessLevel
ACCESS_LEVEL_WRITE: AccessLevel
ACCESS_LEVEL_ADMIN: AccessLevel
DEAL_OUTCOME_UNSPECIFIED: DealOutcome
DEAL_OUTCOME_OPEN: DealOutcome
DEAL_OUTCOME_CONCLUDED: DealOutcome
DEAL_OUTCOME_LOST: DealOutcome
CHANGE_TYPE_UNSPECIFIED: ChangeType
CHANGE_TYPE_FIELD_UPDATED: ChangeType
CHANGE_TYPE_STATUS_CHANGED: ChangeType
CHANGE_TYPE_PRIORITY_CHANGED: ChangeType
CHANGE_TYPE_ASSIGNMENT_CHANGED: ChangeType
CHANGE_TYPE_TAG_ADDED: ChangeType
CHANGE_TYPE_TAG_REMOVED: ChangeType
CHANGE_TYPE_PARTICIPANT_ADDED: ChangeType
CHANGE_TYPE_PARTICIPANT_REMOVED: ChangeType
CHANNEL_UNSPECIFIED: Channel
CHANNEL_WHATSAPP: Channel
CHANNEL_TELEGRAM: Channel
CHANNEL_WEB: Channel
CHANNEL_EMAIL: Channel
CHANNEL_PHONE: Channel
CHANNEL_SMS: Channel
CHANNEL_FACEBOOK: Channel
CHANNEL_INSTAGRAM: Channel
CHANNEL_X: Channel
CHANNEL_SYSTEM: Channel

class TrackingEvent(_message.Message):
    __slots__ = ("type", "occurred_at", "source", "detail", "url", "recipient", "external_event_id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    type: TrackingEventType
    occurred_at: _timestamp_pb2.Timestamp
    source: str
    detail: str
    url: str
    recipient: str
    external_event_id: str
    def __init__(self, type: _Optional[_Union[TrackingEventType, str]] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., source: _Optional[str] = ..., detail: _Optional[str] = ..., url: _Optional[str] = ..., recipient: _Optional[str] = ..., external_event_id: _Optional[str] = ...) -> None: ...

class FieldChange(_message.Message):
    __slots__ = ("field_name", "old_value", "new_value")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    OLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    old_value: str
    new_value: str
    def __init__(self, field_name: _Optional[str] = ..., old_value: _Optional[str] = ..., new_value: _Optional[str] = ...) -> None: ...

class ChangeHistory(_message.Message):
    __slots__ = ("id", "message_id", "user_id", "change_type", "created_at", "description", "field_changes")
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FIELD_CHANGES_FIELD_NUMBER: _ClassVar[int]
    id: str
    message_id: str
    user_id: str
    change_type: ChangeType
    created_at: _timestamp_pb2.Timestamp
    description: str
    field_changes: _containers.RepeatedCompositeFieldContainer[FieldChange]
    def __init__(self, id: _Optional[str] = ..., message_id: _Optional[str] = ..., user_id: _Optional[str] = ..., change_type: _Optional[_Union[ChangeType, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., field_changes: _Optional[_Iterable[_Union[FieldChange, _Mapping]]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("id", "type", "title", "content", "creator_id", "creator_name", "participant_ids", "status", "priority", "tags", "channel", "integration_id", "interactions", "created_at", "updated_at", "resolved_at", "role_access", "ticket_data", "chat_data", "article_data", "knowledge_base_data", "deal_data", "change_history", "starred_by", "liked_by", "stars_count", "likes_count", "custom_fields", "integration_name", "external_message_id", "tracking_events")
    class RoleAccessEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AccessLevel
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AccessLevel, str]] = ...) -> None: ...
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    CREATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_IDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AT_FIELD_NUMBER: _ClassVar[int]
    ROLE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    TICKET_DATA_FIELD_NUMBER: _ClassVar[int]
    CHAT_DATA_FIELD_NUMBER: _ClassVar[int]
    ARTICLE_DATA_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_BASE_DATA_FIELD_NUMBER: _ClassVar[int]
    DEAL_DATA_FIELD_NUMBER: _ClassVar[int]
    CHANGE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    STARRED_BY_FIELD_NUMBER: _ClassVar[int]
    LIKED_BY_FIELD_NUMBER: _ClassVar[int]
    STARS_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIKES_COUNT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TRACKING_EVENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: MessageType
    title: str
    content: str
    creator_id: str
    creator_name: str
    participant_ids: _containers.RepeatedScalarFieldContainer[str]
    status: Status
    priority: Priority
    tags: _containers.RepeatedScalarFieldContainer[str]
    channel: Channel
    integration_id: str
    interactions: _containers.RepeatedCompositeFieldContainer[Interaction]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    resolved_at: _timestamp_pb2.Timestamp
    role_access: _containers.ScalarMap[str, AccessLevel]
    ticket_data: TicketData
    chat_data: ChatData
    article_data: ArticleData
    knowledge_base_data: KnowledgeBaseData
    deal_data: DealData
    change_history: _containers.RepeatedCompositeFieldContainer[ChangeHistory]
    starred_by: _containers.RepeatedScalarFieldContainer[str]
    liked_by: _containers.RepeatedScalarFieldContainer[str]
    stars_count: int
    likes_count: int
    custom_fields: _containers.ScalarMap[str, str]
    integration_name: str
    external_message_id: str
    tracking_events: _containers.RepeatedCompositeFieldContainer[TrackingEvent]
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[MessageType, str]] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., creator_id: _Optional[str] = ..., creator_name: _Optional[str] = ..., participant_ids: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[Status, str]] = ..., priority: _Optional[_Union[Priority, str]] = ..., tags: _Optional[_Iterable[str]] = ..., channel: _Optional[_Union[Channel, str]] = ..., integration_id: _Optional[str] = ..., interactions: _Optional[_Iterable[_Union[Interaction, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., resolved_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., role_access: _Optional[_Mapping[str, AccessLevel]] = ..., ticket_data: _Optional[_Union[TicketData, _Mapping]] = ..., chat_data: _Optional[_Union[ChatData, _Mapping]] = ..., article_data: _Optional[_Union[ArticleData, _Mapping]] = ..., knowledge_base_data: _Optional[_Union[KnowledgeBaseData, _Mapping]] = ..., deal_data: _Optional[_Union[DealData, _Mapping]] = ..., change_history: _Optional[_Iterable[_Union[ChangeHistory, _Mapping]]] = ..., starred_by: _Optional[_Iterable[str]] = ..., liked_by: _Optional[_Iterable[str]] = ..., stars_count: _Optional[int] = ..., likes_count: _Optional[int] = ..., custom_fields: _Optional[_Mapping[str, str]] = ..., integration_name: _Optional[str] = ..., external_message_id: _Optional[str] = ..., tracking_events: _Optional[_Iterable[_Union[TrackingEvent, _Mapping]]] = ...) -> None: ...

class Interaction(_message.Message):
    __slots__ = ("id", "message_id", "author_id", "content", "is_system", "attachments", "created_at", "updated_at", "channel", "role_access", "channel_metadata", "is_bot", "reply_to_interaction_id", "reply_preview", "deleted")
    class RoleAccessEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AccessLevel
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AccessLevel, str]] = ...) -> None: ...
    class ChannelMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    ROLE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    IS_BOT_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_INTERACTION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLY_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    id: str
    message_id: str
    author_id: str
    content: str
    is_system: bool
    attachments: _containers.RepeatedCompositeFieldContainer[Attachment]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    channel: Channel
    role_access: _containers.ScalarMap[str, AccessLevel]
    channel_metadata: _containers.ScalarMap[str, str]
    is_bot: bool
    reply_to_interaction_id: str
    reply_preview: ReplyPreview
    deleted: bool
    def __init__(self, id: _Optional[str] = ..., message_id: _Optional[str] = ..., author_id: _Optional[str] = ..., content: _Optional[str] = ..., is_system: _Optional[bool] = ..., attachments: _Optional[_Iterable[_Union[Attachment, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., channel: _Optional[_Union[Channel, str]] = ..., role_access: _Optional[_Mapping[str, AccessLevel]] = ..., channel_metadata: _Optional[_Mapping[str, str]] = ..., is_bot: _Optional[bool] = ..., reply_to_interaction_id: _Optional[str] = ..., reply_preview: _Optional[_Union[ReplyPreview, _Mapping]] = ..., deleted: _Optional[bool] = ...) -> None: ...

class ReplyPreview(_message.Message):
    __slots__ = ("interaction_id", "author_name", "content", "channel")
    INTERACTION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    interaction_id: str
    author_name: str
    content: str
    channel: Channel
    def __init__(self, interaction_id: _Optional[str] = ..., author_name: _Optional[str] = ..., content: _Optional[str] = ..., channel: _Optional[_Union[Channel, str]] = ...) -> None: ...

class Attachment(_message.Message):
    __slots__ = ("id", "name", "file_id", "data", "format", "size", "url")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    file_id: str
    data: bytes
    format: str
    size: int
    url: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., file_id: _Optional[str] = ..., data: _Optional[bytes] = ..., format: _Optional[str] = ..., size: _Optional[int] = ..., url: _Optional[str] = ...) -> None: ...

class TicketData(_message.Message):
    __slots__ = ("department", "category", "assigned_to", "cc", "bcc", "source")
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_TO_FIELD_NUMBER: _ClassVar[int]
    CC_FIELD_NUMBER: _ClassVar[int]
    BCC_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    department: str
    category: str
    assigned_to: str
    cc: _containers.RepeatedScalarFieldContainer[str]
    bcc: _containers.RepeatedScalarFieldContainer[str]
    source: str
    def __init__(self, department: _Optional[str] = ..., category: _Optional[str] = ..., assigned_to: _Optional[str] = ..., cc: _Optional[_Iterable[str]] = ..., bcc: _Optional[_Iterable[str]] = ..., source: _Optional[str] = ...) -> None: ...

class DealData(_message.Message):
    __slots__ = ("person_id", "person_name", "pipeline_id", "pipeline_name", "stage_id", "stage_name", "amount", "close_forecast", "responsible_id", "responsible_name", "outcome", "loss_reason_id", "loss_reason_name", "currency", "campaign_id", "campaign_name", "probability", "stage_entered_at", "sequence")
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    PERSON_NAME_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_NAME_FIELD_NUMBER: _ClassVar[int]
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FORECAST_FIELD_NUMBER: _ClassVar[int]
    RESPONSIBLE_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSIBLE_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    LOSS_REASON_ID_FIELD_NUMBER: _ClassVar[int]
    LOSS_REASON_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_NAME_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    STAGE_ENTERED_AT_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    person_id: str
    person_name: str
    pipeline_id: str
    pipeline_name: str
    stage_id: str
    stage_name: str
    amount: float
    close_forecast: _timestamp_pb2.Timestamp
    responsible_id: str
    responsible_name: str
    outcome: DealOutcome
    loss_reason_id: str
    loss_reason_name: str
    currency: str
    campaign_id: str
    campaign_name: str
    probability: float
    stage_entered_at: _timestamp_pb2.Timestamp
    sequence: int
    def __init__(self, person_id: _Optional[str] = ..., person_name: _Optional[str] = ..., pipeline_id: _Optional[str] = ..., pipeline_name: _Optional[str] = ..., stage_id: _Optional[str] = ..., stage_name: _Optional[str] = ..., amount: _Optional[float] = ..., close_forecast: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., responsible_id: _Optional[str] = ..., responsible_name: _Optional[str] = ..., outcome: _Optional[_Union[DealOutcome, str]] = ..., loss_reason_id: _Optional[str] = ..., loss_reason_name: _Optional[str] = ..., currency: _Optional[str] = ..., campaign_id: _Optional[str] = ..., campaign_name: _Optional[str] = ..., probability: _Optional[float] = ..., stage_entered_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sequence: _Optional[int] = ...) -> None: ...

class ChatData(_message.Message):
    __slots__ = ("is_group", "platform", "is_bot_enabled")
    IS_GROUP_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    IS_BOT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    is_group: bool
    platform: Channel
    is_bot_enabled: bool
    def __init__(self, is_group: _Optional[bool] = ..., platform: _Optional[_Union[Channel, str]] = ..., is_bot_enabled: _Optional[bool] = ...) -> None: ...

class ArticleData(_message.Message):
    __slots__ = ("author_name", "categories", "slug", "is_featured", "published_at")
    AUTHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    IS_FEATURED_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    author_name: str
    categories: _containers.RepeatedScalarFieldContainer[str]
    slug: str
    is_featured: bool
    published_at: _timestamp_pb2.Timestamp
    def __init__(self, author_name: _Optional[str] = ..., categories: _Optional[_Iterable[str]] = ..., slug: _Optional[str] = ..., is_featured: _Optional[bool] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class KnowledgeBaseData(_message.Message):
    __slots__ = ("category", "related_articles", "helpful_count", "not_helpful_count", "version")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    RELATED_ARTICLES_FIELD_NUMBER: _ClassVar[int]
    HELPFUL_COUNT_FIELD_NUMBER: _ClassVar[int]
    NOT_HELPFUL_COUNT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    category: str
    related_articles: _containers.RepeatedScalarFieldContainer[str]
    helpful_count: int
    not_helpful_count: int
    version: str
    def __init__(self, category: _Optional[str] = ..., related_articles: _Optional[_Iterable[str]] = ..., helpful_count: _Optional[int] = ..., not_helpful_count: _Optional[int] = ..., version: _Optional[str] = ...) -> None: ...
