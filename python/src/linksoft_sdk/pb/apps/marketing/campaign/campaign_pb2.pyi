import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CampaignStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CAMPAIGN_STATUS_UNSPECIFIED: _ClassVar[CampaignStatus]
    CAMPAIGN_STATUS_DRAFT: _ClassVar[CampaignStatus]
    CAMPAIGN_STATUS_SCHEDULED: _ClassVar[CampaignStatus]
    CAMPAIGN_STATUS_SENDING: _ClassVar[CampaignStatus]
    CAMPAIGN_STATUS_PAUSED: _ClassVar[CampaignStatus]
    CAMPAIGN_STATUS_COMPLETED: _ClassVar[CampaignStatus]
    CAMPAIGN_STATUS_FAILED: _ClassVar[CampaignStatus]

class CampaignSendStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CAMPAIGN_SEND_STATUS_UNSPECIFIED: _ClassVar[CampaignSendStatus]
    CAMPAIGN_SEND_STATUS_PENDING: _ClassVar[CampaignSendStatus]
    CAMPAIGN_SEND_STATUS_SENT: _ClassVar[CampaignSendStatus]
    CAMPAIGN_SEND_STATUS_DELIVERED: _ClassVar[CampaignSendStatus]
    CAMPAIGN_SEND_STATUS_OPENED: _ClassVar[CampaignSendStatus]
    CAMPAIGN_SEND_STATUS_CLICKED: _ClassVar[CampaignSendStatus]
    CAMPAIGN_SEND_STATUS_BOUNCED: _ClassVar[CampaignSendStatus]
    CAMPAIGN_SEND_STATUS_FAILED: _ClassVar[CampaignSendStatus]
    CAMPAIGN_SEND_STATUS_UNSUBSCRIBED: _ClassVar[CampaignSendStatus]
CAMPAIGN_STATUS_UNSPECIFIED: CampaignStatus
CAMPAIGN_STATUS_DRAFT: CampaignStatus
CAMPAIGN_STATUS_SCHEDULED: CampaignStatus
CAMPAIGN_STATUS_SENDING: CampaignStatus
CAMPAIGN_STATUS_PAUSED: CampaignStatus
CAMPAIGN_STATUS_COMPLETED: CampaignStatus
CAMPAIGN_STATUS_FAILED: CampaignStatus
CAMPAIGN_SEND_STATUS_UNSPECIFIED: CampaignSendStatus
CAMPAIGN_SEND_STATUS_PENDING: CampaignSendStatus
CAMPAIGN_SEND_STATUS_SENT: CampaignSendStatus
CAMPAIGN_SEND_STATUS_DELIVERED: CampaignSendStatus
CAMPAIGN_SEND_STATUS_OPENED: CampaignSendStatus
CAMPAIGN_SEND_STATUS_CLICKED: CampaignSendStatus
CAMPAIGN_SEND_STATUS_BOUNCED: CampaignSendStatus
CAMPAIGN_SEND_STATUS_FAILED: CampaignSendStatus
CAMPAIGN_SEND_STATUS_UNSUBSCRIBED: CampaignSendStatus

