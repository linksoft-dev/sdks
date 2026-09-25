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

class Bomba(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "numero", "modelo", "num_serie", "tipo_medicao", "fields", "fabricante", "lacres", "intervencoes")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    MODELO_FIELD_NUMBER: _ClassVar[int]
    NUM_SERIE_FIELD_NUMBER: _ClassVar[int]
    TIPO_MEDICAO_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FABRICANTE_FIELD_NUMBER: _ClassVar[int]
    LACRES_FIELD_NUMBER: _ClassVar[int]
    INTERVENCOES_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    numero: str
    modelo: str
    num_serie: str
    tipo_medicao: str
    fields: _metadata_pb2.BasicFields
    fabricante: str
    lacres: _containers.RepeatedCompositeFieldContainer[Lacre]
    intervencoes: _containers.RepeatedCompositeFieldContainer[Intervencao]
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., numero: _Optional[str] = ..., modelo: _Optional[str] = ..., num_serie: _Optional[str] = ..., tipo_medicao: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., fabricante: _Optional[str] = ..., lacres: _Optional[_Iterable[_Union[Lacre, _Mapping]]] = ..., intervencoes: _Optional[_Iterable[_Union[Intervencao, _Mapping]]] = ...) -> None: ...

class Lacre(_message.Message):
    __slots__ = ("numero", "data_aplicacao")
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    DATA_APLICACAO_FIELD_NUMBER: _ClassVar[int]
    numero: str
    data_aplicacao: _timestamp_pb2.Timestamp
    def __init__(self, numero: _Optional[str] = ..., data_aplicacao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Intervencao(_message.Message):
    __slots__ = ("numero", "data_hora", "motivo", "tecnico_nome", "tecnico_cpf", "empresa_cnpj", "leituras")
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    TECNICO_NOME_FIELD_NUMBER: _ClassVar[int]
    TECNICO_CPF_FIELD_NUMBER: _ClassVar[int]
    EMPRESA_CNPJ_FIELD_NUMBER: _ClassVar[int]
    LEITURAS_FIELD_NUMBER: _ClassVar[int]
    numero: int
    data_hora: _timestamp_pb2.Timestamp
    motivo: str
    tecnico_nome: str
    tecnico_cpf: str
    empresa_cnpj: str
    leituras: _containers.RepeatedCompositeFieldContainer[LeituraIntervencao]
    def __init__(self, numero: _Optional[int] = ..., data_hora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., motivo: _Optional[str] = ..., tecnico_nome: _Optional[str] = ..., tecnico_cpf: _Optional[str] = ..., empresa_cnpj: _Optional[str] = ..., leituras: _Optional[_Iterable[_Union[LeituraIntervencao, _Mapping]]] = ...) -> None: ...

class LeituraIntervencao(_message.Message):
    __slots__ = ("numero_bico", "encerrante_antes", "encerrante_depois")
    NUMERO_BICO_FIELD_NUMBER: _ClassVar[int]
    ENCERRANTE_ANTES_FIELD_NUMBER: _ClassVar[int]
    ENCERRANTE_DEPOIS_FIELD_NUMBER: _ClassVar[int]
    numero_bico: int
    encerrante_antes: float
    encerrante_depois: float
    def __init__(self, numero_bico: _Optional[int] = ..., encerrante_antes: _Optional[float] = ..., encerrante_depois: _Optional[float] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("bomba",)
    BOMBA_FIELD_NUMBER: _ClassVar[int]
    bomba: Bomba
    def __init__(self, bomba: _Optional[_Union[Bomba, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("bomba",)
    BOMBA_FIELD_NUMBER: _ClassVar[int]
    bomba: Bomba
    def __init__(self, bomba: _Optional[_Union[Bomba, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "bomba", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    BOMBA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    bomba: Bomba
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., bomba: _Optional[_Union[Bomba, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("bomba",)
    BOMBA_FIELD_NUMBER: _ClassVar[int]
    bomba: Bomba
    def __init__(self, bomba: _Optional[_Union[Bomba, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("bomba",)
    BOMBA_FIELD_NUMBER: _ClassVar[int]
    bomba: Bomba
    def __init__(self, bomba: _Optional[_Union[Bomba, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
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

class ListResponse(_message.Message):
    __slots__ = ("bomba_list", "next_page_token")
    BOMBA_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    bomba_list: _containers.RepeatedCompositeFieldContainer[Bomba]
    next_page_token: str
    def __init__(self, bomba_list: _Optional[_Iterable[_Union[Bomba, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
