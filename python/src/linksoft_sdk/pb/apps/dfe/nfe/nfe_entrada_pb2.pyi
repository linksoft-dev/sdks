import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.apps.dfe.nfe import nfe_pb2 as _nfe_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NfeEntradaImportaImagemRequest(_message.Message):
    __slots__ = ("imagem", "mime_type", "ai_integration_id")
    IMAGEM_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    AI_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    imagem: bytes
    mime_type: str
    ai_integration_id: str
    def __init__(self, imagem: _Optional[bytes] = ..., mime_type: _Optional[str] = ..., ai_integration_id: _Optional[str] = ...) -> None: ...

class NfeEntradaImportaImagemResponse(_message.Message):
    __slots__ = ("nfe", "avisos")
    NFE_FIELD_NUMBER: _ClassVar[int]
    AVISOS_FIELD_NUMBER: _ClassVar[int]
    nfe: _nfe_pb2.Nfe
    avisos: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, nfe: _Optional[_Union[_nfe_pb2.Nfe, _Mapping]] = ..., avisos: _Optional[_Iterable[str]] = ...) -> None: ...

class NfeEntradaVinculaIaRequest(_message.Message):
    __slots__ = ("id", "ai_integration_id", "incluir_desvinculados")
    ID_FIELD_NUMBER: _ClassVar[int]
    AI_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUIR_DESVINCULADOS_FIELD_NUMBER: _ClassVar[int]
    id: str
    ai_integration_id: str
    incluir_desvinculados: bool
    def __init__(self, id: _Optional[str] = ..., ai_integration_id: _Optional[str] = ..., incluir_desvinculados: _Optional[bool] = ...) -> None: ...

class NfeEntradaItemIa(_message.Message):
    __slots__ = ("item_id", "motivo")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    motivo: str
    def __init__(self, item_id: _Optional[str] = ..., motivo: _Optional[str] = ...) -> None: ...

class NfeEntradaVinculaIaResponse(_message.Message):
    __slots__ = ("nfe", "vinculados", "categorizados", "itens")
    NFE_FIELD_NUMBER: _ClassVar[int]
    VINCULADOS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIZADOS_FIELD_NUMBER: _ClassVar[int]
    ITENS_FIELD_NUMBER: _ClassVar[int]
    nfe: _nfe_pb2.Nfe
    vinculados: int
    categorizados: int
    itens: _containers.RepeatedCompositeFieldContainer[NfeEntradaItemIa]
    def __init__(self, nfe: _Optional[_Union[_nfe_pb2.Nfe, _Mapping]] = ..., vinculados: _Optional[int] = ..., categorizados: _Optional[int] = ..., itens: _Optional[_Iterable[_Union[NfeEntradaItemIa, _Mapping]]] = ...) -> None: ...

