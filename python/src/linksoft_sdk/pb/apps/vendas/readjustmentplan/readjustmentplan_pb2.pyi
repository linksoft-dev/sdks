from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TipoReajuste(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_REAJUSTE_UNSPECIFIED: _ClassVar[TipoReajuste]
    TIPO_REAJUSTE_PERCENTUAL: _ClassVar[TipoReajuste]
    TIPO_REAJUSTE_VALOR: _ClassVar[TipoReajuste]
    TIPO_REAJUSTE_INDICE: _ClassVar[TipoReajuste]
TIPO_REAJUSTE_UNSPECIFIED: TipoReajuste
TIPO_REAJUSTE_PERCENTUAL: TipoReajuste
TIPO_REAJUSTE_VALOR: TipoReajuste
TIPO_REAJUSTE_INDICE: TipoReajuste
