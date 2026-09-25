from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPORT_FORMAT_UNSPECIFIED: _ClassVar[ExportFormat]
    EXPORT_FORMAT_JSON: _ClassVar[ExportFormat]
    EXPORT_FORMAT_CSV: _ClassVar[ExportFormat]
EXPORT_FORMAT_UNSPECIFIED: ExportFormat
EXPORT_FORMAT_JSON: ExportFormat
EXPORT_FORMAT_CSV: ExportFormat

class ExportMetadata(_message.Message):
    __slots__ = ("version", "entity", "exported_at", "total_records", "org_id", "fields")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    EXPORTED_AT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RECORDS_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    version: str
    entity: str
    exported_at: str
    total_records: int
    org_id: str
    fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, version: _Optional[str] = ..., entity: _Optional[str] = ..., exported_at: _Optional[str] = ..., total_records: _Optional[int] = ..., org_id: _Optional[str] = ..., fields: _Optional[_Iterable[str]] = ...) -> None: ...

class ExportResponse(_message.Message):
    __slots__ = ("file_content", "file_name", "content_type", "metadata")
    FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    file_content: str
    file_name: str
    content_type: str
    metadata: ExportMetadata
    def __init__(self, file_content: _Optional[str] = ..., file_name: _Optional[str] = ..., content_type: _Optional[str] = ..., metadata: _Optional[_Union[ExportMetadata, _Mapping]] = ...) -> None: ...