class Campaign(_message.Message):
    __slots__ = ("id", "name", "segment_id", "channel", "scheduled_at", "created_at", "updated_at", "creative_id", "integration_id", "status", "subject", "sender_name", "sender_email", "total_recipients", "total_sent", "total_delivered", "total_bounced", "total_opened", "total_clicked", "total_failed", "sent_at", "completed_at", "sent_by", "error_message", "creative_name", "segment_name", "automation_id", "integration_name", "sent_by_name", "dispatch_mode", "stats_collection_completed", "stats_last_sync_at", "dispatch_execution_id", "dispatch_monitor_url", "dispatch_started_at", "dispatch_finished_at", "dispatch_progress_total", "dispatch_progress_processed", "dispatch_progress_sent", "dispatch_progress_failed", "dispatch_last_error", "cost", "number", "track_opens", "total_unsubscribed", "avg_time_to_first_open_seconds", "total_click_events", "clicked_links", "unsubscribe_reasons", "total_complained", "folder_id", "folder_name", "total_open_events", "settings")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATIVE_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SENDER_NAME_FIELD_NUMBER: _ClassVar[int]
    SENDER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SENT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DELIVERED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BOUNCED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_OPENED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CLICKED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FAILED_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    SENT_BY_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CREATIVE_NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    SENT_BY_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    STATS_COLLECTION_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    STATS_LAST_SYNC_AT_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_MONITOR_URL_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_PROGRESS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_PROGRESS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_PROGRESS_SENT_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_PROGRESS_FAILED_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    TRACK_OPENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UNSUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    AVG_TIME_TO_FIRST_OPEN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CLICK_EVENTS_FIELD_NUMBER: _ClassVar[int]
    CLICKED_LINKS_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBE_REASONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COMPLAINED_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_OPEN_EVENTS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    segment_id: str
    channel: str
    scheduled_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    creative_id: str
    integration_id: str
    status: CampaignStatus
    subject: str
    sender_name: str
    sender_email: str
    total_recipients: int
    total_sent: int
    total_delivered: int
    total_bounced: int
    total_opened: int
    total_clicked: int
    total_failed: int
    sent_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    sent_by: str
    error_message: str
    creative_name: str
    segment_name: str
    automation_id: str
    integration_name: str
    sent_by_name: str
    dispatch_mode: str
    stats_collection_completed: bool
    stats_last_sync_at: _timestamp_pb2.Timestamp
    dispatch_execution_id: str
    dispatch_monitor_url: str
    dispatch_started_at: _timestamp_pb2.Timestamp
    dispatch_finished_at: _timestamp_pb2.Timestamp
    dispatch_progress_total: int
    dispatch_progress_processed: int
    dispatch_progress_sent: int
    dispatch_progress_failed: int
    dispatch_last_error: str
    cost: float
    number: int
    track_opens: bool
    total_unsubscribed: int
    avg_time_to_first_open_seconds: int
    total_click_events: int
    clicked_links: _containers.RepeatedCompositeFieldContainer[ClickedLink]
    unsubscribe_reasons: _containers.RepeatedCompositeFieldContainer[UnsubscribeReasonCount]
    total_complained: int
    folder_id: str
    folder_name: str
    total_open_events: int
    settings: CampaignSettings
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., segment_id: _Optional[str] = ..., channel: _Optional[str] = ..., scheduled_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., creative_id: _Optional[str] = ..., integration_id: _Optional[str] = ..., status: _Optional[_Union[CampaignStatus, str]] = ..., subject: _Optional[str] = ..., sender_name: _Optional[str] = ..., sender_email: _Optional[str] = ..., total_recipients: _Optional[int] = ..., total_sent: _Optional[int] = ..., total_delivered: _Optional[int] = ..., total_bounced: _Optional[int] = ..., total_opened: _Optional[int] = ..., total_clicked: _Optional[int] = ..., total_failed: _Optional[int] = ..., sent_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sent_by: _Optional[str] = ..., error_message: _Optional[str] = ..., creative_name: _Optional[str] = ..., segment_name: _Optional[str] = ..., automation_id: _Optional[str] = ..., integration_name: _Optional[str] = ..., sent_by_name: _Optional[str] = ..., dispatch_mode: _Optional[str] = ..., stats_collection_completed: _Optional[bool] = ..., stats_last_sync_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dispatch_execution_id: _Optional[str] = ..., dispatch_monitor_url: _Optional[str] = ..., dispatch_started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dispatch_finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dispatch_progress_total: _Optional[int] = ..., dispatch_progress_processed: _Optional[int] = ..., dispatch_progress_sent: _Optional[int] = ..., dispatch_progress_failed: _Optional[int] = ..., dispatch_last_error: _Optional[str] = ..., cost: _Optional[float] = ..., number: _Optional[int] = ..., track_opens: _Optional[bool] = ..., total_unsubscribed: _Optional[int] = ..., avg_time_to_first_open_seconds: _Optional[int] = ..., total_click_events: _Optional[int] = ..., clicked_links: _Optional[_Iterable[_Union[ClickedLink, _Mapping]]] = ..., unsubscribe_reasons: _Optional[_Iterable[_Union[UnsubscribeReasonCount, _Mapping]]] = ..., total_complained: _Optional[int] = ..., folder_id: _Optional[str] = ..., folder_name: _Optional[str] = ..., total_open_events: _Optional[int] = ..., settings: _Optional[_Union[CampaignSettings, _Mapping]] = ...) -> None: ...

