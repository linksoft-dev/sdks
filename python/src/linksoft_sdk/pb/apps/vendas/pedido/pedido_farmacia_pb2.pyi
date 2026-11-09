import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Farmacia(_message.Message):
    __slots__ = ("receita",)
    RECEITA_FIELD_NUMBER: _ClassVar[int]
    receita: FarmaciaReceita
    def __init__(self, receita: _Optional[_Union[FarmaciaReceita, _Mapping]] = ...) -> None: ...

class FarmaciaReceita(_message.Message):
    __slots__ = ("tipo_receituario", "numero_notificacao", "data_prescricao", "prescritor_nome", "prescritor_registro", "prescritor_conselho", "prescritor_uf", "uso", "comprador_nome", "comprador_tipo_documento", "comprador_documento", "comprador_orgao_expedidor", "comprador_uf_documento", "paciente_nome", "paciente_idade", "paciente_unidade_idade", "paciente_sexo", "paciente_cid", "uso_prolongado")
    TIPO_RECEITUARIO_FIELD_NUMBER: _ClassVar[int]
    NUMERO_NOTIFICACAO_FIELD_NUMBER: _ClassVar[int]
    DATA_PRESCRICAO_FIELD_NUMBER: _ClassVar[int]
    PRESCRITOR_NOME_FIELD_NUMBER: _ClassVar[int]
    PRESCRITOR_REGISTRO_FIELD_NUMBER: _ClassVar[int]
    PRESCRITOR_CONSELHO_FIELD_NUMBER: _ClassVar[int]
    PRESCRITOR_UF_FIELD_NUMBER: _ClassVar[int]
    USO_FIELD_NUMBER: _ClassVar[int]
    COMPRADOR_NOME_FIELD_NUMBER: _ClassVar[int]
    COMPRADOR_TIPO_DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    COMPRADOR_DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    COMPRADOR_ORGAO_EXPEDIDOR_FIELD_NUMBER: _ClassVar[int]
    COMPRADOR_UF_DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    PACIENTE_NOME_FIELD_NUMBER: _ClassVar[int]
    PACIENTE_IDADE_FIELD_NUMBER: _ClassVar[int]
    PACIENTE_UNIDADE_IDADE_FIELD_NUMBER: _ClassVar[int]
    PACIENTE_SEXO_FIELD_NUMBER: _ClassVar[int]
    PACIENTE_CID_FIELD_NUMBER: _ClassVar[int]
    USO_PROLONGADO_FIELD_NUMBER: _ClassVar[int]
    tipo_receituario: int
    numero_notificacao: str
    data_prescricao: _timestamp_pb2.Timestamp
    prescritor_nome: str
    prescritor_registro: str
    prescritor_conselho: str
    prescritor_uf: str
    uso: int
    comprador_nome: str
    comprador_tipo_documento: int
    comprador_documento: str
    comprador_orgao_expedidor: str
    comprador_uf_documento: str
    paciente_nome: str
    paciente_idade: int
    paciente_unidade_idade: int
    paciente_sexo: int
    paciente_cid: str
    uso_prolongado: bool
    def __init__(self, tipo_receituario: _Optional[int] = ..., numero_notificacao: _Optional[str] = ..., data_prescricao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., prescritor_nome: _Optional[str] = ..., prescritor_registro: _Optional[str] = ..., prescritor_conselho: _Optional[str] = ..., prescritor_uf: _Optional[str] = ..., uso: _Optional[int] = ..., comprador_nome: _Optional[str] = ..., comprador_tipo_documento: _Optional[int] = ..., comprador_documento: _Optional[str] = ..., comprador_orgao_expedidor: _Optional[str] = ..., comprador_uf_documento: _Optional[str] = ..., paciente_nome: _Optional[str] = ..., paciente_idade: _Optional[int] = ..., paciente_unidade_idade: _Optional[int] = ..., paciente_sexo: _Optional[int] = ..., paciente_cid: _Optional[str] = ..., uso_prolongado: _Optional[bool] = ...) -> None: ...
