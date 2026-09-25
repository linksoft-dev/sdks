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

class AutomationTrigger(_message.Message):
    __slots__ = ("type", "days", "send_at_time")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    SEND_AT_TIME_FIELD_NUMBER: _ClassVar[int]
    type: str
    days: int
    send_at_time: str
    def __init__(self, type: _Optional[str] = ..., days: _Optional[int] = ..., send_at_time: _Optional[str] = ...) -> None: ...

class AutomationAction(_message.Message):
    __slots__ = ("type", "configuration")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    type: str
    configuration: str
    def __init__(self, type: _Optional[str] = ..., configuration: _Optional[str] = ...) -> None: ...

class AutomationRule(_message.Message):
    __slots__ = ("id", "stage_id", "trigger", "actions", "run_on_every_entry", "enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    RUN_ON_EVERY_ENTRY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    stage_id: str
    trigger: AutomationTrigger
    actions: _containers.RepeatedCompositeFieldContainer[AutomationAction]
    run_on_every_entry: bool
    enabled: bool
    def __init__(self, id: _Optional[str] = ..., stage_id: _Optional[str] = ..., trigger: _Optional[_Union[AutomationTrigger, _Mapping]] = ..., actions: _Optional[_Iterable[_Union[AutomationAction, _Mapping]]] = ..., run_on_every_entry: _Optional[bool] = ..., enabled: _Optional[bool] = ...) -> None: ...

class PipelineAutomation(_message.Message):
    __slots__ = ("id", "name", "pipeline_id", "pipeline_name", "status", "rules", "created_at", "updated_at", "send_window")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    SEND_WINDOW_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    pipeline_id: str
    pipeline_name: str
    status: str
    rules: _containers.RepeatedCompositeFieldContainer[AutomationRule]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    send_window: AutomationSendWindow
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., pipeline_id: _Optional[str] = ..., pipeline_name: _Optional[str] = ..., status: _Optional[str] = ..., rules: _Optional[_Iterable[_Union[AutomationRule, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., send_window: _Optional[_Union[AutomationSendWindow, _Mapping]] = ...) -> None: ...

class AutomationSendWindow(_message.Message):
    __slots__ = ("start_time", "end_time", "weekdays")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    WEEKDAYS_FIELD_NUMBER: _ClassVar[int]
    start_time: str
    end_time: str
    weekdays: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., weekdays: _Optional[_Iterable[int]] = ...) -> None: ...

class AutomationRun(_message.Message):
    __slots__ = ("id", "automation_id", "rule_id", "deal_id", "pipeline_id", "stage_id", "trigger_type", "triggered_at", "stage_entered_at", "status", "error", "action_results", "idempotency_key")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    DEAL_ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRIGGERED_AT_FIELD_NUMBER: _ClassVar[int]
    STAGE_ENTERED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ACTION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    automation_id: str
    rule_id: str
    deal_id: str
    pipeline_id: str
    stage_id: str
    trigger_type: str
    triggered_at: _timestamp_pb2.Timestamp
    stage_entered_at: _timestamp_pb2.Timestamp
    status: str
    error: str
    action_results: _containers.RepeatedCompositeFieldContainer[ActionResult]
    idempotency_key: str
    def __init__(self, id: _Optional[str] = ..., automation_id: _Optional[str] = ..., rule_id: _Optional[str] = ..., deal_id: _Optional[str] = ..., pipeline_id: _Optional[str] = ..., stage_id: _Optional[str] = ..., trigger_type: _Optional[str] = ..., triggered_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stage_entered_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[str] = ..., error: _Optional[str] = ..., action_results: _Optional[_Iterable[_Union[ActionResult, _Mapping]]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class ActionResult(_message.Message):
    __slots__ = ("action_type", "status", "error", "detail")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    action_type: str
    status: str
    error: str
    detail: str
    def __init__(self, action_type: _Optional[str] = ..., status: _Optional[str] = ..., error: _Optional[str] = ..., detail: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("pipeline_automation",)
    PIPELINE_AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    pipeline_automation: PipelineAutomation
    def __init__(self, pipeline_automation: _Optional[_Union[PipelineAutomation, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("pipeline_automation",)
    PIPELINE_AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    pipeline_automation: PipelineAutomation
    def __init__(self, pipeline_automation: _Optional[_Union[PipelineAutomation, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "pipeline_automation", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    pipeline_automation: PipelineAutomation
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., pipeline_automation: _Optional[_Union[PipelineAutomation, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("pipeline_automation",)
    PIPELINE_AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    pipeline_automation: PipelineAutomation
    def __init__(self, pipeline_automation: _Optional[_Union[PipelineAutomation, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("pipeline_automation",)
    PIPELINE_AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    pipeline_automation: PipelineAutomation
    def __init__(self, pipeline_automation: _Optional[_Union[PipelineAutomation, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "pipeline_id", "status", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    pipeline_id: str
    status: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., pipeline_id: _Optional[str] = ..., status: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("pipeline_automation_list",)
    PIPELINE_AUTOMATION_LIST_FIELD_NUMBER: _ClassVar[int]
    pipeline_automation_list: _containers.RepeatedCompositeFieldContainer[PipelineAutomation]
    def __init__(self, pipeline_automation_list: _Optional[_Iterable[_Union[PipelineAutomation, _Mapping]]] = ...) -> None: ...

class SetStatusRequest(_message.Message):
    __slots__ = ("id", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: str
    def __init__(self, id: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class SetStatusResponse(_message.Message):
    __slots__ = ("pipeline_automation",)
    PIPELINE_AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    pipeline_automation: PipelineAutomation
    def __init__(self, pipeline_automation: _Optional[_Union[PipelineAutomation, _Mapping]] = ...) -> None: ...

class ListRunsRequest(_message.Message):
    __slots__ = ("automation_id", "deal_id", "rule_id", "page_size", "page_token", "filter")
    AUTOMATION_ID_FIELD_NUMBER: _ClassVar[int]
    DEAL_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    automation_id: str
    deal_id: str
    rule_id: str
    page_size: int
    page_token: str
    filter: _filter_pb2.Filter
    def __init__(self, automation_id: _Optional[str] = ..., deal_id: _Optional[str] = ..., rule_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListRunsResponse(_message.Message):
    __slots__ = ("runs", "next_page_token")
    RUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[AutomationRun]
    next_page_token: str
    def __init__(self, runs: _Optional[_Iterable[_Union[AutomationRun, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SendTestEmailRequest(_message.Message):
    __slots__ = ("destination", "configuration", "deal_id", "pipeline_id", "stage_id")
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    DEAL_ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    destination: str
    configuration: str
    deal_id: str
    pipeline_id: str
    stage_id: str
    def __init__(self, destination: _Optional[str] = ..., configuration: _Optional[str] = ..., deal_id: _Optional[str] = ..., pipeline_id: _Optional[str] = ..., stage_id: _Optional[str] = ...) -> None: ...

class SendTestEmailResponse(_message.Message):
    __slots__ = ("destination", "deal_title", "subject")
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    DEAL_TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    destination: str
    deal_title: str
    subject: str
    def __init__(self, destination: _Optional[str] = ..., deal_title: _Optional[str] = ..., subject: _Optional[str] = ...) -> None: ...
