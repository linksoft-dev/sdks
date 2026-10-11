import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Otica(_message.Message):
    __slots__ = ("receita", "od", "oe", "acuidade_visual", "lente_contato", "pares", "ocorrencias")
    RECEITA_FIELD_NUMBER: _ClassVar[int]
    OD_FIELD_NUMBER: _ClassVar[int]
    OE_FIELD_NUMBER: _ClassVar[int]
    ACUIDADE_VISUAL_FIELD_NUMBER: _ClassVar[int]
    LENTE_CONTATO_FIELD_NUMBER: _ClassVar[int]
    PARES_FIELD_NUMBER: _ClassVar[int]
    OCORRENCIAS_FIELD_NUMBER: _ClassVar[int]
    receita: OticaReceita
    od: OticaFormula
    oe: OticaFormula
    acuidade_visual: OticaAcuidadeVisual
    lente_contato: OticaLenteContato
    pares: _containers.RepeatedCompositeFieldContainer[OticaPar]
    ocorrencias: _containers.RepeatedCompositeFieldContainer[OticaOcorrencia]
    def __init__(self, receita: _Optional[_Union[OticaReceita, _Mapping]] = ..., od: _Optional[_Union[OticaFormula, _Mapping]] = ..., oe: _Optional[_Union[OticaFormula, _Mapping]] = ..., acuidade_visual: _Optional[_Union[OticaAcuidadeVisual, _Mapping]] = ..., lente_contato: _Optional[_Union[OticaLenteContato, _Mapping]] = ..., pares: _Optional[_Iterable[_Union[OticaPar, _Mapping]]] = ..., ocorrencias: _Optional[_Iterable[_Union[OticaOcorrencia, _Mapping]]] = ...) -> None: ...

class OticaReceita(_message.Message):
    __slots__ = ("tipo", "medico_id", "medico_nome", "medico_registro", "data", "validade", "origem", "pedido_origem_numero", "autoriza_lembrete", "obs")
    TIPO_FIELD_NUMBER: _ClassVar[int]
    MEDICO_ID_FIELD_NUMBER: _ClassVar[int]
    MEDICO_NOME_FIELD_NUMBER: _ClassVar[int]
    MEDICO_REGISTRO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    VALIDADE_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_FIELD_NUMBER: _ClassVar[int]
    PEDIDO_ORIGEM_NUMERO_FIELD_NUMBER: _ClassVar[int]
    AUTORIZA_LEMBRETE_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    tipo: str
    medico_id: str
    medico_nome: str
    medico_registro: str
    data: _timestamp_pb2.Timestamp
    validade: _timestamp_pb2.Timestamp
    origem: str
    pedido_origem_numero: str
    autoriza_lembrete: bool
    obs: str
    def __init__(self, tipo: _Optional[str] = ..., medico_id: _Optional[str] = ..., medico_nome: _Optional[str] = ..., medico_registro: _Optional[str] = ..., data: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., validade: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., origem: _Optional[str] = ..., pedido_origem_numero: _Optional[str] = ..., autoriza_lembrete: _Optional[bool] = ..., obs: _Optional[str] = ...) -> None: ...

class OticaFormula(_message.Message):
    __slots__ = ("esferico", "cilindro", "eixo", "adicao", "dnp", "dnp_perto", "prisma", "base_prisma")
    ESFERICO_FIELD_NUMBER: _ClassVar[int]
    CILINDRO_FIELD_NUMBER: _ClassVar[int]
    EIXO_FIELD_NUMBER: _ClassVar[int]
    ADICAO_FIELD_NUMBER: _ClassVar[int]
    DNP_FIELD_NUMBER: _ClassVar[int]
    DNP_PERTO_FIELD_NUMBER: _ClassVar[int]
    PRISMA_FIELD_NUMBER: _ClassVar[int]
    BASE_PRISMA_FIELD_NUMBER: _ClassVar[int]
    esferico: float
    cilindro: float
    eixo: int
    adicao: float
    dnp: float
    dnp_perto: float
    prisma: float
    base_prisma: str
    def __init__(self, esferico: _Optional[float] = ..., cilindro: _Optional[float] = ..., eixo: _Optional[int] = ..., adicao: _Optional[float] = ..., dnp: _Optional[float] = ..., dnp_perto: _Optional[float] = ..., prisma: _Optional[float] = ..., base_prisma: _Optional[str] = ...) -> None: ...

class OticaAcuidadeVisual(_message.Message):
    __slots__ = ("sc", "cc")
    SC_FIELD_NUMBER: _ClassVar[int]
    CC_FIELD_NUMBER: _ClassVar[int]
    sc: OticaAcuidadeOlhos
    cc: OticaAcuidadeOlhos
    def __init__(self, sc: _Optional[_Union[OticaAcuidadeOlhos, _Mapping]] = ..., cc: _Optional[_Union[OticaAcuidadeOlhos, _Mapping]] = ...) -> None: ...