class NfeEntradaSugerePrecosIaRequest(_message.Message):
    __slots__ = ("id", "ai_integration_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    AI_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    ai_integration_id: str
    def __init__(self, id: _Optional[str] = ..., ai_integration_id: _Optional[str] = ...) -> None: ...

class NfeEntradaPrecoIa(_message.Message):
    __slots__ = ("item_id", "preco_avista", "motivo")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PRECO_AVISTA_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    preco_avista: float
    motivo: str
    def __init__(self, item_id: _Optional[str] = ..., preco_avista: _Optional[float] = ..., motivo: _Optional[str] = ...) -> None: ...

class NfeEntradaSugerePrecosIaResponse(_message.Message):
    __slots__ = ("precos",)
    PRECOS_FIELD_NUMBER: _ClassVar[int]
    precos: _containers.RepeatedCompositeFieldContainer[NfeEntradaPrecoIa]
    def __init__(self, precos: _Optional[_Iterable[_Union[NfeEntradaPrecoIa, _Mapping]]] = ...) -> None: ...

class NfeEntradaAceitarRequest(_message.Message):
    __slots__ = ("id", "cadastra_nao_vinculados", "entrada_aplica_calculo_venda_custo", "emitir_evento_confirmacao", "natureza_operacao", "entrada_data_hora_aceite")
    ID_FIELD_NUMBER: _ClassVar[int]
    CADASTRA_NAO_VINCULADOS_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_APLICA_CALCULO_VENDA_CUSTO_FIELD_NUMBER: _ClassVar[int]
    EMITIR_EVENTO_CONFIRMACAO_FIELD_NUMBER: _ClassVar[int]
    NATUREZA_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_DATA_HORA_ACEITE_FIELD_NUMBER: _ClassVar[int]
    id: str
    cadastra_nao_vinculados: bool
    entrada_aplica_calculo_venda_custo: bool
    emitir_evento_confirmacao: bool
    natureza_operacao: str
    entrada_data_hora_aceite: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., cadastra_nao_vinculados: _Optional[bool] = ..., entrada_aplica_calculo_venda_custo: _Optional[bool] = ..., emitir_evento_confirmacao: _Optional[bool] = ..., natureza_operacao: _Optional[str] = ..., entrada_data_hora_aceite: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class NfeEntradaAceitarResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: _nfe_pb2.Nfe
    def __init__(self, nfe: _Optional[_Union[_nfe_pb2.Nfe, _Mapping]] = ...) -> None: ...

class NfeEntradaDesfazAceiteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class NfeEntradaDesfazAceiteResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: _nfe_pb2.Nfe
    def __init__(self, nfe: _Optional[_Union[_nfe_pb2.Nfe, _Mapping]] = ...) -> None: ...

class NfeEntradaRejeitarRequest(_message.Message):
    __slots__ = ("id", "motivo", "emitir_evento_desconhecimento_operacao", "emitir_evento_operacao_nao_realizada")
    ID_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    EMITIR_EVENTO_DESCONHECIMENTO_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    EMITIR_EVENTO_OPERACAO_NAO_REALIZADA_FIELD_NUMBER: _ClassVar[int]
    id: str
    motivo: str
    emitir_evento_desconhecimento_operacao: bool
    emitir_evento_operacao_nao_realizada: bool
    def __init__(self, id: _Optional[str] = ..., motivo: _Optional[str] = ..., emitir_evento_desconhecimento_operacao: _Optional[bool] = ..., emitir_evento_operacao_nao_realizada: _Optional[bool] = ...) -> None: ...

class NfeEntradaRejeitarResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: _nfe_pb2.Nfe
    def __init__(self, nfe: _Optional[_Union[_nfe_pb2.Nfe, _Mapping]] = ...) -> None: ...

class NfeEntradaImportaPelaChaveRequest(_message.Message):
    __slots__ = ("chave",)
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    chave: str
    def __init__(self, chave: _Optional[str] = ...) -> None: ...

class NfeEntradaImportaPelaChaveResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: _nfe_pb2.Nfe
    def __init__(self, nfe: _Optional[_Union[_nfe_pb2.Nfe, _Mapping]] = ...) -> None: ...

class NfeEntradaConsultaNotaRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NfeEntradaConsultaNotaResponse(_message.Message):
    __slots__ = ("nfeList",)
    NFELIST_FIELD_NUMBER: _ClassVar[int]
    nfeList: _containers.RepeatedCompositeFieldContainer[_nfe_pb2.Nfe]
    def __init__(self, nfeList: _Optional[_Iterable[_Union[_nfe_pb2.Nfe, _Mapping]]] = ...) -> None: ...

class NfeEntradaConsultaSituacaoRequest(_message.Message):
    __slots__ = ("id", "forcar")
    ID_FIELD_NUMBER: _ClassVar[int]
    FORCAR_FIELD_NUMBER: _ClassVar[int]
    id: str
    forcar: bool
    def __init__(self, id: _Optional[str] = ..., forcar: _Optional[bool] = ...) -> None: ...

class NfeEntradaConsultaSituacaoResponse(_message.Message):
    __slots__ = ("nfe", "consultado", "cancelada", "mensagem")
    NFE_FIELD_NUMBER: _ClassVar[int]
    CONSULTADO_FIELD_NUMBER: _ClassVar[int]
    CANCELADA_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    nfe: _nfe_pb2.Nfe
    consultado: bool
    cancelada: bool
    mensagem: str
    def __init__(self, nfe: _Optional[_Union[_nfe_pb2.Nfe, _Mapping]] = ..., consultado: _Optional[bool] = ..., cancelada: _Optional[bool] = ..., mensagem: _Optional[str] = ...) -> None: ...

class NfeEntradaImportaXmlStringRequest(_message.Message):
    __slots__ = ("xmlString",)
    XMLSTRING_FIELD_NUMBER: _ClassVar[int]
    xmlString: str
    def __init__(self, xmlString: _Optional[str] = ...) -> None: ...

class NfeEntradaImportaXmlStringResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: _nfe_pb2.Nfe
    def __init__(self, nfe: _Optional[_Union[_nfe_pb2.Nfe, _Mapping]] = ...) -> None: ...

class NfeEntradaConfirmarOperacaoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class NfeEntradaConfirmarOperacaoResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: _nfe_pb2.Nfe
    def __init__(self, nfe: _Optional[_Union[_nfe_pb2.Nfe, _Mapping]] = ...) -> None: ...

class NfeEntradaCienciaOperacaoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class NfeEntradaCienciaOperacaoResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: _nfe_pb2.Nfe
    def __init__(self, nfe: _Optional[_Union[_nfe_pb2.Nfe, _Mapping]] = ...) -> None: ...

class NfeEntradaDesconhecimentoOperacaoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class NfeEntradaDesconhecimentoOperacaoResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: _nfe_pb2.Nfe
    def __init__(self, nfe: _Optional[_Union[_nfe_pb2.Nfe, _Mapping]] = ...) -> None: ...

class NfeEntradaOperacaoNaoRealizadaRequest(_message.Message):
    __slots__ = ("id", "motivo")
    ID_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    id: str
    motivo: str
    def __init__(self, id: _Optional[str] = ..., motivo: _Optional[str] = ...) -> None: ...

class NfeEntradaOperacaoNaoRealizadaResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: _nfe_pb2.Nfe
    def __init__(self, nfe: _Optional[_Union[_nfe_pb2.Nfe, _Mapping]] = ...) -> None: ...
