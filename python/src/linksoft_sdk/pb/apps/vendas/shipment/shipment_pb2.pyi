import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_UNSPECIFIED: _ClassVar[Status]
    OPEN: _ClassVar[Status]
    CONCLUDED: _ClassVar[Status]
    CANCELLED: _ClassVar[Status]

class ShipmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHIPMENT_TYPE_UNSPECIFIED: _ClassVar[ShipmentType]
    DELIVERY: _ClassVar[ShipmentType]
    LONG_HAUL: _ClassVar[ShipmentType]
    PICKUP: _ClassVar[ShipmentType]

class DispatchStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISPATCH_STATUS_UNSPECIFIED: _ClassVar[DispatchStatus]
    DRAFT: _ClassVar[DispatchStatus]
    CHECKED: _ClassVar[DispatchStatus]
    IN_TRANSIT: _ClassVar[DispatchStatus]
    COMPLETED: _ClassVar[DispatchStatus]
    CANCELLED_DISPATCH: _ClassVar[DispatchStatus]

class OrderDeliveryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDER_DELIVERY_STATUS_UNSPECIFIED: _ClassVar[OrderDeliveryStatus]
    PENDING: _ClassVar[OrderDeliveryStatus]
    OUT_FOR_DELIVERY: _ClassVar[OrderDeliveryStatus]
    DELIVERED: _ClassVar[OrderDeliveryStatus]
    DELIVERY_FAILED: _ClassVar[OrderDeliveryStatus]
    RETURNED: _ClassVar[OrderDeliveryStatus]
STATUS_UNSPECIFIED: Status
OPEN: Status
CONCLUDED: Status
CANCELLED: Status
SHIPMENT_TYPE_UNSPECIFIED: ShipmentType
DELIVERY: ShipmentType
LONG_HAUL: ShipmentType
PICKUP: ShipmentType
DISPATCH_STATUS_UNSPECIFIED: DispatchStatus
DRAFT: DispatchStatus
CHECKED: DispatchStatus
IN_TRANSIT: DispatchStatus
COMPLETED: DispatchStatus
CANCELLED_DISPATCH: DispatchStatus
ORDER_DELIVERY_STATUS_UNSPECIFIED: OrderDeliveryStatus
PENDING: OrderDeliveryStatus
OUT_FOR_DELIVERY: OrderDeliveryStatus
DELIVERED: OrderDeliveryStatus
DELIVERY_FAILED: OrderDeliveryStatus
RETURNED: OrderDeliveryStatus

class Shipment(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "status", "driver_id", "driver_name", "fields", "number", "destination", "total", "orders", "items", "notes", "gross_weight", "type", "dispatch_status", "carrier_person_id", "carrier_name", "vehicle_plate", "vehicle_id", "vehicle_nickname", "expected_delivery", "dispatched_at", "completed_at", "external_shipment_code", "tracking_code", "route")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DRIVER_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVER_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    GROSS_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_STATUS_FIELD_NUMBER: _ClassVar[int]
    CARRIER_PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    CARRIER_NAME_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_PLATE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_NICKNAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    DISPATCHED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SHIPMENT_CODE_FIELD_NUMBER: _ClassVar[int]
    TRACKING_CODE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    status: Status
    driver_id: str
    driver_name: str
    fields: _metadata_pb2.BasicFields
    number: int
    destination: str
    total: float
    orders: _containers.RepeatedCompositeFieldContainer[ShipmentOrder]
    items: _containers.RepeatedCompositeFieldContainer[ShipmentItem]
    notes: str
    gross_weight: float
    type: ShipmentType
    dispatch_status: DispatchStatus
    carrier_person_id: str
    carrier_name: str
    vehicle_plate: str
    vehicle_id: str
    vehicle_nickname: str
    expected_delivery: _timestamp_pb2.Timestamp
    dispatched_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    external_shipment_code: str
    tracking_code: str
    route: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., status: _Optional[_Union[Status, str]] = ..., driver_id: _Optional[str] = ..., driver_name: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., number: _Optional[int] = ..., destination: _Optional[str] = ..., total: _Optional[float] = ..., orders: _Optional[_Iterable[_Union[ShipmentOrder, _Mapping]]] = ..., items: _Optional[_Iterable[_Union[ShipmentItem, _Mapping]]] = ..., notes: _Optional[str] = ..., gross_weight: _Optional[float] = ..., type: _Optional[_Union[ShipmentType, str]] = ..., dispatch_status: _Optional[_Union[DispatchStatus, str]] = ..., carrier_person_id: _Optional[str] = ..., carrier_name: _Optional[str] = ..., vehicle_plate: _Optional[str] = ..., vehicle_id: _Optional[str] = ..., vehicle_nickname: _Optional[str] = ..., expected_delivery: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dispatched_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., external_shipment_code: _Optional[str] = ..., tracking_code: _Optional[str] = ..., route: _Optional[_Iterable[str]] = ...) -> None: ...

