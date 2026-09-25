from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FilterData(_message.Message):
    __slots__ = ("id", "fields", "name", "description", "module", "conditions", "main_label", "main_fields", "padrao_sistema", "user_id", "shared", "preset", "main", "main_help")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    MAIN_LABEL_FIELD_NUMBER: _ClassVar[int]
    MAIN_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PADRAO_SISTEMA_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SHARED_FIELD_NUMBER: _ClassVar[int]
    PRESET_FIELD_NUMBER: _ClassVar[int]
    MAIN_FIELD_NUMBER: _ClassVar[int]
    MAIN_HELP_FIELD_NUMBER: _ClassVar[int]
    id: str
    fields: _metadata_pb2.BasicFields
    name: str
    description: str
    module: str
    conditions: _containers.RepeatedCompositeFieldContainer[_filter_pb2.condition]
    main_label: str
    main_fields: _containers.RepeatedCompositeFieldContainer[_filter_pb2.condition]
    padrao_sistema: bool
    user_id: str
    shared: bool
    preset: bool
    main: str
    main_help: str
    def __init__(self, id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., module: _Optional[str] = ..., conditions: _Optional[_Iterable[_Union[_filter_pb2.condition, _Mapping]]] = ..., main_label: _Optional[str] = ..., main_fields: _Optional[_Iterable[_Union[_filter_pb2.condition, _Mapping]]] = ..., padrao_sistema: _Optional[bool] = ..., user_id: _Optional[str] = ..., shared: _Optional[bool] = ..., preset: _Optional[bool] = ..., main: _Optional[str] = ..., main_help: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("filter_data",)
    FILTER_DATA_FIELD_NUMBER: _ClassVar[int]
    filter_data: FilterData
    def __init__(self, filter_data: _Optional[_Union[FilterData, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("filter_data",)
    FILTER_DATA_FIELD_NUMBER: _ClassVar[int]
    filter_data: FilterData
    def __init__(self, filter_data: _Optional[_Union[FilterData, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "filter_data", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_DATA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    filter_data: FilterData
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., filter_data: _Optional[_Union[FilterData, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("filter_data",)
    FILTER_DATA_FIELD_NUMBER: _ClassVar[int]
    filter_data: FilterData
    def __init__(self, filter_data: _Optional[_Union[FilterData, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("ids", "name", "module", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    name: str
    module: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., module: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("filter_data_list",)
    FILTER_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    filter_data_list: _containers.RepeatedCompositeFieldContainer[FilterData]
    def __init__(self, filter_data_list: _Optional[_Iterable[_Union[FilterData, _Mapping]]] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("filter_data",)
    FILTER_DATA_FIELD_NUMBER: _ClassVar[int]
    filter_data: FilterData
    def __init__(self, filter_data: _Optional[_Union[FilterData, _Mapping]] = ...) -> None: ...

class FacetsRequest(_message.Message):
    __slots__ = ("module", "filter", "facet_fields", "presets")
    MODULE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FACET_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PRESETS_FIELD_NUMBER: _ClassVar[int]
    module: str
    filter: _filter_pb2.Filter
    facet_fields: _containers.RepeatedScalarFieldContainer[str]
    presets: _containers.RepeatedCompositeFieldContainer[FacetPreset]
    def __init__(self, module: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., facet_fields: _Optional[_Iterable[str]] = ..., presets: _Optional[_Iterable[_Union[FacetPreset, _Mapping]]] = ...) -> None: ...

class FacetPreset(_message.Message):
    __slots__ = ("id", "filter")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    id: str
    filter: _filter_pb2.Filter
    def __init__(self, id: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class FacetsResponse(_message.Message):
    __slots__ = ("total", "filtered_total", "fields", "presets")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    FILTERED_TOTAL_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    PRESETS_FIELD_NUMBER: _ClassVar[int]
    total: int
    filtered_total: int
    fields: _containers.RepeatedCompositeFieldContainer[FieldFacet]
    presets: _containers.RepeatedCompositeFieldContainer[PresetCount]
    def __init__(self, total: _Optional[int] = ..., filtered_total: _Optional[int] = ..., fields: _Optional[_Iterable[_Union[FieldFacet, _Mapping]]] = ..., presets: _Optional[_Iterable[_Union[PresetCount, _Mapping]]] = ...) -> None: ...

class FieldFacet(_message.Message):
    __slots__ = ("field_name", "values")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    values: _containers.RepeatedCompositeFieldContainer[FacetValue]
    def __init__(self, field_name: _Optional[str] = ..., values: _Optional[_Iterable[_Union[FacetValue, _Mapping]]] = ...) -> None: ...

class FacetValue(_message.Message):
    __slots__ = ("value", "count", "label")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    value: str
    count: int
    label: str
    def __init__(self, value: _Optional[str] = ..., count: _Optional[int] = ..., label: _Optional[str] = ...) -> None: ...

class PresetCount(_message.Message):
    __slots__ = ("id", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    count: int
    def __init__(self, id: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...
