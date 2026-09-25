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

class Fabricante(_message.Message):
    __slots__ = ("id", "nome", "productsCount", "slug", "fields")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    PRODUCTSCOUNT_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    nome: str
    productsCount: int
    slug: str
    fields: _metadata_pb2.BasicFields
    def __init__(self, id: _Optional[str] = ..., nome: _Optional[str] = ..., productsCount: _Optional[int] = ..., slug: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ...) -> None: ...

class CreateFabricanteRequest(_message.Message):
    __slots__ = ("fabricante",)
    FABRICANTE_FIELD_NUMBER: _ClassVar[int]
    fabricante: Fabricante
    def __init__(self, fabricante: _Optional[_Union[Fabricante, _Mapping]] = ...) -> None: ...

class CreateFabricanteResponse(_message.Message):
    __slots__ = ("fabricante",)
    FABRICANTE_FIELD_NUMBER: _ClassVar[int]
    fabricante: Fabricante
    def __init__(self, fabricante: _Optional[_Union[Fabricante, _Mapping]] = ...) -> None: ...

class UpdateFabricanteRequest(_message.Message):
    __slots__ = ("id", "fabricante", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    FABRICANTE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    fabricante: Fabricante
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., fabricante: _Optional[_Union[Fabricante, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateFabricanteResponse(_message.Message):
    __slots__ = ("fabricante",)
    FABRICANTE_FIELD_NUMBER: _ClassVar[int]
    fabricante: Fabricante
    def __init__(self, fabricante: _Optional[_Union[Fabricante, _Mapping]] = ...) -> None: ...

class DeleteFabricanteRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteFabricanteResponse(_message.Message):
    __slots__ = ("id", "avisos")
    ID_FIELD_NUMBER: _ClassVar[int]
    AVISOS_FIELD_NUMBER: _ClassVar[int]
    id: str
    avisos: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., avisos: _Optional[_Iterable[str]] = ...) -> None: ...

class GetFabricanteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetFabricanteResponse(_message.Message):
    __slots__ = ("fabricante",)
    FABRICANTE_FIELD_NUMBER: _ClassVar[int]
    fabricante: Fabricante
    def __init__(self, fabricante: _Optional[_Union[Fabricante, _Mapping]] = ...) -> None: ...

class ListFabricanteRequest(_message.Message):
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

class ListFabricanteResponse(_message.Message):
    __slots__ = ("fabricanteList", "next_page_token")
    FABRICANTELIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    fabricanteList: _containers.RepeatedCompositeFieldContainer[Fabricante]
    next_page_token: str
    def __init__(self, fabricanteList: _Optional[_Iterable[_Union[Fabricante, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
