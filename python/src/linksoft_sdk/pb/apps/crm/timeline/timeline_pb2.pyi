import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimelineEvent(_message.Message):
    __slots__ = ("id", "reference_id", "title", "detail", "occurred_at", "created_at", "updated_at", "person_id", "event_type", "origin", "user_id", "user_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    reference_id: str
    title: str
    detail: str
    occurred_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    person_id: str
    event_type: str
    origin: str
    user_id: str
    user_name: str
    def __init__(self, id: _Optional[str] = ..., reference_id: _Optional[str] = ..., title: _Optional[str] = ..., detail: _Optional[str] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., person_id: _Optional[str] = ..., event_type: _Optional[str] = ..., origin: _Optional[str] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("timeline_event",)
    TIMELINE_EVENT_FIELD_NUMBER: _ClassVar[int]
    timeline_event: TimelineEvent
    def __init__(self, timeline_event: _Optional[_Union[TimelineEvent, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("timeline_event",)
    TIMELINE_EVENT_FIELD_NUMBER: _ClassVar[int]
    timeline_event: TimelineEvent
    def __init__(self, timeline_event: _Optional[_Union[TimelineEvent, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "timeline_event", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_EVENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    timeline_event: TimelineEvent
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., timeline_event: _Optional[_Union[TimelineEvent, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("timeline_event",)
    TIMELINE_EVENT_FIELD_NUMBER: _ClassVar[int]
    timeline_event: TimelineEvent
    def __init__(self, timeline_event: _Optional[_Union[TimelineEvent, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("timeline_event",)
    TIMELINE_EVENT_FIELD_NUMBER: _ClassVar[int]
    timeline_event: TimelineEvent
    def __init__(self, timeline_event: _Optional[_Union[TimelineEvent, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "reference_id", "occurred_at_gte", "occurred_at_lte", "filter", "person_id", "event_type")
    IDS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    reference_id: str
    occurred_at_gte: _timestamp_pb2.Timestamp
    occurred_at_lte: _timestamp_pb2.Timestamp
    filter: _filter_pb2.Filter
    person_id: str
    event_type: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., reference_id: _Optional[str] = ..., occurred_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., occurred_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., person_id: _Optional[str] = ..., event_type: _Optional[str] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("timeline_event_list",)
    TIMELINE_EVENT_LIST_FIELD_NUMBER: _ClassVar[int]
    timeline_event_list: _containers.RepeatedCompositeFieldContainer[TimelineEvent]
    def __init__(self, timeline_event_list: _Optional[_Iterable[_Union[TimelineEvent, _Mapping]]] = ...) -> None: ...