class OticaAcuidadeOlhos(_message.Message):
    __slots__ = ("olho_direito", "olho_esquerdo", "ambos_olhos")
    OLHO_DIREITO_FIELD_NUMBER: _ClassVar[int]
    OLHO_ESQUERDO_FIELD_NUMBER: _ClassVar[int]
    AMBOS_OLHOS_FIELD_NUMBER: _ClassVar[int]
    olho_direito: OticaAcuidade
    olho_esquerdo: OticaAcuidade
    ambos_olhos: OticaAcuidade
    def __init__(self, olho_direito: _Optional[_Union[OticaAcuidade, _Mapping]] = ..., olho_esquerdo: _Optional[_Union[OticaAcuidade, _Mapping]] = ..., ambos_olhos: _Optional[_Union[OticaAcuidade, _Mapping]] = ...) -> None: ...

class OticaAcuidade(_message.Message):
    __slots__ = ("longe", "perto")
    LONGE_FIELD_NUMBER: _ClassVar[int]
    PERTO_FIELD_NUMBER: _ClassVar[int]
    longe: str
    perto: str
    def __init__(self, longe: _Optional[str] = ..., perto: _Optional[str] = ...) -> None: ...

class OticaLenteContato(_message.Message):
    __slots__ = ("od", "oe", "descarte", "caixas")
    OD_FIELD_NUMBER: _ClassVar[int]
    OE_FIELD_NUMBER: _ClassVar[int]
    DESCARTE_FIELD_NUMBER: _ClassVar[int]
    CAIXAS_FIELD_NUMBER: _ClassVar[int]
    od: OticaLenteContatoOlho
    oe: OticaLenteContatoOlho
    descarte: str
    caixas: int
    def __init__(self, od: _Optional[_Union[OticaLenteContatoOlho, _Mapping]] = ..., oe: _Optional[_Union[OticaLenteContatoOlho, _Mapping]] = ..., descarte: _Optional[str] = ..., caixas: _Optional[int] = ...) -> None: ...

class OticaLenteContatoOlho(_message.Message):
    __slots__ = ("curva_base", "diametro", "marca_modelo")
    CURVA_BASE_FIELD_NUMBER: _ClassVar[int]
    DIAMETRO_FIELD_NUMBER: _ClassVar[int]
    MARCA_MODELO_FIELD_NUMBER: _ClassVar[int]
    curva_base: str
    diametro: str
    marca_modelo: str
    def __init__(self, curva_base: _Optional[str] = ..., diametro: _Optional[str] = ..., marca_modelo: _Optional[str] = ...) -> None: ...

class OticaPar(_message.Message):
    __slots__ = ("id", "uso", "solar", "lente_produto_id", "lente_descricao", "material", "indice", "tratamentos", "armacao_produto_id", "armacao_descricao", "armacao_do_cliente", "montagem", "altura_od", "altura_oe", "medidas", "laboratorio", "conferencia", "obs")
    ID_FIELD_NUMBER: _ClassVar[int]
    USO_FIELD_NUMBER: _ClassVar[int]
    SOLAR_FIELD_NUMBER: _ClassVar[int]
    LENTE_PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    LENTE_DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_FIELD_NUMBER: _ClassVar[int]
    INDICE_FIELD_NUMBER: _ClassVar[int]
    TRATAMENTOS_FIELD_NUMBER: _ClassVar[int]
    ARMACAO_PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    ARMACAO_DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    ARMACAO_DO_CLIENTE_FIELD_NUMBER: _ClassVar[int]
    MONTAGEM_FIELD_NUMBER: _ClassVar[int]
    ALTURA_OD_FIELD_NUMBER: _ClassVar[int]
    ALTURA_OE_FIELD_NUMBER: _ClassVar[int]
    MEDIDAS_FIELD_NUMBER: _ClassVar[int]
    LABORATORIO_FIELD_NUMBER: _ClassVar[int]
    CONFERENCIA_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    id: str
    uso: str
    solar: bool
    lente_produto_id: str
    lente_descricao: str
    material: str
    indice: str
    tratamentos: _containers.RepeatedScalarFieldContainer[str]
    armacao_produto_id: str
    armacao_descricao: str
    armacao_do_cliente: bool
    montagem: str
    altura_od: float
    altura_oe: float
    medidas: OticaMedidas
    laboratorio: OticaLaboratorio
    conferencia: OticaConferencia
    obs: str
    def __init__(self, id: _Optional[str] = ..., uso: _Optional[str] = ..., solar: _Optional[bool] = ..., lente_produto_id: _Optional[str] = ..., lente_descricao: _Optional[str] = ..., material: _Optional[str] = ..., indice: _Optional[str] = ..., tratamentos: _Optional[_Iterable[str]] = ..., armacao_produto_id: _Optional[str] = ..., armacao_descricao: _Optional[str] = ..., armacao_do_cliente: _Optional[bool] = ..., montagem: _Optional[str] = ..., altura_od: _Optional[float] = ..., altura_oe: _Optional[float] = ..., medidas: _Optional[_Union[OticaMedidas, _Mapping]] = ..., laboratorio: _Optional[_Union[OticaLaboratorio, _Mapping]] = ..., conferencia: _Optional[_Union[OticaConferencia, _Mapping]] = ..., obs: _Optional[str] = ...) -> None: ...

