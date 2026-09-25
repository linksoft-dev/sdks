import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTIVITY_TYPE_UNSPECIFIED: _ClassVar[ActivityType]
    ACTIVITY_TYPE_TASK: _ClassVar[ActivityType]
    ACTIVITY_TYPE_CALL: _ClassVar[ActivityType]
    ACTIVITY_TYPE_EMAIL: _ClassVar[ActivityType]
    ACTIVITY_TYPE_WHATSAPP: _ClassVar[ActivityType]
    ACTIVITY_TYPE_MEETING: _ClassVar[ActivityType]
ACTIVITY_TYPE_UNSPECIFIED: ActivityType
ACTIVITY_TYPE_TASK: ActivityType
ACTIVITY_TYPE_CALL: ActivityType
ACTIVITY_TYPE_EMAIL: ActivityType
ACTIVITY_TYPE_WHATSAPP: ActivityType
ACTIVITY_TYPE_MEETING: ActivityType

class Activity(_message.Message):
    __slots__ = ("id", "deal_id", "type", "title", "due_at", "completed_at", "created_at", "updated_at", "person_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEAL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DUE_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    deal_id: str
    type: ActivityType
    title: str
    due_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    person_id: str
    def __init__(self, id: _Optional[str] = ..., deal_id: _Optional[str] = ..., type: _Optional[_Union[ActivityType, str]] = ..., title: _Optional[str] = ..., due_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., person_id: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("activity",)
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    activity: Activity
    def __init__(self, activity: _Optional[_Union[Activity, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("activity",)
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    activity: Activity
    def __init__(self, activity: _Optional[_Union[Activity, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "activity", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    activity: Activity
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., activity: _Optional[_Union[Activity, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("activity",)
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    activity: Activity
    def __init__(self, activity: _Optional[_Union[Activity, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("activity",)
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    activity: Activity
    def __init__(self, activity: _Optional[_Union[Activity, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "deal_id", "type", "due_at_gte", "due_at_lte", "filter", "person_id")
    IDS_FIELD_NUMBER: _ClassVar[int]
    DEAL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DUE_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    DUE_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    deal_id: str
    type: ActivityType
    due_at_gte: _timestamp_pb2.Timestamp
    due_at_lte: _timestamp_pb2.Timestamp
    filter: _filter_pb2.Filter
    person_id: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., deal_id: _Optional[str] = ..., type: _Optional[_Union[ActivityType, str]] = ..., due_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., due_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., person_id: _Optional[str] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("activity_list",)
    ACTIVITY_LIST_FIELD_NUMBER: _ClassVar[int]
    activity_list: _containers.RepeatedCompositeFieldContainer[Activity]
    def __init__(self, activity_list: _Optional[_Iterable[_Union[Activity, _Mapping]]] = ...) -> None: ...
