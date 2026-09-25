from google.api import annotations_pb2 as _annotations_pb2
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

class Variation(_message.Message):
    __slots__ = ("fields", "id", "name", "attributes", "active")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: VariationAttributeValues
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[VariationAttributeValues, _Mapping]] = ...) -> None: ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    fields: _metadata_pb2.BasicFields
    id: str
    name: str
    attributes: _containers.MessageMap[str, VariationAttributeValues]
    active: bool
    def __init__(self, fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., attributes: _Optional[_Mapping[str, VariationAttributeValues]] = ..., active: _Optional[bool] = ...) -> None: ...

class VariationAttributeValues(_message.Message):
    __slots__ = ("values", "order")
    VALUES_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    order: int
    def __init__(self, values: _Optional[_Iterable[str]] = ..., order: _Optional[int] = ...) -> None: ...

class CreateVariationRequest(_message.Message):
    __slots__ = ("variation",)
    VARIATION_FIELD_NUMBER: _ClassVar[int]
    variation: Variation
    def __init__(self, variation: _Optional[_Union[Variation, _Mapping]] = ...) -> None: ...

class CreateVariationResponse(_message.Message):
    __slots__ = ("variation",)
    VARIATION_FIELD_NUMBER: _ClassVar[int]
    variation: Variation
    def __init__(self, variation: _Optional[_Union[Variation, _Mapping]] = ...) -> None: ...

class UpdateVariationRequest(_message.Message):
    __slots__ = ("id", "variation", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    VARIATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    variation: Variation
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., variation: _Optional[_Union[Variation, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateVariationResponse(_message.Message):
    __slots__ = ("variation",)
    VARIATION_FIELD_NUMBER: _ClassVar[int]
    variation: Variation
    def __init__(self, variation: _Optional[_Union[Variation, _Mapping]] = ...) -> None: ...

class DeleteVariationRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteVariationResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetVariationRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetVariationResponse(_message.Message):
    __slots__ = ("variation",)
    VARIATION_FIELD_NUMBER: _ClassVar[int]
    variation: Variation
    def __init__(self, variation: _Optional[_Union[Variation, _Mapping]] = ...) -> None: ...

class ListVariationRequest(_message.Message):
    __slots__ = ("ids", "names", "active", "filter", "page_size", "page_token")
    IDS_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    names: _containers.RepeatedScalarFieldContainer[str]
    active: bool
    filter: _filter_pb2.Filter
    page_size: int
    page_token: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., names: _Optional[_Iterable[str]] = ..., active: _Optional[bool] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListVariationResponse(_message.Message):
    __slots__ = ("variation_list", "next_page_token")
    VARIATION_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    variation_list: _containers.RepeatedCompositeFieldContainer[Variation]
    next_page_token: str
    def __init__(self, variation_list: _Optional[_Iterable[_Union[Variation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
