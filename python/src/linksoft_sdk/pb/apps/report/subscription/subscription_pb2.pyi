import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DAILY: _ClassVar[ScheduleType]
    WEEKLY: _ClassVar[ScheduleType]
    MONTHLY: _ClassVar[ScheduleType]
    CRON: _ClassVar[ScheduleType]

class DeliveryChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMAIL: _ClassVar[DeliveryChannel]
    WHATSAPP: _ClassVar[DeliveryChannel]
DAILY: ScheduleType
WEEKLY: ScheduleType
MONTHLY: ScheduleType
CRON: ScheduleType
EMAIL: DeliveryChannel
WHATSAPP: DeliveryChannel

class ReportSubscription(_message.Message):
    __slots__ = ("id", "fields", "name", "description", "report_view_id", "user_id", "user_group_id", "delivery_channel", "email_addresses", "schedule", "enabled", "last_sent", "next_send")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REPORT_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    LAST_SENT_FIELD_NUMBER: _ClassVar[int]
    NEXT_SEND_FIELD_NUMBER: _ClassVar[int]
    id: str
    fields: _metadata_pb2.BasicFields
    name: str
    description: str
    report_view_id: str
    user_id: str
    user_group_id: str
    delivery_channel: DeliveryChannel
    email_addresses: _containers.RepeatedScalarFieldContainer[str]
    schedule: Schedule
    enabled: bool
    last_sent: _timestamp_pb2.Timestamp
    next_send: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., report_view_id: _Optional[str] = ..., user_id: _Optional[str] = ..., user_group_id: _Optional[str] = ..., delivery_channel: _Optional[_Union[DeliveryChannel, str]] = ..., email_addresses: _Optional[_Iterable[str]] = ..., schedule: _Optional[_Union[Schedule, _Mapping]] = ..., enabled: _Optional[bool] = ..., last_sent: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., next_send: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Schedule(_message.Message):
    __slots__ = ("type", "hour", "day_of_week", "day_of_month", "cron_expression")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    CRON_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    type: ScheduleType
    hour: int
    day_of_week: int
    day_of_month: int
    cron_expression: str
    def __init__(self, type: _Optional[_Union[ScheduleType, str]] = ..., hour: _Optional[int] = ..., day_of_week: _Optional[int] = ..., day_of_month: _Optional[int] = ..., cron_expression: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("report_subscription",)
    REPORT_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    report_subscription: ReportSubscription
    def __init__(self, report_subscription: _Optional[_Union[ReportSubscription, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("report_subscription",)
    REPORT_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    report_subscription: ReportSubscription
    def __init__(self, report_subscription: _Optional[_Union[ReportSubscription, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "report_subscription", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    report_subscription: ReportSubscription
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., report_subscription: _Optional[_Union[ReportSubscription, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("report_subscription",)
    REPORT_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    report_subscription: ReportSubscription
    def __init__(self, report_subscription: _Optional[_Union[ReportSubscription, _Mapping]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "name", "report_view_id", "user_id", "user_group_id", "enabled", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REPORT_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    name: str
    report_view_id: str
    user_id: str
    user_group_id: str
    enabled: bool
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., report_view_id: _Optional[str] = ..., user_id: _Optional[str] = ..., user_group_id: _Optional[str] = ..., enabled: _Optional[bool] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("report_subscription_list",)
    REPORT_SUBSCRIPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    report_subscription_list: _containers.RepeatedCompositeFieldContainer[ReportSubscription]
    def __init__(self, report_subscription_list: _Optional[_Iterable[_Union[ReportSubscription, _Mapping]]] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("report_subscription",)
    REPORT_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    report_subscription: ReportSubscription
    def __init__(self, report_subscription: _Optional[_Union[ReportSubscription, _Mapping]] = ...) -> None: ...
