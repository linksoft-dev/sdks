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

class Import(_message.Message):
    __slots__ = ("id", "name", "entity_type", "target_structure", "field_mapping", "active", "description")
    class FieldMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MAPPING_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    entity_type: str
    target_structure: str
    field_mapping: _containers.ScalarMap[str, str]
    active: bool
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., entity_type: _Optional[str] = ..., target_structure: _Optional[str] = ..., field_mapping: _Optional[_Mapping[str, str]] = ..., active: _Optional[bool] = ..., description: _Optional[str] = ...) -> None: ...

class CreateImportRequest(_message.Message):
    __slots__ = ()
    IMPORT_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, **kwargs) -> None: ...

class CreateImportResponse(_message.Message):
    __slots__ = ()
    IMPORT_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, **kwargs) -> None: ...

class UpdateImportRequest(_message.Message):
    __slots__ = ("id", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    IMPORT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ..., **kwargs) -> None: ...

class UpdateImportResponse(_message.Message):
    __slots__ = ()
    IMPORT_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, **kwargs) -> None: ...

class DeleteImportRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteImportResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetImportRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetImportResponse(_message.Message):
    __slots__ = ()
    IMPORT_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, **kwargs) -> None: ...

class ListImportRequest(_message.Message):
    __slots__ = ("ids", "page_size", "page_token", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListImportResponse(_message.Message):
    __slots__ = ("import_list", "next_page_token")
    IMPORT_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    import_list: _containers.RepeatedCompositeFieldContainer[Import]
    next_page_token: str
    def __init__(self, import_list: _Optional[_Iterable[_Union[Import, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
