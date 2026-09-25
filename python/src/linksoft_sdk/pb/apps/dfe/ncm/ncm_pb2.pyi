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

class StatusNcm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ATIVO: _ClassVar[StatusNcm]
    DESCONTINUADO: _ClassVar[StatusNcm]
ATIVO: StatusNcm
DESCONTINUADO: StatusNcm

class CreateNcmRequest(_message.Message):
    __slots__ = ("ncm",)
    NCM_FIELD_NUMBER: _ClassVar[int]
    ncm: Ncm
    def __init__(self, ncm: _Optional[_Union[Ncm, _Mapping]] = ...) -> None: ...

class CreateNcmResponse(_message.Message):
    __slots__ = ("ncm",)
    NCM_FIELD_NUMBER: _ClassVar[int]
    ncm: Ncm
    def __init__(self, ncm: _Optional[_Union[Ncm, _Mapping]] = ...) -> None: ...

class UpdateNcmRequest(_message.Message):
    __slots__ = ("id", "ncm", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    NCM_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    ncm: Ncm
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., ncm: _Optional[_Union[Ncm, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateNcmResponse(_message.Message):
    __slots__ = ("ncm",)
    NCM_FIELD_NUMBER: _ClassVar[int]
    ncm: Ncm
    def __init__(self, ncm: _Optional[_Union[Ncm, _Mapping]] = ...) -> None: ...

class ListNcmRequest(_message.Message):
    __slots__ = ("ids", "ncm", "tributacao_id", "filter", "skip_ibpt_auto_register")
    IDS_FIELD_NUMBER: _ClassVar[int]
    NCM_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAO_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SKIP_IBPT_AUTO_REGISTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    ncm: _containers.RepeatedScalarFieldContainer[str]
    tributacao_id: str
    filter: _filter_pb2.Filter
    skip_ibpt_auto_register: bool
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., ncm: _Optional[_Iterable[str]] = ..., tributacao_id: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., skip_ibpt_auto_register: _Optional[bool] = ...) -> None: ...

class ListNcmResponse(_message.Message):
    __slots__ = ("ncmList",)
    NCMLIST_FIELD_NUMBER: _ClassVar[int]
    ncmList: _containers.RepeatedCompositeFieldContainer[Ncm]
    def __init__(self, ncmList: _Optional[_Iterable[_Union[Ncm, _Mapping]]] = ...) -> None: ...

class GetNcmRequest(_message.Message):
    __slots__ = ("id", "codigo")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    id: str
    codigo: str
    def __init__(self, id: _Optional[str] = ..., codigo: _Optional[str] = ...) -> None: ...

class GetNcmResponse(_message.Message):
    __slots__ = ("ncm",)
    NCM_FIELD_NUMBER: _ClassVar[int]
    ncm: Ncm
    def __init__(self, ncm: _Optional[_Union[Ncm, _Mapping]] = ...) -> None: ...

class ImportaTabelaRequest(_message.Message):
    __slots__ = ("file_string",)
    FILE_STRING_FIELD_NUMBER: _ClassVar[int]
    file_string: str
    def __init__(self, file_string: _Optional[str] = ...) -> None: ...

class ImportaTabelaResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class ConsultarIbptRequest(_message.Message):
    __slots__ = ("codigo", "uf")
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    UF_FIELD_NUMBER: _ClassVar[int]
    codigo: str
    uf: str
    def __init__(self, codigo: _Optional[str] = ..., uf: _Optional[str] = ...) -> None: ...

class ConsultarIbptResponse(_message.Message):
    __slots__ = ("codigo", "uf", "descricao", "aliquota_federal", "aliquota_federal_importados", "aliquota_estadual", "aliquota_municipal", "tipo", "vigencia_inicio", "vigencia_fim", "chave", "versao", "fonte")
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    UF_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_FEDERAL_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_FEDERAL_IMPORTADOS_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_ESTADUAL_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_MUNICIPAL_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    VIGENCIA_INICIO_FIELD_NUMBER: _ClassVar[int]
    VIGENCIA_FIM_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    VERSAO_FIELD_NUMBER: _ClassVar[int]
    FONTE_FIELD_NUMBER: _ClassVar[int]
    codigo: str
    uf: str
    descricao: str
    aliquota_federal: float
    aliquota_federal_importados: float
    aliquota_estadual: float
    aliquota_municipal: float
    tipo: str
    vigencia_inicio: _timestamp_pb2.Timestamp
    vigencia_fim: _timestamp_pb2.Timestamp
    chave: str
    versao: str
    fonte: str
    def __init__(self, codigo: _Optional[str] = ..., uf: _Optional[str] = ..., descricao: _Optional[str] = ..., aliquota_federal: _Optional[float] = ..., aliquota_federal_importados: _Optional[float] = ..., aliquota_estadual: _Optional[float] = ..., aliquota_municipal: _Optional[float] = ..., tipo: _Optional[str] = ..., vigencia_inicio: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., vigencia_fim: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., chave: _Optional[str] = ..., versao: _Optional[str] = ..., fonte: _Optional[str] = ...) -> None: ...

class SincronizaTabelaOficialRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SincronizaTabelaOficialResponse(_message.Message):
    __slots__ = ("ato", "vigentes_oficiais", "cadastrados", "descontinuados", "reativados", "atualizados", "resultado")
    ATO_FIELD_NUMBER: _ClassVar[int]
    VIGENTES_OFICIAIS_FIELD_NUMBER: _ClassVar[int]
    CADASTRADOS_FIELD_NUMBER: _ClassVar[int]
    DESCONTINUADOS_FIELD_NUMBER: _ClassVar[int]
    REATIVADOS_FIELD_NUMBER: _ClassVar[int]
    ATUALIZADOS_FIELD_NUMBER: _ClassVar[int]
    RESULTADO_FIELD_NUMBER: _ClassVar[int]
    ato: str
    vigentes_oficiais: int
    cadastrados: int
    descontinuados: int
    reativados: int
    atualizados: int
    resultado: str
    def __init__(self, ato: _Optional[str] = ..., vigentes_oficiais: _Optional[int] = ..., cadastrados: _Optional[int] = ..., descontinuados: _Optional[int] = ..., reativados: _Optional[int] = ..., atualizados: _Optional[int] = ..., resultado: _Optional[str] = ...) -> None: ...

class NcmSubstituto(_message.Message):
    __slots__ = ("codigo", "descricao")
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    codigo: str
    descricao: str
    def __init__(self, codigo: _Optional[str] = ..., descricao: _Optional[str] = ...) -> None: ...

class Ncm(_message.Message):
    __slots__ = ("id", "descricao", "categoria", "codigo", "padrao", "aliquota_federal_importados", "aliquota_federal", "aliquota_estadual", "aliquota_municipal", "tributacao_id", "tributacao_nome", "codigo_cest", "un_trib", "un_trib_descricao", "ipi", "obs", "inicio_virgencia", "fim_virgencia", "gtin_producao", "gtin_homologacao", "cadastrado_automaticamente", "status", "substitutos", "aliquotas_consultadas_em")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    PADRAO_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_FEDERAL_IMPORTADOS_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_FEDERAL_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_ESTADUAL_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_MUNICIPAL_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAO_ID_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAO_NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_CEST_FIELD_NUMBER: _ClassVar[int]
    UN_TRIB_FIELD_NUMBER: _ClassVar[int]
    UN_TRIB_DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    IPI_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    INICIO_VIRGENCIA_FIELD_NUMBER: _ClassVar[int]
    FIM_VIRGENCIA_FIELD_NUMBER: _ClassVar[int]
    GTIN_PRODUCAO_FIELD_NUMBER: _ClassVar[int]
    GTIN_HOMOLOGACAO_FIELD_NUMBER: _ClassVar[int]
    CADASTRADO_AUTOMATICAMENTE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTOS_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTAS_CONSULTADAS_EM_FIELD_NUMBER: _ClassVar[int]
    id: str
    descricao: str
    categoria: str
    codigo: str
    padrao: bool
    aliquota_federal_importados: float
    aliquota_federal: float
    aliquota_estadual: float
    aliquota_municipal: float
    tributacao_id: str
    tributacao_nome: str
    codigo_cest: str
    un_trib: str
    un_trib_descricao: str
    ipi: str
    obs: str
    inicio_virgencia: _timestamp_pb2.Timestamp
    fim_virgencia: _timestamp_pb2.Timestamp
    gtin_producao: _timestamp_pb2.Timestamp
    gtin_homologacao: _timestamp_pb2.Timestamp
    cadastrado_automaticamente: bool
    status: StatusNcm
    substitutos: _containers.RepeatedCompositeFieldContainer[NcmSubstituto]
    aliquotas_consultadas_em: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., descricao: _Optional[str] = ..., categoria: _Optional[str] = ..., codigo: _Optional[str] = ..., padrao: _Optional[bool] = ..., aliquota_federal_importados: _Optional[float] = ..., aliquota_federal: _Optional[float] = ..., aliquota_estadual: _Optional[float] = ..., aliquota_municipal: _Optional[float] = ..., tributacao_id: _Optional[str] = ..., tributacao_nome: _Optional[str] = ..., codigo_cest: _Optional[str] = ..., un_trib: _Optional[str] = ..., un_trib_descricao: _Optional[str] = ..., ipi: _Optional[str] = ..., obs: _Optional[str] = ..., inicio_virgencia: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., fim_virgencia: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., gtin_producao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., gtin_homologacao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cadastrado_automaticamente: _Optional[bool] = ..., status: _Optional[_Union[StatusNcm, str]] = ..., substitutos: _Optional[_Iterable[_Union[NcmSubstituto, _Mapping]]] = ..., aliquotas_consultadas_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
