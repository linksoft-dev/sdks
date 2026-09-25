import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Boolean(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[Boolean]
    YES: _ClassVar[Boolean]
    NO: _ClassVar[Boolean]
UNSPECIFIED: Boolean
YES: Boolean
NO: Boolean

class FieldMask(_message.Message):
    __slots__ = ("paths",)
    PATHS_FIELD_NUMBER: _ClassVar[int]
    paths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, paths: _Optional[_Iterable[str]] = ...) -> None: ...

class BasicFields(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "version", "deletedAt", "actions")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DELETEDAT_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    version: int
    deletedAt: _timestamp_pb2.Timestamp
    actions: _containers.RepeatedCompositeFieldContainer[ActionModel]
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ..., deletedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., actions: _Optional[_Iterable[_Union[ActionModel, _Mapping]]] = ...) -> None: ...

class ActionModel(_message.Message):
    __slots__ = ("id", "createdAt", "userId", "userName", "type", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    createdAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    type: str
    description: str
    def __init__(self, id: _Optional[str] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., type: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CustomField(_message.Message):
    __slots__ = ("value", "id")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    value: str
    id: str
    def __init__(self, value: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
