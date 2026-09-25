from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STRING: _ClassVar[FieldType]
    INT: _ClassVar[FieldType]
    FLOAT: _ClassVar[FieldType]
    BOOLEAN: _ClassVar[FieldType]
    DATE_TIME: _ClassVar[FieldType]
    DATE: _ClassVar[FieldType]
    MULTI_SELECT: _ClassVar[FieldType]
    SELECT: _ClassVar[FieldType]
    LOOKUP: _ClassVar[FieldType]

class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASC: _ClassVar[Direction]
    DESC: _ClassVar[Direction]

class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EQUALS: _ClassVar[Operator]
    CONTAINS: _ClassVar[Operator]
    STARTS: _ClassVar[Operator]
    ENDS: _ClassVar[Operator]
    IN: _ClassVar[Operator]
    GT: _ClassVar[Operator]
    GTE: _ClassVar[Operator]
    LT: _ClassVar[Operator]
    LTE: _ClassVar[Operator]
    NOT_NULL: _ClassVar[Operator]
    NULL: _ClassVar[Operator]
    BETWEEN: _ClassVar[Operator]
STRING: FieldType
INT: FieldType
FLOAT: FieldType
BOOLEAN: FieldType
DATE_TIME: FieldType
DATE: FieldType
MULTI_SELECT: FieldType
SELECT: FieldType
LOOKUP: FieldType
ASC: Direction
DESC: Direction
EQUALS: Operator
CONTAINS: Operator
STARTS: Operator
ENDS: Operator
IN: Operator
GT: Operator
GTE: Operator
LT: Operator
LTE: Operator
NOT_NULL: Operator
NULL: Operator
BETWEEN: Operator

class Filter(_message.Message):
    __slots__ = ("main", "main_label", "main_fields", "select_fields", "ids", "conditions", "or_conditions", "orderBy", "where", "limit", "skip", "first", "last", "rawFilter", "ignoreSoftDelete", "page", "excludeFields", "main_help")
    MAIN_FIELD_NUMBER: _ClassVar[int]
    MAIN_LABEL_FIELD_NUMBER: _ClassVar[int]
    MAIN_FIELDS_FIELD_NUMBER: _ClassVar[int]
    SELECT_FIELDS_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    OR_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    ORDERBY_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    FIRST_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    RAWFILTER_FIELD_NUMBER: _ClassVar[int]
    IGNORESOFTDELETE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDEFIELDS_FIELD_NUMBER: _ClassVar[int]
    MAIN_HELP_FIELD_NUMBER: _ClassVar[int]
    main: str
    main_label: str
    main_fields: _containers.RepeatedCompositeFieldContainer[condition]
    select_fields: _containers.RepeatedScalarFieldContainer[str]
    ids: _containers.RepeatedScalarFieldContainer[str]
    conditions: _containers.RepeatedCompositeFieldContainer[condition]
    or_conditions: _containers.RepeatedCompositeFieldContainer[condition]
    orderBy: _containers.RepeatedCompositeFieldContainer[OrderBy]
    where: _containers.RepeatedScalarFieldContainer[str]
    limit: int
    skip: int
    first: int
    last: int
    rawFilter: str
    ignoreSoftDelete: bool
    page: int
    excludeFields: _containers.RepeatedScalarFieldContainer[str]
    main_help: str
    def __init__(self, main: _Optional[str] = ..., main_label: _Optional[str] = ..., main_fields: _Optional[_Iterable[_Union[condition, _Mapping]]] = ..., select_fields: _Optional[_Iterable[str]] = ..., ids: _Optional[_Iterable[str]] = ..., conditions: _Optional[_Iterable[_Union[condition, _Mapping]]] = ..., or_conditions: _Optional[_Iterable[_Union[condition, _Mapping]]] = ..., orderBy: _Optional[_Iterable[_Union[OrderBy, _Mapping]]] = ..., where: _Optional[_Iterable[str]] = ..., limit: _Optional[int] = ..., skip: _Optional[int] = ..., first: _Optional[int] = ..., last: _Optional[int] = ..., rawFilter: _Optional[str] = ..., ignoreSoftDelete: _Optional[bool] = ..., page: _Optional[int] = ..., excludeFields: _Optional[_Iterable[str]] = ..., main_help: _Optional[str] = ...) -> None: ...

class Values(_message.Message):
    __slots__ = ("value", "label")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    value: str
    label: str
    def __init__(self, value: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class condition(_message.Message):
    __slots__ = ("field_name", "label", "field_type", "operator", "value", "lookup_url", "lookup_value", "values", "filter_operator", "raw", "pin", "view_only")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_URL_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    NOT_FIELD_NUMBER: _ClassVar[int]
    FILTER_OPERATOR_FIELD_NUMBER: _ClassVar[int]
    RAW_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    VIEW_ONLY_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    label: str
    field_type: FieldType
    operator: Operator
    value: str
    lookup_url: str
    lookup_value: str
    values: _containers.RepeatedCompositeFieldContainer[Values]
    filter_operator: str
    raw: str
    pin: bool
    view_only: bool
    def __init__(self, field_name: _Optional[str] = ..., label: _Optional[str] = ..., field_type: _Optional[_Union[FieldType, str]] = ..., operator: _Optional[_Union[Operator, str]] = ..., value: _Optional[str] = ..., lookup_url: _Optional[str] = ..., lookup_value: _Optional[str] = ..., values: _Optional[_Iterable[_Union[Values, _Mapping]]] = ..., filter_operator: _Optional[str] = ..., raw: _Optional[str] = ..., pin: _Optional[bool] = ..., view_only: _Optional[bool] = ..., **kwargs) -> None: ...

class OrderBy(_message.Message):
    __slots__ = ("field_name", "direction")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    direction: Direction
    def __init__(self, field_name: _Optional[str] = ..., direction: _Optional[_Union[Direction, str]] = ...) -> None: ...
