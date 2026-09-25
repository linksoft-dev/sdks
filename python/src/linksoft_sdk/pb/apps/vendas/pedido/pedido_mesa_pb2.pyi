import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConsumptionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONSUMPTION_STATUS_UNSPECIFIED: _ClassVar[ConsumptionStatus]
    CONSUMPTION_STATUS_FREE: _ClassVar[ConsumptionStatus]
    CONSUMPTION_STATUS_OCCUPIED: _ClassVar[ConsumptionStatus]
    CONSUMPTION_STATUS_RESERVED: _ClassVar[ConsumptionStatus]
    CONSUMPTION_STATUS_BLOCKED: _ClassVar[ConsumptionStatus]
    CONSUMPTION_STATUS_CLOSING: _ClassVar[ConsumptionStatus]

class PedidoEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PEDIDO_EVENT_TYPE_UNSPECIFIED: _ClassVar[PedidoEventType]
    PEDIDO_EVENT_TYPE_CREATED: _ClassVar[PedidoEventType]
    PEDIDO_EVENT_TYPE_TABLE_TRANSFER: _ClassVar[PedidoEventType]
    PEDIDO_EVENT_TYPE_REQUEST_CLOSING: _ClassVar[PedidoEventType]
    PEDIDO_EVENT_TYPE_FROM_RESERVATION: _ClassVar[PedidoEventType]
    PEDIDO_EVENT_TYPE_TABLE_RELEASED: _ClassVar[PedidoEventType]
    PEDIDO_EVENT_TYPE_TABLE_REASSIGNED: _ClassVar[PedidoEventType]
    PEDIDO_EVENT_TYPE_STAGE_CHANGED: _ClassVar[PedidoEventType]
    PEDIDO_EVENT_TYPE_SENT_TO_CUSTOMER: _ClassVar[PedidoEventType]
    PEDIDO_EVENT_TYPE_CUSTOMER_VIEWED: _ClassVar[PedidoEventType]
    PEDIDO_EVENT_TYPE_REMINDER_SENT: _ClassVar[PedidoEventType]
    PEDIDO_EVENT_TYPE_CUSTOMER_RESPONSE: _ClassVar[PedidoEventType]
CONSUMPTION_STATUS_UNSPECIFIED: ConsumptionStatus
CONSUMPTION_STATUS_FREE: ConsumptionStatus
CONSUMPTION_STATUS_OCCUPIED: ConsumptionStatus
CONSUMPTION_STATUS_RESERVED: ConsumptionStatus
CONSUMPTION_STATUS_BLOCKED: ConsumptionStatus
CONSUMPTION_STATUS_CLOSING: ConsumptionStatus
PEDIDO_EVENT_TYPE_UNSPECIFIED: PedidoEventType
PEDIDO_EVENT_TYPE_CREATED: PedidoEventType
PEDIDO_EVENT_TYPE_TABLE_TRANSFER: PedidoEventType
PEDIDO_EVENT_TYPE_REQUEST_CLOSING: PedidoEventType
PEDIDO_EVENT_TYPE_FROM_RESERVATION: PedidoEventType
PEDIDO_EVENT_TYPE_TABLE_RELEASED: PedidoEventType
PEDIDO_EVENT_TYPE_TABLE_REASSIGNED: PedidoEventType
PEDIDO_EVENT_TYPE_STAGE_CHANGED: PedidoEventType
PEDIDO_EVENT_TYPE_SENT_TO_CUSTOMER: PedidoEventType
PEDIDO_EVENT_TYPE_CUSTOMER_VIEWED: PedidoEventType
PEDIDO_EVENT_TYPE_REMINDER_SENT: PedidoEventType
PEDIDO_EVENT_TYPE_CUSTOMER_RESPONSE: PedidoEventType

class ConsumptionControl(_message.Message):
    __slots__ = ("type", "number", "sector", "sector_name", "display_name", "opened_at", "elapsed_time", "status", "reservation_id", "guests_count", "closing_requested", "nfc_uid", "released_at")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    SECTOR_FIELD_NUMBER: _ClassVar[int]
    SECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    ELAPSED_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_ID_FIELD_NUMBER: _ClassVar[int]
    GUESTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    CLOSING_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    NFC_UID_FIELD_NUMBER: _ClassVar[int]
    RELEASED_AT_FIELD_NUMBER: _ClassVar[int]
    type: str
    number: int
    sector: str
    sector_name: str
    display_name: str
    opened_at: _timestamp_pb2.Timestamp
    elapsed_time: str
    status: ConsumptionStatus
    reservation_id: str
    guests_count: int
    closing_requested: bool
    nfc_uid: str
    released_at: _timestamp_pb2.Timestamp
    def __init__(self, type: _Optional[str] = ..., number: _Optional[int] = ..., sector: _Optional[str] = ..., sector_name: _Optional[str] = ..., display_name: _Optional[str] = ..., opened_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., elapsed_time: _Optional[str] = ..., status: _Optional[_Union[ConsumptionStatus, str]] = ..., reservation_id: _Optional[str] = ..., guests_count: _Optional[int] = ..., closing_requested: _Optional[bool] = ..., nfc_uid: _Optional[str] = ..., released_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PedidoEvent(_message.Message):
    __slots__ = ("id", "created_at", "type", "description", "details")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    type: PedidoEventType
    description: str
    details: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., type: _Optional[_Union[PedidoEventType, str]] = ..., description: _Optional[str] = ..., details: _Optional[str] = ...) -> None: ...