class OticaMedidas(_message.Message):
    __slots__ = ("horizontal", "vertical", "ponte", "diagonal", "haste", "pantoscopico", "vertice", "curvatura")
    HORIZONTAL_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_FIELD_NUMBER: _ClassVar[int]
    PONTE_FIELD_NUMBER: _ClassVar[int]
    DIAGONAL_FIELD_NUMBER: _ClassVar[int]
    HASTE_FIELD_NUMBER: _ClassVar[int]
    PANTOSCOPICO_FIELD_NUMBER: _ClassVar[int]
    VERTICE_FIELD_NUMBER: _ClassVar[int]
    CURVATURA_FIELD_NUMBER: _ClassVar[int]
    horizontal: float
    vertical: float
    ponte: float
    diagonal: float
    haste: float
    pantoscopico: float
    vertice: float
    curvatura: float
    def __init__(self, horizontal: _Optional[float] = ..., vertical: _Optional[float] = ..., ponte: _Optional[float] = ..., diagonal: _Optional[float] = ..., haste: _Optional[float] = ..., pantoscopico: _Optional[float] = ..., vertice: _Optional[float] = ..., curvatura: _Optional[float] = ...) -> None: ...

class OticaLaboratorio(_message.Message):
    __slots__ = ("pessoa_id", "pessoa_nome", "numero_os", "enviado_em", "previsao")
    PESSOA_ID_FIELD_NUMBER: _ClassVar[int]
    PESSOA_NOME_FIELD_NUMBER: _ClassVar[int]
    NUMERO_OS_FIELD_NUMBER: _ClassVar[int]
    ENVIADO_EM_FIELD_NUMBER: _ClassVar[int]
    PREVISAO_FIELD_NUMBER: _ClassVar[int]
    pessoa_id: str
    pessoa_nome: str
    numero_os: str
    enviado_em: _timestamp_pb2.Timestamp
    previsao: _timestamp_pb2.Timestamp
    def __init__(self, pessoa_id: _Optional[str] = ..., pessoa_nome: _Optional[str] = ..., numero_os: _Optional[str] = ..., enviado_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., previsao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class OticaConferencia(_message.Message):
    __slots__ = ("od", "oe", "montado_por", "conferido_por", "conferido_em")
    OD_FIELD_NUMBER: _ClassVar[int]
    OE_FIELD_NUMBER: _ClassVar[int]
    MONTADO_POR_FIELD_NUMBER: _ClassVar[int]
    CONFERIDO_POR_FIELD_NUMBER: _ClassVar[int]
    CONFERIDO_EM_FIELD_NUMBER: _ClassVar[int]
    od: OticaFormula
    oe: OticaFormula
    montado_por: str
    conferido_por: str
    conferido_em: _timestamp_pb2.Timestamp
    def __init__(self, od: _Optional[_Union[OticaFormula, _Mapping]] = ..., oe: _Optional[_Union[OticaFormula, _Mapping]] = ..., montado_por: _Optional[str] = ..., conferido_por: _Optional[str] = ..., conferido_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class OticaOcorrencia(_message.Message):
    __slots__ = ("id", "par_id", "aberta_em", "motivo", "responsavel", "custo", "refazer", "chamado_numero", "chamado_em", "novo_prazo", "descricao", "resolvida_em")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAR_ID_FIELD_NUMBER: _ClassVar[int]
    ABERTA_EM_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    RESPONSAVEL_FIELD_NUMBER: _ClassVar[int]
    CUSTO_FIELD_NUMBER: _ClassVar[int]
    REFAZER_FIELD_NUMBER: _ClassVar[int]
    CHAMADO_NUMERO_FIELD_NUMBER: _ClassVar[int]
    CHAMADO_EM_FIELD_NUMBER: _ClassVar[int]
    NOVO_PRAZO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    RESOLVIDA_EM_FIELD_NUMBER: _ClassVar[int]
    id: str
    par_id: str
    aberta_em: _timestamp_pb2.Timestamp
    motivo: str
    responsavel: str
    custo: float
    refazer: str
    chamado_numero: str
    chamado_em: _timestamp_pb2.Timestamp
    novo_prazo: _timestamp_pb2.Timestamp
    descricao: str
    resolvida_em: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., par_id: _Optional[str] = ..., aberta_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., motivo: _Optional[str] = ..., responsavel: _Optional[str] = ..., custo: _Optional[float] = ..., refazer: _Optional[str] = ..., chamado_numero: _Optional[str] = ..., chamado_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., novo_prazo: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., descricao: _Optional[str] = ..., resolvida_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
