from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnpCodigo(_message.Message):
    __slots__ = ("id", "codigo", "descricao", "icms_monofasico", "unidade_monofasico", "percentual_biodiesel")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    ICMS_MONOFASICO_FIELD_NUMBER: _ClassVar[int]
    UNIDADE_MONOFASICO_FIELD_NUMBER: _ClassVar[int]
    PERCENTUAL_BIODIESEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    codigo: str
    descricao: str
    icms_monofasico: float
    unidade_monofasico: str
    percentual_biodiesel: float
    def __init__(self, id: _Optional[str] = ..., codigo: _Optional[str] = ..., descricao: _Optional[str] = ..., icms_monofasico: _Optional[float] = ..., unidade_monofasico: _Optional[str] = ..., percentual_biodiesel: _Optional[float] = ...) -> None: ...

class ListAnpRequest(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: _filter_pb2.Filter
    def __init__(self, filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListAnpResponse(_message.Message):
    __slots__ = ("anp_list",)
    ANP_LIST_FIELD_NUMBER: _ClassVar[int]
    anp_list: _containers.RepeatedCompositeFieldContainer[AnpCodigo]
    def __init__(self, anp_list: _Optional[_Iterable[_Union[AnpCodigo, _Mapping]]] = ...) -> None: ...
