from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.api import resource_pb2 as _resource_pb2
from linksoft_sdk.pb.apps.datasource import datasource_pb2 as _datasource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WEBVIEW: _ClassVar[Format]
    PDF: _ClassVar[Format]

class FrameworkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FRAMEWORK_TYPE_STIMULSOFT: _ClassVar[FrameworkType]
    FRAMEWORK_TYPE_HTML: _ClassVar[FrameworkType]
    FRAMEWORK_TYPE_POWER_BI: _ClassVar[FrameworkType]

class ReportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[ReportType]
    REPORT: _ClassVar[ReportType]
    DASHBOARD: _ClassVar[ReportType]

class ReportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_FORMAT_UNSPECIFIED: _ClassVar[ReportFormat]
    REPORT_FORMAT_PDF: _ClassVar[ReportFormat]
    REPORT_FORMAT_EXCEL: _ClassVar[ReportFormat]
    REPORT_FORMAT_WORD: _ClassVar[ReportFormat]
    REPORT_FORMAT_HTML: _ClassVar[ReportFormat]
    REPORT_FORMAT_PPT: _ClassVar[ReportFormat]
    REPORT_FORMAT_RTF: _ClassVar[ReportFormat]
    REPORT_FORMAT_ODT: _ClassVar[ReportFormat]
    REPORT_FORMAT_ODS: _ClassVar[ReportFormat]
    REPORT_FORMAT_PNG: _ClassVar[ReportFormat]
    REPORT_FORMAT_JPEG: _ClassVar[ReportFormat]
    REPORT_FORMAT_TEXT: _ClassVar[ReportFormat]
    REPORT_FORMAT_CSV: _ClassVar[ReportFormat]
WEBVIEW: Format
PDF: Format
FRAMEWORK_TYPE_STIMULSOFT: FrameworkType
FRAMEWORK_TYPE_HTML: FrameworkType
FRAMEWORK_TYPE_POWER_BI: FrameworkType
UNSPECIFIED: ReportType
REPORT: ReportType
DASHBOARD: ReportType
REPORT_FORMAT_UNSPECIFIED: ReportFormat
REPORT_FORMAT_PDF: ReportFormat
REPORT_FORMAT_EXCEL: ReportFormat
REPORT_FORMAT_WORD: ReportFormat
REPORT_FORMAT_HTML: ReportFormat
REPORT_FORMAT_PPT: ReportFormat
REPORT_FORMAT_RTF: ReportFormat
REPORT_FORMAT_ODT: ReportFormat
REPORT_FORMAT_ODS: ReportFormat
REPORT_FORMAT_PNG: ReportFormat
REPORT_FORMAT_JPEG: ReportFormat
REPORT_FORMAT_TEXT: ReportFormat
REPORT_FORMAT_CSV: ReportFormat

