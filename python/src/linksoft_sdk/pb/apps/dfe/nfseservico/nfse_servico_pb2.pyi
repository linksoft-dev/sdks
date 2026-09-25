from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListaNacional(_message.Message):
    __slots__ = ("item", "subitem", "desdobro_nacional", "codigo_tributacao_nacional")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    SUBITEM_FIELD_NUMBER: _ClassVar[int]
    DESDOBRO_NACIONAL_FIELD_NUMBER: _ClassVar[int]
    CODIGO_TRIBUTACAO_NACIONAL_FIELD_NUMBER: _ClassVar[int]
    item: str
    subitem: str
    desdobro_nacional: str
    codigo_tributacao_nacional: str
    def __init__(self, item: _Optional[str] = ..., subitem: _Optional[str] = ..., desdobro_nacional: _Optional[str] = ..., codigo_tributacao_nacional: _Optional[str] = ...) -> None: ...

class NBS(_message.Message):
    __slots__ = ("codigo", "descricao")
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    codigo: str
    descricao: str
    def __init__(self, codigo: _Optional[str] = ..., descricao: _Optional[str] = ...) -> None: ...

class Servico(_message.Message):
    __slots__ = ("id", "nome", "fields", "codigo", "cnaes", "lista_nacional", "nbs", "codigo_tributacao_municipal")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    CNAES_FIELD_NUMBER: _ClassVar[int]
    LISTA_NACIONAL_FIELD_NUMBER: _ClassVar[int]
    NBS_FIELD_NUMBER: _ClassVar[int]
    CODIGO_TRIBUTACAO_MUNICIPAL_FIELD_NUMBER: _ClassVar[int]
    id: str
    nome: str
    fields: _metadata_pb2.BasicFields
    codigo: str
    cnaes: _containers.RepeatedScalarFieldContainer[str]
    lista_nacional: ListaNacional
    nbs: NBS
    codigo_tributacao_municipal: str
    def __init__(self, id: _Optional[str] = ..., nome: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., codigo: _Optional[str] = ..., cnaes: _Optional[_Iterable[str]] = ..., lista_nacional: _Optional[_Union[ListaNacional, _Mapping]] = ..., nbs: _Optional[_Union[NBS, _Mapping]] = ..., codigo_tributacao_municipal: _Optional[str] = ...) -> None: ...

class CreateServicoRequest(_message.Message):
    __slots__ = ("servico",)
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    servico: Servico
    def __init__(self, servico: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...

class CreateServicoResponse(_message.Message):
    __slots__ = ("servico",)
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    servico: Servico
    def __init__(self, servico: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...

class UpdateServicoRequest(_message.Message):
    __slots__ = ("id", "servico", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    servico: Servico
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., servico: _Optional[_Union[Servico, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateServicoResponse(_message.Message):
    __slots__ = ("servico",)
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    servico: Servico
    def __init__(self, servico: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...

class DeleteServicoRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteServicoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListServicoRequest(_message.Message):
    __slots__ = ("ids", "cnaes", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    CNAES_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    cnaes: _containers.RepeatedScalarFieldContainer[str]
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., cnaes: _Optional[_Iterable[str]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListServicoResponse(_message.Message):
    __slots__ = ("servico_list",)
    SERVICO_LIST_FIELD_NUMBER: _ClassVar[int]
    servico_list: _containers.RepeatedCompositeFieldContainer[Servico]
    def __init__(self, servico_list: _Optional[_Iterable[_Union[Servico, _Mapping]]] = ...) -> None: ...

class GetServicoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetServicoResponse(_message.Message):
    __slots__ = ("servico",)
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    servico: Servico
    def __init__(self, servico: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...

class ImportServicoRequest(_message.Message):
    __slots__ = ("arquivoBase64", "substituir_existente")
    ARQUIVOBASE64_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUIR_EXISTENTE_FIELD_NUMBER: _ClassVar[int]
    arquivoBase64: str
    substituir_existente: bool
    def __init__(self, arquivoBase64: _Optional[str] = ..., substituir_existente: _Optional[bool] = ...) -> None: ...

class ImportServicoResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...
