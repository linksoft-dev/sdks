import datetime

from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Situacao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SITUACAO_UNSPECIFIED: _ClassVar[Situacao]
    SITUACAO_ATIVO: _ClassVar[Situacao]
    SITUACAO_INATIVO: _ClassVar[Situacao]

class TipoGrupo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_GRUPO_UNSPECIFIED: _ClassVar[TipoGrupo]
    TIPO_GRUPO_CLIENTE: _ClassVar[TipoGrupo]
    TIPO_GRUPO_VENDEDOR: _ClassVar[TipoGrupo]

class Agenda(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENDA_UNSPECIFIED: _ClassVar[Agenda]
    AGENDA_RELATIVA: _ClassVar[Agenda]
    AGENDA_DIA_DO_MES: _ClassVar[Agenda]

class Canal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CANAL_UNSPECIFIED: _ClassVar[Canal]
    CANAL_EMAIL: _ClassVar[Canal]
    CANAL_WHATSAPP: _ClassVar[Canal]
    CANAL_SMS: _ClassVar[Canal]
SITUACAO_UNSPECIFIED: Situacao
SITUACAO_ATIVO: Situacao
SITUACAO_INATIVO: Situacao
TIPO_GRUPO_UNSPECIFIED: TipoGrupo
TIPO_GRUPO_CLIENTE: TipoGrupo
TIPO_GRUPO_VENDEDOR: TipoGrupo
AGENDA_UNSPECIFIED: Agenda
AGENDA_RELATIVA: Agenda
AGENDA_DIA_DO_MES: Agenda
CANAL_UNSPECIFIED: Canal
CANAL_EMAIL: Canal
CANAL_WHATSAPP: Canal
CANAL_SMS: Canal

class BillingPlan(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "fields", "name", "start_days", "interval_days", "max_billings", "situacao", "tipo_documento", "tipo_grupo", "grupo_id", "grupo_nome", "pessoa_id", "pessoa_nome", "agenda", "dias_do_mes", "cobrar_a_partir_de", "canais", "email_integration_id", "whatsapp_integration_id", "dias_limite", "pular_fim_de_semana", "pular_feriados", "hora", "tags", "valor_minimo", "valor_maximo", "anexos", "sms_integration_id", "dias_de_envio")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_DAYS_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_DAYS_FIELD_NUMBER: _ClassVar[int]
    MAX_BILLINGS_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    TIPO_DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    TIPO_GRUPO_FIELD_NUMBER: _ClassVar[int]
    GRUPO_ID_FIELD_NUMBER: _ClassVar[int]
    GRUPO_NOME_FIELD_NUMBER: _ClassVar[int]
    PESSOA_ID_FIELD_NUMBER: _ClassVar[int]
    PESSOA_NOME_FIELD_NUMBER: _ClassVar[int]
    AGENDA_FIELD_NUMBER: _ClassVar[int]
    DIAS_DO_MES_FIELD_NUMBER: _ClassVar[int]
    COBRAR_A_PARTIR_DE_FIELD_NUMBER: _ClassVar[int]
    CANAIS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    DIAS_LIMITE_FIELD_NUMBER: _ClassVar[int]
    PULAR_FIM_DE_SEMANA_FIELD_NUMBER: _ClassVar[int]
    PULAR_FERIADOS_FIELD_NUMBER: _ClassVar[int]
    HORA_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    VALOR_MINIMO_FIELD_NUMBER: _ClassVar[int]
    VALOR_MAXIMO_FIELD_NUMBER: _ClassVar[int]
    ANEXOS_FIELD_NUMBER: _ClassVar[int]
    SMS_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    DIAS_DE_ENVIO_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    fields: _metadata_pb2.BasicFields
    name: str
    start_days: int
    interval_days: int
    max_billings: int
    situacao: Situacao
    tipo_documento: str
    tipo_grupo: TipoGrupo
    grupo_id: str
    grupo_nome: str
    pessoa_id: str
    pessoa_nome: str
    agenda: Agenda
    dias_do_mes: _containers.RepeatedScalarFieldContainer[int]
    cobrar_a_partir_de: _timestamp_pb2.Timestamp
    canais: _containers.RepeatedScalarFieldContainer[Canal]
    email_integration_id: str
    whatsapp_integration_id: str
    dias_limite: int
    pular_fim_de_semana: bool
    pular_feriados: bool
    hora: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    valor_minimo: float
    valor_maximo: float
    anexos: _containers.RepeatedScalarFieldContainer[str]
    sms_integration_id: str
    dias_de_envio: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., name: _Optional[str] = ..., start_days: _Optional[int] = ..., interval_days: _Optional[int] = ..., max_billings: _Optional[int] = ..., situacao: _Optional[_Union[Situacao, str]] = ..., tipo_documento: _Optional[str] = ..., tipo_grupo: _Optional[_Union[TipoGrupo, str]] = ..., grupo_id: _Optional[str] = ..., grupo_nome: _Optional[str] = ..., pessoa_id: _Optional[str] = ..., pessoa_nome: _Optional[str] = ..., agenda: _Optional[_Union[Agenda, str]] = ..., dias_do_mes: _Optional[_Iterable[int]] = ..., cobrar_a_partir_de: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., canais: _Optional[_Iterable[_Union[Canal, str]]] = ..., email_integration_id: _Optional[str] = ..., whatsapp_integration_id: _Optional[str] = ..., dias_limite: _Optional[int] = ..., pular_fim_de_semana: _Optional[bool] = ..., pular_feriados: _Optional[bool] = ..., hora: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ..., valor_minimo: _Optional[float] = ..., valor_maximo: _Optional[float] = ..., anexos: _Optional[_Iterable[str]] = ..., sms_integration_id: _Optional[str] = ..., dias_de_envio: _Optional[_Iterable[int]] = ...) -> None: ...