class Response(_message.Message):
    __slots__ = ("id", "pdf_base64", "html_content", "template", "data")
    ID_FIELD_NUMBER: _ClassVar[int]
    PDF_BASE64_FIELD_NUMBER: _ClassVar[int]
    HTML_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    pdf_base64: str
    html_content: str
    template: str
    data: str
    def __init__(self, id: _Optional[str] = ..., pdf_base64: _Optional[str] = ..., html_content: _Optional[str] = ..., template: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...

class CreateReportRequest(_message.Message):
    __slots__ = ("report",)
    REPORT_FIELD_NUMBER: _ClassVar[int]
    report: Report
    def __init__(self, report: _Optional[_Union[Report, _Mapping]] = ...) -> None: ...

class CreateReportResponse(_message.Message):
    __slots__ = ("report",)
    REPORT_FIELD_NUMBER: _ClassVar[int]
    report: Report
    def __init__(self, report: _Optional[_Union[Report, _Mapping]] = ...) -> None: ...

class UpdateReportRequest(_message.Message):
    __slots__ = ("id", "report", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    report: Report
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., report: _Optional[_Union[Report, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateReportResponse(_message.Message):
    __slots__ = ("report",)
    REPORT_FIELD_NUMBER: _ClassVar[int]
    report: Report
    def __init__(self, report: _Optional[_Union[Report, _Mapping]] = ...) -> None: ...

class DeleteReportRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteReportResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListReportRequest(_message.Message):
    __slots__ = ("ids", "nome", "modulo", "tipo", "padraoSistema", "analytic", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    MODULO_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    PADRAOSISTEMA_FIELD_NUMBER: _ClassVar[int]
    ANALYTIC_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    nome: str
    modulo: str
    tipo: ReportType
    padraoSistema: bool
    analytic: bool
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., nome: _Optional[str] = ..., modulo: _Optional[str] = ..., tipo: _Optional[_Union[ReportType, str]] = ..., padraoSistema: _Optional[bool] = ..., analytic: _Optional[bool] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListReportResponse(_message.Message):
    __slots__ = ("reportList",)
    REPORTLIST_FIELD_NUMBER: _ClassVar[int]
    reportList: _containers.RepeatedCompositeFieldContainer[Report]
    def __init__(self, reportList: _Optional[_Iterable[_Union[Report, _Mapping]]] = ...) -> None: ...

class GetReportRequest(_message.Message):
    __slots__ = ("id", "report_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    report_name: str
    def __init__(self, id: _Optional[str] = ..., report_name: _Optional[str] = ...) -> None: ...

class GetReportResponse(_message.Message):
    __slots__ = ("report",)
    REPORT_FIELD_NUMBER: _ClassVar[int]
    report: Report
    def __init__(self, report: _Optional[_Union[Report, _Mapping]] = ...) -> None: ...

class GenerateReportRequest(_message.Message):
    __slots__ = ("report_name", "data", "output_file")
    REPORT_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FILE_FIELD_NUMBER: _ClassVar[int]
    report_name: str
    data: str
    output_file: str
    def __init__(self, report_name: _Optional[str] = ..., data: _Optional[str] = ..., output_file: _Optional[str] = ...) -> None: ...

class GenerateReportResponse(_message.Message):
    __slots__ = ("format", "result")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    format: str
    result: str
    def __init__(self, format: _Optional[str] = ..., result: _Optional[str] = ...) -> None: ...

class SendByEmailRequest(_message.Message):
    __slots__ = ("from_email", "from_name", "to", "subject", "body", "report_id", "report_name", "report_module", "report_data", "formats", "attachment_data", "attachment_name", "attachment_format")
    FROM_EMAIL_FIELD_NUMBER: _ClassVar[int]
    FROM_NAME_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_NAME_FIELD_NUMBER: _ClassVar[int]
    REPORT_MODULE_FIELD_NUMBER: _ClassVar[int]
    REPORT_DATA_FIELD_NUMBER: _ClassVar[int]
    FORMATS_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    from_email: str
    from_name: str
    to: _containers.RepeatedScalarFieldContainer[str]
    subject: str
    body: str
    report_id: str
    report_name: str
    report_module: str
    report_data: str
    formats: _containers.RepeatedScalarFieldContainer[Format]
    attachment_data: str
    attachment_name: str
    attachment_format: str
    def __init__(self, from_email: _Optional[str] = ..., from_name: _Optional[str] = ..., to: _Optional[_Iterable[str]] = ..., subject: _Optional[str] = ..., body: _Optional[str] = ..., report_id: _Optional[str] = ..., report_name: _Optional[str] = ..., report_module: _Optional[str] = ..., report_data: _Optional[str] = ..., formats: _Optional[_Iterable[_Union[Format, str]]] = ..., attachment_data: _Optional[str] = ..., attachment_name: _Optional[str] = ..., attachment_format: _Optional[str] = ...) -> None: ...

class SendByEmailResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class SetDefaultReportRequest(_message.Message):
    __slots__ = ("module", "id")
    MODULE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    module: str
    id: str
    def __init__(self, module: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class SetDefaultReportResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class Report(_message.Message):
    __slots__ = ("id", "fields", "tipo", "categoria", "modulo", "nome", "descricao", "subTitle", "analytic", "template", "dadosExemplo", "framework", "padraoSistema", "padrao", "datasource", "filter", "autoFilter", "allowedModules", "priority", "category_priority")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    MODULO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    ANALYTIC_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DADOSEXEMPLO_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    PADRAOSISTEMA_FIELD_NUMBER: _ClassVar[int]
    PADRAO_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    AUTOFILTER_FIELD_NUMBER: _ClassVar[int]
    ALLOWEDMODULES_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    fields: _metadata_pb2.BasicFields
    tipo: ReportType
    categoria: str
    modulo: str
    nome: str
    descricao: str
    subTitle: str
    analytic: bool
    template: str
    dadosExemplo: str
    framework: FrameworkType
    padraoSistema: bool
    padrao: bool
    datasource: _datasource_pb2.DataSource
    filter: _filter_pb2.Filter
    autoFilter: bool
    allowedModules: _containers.RepeatedScalarFieldContainer[str]
    priority: int
    category_priority: int
    def __init__(self, id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., tipo: _Optional[_Union[ReportType, str]] = ..., categoria: _Optional[str] = ..., modulo: _Optional[str] = ..., nome: _Optional[str] = ..., descricao: _Optional[str] = ..., subTitle: _Optional[str] = ..., analytic: _Optional[bool] = ..., template: _Optional[str] = ..., dadosExemplo: _Optional[str] = ..., framework: _Optional[_Union[FrameworkType, str]] = ..., padraoSistema: _Optional[bool] = ..., padrao: _Optional[bool] = ..., datasource: _Optional[_Union[_datasource_pb2.DataSource, _Mapping]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., autoFilter: _Optional[bool] = ..., allowedModules: _Optional[_Iterable[str]] = ..., priority: _Optional[int] = ..., category_priority: _Optional[int] = ...) -> None: ...