class CampaignSettings(_message.Message):
    __slots__ = ("recipient_name_template", "reply_to", "utm_enabled", "utm_source", "utm_medium", "utm_campaign", "header_html", "footer_html", "tags")
    RECIPIENT_NAME_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    UTM_ENABLED_FIELD_NUMBER: _ClassVar[int]
    UTM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    UTM_MEDIUM_FIELD_NUMBER: _ClassVar[int]
    UTM_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    HEADER_HTML_FIELD_NUMBER: _ClassVar[int]
    FOOTER_HTML_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    recipient_name_template: str
    reply_to: str
    utm_enabled: bool
    utm_source: str
    utm_medium: str
    utm_campaign: str
    header_html: str
    footer_html: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, recipient_name_template: _Optional[str] = ..., reply_to: _Optional[str] = ..., utm_enabled: _Optional[bool] = ..., utm_source: _Optional[str] = ..., utm_medium: _Optional[str] = ..., utm_campaign: _Optional[str] = ..., header_html: _Optional[str] = ..., footer_html: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class ClickedLink(_message.Message):
    __slots__ = ("url", "click_count", "unique_contacts")
    URL_FIELD_NUMBER: _ClassVar[int]
    CLICK_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CONTACTS_FIELD_NUMBER: _ClassVar[int]
    url: str
    click_count: int
    unique_contacts: int
    def __init__(self, url: _Optional[str] = ..., click_count: _Optional[int] = ..., unique_contacts: _Optional[int] = ...) -> None: ...