class ShipmentOrder(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "order_id", "order_number", "order_status", "order_products_total", "order_total", "items_count", "delivery_status", "dispatched_at", "delivered_at", "recipient_name", "recipient_document", "proof_photo_url", "signature_url", "delivery_location", "delivery_notes", "order_tracking_code", "attempts", "items")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORDER_STATUS_FIELD_NUMBER: _ClassVar[int]
    ORDER_PRODUCTS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    ORDER_TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_COUNT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_STATUS_FIELD_NUMBER: _ClassVar[int]
    DISPATCHED_AT_FIELD_NUMBER: _ClassVar[int]
    DELIVERED_AT_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    PROOF_PHOTO_URL_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_URL_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_NOTES_FIELD_NUMBER: _ClassVar[int]
    ORDER_TRACKING_CODE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    order_id: str
    order_number: int
    order_status: str
    order_products_total: float
    order_total: float
    items_count: int
    delivery_status: OrderDeliveryStatus
    dispatched_at: _timestamp_pb2.Timestamp
    delivered_at: _timestamp_pb2.Timestamp
    recipient_name: str
    recipient_document: str
    proof_photo_url: str
    signature_url: str
    delivery_location: GeoLocation
    delivery_notes: str
    order_tracking_code: str
    attempts: _containers.RepeatedCompositeFieldContainer[DeliveryAttempt]
    items: _containers.RepeatedCompositeFieldContainer[ShipmentOrderItem]
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., order_id: _Optional[str] = ..., order_number: _Optional[int] = ..., order_status: _Optional[str] = ..., order_products_total: _Optional[float] = ..., order_total: _Optional[float] = ..., items_count: _Optional[int] = ..., delivery_status: _Optional[_Union[OrderDeliveryStatus, str]] = ..., dispatched_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., delivered_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., recipient_name: _Optional[str] = ..., recipient_document: _Optional[str] = ..., proof_photo_url: _Optional[str] = ..., signature_url: _Optional[str] = ..., delivery_location: _Optional[_Union[GeoLocation, _Mapping]] = ..., delivery_notes: _Optional[str] = ..., order_tracking_code: _Optional[str] = ..., attempts: _Optional[_Iterable[_Union[DeliveryAttempt, _Mapping]]] = ..., items: _Optional[_Iterable[_Union[ShipmentOrderItem, _Mapping]]] = ...) -> None: ...

class ShipmentOrderItem(_message.Message):
    __slots__ = ("id", "order_item_id", "product_id", "product_name", "product_unit", "code", "quantity", "unit_price", "total", "batches")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UNIT_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UNIT_PRICE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    BATCHES_FIELD_NUMBER: _ClassVar[int]
    id: str
    order_item_id: str
    product_id: str
    product_name: str
    product_unit: str
    code: str
    quantity: float
    unit_price: float
    total: float
    batches: _containers.RepeatedCompositeFieldContainer[ShipmentOrderItemBatch]
    def __init__(self, id: _Optional[str] = ..., order_item_id: _Optional[str] = ..., product_id: _Optional[str] = ..., product_name: _Optional[str] = ..., product_unit: _Optional[str] = ..., code: _Optional[str] = ..., quantity: _Optional[float] = ..., unit_price: _Optional[float] = ..., total: _Optional[float] = ..., batches: _Optional[_Iterable[_Union[ShipmentOrderItemBatch, _Mapping]]] = ...) -> None: ...

class ShipmentOrderItemBatch(_message.Message):
    __slots__ = ("batch_code", "quantity", "production_order_id", "production_order_number")
    BATCH_CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    batch_code: str
    quantity: float
    production_order_id: str
    production_order_number: int
    def __init__(self, batch_code: _Optional[str] = ..., quantity: _Optional[float] = ..., production_order_id: _Optional[str] = ..., production_order_number: _Optional[int] = ...) -> None: ...

class DeliveryAttempt(_message.Message):
    __slots__ = ("attempted_at", "failure_reason", "photo_url")
    ATTEMPTED_AT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    PHOTO_URL_FIELD_NUMBER: _ClassVar[int]
    attempted_at: _timestamp_pb2.Timestamp
    failure_reason: str
    photo_url: str
    def __init__(self, attempted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., failure_reason: _Optional[str] = ..., photo_url: _Optional[str] = ...) -> None: ...

