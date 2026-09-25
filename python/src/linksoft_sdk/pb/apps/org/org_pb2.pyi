import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WhiteLabelStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WHITE_LABEL_STATUS_UNSPECIFIED: _ClassVar[WhiteLabelStatus]
    WHITE_LABEL_STATUS_INACTIVE: _ClassVar[WhiteLabelStatus]
    WHITE_LABEL_STATUS_PENDING_APPROVAL: _ClassVar[WhiteLabelStatus]
    WHITE_LABEL_STATUS_ACTIVE: _ClassVar[WhiteLabelStatus]
    WHITE_LABEL_STATUS_REJECTED: _ClassVar[WhiteLabelStatus]
    WHITE_LABEL_STATUS_SUSPENDED: _ClassVar[WhiteLabelStatus]
WHITE_LABEL_STATUS_UNSPECIFIED: WhiteLabelStatus
WHITE_LABEL_STATUS_INACTIVE: WhiteLabelStatus
WHITE_LABEL_STATUS_PENDING_APPROVAL: WhiteLabelStatus
WHITE_LABEL_STATUS_ACTIVE: WhiteLabelStatus
WHITE_LABEL_STATUS_REJECTED: WhiteLabelStatus
WHITE_LABEL_STATUS_SUSPENDED: WhiteLabelStatus

class WhiteLabelConfig(_message.Message):
    __slots__ = ("system_name", "logo_url", "logo_small_url", "domain", "site_url", "status", "favicon_url", "footer_text", "submitted_at", "review_note", "history")
    SYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    LOGO_SMALL_URL_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SITE_URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FAVICON_URL_FIELD_NUMBER: _ClassVar[int]
    FOOTER_TEXT_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    REVIEW_NOTE_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    system_name: str
    logo_url: str
    logo_small_url: str
    domain: str
    site_url: str
    status: WhiteLabelStatus
    favicon_url: str
    footer_text: str
    submitted_at: _timestamp_pb2.Timestamp
    review_note: str
    history: _containers.RepeatedCompositeFieldContainer[WhiteLabelHistoryEntry]
    def __init__(self, system_name: _Optional[str] = ..., logo_url: _Optional[str] = ..., logo_small_url: _Optional[str] = ..., domain: _Optional[str] = ..., site_url: _Optional[str] = ..., status: _Optional[_Union[WhiteLabelStatus, str]] = ..., favicon_url: _Optional[str] = ..., footer_text: _Optional[str] = ..., submitted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., review_note: _Optional[str] = ..., history: _Optional[_Iterable[_Union[WhiteLabelHistoryEntry, _Mapping]]] = ...) -> None: ...

class WhiteLabelHistoryEntry(_message.Message):
    __slots__ = ("at", "status", "actor_org_id", "actor_name", "note")
    AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    at: _timestamp_pb2.Timestamp
    status: WhiteLabelStatus
    actor_org_id: str
    actor_name: str
    note: str
    def __init__(self, at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[WhiteLabelStatus, str]] = ..., actor_org_id: _Optional[str] = ..., actor_name: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class LicencaDetalhe(_message.Message):
    __slots__ = ("situacao", "numero", "total", "vencimento", "modulos", "checkoutUrl")
    class ModulosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bool] = ...) -> None: ...
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    MODULOS_FIELD_NUMBER: _ClassVar[int]
    CHECKOUTURL_FIELD_NUMBER: _ClassVar[int]
    situacao: str
    numero: str
    total: float
    vencimento: _timestamp_pb2.Timestamp
    modulos: _containers.ScalarMap[str, bool]
    checkoutUrl: str
    def __init__(self, situacao: _Optional[str] = ..., numero: _Optional[str] = ..., total: _Optional[float] = ..., vencimento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modulos: _Optional[_Mapping[str, bool]] = ..., checkoutUrl: _Optional[str] = ...) -> None: ...

class Licenciamento(_message.Message):
    __slots__ = ("situacao", "numeroSerie", "total", "licenca", "modulos", "vencimento", "vencimentoAnterior", "diasExpirar", "checkoutUrl", "motivoBloqueio", "usuariosExtras", "licencas", "ai_credits_monthly", "planos", "periodicidade", "acessoAte", "quantidades")
    class ModulosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bool] = ...) -> None: ...
    class QuantidadesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    NUMEROSERIE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    LICENCA_FIELD_NUMBER: _ClassVar[int]
    MODULOS_FIELD_NUMBER: _ClassVar[int]
    VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    VENCIMENTOANTERIOR_FIELD_NUMBER: _ClassVar[int]
    DIASEXPIRAR_FIELD_NUMBER: _ClassVar[int]
    CHECKOUTURL_FIELD_NUMBER: _ClassVar[int]
    MOTIVOBLOQUEIO_FIELD_NUMBER: _ClassVar[int]
    USUARIOSEXTRAS_FIELD_NUMBER: _ClassVar[int]
    LICENCAS_FIELD_NUMBER: _ClassVar[int]
    AI_CREDITS_MONTHLY_FIELD_NUMBER: _ClassVar[int]
    PLANOS_FIELD_NUMBER: _ClassVar[int]
    PERIODICIDADE_FIELD_NUMBER: _ClassVar[int]
    ACESSOATE_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADES_FIELD_NUMBER: _ClassVar[int]
    situacao: str
    numeroSerie: str
    total: float
    licenca: str
    modulos: _containers.ScalarMap[str, bool]
    vencimento: _timestamp_pb2.Timestamp
    vencimentoAnterior: _timestamp_pb2.Timestamp
    diasExpirar: int
    checkoutUrl: str
    motivoBloqueio: str
    usuariosExtras: int
    licencas: _containers.RepeatedCompositeFieldContainer[LicencaDetalhe]
    ai_credits_monthly: int
    planos: _containers.RepeatedCompositeFieldContainer[LicencaPlano]
    periodicidade: str
    acessoAte: _timestamp_pb2.Timestamp
    quantidades: _containers.ScalarMap[str, int]
    def __init__(self, situacao: _Optional[str] = ..., numeroSerie: _Optional[str] = ..., total: _Optional[float] = ..., licenca: _Optional[str] = ..., modulos: _Optional[_Mapping[str, bool]] = ..., vencimento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., vencimentoAnterior: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., diasExpirar: _Optional[int] = ..., checkoutUrl: _Optional[str] = ..., motivoBloqueio: _Optional[str] = ..., usuariosExtras: _Optional[int] = ..., licencas: _Optional[_Iterable[_Union[LicencaDetalhe, _Mapping]]] = ..., ai_credits_monthly: _Optional[int] = ..., planos: _Optional[_Iterable[_Union[LicencaPlano, _Mapping]]] = ..., periodicidade: _Optional[str] = ..., acessoAte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., quantidades: _Optional[_Mapping[str, int]] = ...) -> None: ...

class LicencaPlano(_message.Message):
    __slots__ = ("nome", "codigo", "valor", "modulos")
    NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    MODULOS_FIELD_NUMBER: _ClassVar[int]
    nome: str
    codigo: str
    valor: float
    modulos: _containers.RepeatedCompositeFieldContainer[LicencaPlanoModulo]
    def __init__(self, nome: _Optional[str] = ..., codigo: _Optional[str] = ..., valor: _Optional[float] = ..., modulos: _Optional[_Iterable[_Union[LicencaPlanoModulo, _Mapping]]] = ...) -> None: ...

class LicencaPlanoModulo(_message.Message):
    __slots__ = ("codigo", "nome")
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    codigo: str
    nome: str
    def __init__(self, codigo: _Optional[str] = ..., nome: _Optional[str] = ...) -> None: ...
