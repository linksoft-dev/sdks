from google.api import annotations_pb2 as _annotations_pb2
from google.api import resource_pb2 as _resource_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("production_cost",)
    PRODUCTION_COST_FIELD_NUMBER: _ClassVar[int]
    production_cost: ProductionCost
    def __init__(self, production_cost: _Optional[_Union[ProductionCost, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("production_cost",)
    PRODUCTION_COST_FIELD_NUMBER: _ClassVar[int]
    production_cost: ProductionCost
    def __init__(self, production_cost: _Optional[_Union[ProductionCost, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "production_cost", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_COST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    production_cost: ProductionCost
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., production_cost: _Optional[_Union[ProductionCost, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("production_cost",)
    PRODUCTION_COST_FIELD_NUMBER: _ClassVar[int]
    production_cost: ProductionCost
    def __init__(self, production_cost: _Optional[_Union[ProductionCost, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("ids", "only_active", "only_default", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    ONLY_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ONLY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    only_active: bool
    only_default: bool
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., only_active: _Optional[bool] = ..., only_default: _Optional[bool] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("production_cost_list",)
    PRODUCTION_COST_LIST_FIELD_NUMBER: _ClassVar[int]
    production_cost_list: _containers.RepeatedCompositeFieldContainer[ProductionCost]
    def __init__(self, production_cost_list: _Optional[_Iterable[_Union[ProductionCost, _Mapping]]] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("production_cost",)
    PRODUCTION_COST_FIELD_NUMBER: _ClassVar[int]
    production_cost: ProductionCost
    def __init__(self, production_cost: _Optional[_Union[ProductionCost, _Mapping]] = ...) -> None: ...

class ProductionCost(_message.Message):
    __slots__ = ("id", "fields", "name", "description", "value", "type", "apply_by_default", "active", "category_ids", "category_names", "tag_names")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    APPLY_BY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_IDS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_NAMES_FIELD_NUMBER: _ClassVar[int]
    TAG_NAMES_FIELD_NUMBER: _ClassVar[int]
    id: str
    fields: _metadata_pb2.BasicFields
    name: str
    description: str
    value: float
    type: str
    apply_by_default: bool
    active: bool
    category_ids: _containers.RepeatedScalarFieldContainer[str]
    category_names: _containers.RepeatedScalarFieldContainer[str]
    tag_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., value: _Optional[float] = ..., type: _Optional[str] = ..., apply_by_default: _Optional[bool] = ..., active: _Optional[bool] = ..., category_ids: _Optional[_Iterable[str]] = ..., category_names: _Optional[_Iterable[str]] = ..., tag_names: _Optional[_Iterable[str]] = ...) -> None: ...