class GeoLocation(_message.Message):
    __slots__ = ("latitude", "longitude", "captured_at")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_AT_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    captured_at: _timestamp_pb2.Timestamp
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., captured_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ShipmentItem(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "code", "product_id", "product_name", "product_unit", "unit_weight", "gross_weight", "quantity", "total")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UNIT_FIELD_NUMBER: _ClassVar[int]
    UNIT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    GROSS_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    code: str
    product_id: str
    product_name: str
    product_unit: str
    unit_weight: float
    gross_weight: float
    quantity: float
    total: float
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., code: _Optional[str] = ..., product_id: _Optional[str] = ..., product_name: _Optional[str] = ..., product_unit: _Optional[str] = ..., unit_weight: _Optional[float] = ..., gross_weight: _Optional[float] = ..., quantity: _Optional[float] = ..., total: _Optional[float] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("shipment",)
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    shipment: Shipment
    def __init__(self, shipment: _Optional[_Union[Shipment, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("shipment",)
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    shipment: Shipment
    def __init__(self, shipment: _Optional[_Union[Shipment, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "shipment", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    shipment: Shipment
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., shipment: _Optional[_Union[Shipment, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("shipment",)
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    shipment: Shipment
    def __init__(self, shipment: _Optional[_Union[Shipment, _Mapping]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("shipment",)
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    shipment: Shipment
    def __init__(self, shipment: _Optional[_Union[Shipment, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "orders_ids", "page_size", "page_token", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    ORDERS_IDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    orders_ids: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., orders_ids: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("shipmentList", "next_page_token")
    SHIPMENTLIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    shipmentList: _containers.RepeatedCompositeFieldContainer[Shipment]
    next_page_token: str
    def __init__(self, shipmentList: _Optional[_Iterable[_Union[Shipment, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AddOrdersRequest(_message.Message):
    __slots__ = ("id", "orders_ids", "items")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORDERS_IDS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    id: str
    orders_ids: _containers.RepeatedScalarFieldContainer[str]
    items: _containers.RepeatedCompositeFieldContainer[AddOrderItemInput]
    def __init__(self, id: _Optional[str] = ..., orders_ids: _Optional[_Iterable[str]] = ..., items: _Optional[_Iterable[_Union[AddOrderItemInput, _Mapping]]] = ...) -> None: ...

class AddOrderItemInput(_message.Message):
    __slots__ = ("order_id", "order_item_id", "quantity")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    order_item_id: str
    quantity: float
    def __init__(self, order_id: _Optional[str] = ..., order_item_id: _Optional[str] = ..., quantity: _Optional[float] = ...) -> None: ...

class AddOrdersResponse(_message.Message):
    __slots__ = ("shipment",)
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    shipment: Shipment
    def __init__(self, shipment: _Optional[_Union[Shipment, _Mapping]] = ...) -> None: ...

class RemoveOrdersRequest(_message.Message):
    __slots__ = ("id", "orders_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORDERS_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    orders_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., orders_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class RemoveOrdersResponse(_message.Message):
    __slots__ = ("shipment",)
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    shipment: Shipment
    def __init__(self, shipment: _Optional[_Union[Shipment, _Mapping]] = ...) -> None: ...

class CutProductRequest(_message.Message):
    __slots__ = ("id", "product_id", "quantity")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    product_id: str
    quantity: float
    def __init__(self, id: _Optional[str] = ..., product_id: _Optional[str] = ..., quantity: _Optional[float] = ...) -> None: ...

class CutProductResponse(_message.Message):
    __slots__ = ("shipment",)
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    shipment: Shipment
    def __init__(self, shipment: _Optional[_Union[Shipment, _Mapping]] = ...) -> None: ...

class PrintRequest(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ...) -> None: ...

class PrintResponse(_message.Message):
    __slots__ = ("id", "html_content", "template", "data")
    ID_FIELD_NUMBER: _ClassVar[int]
    HTML_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    html_content: str
    template: str
    data: str
    def __init__(self, id: _Optional[str] = ..., html_content: _Optional[str] = ..., template: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...

class PrintOrdersRequest(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ...) -> None: ...

class PrintOrdersResponse(_message.Message):
    __slots__ = ("id", "html_content", "template", "data")
    ID_FIELD_NUMBER: _ClassVar[int]
    HTML_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    html_content: str
    template: str
    data: str
    def __init__(self, id: _Optional[str] = ..., html_content: _Optional[str] = ..., template: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...

class SynchronizeOrderRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class SynchronizeOrderResponse(_message.Message):
    __slots__ = ("shipment",)
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    shipment: Shipment
    def __init__(self, shipment: _Optional[_Union[Shipment, _Mapping]] = ...) -> None: ...

class InvoiceOrdersRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class InvoiceOrdersResponse(_message.Message):
    __slots__ = ("shipment", "invoiced_orders", "failed_orders", "results")
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    INVOICED_ORDERS_FIELD_NUMBER: _ClassVar[int]
    FAILED_ORDERS_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    shipment: Shipment
    invoiced_orders: int
    failed_orders: int
    results: _containers.RepeatedCompositeFieldContainer[InvoiceOrderResult]
    def __init__(self, shipment: _Optional[_Union[Shipment, _Mapping]] = ..., invoiced_orders: _Optional[int] = ..., failed_orders: _Optional[int] = ..., results: _Optional[_Iterable[_Union[InvoiceOrderResult, _Mapping]]] = ...) -> None: ...

class InvoiceOrderResult(_message.Message):
    __slots__ = ("order_id", "order_number", "success", "message", "pending_payment", "person_name", "balance")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PENDING_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    PERSON_NAME_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    order_number: int
    success: bool
    message: str
    pending_payment: bool
    person_name: str
    balance: float
    def __init__(self, order_id: _Optional[str] = ..., order_number: _Optional[int] = ..., success: _Optional[bool] = ..., message: _Optional[str] = ..., pending_payment: _Optional[bool] = ..., person_name: _Optional[str] = ..., balance: _Optional[float] = ...) -> None: ...

class SettlementReportRequest(_message.Message):
    __slots__ = ("id", "detailed")
    ID_FIELD_NUMBER: _ClassVar[int]
    DETAILED_FIELD_NUMBER: _ClassVar[int]
    id: str
    detailed: bool
    def __init__(self, id: _Optional[str] = ..., detailed: _Optional[bool] = ...) -> None: ...

class SettlementReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class CheckRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CheckResponse(_message.Message):
    __slots__ = ("shipment",)
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    shipment: Shipment
    def __init__(self, shipment: _Optional[_Union[Shipment, _Mapping]] = ...) -> None: ...

class StartTransitRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class StartTransitResponse(_message.Message):
    __slots__ = ("shipment",)
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    shipment: Shipment
    def __init__(self, shipment: _Optional[_Union[Shipment, _Mapping]] = ...) -> None: ...

class CompleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CompleteResponse(_message.Message):
    __slots__ = ("shipment",)
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    shipment: Shipment
    def __init__(self, shipment: _Optional[_Union[Shipment, _Mapping]] = ...) -> None: ...

class CancelDispatchRequest(_message.Message):
    __slots__ = ("id", "reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    reason: str
    def __init__(self, id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelDispatchResponse(_message.Message):
    __slots__ = ("shipment",)
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    shipment: Shipment
    def __init__(self, shipment: _Optional[_Union[Shipment, _Mapping]] = ...) -> None: ...

class UpdateOrderDeliveryStatusRequest(_message.Message):
    __slots__ = ("shipment_id", "order_id", "new_status", "recipient_name", "recipient_document", "proof_photo_url", "signature_url", "delivery_location", "delivery_notes", "failure_reason", "failure_photo_url")
    SHIPMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    PROOF_PHOTO_URL_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_URL_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_NOTES_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    FAILURE_PHOTO_URL_FIELD_NUMBER: _ClassVar[int]
    shipment_id: str
    order_id: str
    new_status: OrderDeliveryStatus
    recipient_name: str
    recipient_document: str
    proof_photo_url: str
    signature_url: str
    delivery_location: GeoLocation
    delivery_notes: str
    failure_reason: str
    failure_photo_url: str
    def __init__(self, shipment_id: _Optional[str] = ..., order_id: _Optional[str] = ..., new_status: _Optional[_Union[OrderDeliveryStatus, str]] = ..., recipient_name: _Optional[str] = ..., recipient_document: _Optional[str] = ..., proof_photo_url: _Optional[str] = ..., signature_url: _Optional[str] = ..., delivery_location: _Optional[_Union[GeoLocation, _Mapping]] = ..., delivery_notes: _Optional[str] = ..., failure_reason: _Optional[str] = ..., failure_photo_url: _Optional[str] = ...) -> None: ...

class UpdateOrderDeliveryStatusResponse(_message.Message):
    __slots__ = ("shipment",)
    SHIPMENT_FIELD_NUMBER: _ClassVar[int]
    shipment: Shipment
    def __init__(self, shipment: _Optional[_Union[Shipment, _Mapping]] = ...) -> None: ...

class MyShipmentsRequest(_message.Message):
    __slots__ = ("dispatch_statuses", "page_size", "page_token")
    DISPATCH_STATUSES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    dispatch_statuses: _containers.RepeatedScalarFieldContainer[DispatchStatus]
    page_size: int
    page_token: str
    def __init__(self, dispatch_statuses: _Optional[_Iterable[_Union[DispatchStatus, str]]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class MyShipmentsResponse(_message.Message):
    __slots__ = ("shipmentList", "next_page_token")
    SHIPMENTLIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    shipmentList: _containers.RepeatedCompositeFieldContainer[Shipment]
    next_page_token: str
    def __init__(self, shipmentList: _Optional[_Iterable[_Union[Shipment, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
