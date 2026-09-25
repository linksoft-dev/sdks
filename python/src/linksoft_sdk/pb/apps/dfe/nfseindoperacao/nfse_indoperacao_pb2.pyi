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

class IndOperacao(_message.Message):
    __slots__ = ("id", "fields", "art_11", "tipo_operacao", "local_operacao", "caracteristica_fornecimento", "codigo_indop", "local_fornecimento_dfe")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ART_11_FIELD_NUMBER: _ClassVar[int]
    TIPO_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    LOCAL_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    CARACTERISTICA_FORNECIMENTO_FIELD_NUMBER: _ClassVar[int]
    CODIGO_INDOP_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FORNECIMENTO_DFE_FIELD_NUMBER: _ClassVar[int]
    id: str
    fields: _metadata_pb2.BasicFields
    art_11: str
    tipo_operacao: str
    local_operacao: str
    caracteristica_fornecimento: str
    codigo_indop: str
    local_fornecimento_dfe: str
    def __init__(self, id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., art_11: _Optional[str] = ..., tipo_operacao: _Optional[str] = ..., local_operacao: _Optional[str] = ..., caracteristica_fornecimento: _Optional[str] = ..., codigo_indop: _Optional[str] = ..., local_fornecimento_dfe: _Optional[str] = ...) -> None: ...

class CreateIndOperacaoRequest(_message.Message):
    __slots__ = ("ind_operacao",)
    IND_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    ind_operacao: IndOperacao
    def __init__(self, ind_operacao: _Optional[_Union[IndOperacao, _Mapping]] = ...) -> None: ...

class CreateIndOperacaoResponse(_message.Message):
    __slots__ = ("ind_operacao",)
    IND_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    ind_operacao: IndOperacao
    def __init__(self, ind_operacao: _Optional[_Union[IndOperacao, _Mapping]] = ...) -> None: ...

class UpdateIndOperacaoRequest(_message.Message):
    __slots__ = ("id", "ind_operacao", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    IND_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    ind_operacao: IndOperacao
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., ind_operacao: _Optional[_Union[IndOperacao, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateIndOperacaoResponse(_message.Message):
    __slots__ = ("ind_operacao",)
    IND_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    ind_operacao: IndOperacao
    def __init__(self, ind_operacao: _Optional[_Union[IndOperacao, _Mapping]] = ...) -> None: ...

class DeleteIndOperacaoRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteIndOperacaoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListIndOperacaoRequest(_message.Message):
    __slots__ = ("ids", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListIndOperacaoResponse(_message.Message):
    __slots__ = ("ind_operacao_list",)
    IND_OPERACAO_LIST_FIELD_NUMBER: _ClassVar[int]
    ind_operacao_list: _containers.RepeatedCompositeFieldContainer[IndOperacao]
    def __init__(self, ind_operacao_list: _Optional[_Iterable[_Union[IndOperacao, _Mapping]]] = ...) -> None: ...

class GetIndOperacaoRequest(_message.Message):
    __slots__ = ("id", "codigo_indop")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODIGO_INDOP_FIELD_NUMBER: _ClassVar[int]
    id: str
    codigo_indop: str
    def __init__(self, id: _Optional[str] = ..., codigo_indop: _Optional[str] = ...) -> None: ...

class GetIndOperacaoResponse(_message.Message):
    __slots__ = ("ind_operacao",)
    IND_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    ind_operacao: IndOperacao
    def __init__(self, ind_operacao: _Optional[_Union[IndOperacao, _Mapping]] = ...) -> None: ...

class ImportIndOperacaoRequest(_message.Message):
    __slots__ = ("arquivo_base64",)
    ARQUIVO_BASE64_FIELD_NUMBER: _ClassVar[int]
    arquivo_base64: str
    def __init__(self, arquivo_base64: _Optional[str] = ...) -> None: ...

class ImportIndOperacaoResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...
