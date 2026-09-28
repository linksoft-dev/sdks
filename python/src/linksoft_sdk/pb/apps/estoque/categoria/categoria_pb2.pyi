from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCategoriaRequest(_message.Message):
    __slots__ = ("categoria",)
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    categoria: Categoria
    def __init__(self, categoria: _Optional[_Union[Categoria, _Mapping]] = ...) -> None: ...

class CreateCategoriaResponse(_message.Message):
    __slots__ = ("categoria",)
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    categoria: Categoria
    def __init__(self, categoria: _Optional[_Union[Categoria, _Mapping]] = ...) -> None: ...

class UpdateCategoriaRequest(_message.Message):
    __slots__ = ("id", "categoria", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    categoria: Categoria
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., categoria: _Optional[_Union[Categoria, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCategoriaResponse(_message.Message):
    __slots__ = ("categoria",)
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    categoria: Categoria
    def __init__(self, categoria: _Optional[_Union[Categoria, _Mapping]] = ...) -> None: ...

class DeleteCategoriaRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteCategoriaResponse(_message.Message):
    __slots__ = ("avisos",)
    AVISOS_FIELD_NUMBER: _ClassVar[int]
    avisos: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, avisos: _Optional[_Iterable[str]] = ...) -> None: ...

class ListCategoriaRequest(_message.Message):
    __slots__ = ("ids", "nome", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    nome: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., nome: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListCategoriaResponse(_message.Message):
    __slots__ = ("categoriaList",)
    CATEGORIALIST_FIELD_NUMBER: _ClassVar[int]
    categoriaList: _containers.RepeatedCompositeFieldContainer[Categoria]
    def __init__(self, categoriaList: _Optional[_Iterable[_Union[Categoria, _Mapping]]] = ...) -> None: ...

class GetCategoriaRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCategoriaResponse(_message.Message):
    __slots__ = ("categoria",)
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    categoria: Categoria
    def __init__(self, categoria: _Optional[_Union[Categoria, _Mapping]] = ...) -> None: ...

class Categoria(_message.Message):
    __slots__ = ("id", "nome", "tributacaoId", "tributacaoNome", "tributacaoRevendaId", "tributacaoRevendaNome", "ncm", "quantidadeMinima", "quantidadeMaxima", "margemLucroPadrao", "productsCount", "ecommerce_available", "image_url", "code", "slug", "grupoProducao", "impressoraId", "impressoraNome", "tags", "fields")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAOID_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAONOME_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAOREVENDAID_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAOREVENDANOME_FIELD_NUMBER: _ClassVar[int]
    NCM_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADEMINIMA_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADEMAXIMA_FIELD_NUMBER: _ClassVar[int]
    MARGEMLUCROPADRAO_FIELD_NUMBER: _ClassVar[int]
    PRODUCTSCOUNT_FIELD_NUMBER: _ClassVar[int]
    ECOMMERCE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    GRUPOPRODUCAO_FIELD_NUMBER: _ClassVar[int]
    IMPRESSORAID_FIELD_NUMBER: _ClassVar[int]
    IMPRESSORANOME_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    nome: str
    tributacaoId: str
    tributacaoNome: str
    tributacaoRevendaId: str
    tributacaoRevendaNome: str
    ncm: str
    quantidadeMinima: float
    quantidadeMaxima: float
    margemLucroPadrao: float
    productsCount: int
    ecommerce_available: bool
    image_url: str
    code: str
    slug: str
    grupoProducao: str
    impressoraId: str
    impressoraNome: str
    tags: _containers.RepeatedCompositeFieldContainer[CategoriaTag]
    fields: _metadata_pb2.BasicFields
    def __init__(self, id: _Optional[str] = ..., nome: _Optional[str] = ..., tributacaoId: _Optional[str] = ..., tributacaoNome: _Optional[str] = ..., tributacaoRevendaId: _Optional[str] = ..., tributacaoRevendaNome: _Optional[str] = ..., ncm: _Optional[str] = ..., quantidadeMinima: _Optional[float] = ..., quantidadeMaxima: _Optional[float] = ..., margemLucroPadrao: _Optional[float] = ..., productsCount: _Optional[int] = ..., ecommerce_available: _Optional[bool] = ..., image_url: _Optional[str] = ..., code: _Optional[str] = ..., slug: _Optional[str] = ..., grupoProducao: _Optional[str] = ..., impressoraId: _Optional[str] = ..., impressoraNome: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[CategoriaTag, _Mapping]]] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ...) -> None: ...

class CategoriaTag(_message.Message):
    __slots__ = ("value", "color")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    value: str
    color: str
    def __init__(self, value: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...
