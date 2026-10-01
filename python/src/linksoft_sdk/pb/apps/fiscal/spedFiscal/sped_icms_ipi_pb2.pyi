import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FinalidadeArquivo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FINALIDADE_ARQUIVO_UNSPECIFIED: _ClassVar[FinalidadeArquivo]
    FINALIDADE_ARQUIVO_ORIGINAL: _ClassVar[FinalidadeArquivo]
    FINALIDADE_ARQUIVO_RETIFICACAO: _ClassVar[FinalidadeArquivo]

class CriterioInclusaoNf(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CRITERIO_INCLUSAO_NF_UNSPECIFIED: _ClassVar[CriterioInclusaoNf]
    CRITERIO_INCLUSAO_NF_ACEITACAO: _ClassVar[CriterioInclusaoNf]
    CRITERIO_INCLUSAO_NF_EMISSAO: _ClassVar[CriterioInclusaoNf]

class SituacaoNfEntrada(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SITUACAO_NF_ENTRADA_UNSPECIFIED: _ClassVar[SituacaoNfEntrada]
    SITUACAO_NF_ENTRADA_ACEITAS: _ClassVar[SituacaoNfEntrada]
    SITUACAO_NF_ENTRADA_TODAS: _ClassVar[SituacaoNfEntrada]

class LeiauteBlocoK(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LEIAUTE_BLOCO_K_UNSPECIFIED: _ClassVar[LeiauteBlocoK]
    LEIAUTE_BLOCO_K_COMPLETO: _ClassVar[LeiauteBlocoK]
    LEIAUTE_BLOCO_K_SIMPLIFICADO: _ClassVar[LeiauteBlocoK]
FINALIDADE_ARQUIVO_UNSPECIFIED: FinalidadeArquivo
FINALIDADE_ARQUIVO_ORIGINAL: FinalidadeArquivo
FINALIDADE_ARQUIVO_RETIFICACAO: FinalidadeArquivo
CRITERIO_INCLUSAO_NF_UNSPECIFIED: CriterioInclusaoNf
CRITERIO_INCLUSAO_NF_ACEITACAO: CriterioInclusaoNf
CRITERIO_INCLUSAO_NF_EMISSAO: CriterioInclusaoNf
SITUACAO_NF_ENTRADA_UNSPECIFIED: SituacaoNfEntrada
SITUACAO_NF_ENTRADA_ACEITAS: SituacaoNfEntrada
SITUACAO_NF_ENTRADA_TODAS: SituacaoNfEntrada
LEIAUTE_BLOCO_K_UNSPECIFIED: LeiauteBlocoK
LEIAUTE_BLOCO_K_COMPLETO: LeiauteBlocoK
LEIAUTE_BLOCO_K_SIMPLIFICADO: LeiauteBlocoK

class SpedFiscal(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "auto_create", "mes", "ano", "finalidade", "arquivo_nome", "arquivo_file_path", "inventario_id", "inventario_nome", "criterio_inclusao_nf", "situacao_nf_entrada", "leiaute_bloco_k")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_CREATE_FIELD_NUMBER: _ClassVar[int]
    MES_FIELD_NUMBER: _ClassVar[int]
    ANO_FIELD_NUMBER: _ClassVar[int]
    FINALIDADE_FIELD_NUMBER: _ClassVar[int]
    ARQUIVO_NOME_FIELD_NUMBER: _ClassVar[int]
    ARQUIVO_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    INVENTARIO_ID_FIELD_NUMBER: _ClassVar[int]
    INVENTARIO_NOME_FIELD_NUMBER: _ClassVar[int]
    CRITERIO_INCLUSAO_NF_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_NF_ENTRADA_FIELD_NUMBER: _ClassVar[int]
    LEIAUTE_BLOCO_K_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    auto_create: bool
    mes: int
    ano: int
    finalidade: FinalidadeArquivo
    arquivo_nome: str
    arquivo_file_path: str
    inventario_id: str
    inventario_nome: str
    criterio_inclusao_nf: CriterioInclusaoNf
    situacao_nf_entrada: SituacaoNfEntrada
    leiaute_bloco_k: LeiauteBlocoK
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., auto_create: _Optional[bool] = ..., mes: _Optional[int] = ..., ano: _Optional[int] = ..., finalidade: _Optional[_Union[FinalidadeArquivo, str]] = ..., arquivo_nome: _Optional[str] = ..., arquivo_file_path: _Optional[str] = ..., inventario_id: _Optional[str] = ..., inventario_nome: _Optional[str] = ..., criterio_inclusao_nf: _Optional[_Union[CriterioInclusaoNf, str]] = ..., situacao_nf_entrada: _Optional[_Union[SituacaoNfEntrada, str]] = ..., leiaute_bloco_k: _Optional[_Union[LeiauteBlocoK, str]] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("sped_fiscal",)
    SPED_FISCAL_FIELD_NUMBER: _ClassVar[int]
    sped_fiscal: SpedFiscal
    def __init__(self, sped_fiscal: _Optional[_Union[SpedFiscal, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("sped_fiscal",)
    SPED_FISCAL_FIELD_NUMBER: _ClassVar[int]
    sped_fiscal: SpedFiscal
    def __init__(self, sped_fiscal: _Optional[_Union[SpedFiscal, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "sped_fiscal", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPED_FISCAL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    sped_fiscal: SpedFiscal
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., sped_fiscal: _Optional[_Union[SpedFiscal, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("sped_fiscal",)
    SPED_FISCAL_FIELD_NUMBER: _ClassVar[int]
    sped_fiscal: SpedFiscal
    def __init__(self, sped_fiscal: _Optional[_Union[SpedFiscal, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("sped_fiscal",)
    SPED_FISCAL_FIELD_NUMBER: _ClassVar[int]
    sped_fiscal: SpedFiscal
    def __init__(self, sped_fiscal: _Optional[_Union[SpedFiscal, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("sped_fiscal_list", "next_page_token")
    SPED_FISCAL_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sped_fiscal_list: _containers.RepeatedCompositeFieldContainer[SpedFiscal]
    next_page_token: str
    def __init__(self, sped_fiscal_list: _Optional[_Iterable[_Union[SpedFiscal, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GeraRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GeraResponse(_message.Message):
    __slots__ = ("sped_fiscal", "avisos")
    SPED_FISCAL_FIELD_NUMBER: _ClassVar[int]
    AVISOS_FIELD_NUMBER: _ClassVar[int]
    sped_fiscal: SpedFiscal
    avisos: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, sped_fiscal: _Optional[_Union[SpedFiscal, _Mapping]] = ..., avisos: _Optional[_Iterable[str]] = ...) -> None: ...

class EnviarEmailRequest(_message.Message):
    __slots__ = ("id", "email", "nome_destinatario", "automatico")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NOME_DESTINATARIO_FIELD_NUMBER: _ClassVar[int]
    AUTOMATICO_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    nome_destinatario: str
    automatico: bool
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., nome_destinatario: _Optional[str] = ..., automatico: _Optional[bool] = ...) -> None: ...

class EnviarEmailResponse(_message.Message):
    __slots__ = ("sped_fiscal",)
    SPED_FISCAL_FIELD_NUMBER: _ClassVar[int]
    sped_fiscal: SpedFiscal
    def __init__(self, sped_fiscal: _Optional[_Union[SpedFiscal, _Mapping]] = ...) -> None: ...
