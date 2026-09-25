import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListTrashRequest(_message.Message):
    __slots__ = ("module", "search", "limit")
    MODULE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    module: str
    search: str
    limit: int
    def __init__(self, module: _Optional[str] = ..., search: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class TrashItem(_message.Message):
    __slots__ = ("id", "description", "deleted_at", "deleted_by")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    deleted_at: _timestamp_pb2.Timestamp
    deleted_by: str
    def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ..., deleted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_by: _Optional[str] = ...) -> None: ...

class ListTrashResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[TrashItem]
    def __init__(self, items: _Optional[_Iterable[_Union[TrashItem, _Mapping]]] = ...) -> None: ...

class RestoreTrashRequest(_message.Message):
    __slots__ = ("module", "id")
    MODULE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    module: str
    id: str
    def __init__(self, module: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class RestoreTrashResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
