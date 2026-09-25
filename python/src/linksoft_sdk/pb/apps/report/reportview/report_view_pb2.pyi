from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReportView(_message.Message):
    __slots__ = ("id", "fields", "name", "description", "reports_names")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REPORTS_NAMES_FIELD_NUMBER: _ClassVar[int]
    id: str
    fields: _metadata_pb2.BasicFields
    name: str
    description: str
    reports_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., reports_names: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("report_view",)
    REPORT_VIEW_FIELD_NUMBER: _ClassVar[int]
    report_view: ReportView
    def __init__(self, report_view: _Optional[_Union[ReportView, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("report_view",)
    REPORT_VIEW_FIELD_NUMBER: _ClassVar[int]
    report_view: ReportView
    def __init__(self, report_view: _Optional[_Union[ReportView, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "report_view", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_VIEW_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    report_view: ReportView
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., report_view: _Optional[_Union[ReportView, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("report_view",)
    REPORT_VIEW_FIELD_NUMBER: _ClassVar[int]
    report_view: ReportView
    def __init__(self, report_view: _Optional[_Union[ReportView, _Mapping]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "name", "category", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    name: str
    category: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., category: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("report_view_list",)
    REPORT_VIEW_LIST_FIELD_NUMBER: _ClassVar[int]
    report_view_list: _containers.RepeatedCompositeFieldContainer[ReportView]
    def __init__(self, report_view_list: _Optional[_Iterable[_Union[ReportView, _Mapping]]] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("report_view",)
    REPORT_VIEW_FIELD_NUMBER: _ClassVar[int]
    report_view: ReportView
    def __init__(self, report_view: _Optional[_Union[ReportView, _Mapping]] = ...) -> None: ...
