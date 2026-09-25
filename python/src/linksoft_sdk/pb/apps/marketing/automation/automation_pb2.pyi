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

class AutomationStep(_message.Message):
    __slots__ = ("id", "type", "configuration", "campaign_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    configuration: str
    campaign_id: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., configuration: _Optional[str] = ..., campaign_id: _Optional[str] = ...) -> None: ...

class Automation(_message.Message):
    __slots__ = ("id", "name", "steps", "created_at", "updated_at", "start_at", "segment_id", "integration_id", "status", "segment_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    START_AT_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    steps: _containers.RepeatedCompositeFieldContainer[AutomationStep]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    start_at: _timestamp_pb2.Timestamp
    segment_id: str
    integration_id: str
    status: str
    segment_name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., steps: _Optional[_Iterable[_Union[AutomationStep, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., start_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., segment_id: _Optional[str] = ..., integration_id: _Optional[str] = ..., status: _Optional[str] = ..., segment_name: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("automation",)
    AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    automation: Automation
    def __init__(self, automation: _Optional[_Union[Automation, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("automation",)
    AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    automation: Automation
    def __init__(self, automation: _Optional[_Union[Automation, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "automation", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    automation: Automation
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., automation: _Optional[_Union[Automation, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("automation",)
    AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    automation: Automation
    def __init__(self, automation: _Optional[_Union[Automation, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("automation",)
    AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    automation: Automation
    def __init__(self, automation: _Optional[_Union[Automation, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "step_type", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    STEP_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    step_type: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., step_type: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("automation_list",)
    AUTOMATION_LIST_FIELD_NUMBER: _ClassVar[int]
    automation_list: _containers.RepeatedCompositeFieldContainer[Automation]
    def __init__(self, automation_list: _Optional[_Iterable[_Union[Automation, _Mapping]]] = ...) -> None: ...

class GenerateCampaignsRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GenerateCampaignsResponse(_message.Message):
    __slots__ = ("automation", "campaigns_created", "campaigns_updated", "message")
    AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGNS_CREATED_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGNS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    automation: Automation
    campaigns_created: int
    campaigns_updated: int
    message: str
    def __init__(self, automation: _Optional[_Union[Automation, _Mapping]] = ..., campaigns_created: _Optional[int] = ..., campaigns_updated: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