class UnsubscribeReasonCount(_message.Message):
    __slots__ = ("reason", "count")
    REASON_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    reason: str
    count: int
    def __init__(self, reason: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("campaign",)
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    campaign: Campaign
    def __init__(self, campaign: _Optional[_Union[Campaign, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("campaign",)
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    campaign: Campaign
    def __init__(self, campaign: _Optional[_Union[Campaign, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "campaign", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    campaign: Campaign
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., campaign: _Optional[_Union[Campaign, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("campaign",)
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    campaign: Campaign
    def __init__(self, campaign: _Optional[_Union[Campaign, _Mapping]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("campaign",)
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    campaign: Campaign
    def __init__(self, campaign: _Optional[_Union[Campaign, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "segment_id", "folder_id", "channel", "scheduled_at_gte", "scheduled_at_lte", "filter", "status", "creative_id")
    IDS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATIVE_ID_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    segment_id: str
    folder_id: str
    channel: str
    scheduled_at_gte: _timestamp_pb2.Timestamp
    scheduled_at_lte: _timestamp_pb2.Timestamp
    filter: _filter_pb2.Filter
    status: CampaignStatus
    creative_id: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., segment_id: _Optional[str] = ..., folder_id: _Optional[str] = ..., channel: _Optional[str] = ..., scheduled_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., scheduled_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., status: _Optional[_Union[CampaignStatus, str]] = ..., creative_id: _Optional[str] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("campaign_list",)
    CAMPAIGN_LIST_FIELD_NUMBER: _ClassVar[int]
    campaign_list: _containers.RepeatedCompositeFieldContainer[Campaign]
    def __init__(self, campaign_list: _Optional[_Iterable[_Union[Campaign, _Mapping]]] = ...) -> None: ...

class CloneRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CloneResponse(_message.Message):
    __slots__ = ("campaign",)
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    campaign: Campaign
    def __init__(self, campaign: _Optional[_Union[Campaign, _Mapping]] = ...) -> None: ...

class CampaignSend(_message.Message):
    __slots__ = ("id", "campaign_id", "campaign_name", "contact_id", "contact_name", "recipient_value", "channel", "integration_id", "integration_name", "dispatch_mode", "attempt", "status", "open_count", "click_count", "sent_at", "delivered_at", "first_opened_at", "last_opened_at", "first_clicked_at", "last_clicked_at", "failed_at", "bounced_at", "external_message_id", "error_message", "created_at", "updated_at", "stats_collection_completed", "stats_collection_completed_at", "stats_collection_reason", "stats_last_sync_at", "stats_next_sync_at", "stats_sync_error", "stats_provider_cursor", "stats_last_event_key", "unsubscribed_at", "unsubscribe_token", "time_to_first_open_seconds", "clicked_links", "unsubscribe_reason", "complained_at", "message_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_NAME_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OPEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    CLICK_COUNT_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    DELIVERED_AT_FIELD_NUMBER: _ClassVar[int]
    FIRST_OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    FIRST_CLICKED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_CLICKED_AT_FIELD_NUMBER: _ClassVar[int]
    FAILED_AT_FIELD_NUMBER: _ClassVar[int]
    BOUNCED_AT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    STATS_COLLECTION_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    STATS_COLLECTION_COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    STATS_COLLECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    STATS_LAST_SYNC_AT_FIELD_NUMBER: _ClassVar[int]
    STATS_NEXT_SYNC_AT_FIELD_NUMBER: _ClassVar[int]
    STATS_SYNC_ERROR_FIELD_NUMBER: _ClassVar[int]
    STATS_PROVIDER_CURSOR_FIELD_NUMBER: _ClassVar[int]
    STATS_LAST_EVENT_KEY_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBED_AT_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIRST_OPEN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CLICKED_LINKS_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBE_REASON_FIELD_NUMBER: _ClassVar[int]
    COMPLAINED_AT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    campaign_id: str
    campaign_name: str
    contact_id: str
    contact_name: str
    recipient_value: str
    channel: str
    integration_id: str
    integration_name: str
    dispatch_mode: str
    attempt: int
    status: CampaignSendStatus
    open_count: int
    click_count: int
    sent_at: _timestamp_pb2.Timestamp
    delivered_at: _timestamp_pb2.Timestamp
    first_opened_at: _timestamp_pb2.Timestamp
    last_opened_at: _timestamp_pb2.Timestamp
    first_clicked_at: _timestamp_pb2.Timestamp
    last_clicked_at: _timestamp_pb2.Timestamp
    failed_at: _timestamp_pb2.Timestamp
    bounced_at: _timestamp_pb2.Timestamp
    external_message_id: str
    error_message: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    stats_collection_completed: bool
    stats_collection_completed_at: _timestamp_pb2.Timestamp
    stats_collection_reason: str
    stats_last_sync_at: _timestamp_pb2.Timestamp
    stats_next_sync_at: _timestamp_pb2.Timestamp
    stats_sync_error: str
    stats_provider_cursor: str
    stats_last_event_key: str
    unsubscribed_at: _timestamp_pb2.Timestamp
    unsubscribe_token: str
    time_to_first_open_seconds: int
    clicked_links: _containers.RepeatedCompositeFieldContainer[ClickedLink]
    unsubscribe_reason: str
    complained_at: _timestamp_pb2.Timestamp
    message_id: str
    def __init__(self, id: _Optional[str] = ..., campaign_id: _Optional[str] = ..., campaign_name: _Optional[str] = ..., contact_id: _Optional[str] = ..., contact_name: _Optional[str] = ..., recipient_value: _Optional[str] = ..., channel: _Optional[str] = ..., integration_id: _Optional[str] = ..., integration_name: _Optional[str] = ..., dispatch_mode: _Optional[str] = ..., attempt: _Optional[int] = ..., status: _Optional[_Union[CampaignSendStatus, str]] = ..., open_count: _Optional[int] = ..., click_count: _Optional[int] = ..., sent_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., delivered_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., first_opened_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_opened_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., first_clicked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_clicked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., failed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., bounced_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., external_message_id: _Optional[str] = ..., error_message: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stats_collection_completed: _Optional[bool] = ..., stats_collection_completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stats_collection_reason: _Optional[str] = ..., stats_last_sync_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stats_next_sync_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stats_sync_error: _Optional[str] = ..., stats_provider_cursor: _Optional[str] = ..., stats_last_event_key: _Optional[str] = ..., unsubscribed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., unsubscribe_token: _Optional[str] = ..., time_to_first_open_seconds: _Optional[int] = ..., clicked_links: _Optional[_Iterable[_Union[ClickedLink, _Mapping]]] = ..., unsubscribe_reason: _Optional[str] = ..., complained_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., message_id: _Optional[str] = ...) -> None: ...

class GetCampaignSendRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCampaignSendResponse(_message.Message):
    __slots__ = ("campaign_send",)
    CAMPAIGN_SEND_FIELD_NUMBER: _ClassVar[int]
    campaign_send: CampaignSend
    def __init__(self, campaign_send: _Optional[_Union[CampaignSend, _Mapping]] = ...) -> None: ...

class ListCampaignSendsRequest(_message.Message):
    __slots__ = ("ids", "campaign_id", "contact_id", "channel", "status", "integration_id", "sent_at_gte", "sent_at_lte", "opened_at_gte", "opened_at_lte", "clicked_at_gte", "clicked_at_lte", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    CLICKED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    CLICKED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    campaign_id: str
    contact_id: str
    channel: str
    status: CampaignSendStatus
    integration_id: str
    sent_at_gte: _timestamp_pb2.Timestamp
    sent_at_lte: _timestamp_pb2.Timestamp
    opened_at_gte: _timestamp_pb2.Timestamp
    opened_at_lte: _timestamp_pb2.Timestamp
    clicked_at_gte: _timestamp_pb2.Timestamp
    clicked_at_lte: _timestamp_pb2.Timestamp
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., campaign_id: _Optional[str] = ..., contact_id: _Optional[str] = ..., channel: _Optional[str] = ..., status: _Optional[_Union[CampaignSendStatus, str]] = ..., integration_id: _Optional[str] = ..., sent_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sent_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., opened_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., opened_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., clicked_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., clicked_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListCampaignSendsResponse(_message.Message):
    __slots__ = ("campaign_send_list",)
    CAMPAIGN_SEND_LIST_FIELD_NUMBER: _ClassVar[int]
    campaign_send_list: _containers.RepeatedCompositeFieldContainer[CampaignSend]
    def __init__(self, campaign_send_list: _Optional[_Iterable[_Union[CampaignSend, _Mapping]]] = ...) -> None: ...

class DispatchRequest(_message.Message):
    __slots__ = ("id", "schedule", "automatic")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    id: str
    schedule: bool
    automatic: bool
    def __init__(self, id: _Optional[str] = ..., schedule: _Optional[bool] = ..., automatic: _Optional[bool] = ...) -> None: ...

class DispatchResponse(_message.Message):
    __slots__ = ("campaign", "message")
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    campaign: Campaign
    message: str
    def __init__(self, campaign: _Optional[_Union[Campaign, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class PreviewRequest(_message.Message):
    __slots__ = ("id", "contact_id", "filter", "creative_id", "segment_id", "html_content", "text_content")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CREATIVE_ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    HTML_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TEXT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    contact_id: str
    filter: _filter_pb2.Filter
    creative_id: str
    segment_id: str
    html_content: str
    text_content: str
    def __init__(self, id: _Optional[str] = ..., contact_id: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., creative_id: _Optional[str] = ..., segment_id: _Optional[str] = ..., html_content: _Optional[str] = ..., text_content: _Optional[str] = ...) -> None: ...

class PreviewContact(_message.Message):
    __slots__ = ("id", "name", "email", "phone", "recipient_value")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    email: str
    phone: str
    recipient_value: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., recipient_value: _Optional[str] = ...) -> None: ...

class PreviewResponse(_message.Message):
    __slots__ = ("selected_contact", "contacts", "rendered_subject", "rendered_html", "rendered_text", "recipient_value", "missing_variables", "channel")
    SELECTED_CONTACT_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    RENDERED_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    RENDERED_HTML_FIELD_NUMBER: _ClassVar[int]
    RENDERED_TEXT_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    MISSING_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    selected_contact: PreviewContact
    contacts: _containers.RepeatedCompositeFieldContainer[PreviewContact]
    rendered_subject: str
    rendered_html: str
    rendered_text: str
    recipient_value: str
    missing_variables: _containers.RepeatedScalarFieldContainer[str]
    channel: str
    def __init__(self, selected_contact: _Optional[_Union[PreviewContact, _Mapping]] = ..., contacts: _Optional[_Iterable[_Union[PreviewContact, _Mapping]]] = ..., rendered_subject: _Optional[str] = ..., rendered_html: _Optional[str] = ..., rendered_text: _Optional[str] = ..., recipient_value: _Optional[str] = ..., missing_variables: _Optional[_Iterable[str]] = ..., channel: _Optional[str] = ...) -> None: ...

class SimulateSendRequest(_message.Message):
    __slots__ = ("id", "contact_id", "destination", "creative_id", "segment_id", "html_content", "text_content")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    CREATIVE_ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    HTML_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TEXT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    contact_id: str
    destination: str
    creative_id: str
    segment_id: str
    html_content: str
    text_content: str
    def __init__(self, id: _Optional[str] = ..., contact_id: _Optional[str] = ..., destination: _Optional[str] = ..., creative_id: _Optional[str] = ..., segment_id: _Optional[str] = ..., html_content: _Optional[str] = ..., text_content: _Optional[str] = ...) -> None: ...

class SimulateSendResponse(_message.Message):
    __slots__ = ("destination", "rendered_subject", "rendered_html", "rendered_text", "message")
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    RENDERED_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    RENDERED_HTML_FIELD_NUMBER: _ClassVar[int]
    RENDERED_TEXT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    destination: str
    rendered_subject: str
    rendered_html: str
    rendered_text: str
    message: str
    def __init__(self, destination: _Optional[str] = ..., rendered_subject: _Optional[str] = ..., rendered_html: _Optional[str] = ..., rendered_text: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class SyncStatsRequest(_message.Message):
    __slots__ = ("id", "pending_only")
    ID_FIELD_NUMBER: _ClassVar[int]
    PENDING_ONLY_FIELD_NUMBER: _ClassVar[int]
    id: str
    pending_only: bool
    def __init__(self, id: _Optional[str] = ..., pending_only: _Optional[bool] = ...) -> None: ...

class SyncStatsResponse(_message.Message):
    __slots__ = ("campaign", "synced_sends", "applied_events", "message")
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    SYNCED_SENDS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_EVENTS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    campaign: Campaign
    synced_sends: int
    applied_events: int
    message: str
    def __init__(self, campaign: _Optional[_Union[Campaign, _Mapping]] = ..., synced_sends: _Optional[int] = ..., applied_events: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class DashboardRequest(_message.Message):
    __slots__ = ("filter", "date_from", "date_to")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    DATE_FROM_FIELD_NUMBER: _ClassVar[int]
    DATE_TO_FIELD_NUMBER: _ClassVar[int]
    filter: _filter_pb2.Filter
    date_from: _timestamp_pb2.Timestamp
    date_to: _timestamp_pb2.Timestamp
    def __init__(self, filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., date_from: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CampaignSummary(_message.Message):
    __slots__ = ("id", "name", "channel", "status", "total_recipients", "total_sent", "total_opened", "total_clicked", "sent_at", "segment_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SENT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_OPENED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CLICKED_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    channel: str
    status: CampaignStatus
    total_recipients: int
    total_sent: int
    total_opened: int
    total_clicked: int
    sent_at: _timestamp_pb2.Timestamp
    segment_name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., channel: _Optional[str] = ..., status: _Optional[_Union[CampaignStatus, str]] = ..., total_recipients: _Optional[int] = ..., total_sent: _Optional[int] = ..., total_opened: _Optional[int] = ..., total_clicked: _Optional[int] = ..., sent_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., segment_name: _Optional[str] = ...) -> None: ...

class StatusCount(_message.Message):
    __slots__ = ("status", "count")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    status: CampaignStatus
    count: int
    def __init__(self, status: _Optional[_Union[CampaignStatus, str]] = ..., count: _Optional[int] = ...) -> None: ...

class DashboardResponse(_message.Message):
    __slots__ = ("total_campaigns", "active_campaigns", "total_sent", "total_delivered", "avg_open_rate", "avg_click_rate", "recent_campaigns", "status_distribution")
    TOTAL_CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SENT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DELIVERED_FIELD_NUMBER: _ClassVar[int]
    AVG_OPEN_RATE_FIELD_NUMBER: _ClassVar[int]
    AVG_CLICK_RATE_FIELD_NUMBER: _ClassVar[int]
    RECENT_CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    STATUS_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    total_campaigns: int
    active_campaigns: int
    total_sent: int
    total_delivered: int
    avg_open_rate: float
    avg_click_rate: float
    recent_campaigns: _containers.RepeatedCompositeFieldContainer[CampaignSummary]
    status_distribution: _containers.RepeatedCompositeFieldContainer[StatusCount]
    def __init__(self, total_campaigns: _Optional[int] = ..., active_campaigns: _Optional[int] = ..., total_sent: _Optional[int] = ..., total_delivered: _Optional[int] = ..., avg_open_rate: _Optional[float] = ..., avg_click_rate: _Optional[float] = ..., recent_campaigns: _Optional[_Iterable[_Union[CampaignSummary, _Mapping]]] = ..., status_distribution: _Optional[_Iterable[_Union[StatusCount, _Mapping]]] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("list_request", "tipo_relatorio")
    LIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TIPO_RELATORIO_FIELD_NUMBER: _ClassVar[int]
    list_request: ListRequest
    tipo_relatorio: str
    def __init__(self, list_request: _Optional[_Union[ListRequest, _Mapping]] = ..., tipo_relatorio: _Optional[str] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...
