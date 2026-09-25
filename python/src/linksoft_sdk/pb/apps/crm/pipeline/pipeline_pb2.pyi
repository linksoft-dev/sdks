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

class PipelineStage(_message.Message):
    __slots__ = ("id", "name", "position", "probability", "color", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    position: int
    probability: float
    color: str
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., position: _Optional[int] = ..., probability: _Optional[float] = ..., color: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class PipelineLossReason(_message.Message):
    __slots__ = ("id", "name", "color", "position")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    color: str
    position: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., color: _Optional[str] = ..., position: _Optional[int] = ...) -> None: ...

class Pipeline(_message.Message):
    __slots__ = ("id", "name", "stages", "created_at", "updated_at", "loss_reasons", "description", "fields")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LOSS_REASONS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    stages: _containers.RepeatedCompositeFieldContainer[PipelineStage]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    loss_reasons: _containers.RepeatedCompositeFieldContainer[PipelineLossReason]
    description: str
    fields: _metadata_pb2.BasicFields
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., stages: _Optional[_Iterable[_Union[PipelineStage, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., loss_reasons: _Optional[_Iterable[_Union[PipelineLossReason, _Mapping]]] = ..., description: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("pipeline",)
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    pipeline: Pipeline
    def __init__(self, pipeline: _Optional[_Union[Pipeline, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("pipeline",)
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    pipeline: Pipeline
    def __init__(self, pipeline: _Optional[_Union[Pipeline, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "pipeline", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    pipeline: Pipeline
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., pipeline: _Optional[_Union[Pipeline, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("pipeline",)
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    pipeline: Pipeline
    def __init__(self, pipeline: _Optional[_Union[Pipeline, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("pipeline",)
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    pipeline: Pipeline
    def __init__(self, pipeline: _Optional[_Union[Pipeline, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("pipeline_list",)
    PIPELINE_LIST_FIELD_NUMBER: _ClassVar[int]
    pipeline_list: _containers.RepeatedCompositeFieldContainer[Pipeline]
    def __init__(self, pipeline_list: _Optional[_Iterable[_Union[Pipeline, _Mapping]]] = ...) -> None: ...
