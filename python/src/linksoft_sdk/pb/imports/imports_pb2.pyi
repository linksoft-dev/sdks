from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImportResponse(_message.Message):
    __slots__ = ("report_title", "result", "success", "failed", "total", "erros_by_category", "html_report")
    class ErrosByCategoryEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ImportErrorGroup
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ImportErrorGroup, _Mapping]] = ...) -> None: ...
    REPORT_TITLE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ERROS_BY_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    HTML_REPORT_FIELD_NUMBER: _ClassVar[int]
    report_title: str
    result: str
    success: int
    failed: int
    total: int
    erros_by_category: _containers.MessageMap[str, ImportErrorGroup]
    html_report: str
    def __init__(self, report_title: _Optional[str] = ..., result: _Optional[str] = ..., success: _Optional[int] = ..., failed: _Optional[int] = ..., total: _Optional[int] = ..., erros_by_category: _Optional[_Mapping[str, ImportErrorGroup]] = ..., html_report: _Optional[str] = ...) -> None: ...

class ImportErrorGroup(_message.Message):
    __slots__ = ("errors",)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[ImportError]
    def __init__(self, errors: _Optional[_Iterable[_Union[ImportError, _Mapping]]] = ...) -> None: ...

class ImportError(_message.Message):
    __slots__ = ("account", "reason", "details")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    account: str
    reason: str
    details: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, account: _Optional[str] = ..., reason: _Optional[str] = ..., details: _Optional[_Iterable[str]] = ...) -> None: ...
