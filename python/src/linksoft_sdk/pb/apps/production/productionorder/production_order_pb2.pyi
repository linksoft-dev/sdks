import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductionOrder(_message.Message):
    __slots__ = ("fields", "id", "number", "status", "product_id", "product_name", "product_unit", "product_code", "planned_quantity", "produced_quantity", "lost_quantity", "loss_percentage", "input_cost", "labor_cost", "other_cost", "total_cost", "unit_cost", "planned_total_cost", "planned_unit_cost", "extra_costs", "inputs", "expected_date", "start_date", "finish_date", "batch_code", "batch_manufacture_date", "batch_expiration_date", "notes", "batch_id", "created_at", "updated_at", "user_id", "user_name", "sale_order_id", "sale_order_number", "input_stock_name", "output_stock_name", "is_late", "explode_sub_assemblies", "demands", "entries", "standard_unit_cost", "tags", "product_category_id", "product_category_name")
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UNIT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CODE_FIELD_NUMBER: _ClassVar[int]
    PLANNED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRODUCED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LOST_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LOSS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    INPUT_COST_FIELD_NUMBER: _ClassVar[int]
    LABOR_COST_FIELD_NUMBER: _ClassVar[int]
    OTHER_COST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
    UNIT_COST_FIELD_NUMBER: _ClassVar[int]
    PLANNED_TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
    PLANNED_UNIT_COST_FIELD_NUMBER: _ClassVar[int]
    EXTRA_COSTS_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DATE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    FINISH_DATE_FIELD_NUMBER: _ClassVar[int]
    BATCH_CODE_FIELD_NUMBER: _ClassVar[int]
    BATCH_MANUFACTURE_DATE_FIELD_NUMBER: _ClassVar[int]
    BATCH_EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    SALE_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    SALE_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    INPUT_STOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_STOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_LATE_FIELD_NUMBER: _ClassVar[int]
    EXPLODE_SUB_ASSEMBLIES_FIELD_NUMBER: _ClassVar[int]
    DEMANDS_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    STANDARD_UNIT_COST_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEGORY_NAME_FIELD_NUMBER: _ClassVar[int]
    fields: _metadata_pb2.BasicFields
    id: str
    number: int
    status: str
    product_id: str
    product_name: str
    product_unit: str
    product_code: str
    planned_quantity: float
    produced_quantity: float
    lost_quantity: float
    loss_percentage: float
    input_cost: float
    labor_cost: float
    other_cost: float
    total_cost: float
    unit_cost: float
    planned_total_cost: float
    planned_unit_cost: float
    extra_costs: _containers.RepeatedCompositeFieldContainer[ExtraCost]
    inputs: _containers.RepeatedCompositeFieldContainer[ProductionInput]
    expected_date: _timestamp_pb2.Timestamp
    start_date: _timestamp_pb2.Timestamp
    finish_date: _timestamp_pb2.Timestamp
    batch_code: str
    batch_manufacture_date: _timestamp_pb2.Timestamp
    batch_expiration_date: _timestamp_pb2.Timestamp
    notes: str
    batch_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    sale_order_id: str
    sale_order_number: int
    input_stock_name: str
    output_stock_name: str
    is_late: bool
    explode_sub_assemblies: bool
    demands: _containers.RepeatedCompositeFieldContainer[SaleOrderDemand]
    entries: _containers.RepeatedCompositeFieldContainer[ProductionEntry]
    standard_unit_cost: float
    tags: _containers.RepeatedCompositeFieldContainer[ProductionTag]
    product_category_id: str
    product_category_name: str
    def __init__(self, fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., id: _Optional[str] = ..., number: _Optional[int] = ..., status: _Optional[str] = ..., product_id: _Optional[str] = ..., product_name: _Optional[str] = ..., product_unit: _Optional[str] = ..., product_code: _Optional[str] = ..., planned_quantity: _Optional[float] = ..., produced_quantity: _Optional[float] = ..., lost_quantity: _Optional[float] = ..., loss_percentage: _Optional[float] = ..., input_cost: _Optional[float] = ..., labor_cost: _Optional[float] = ..., other_cost: _Optional[float] = ..., total_cost: _Optional[float] = ..., unit_cost: _Optional[float] = ..., planned_total_cost: _Optional[float] = ..., planned_unit_cost: _Optional[float] = ..., extra_costs: _Optional[_Iterable[_Union[ExtraCost, _Mapping]]] = ..., inputs: _Optional[_Iterable[_Union[ProductionInput, _Mapping]]] = ..., expected_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finish_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., batch_code: _Optional[str] = ..., batch_manufacture_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., batch_expiration_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., batch_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., sale_order_id: _Optional[str] = ..., sale_order_number: _Optional[int] = ..., input_stock_name: _Optional[str] = ..., output_stock_name: _Optional[str] = ..., is_late: _Optional[bool] = ..., explode_sub_assemblies: _Optional[bool] = ..., demands: _Optional[_Iterable[_Union[SaleOrderDemand, _Mapping]]] = ..., entries: _Optional[_Iterable[_Union[ProductionEntry, _Mapping]]] = ..., standard_unit_cost: _Optional[float] = ..., tags: _Optional[_Iterable[_Union[ProductionTag, _Mapping]]] = ..., product_category_id: _Optional[str] = ..., product_category_name: _Optional[str] = ...) -> None: ...

class ProductionTag(_message.Message):
    __slots__ = ("value", "color")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    value: str
    color: str
    def __init__(self, value: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class SaleOrderDemand(_message.Message):
    __slots__ = ("id", "sale_order_id", "sale_order_number", "sale_order_item_id", "customer_name", "quantity", "fulfilled_quantity", "order_date", "delivery_date")
    ID_FIELD_NUMBER: _ClassVar[int]
    SALE_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    SALE_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SALE_ORDER_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    FULFILLED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ORDER_DATE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_DATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    sale_order_id: str
    sale_order_number: int
    sale_order_item_id: str
    customer_name: str
    quantity: float
    fulfilled_quantity: float
    order_date: _timestamp_pb2.Timestamp
    delivery_date: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., sale_order_id: _Optional[str] = ..., sale_order_number: _Optional[int] = ..., sale_order_item_id: _Optional[str] = ..., customer_name: _Optional[str] = ..., quantity: _Optional[float] = ..., fulfilled_quantity: _Optional[float] = ..., order_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., delivery_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ProductionEntry(_message.Message):
    __slots__ = ("id", "number", "date", "good_quantity", "lost_quantity", "user_id", "user_name", "notes", "inputs", "allocations")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    GOOD_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LOST_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    ALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    number: int
    date: _timestamp_pb2.Timestamp
    good_quantity: float
    lost_quantity: float
    user_id: str
    user_name: str
    notes: str
    inputs: _containers.RepeatedCompositeFieldContainer[EntryInput]
    allocations: _containers.RepeatedCompositeFieldContainer[EntryAllocation]
    def __init__(self, id: _Optional[str] = ..., number: _Optional[int] = ..., date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., good_quantity: _Optional[float] = ..., lost_quantity: _Optional[float] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., notes: _Optional[str] = ..., inputs: _Optional[_Iterable[_Union[EntryInput, _Mapping]]] = ..., allocations: _Optional[_Iterable[_Union[EntryAllocation, _Mapping]]] = ...) -> None: ...

class EntryInput(_message.Message):
    __slots__ = ("product_id", "product_name", "quantity", "unit_cost", "consumed_batches")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UNIT_COST_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_BATCHES_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    product_name: str
    quantity: float
    unit_cost: float
    consumed_batches: _containers.RepeatedCompositeFieldContainer[ConsumedBatch]
    def __init__(self, product_id: _Optional[str] = ..., product_name: _Optional[str] = ..., quantity: _Optional[float] = ..., unit_cost: _Optional[float] = ..., consumed_batches: _Optional[_Iterable[_Union[ConsumedBatch, _Mapping]]] = ...) -> None: ...

class EntryAllocation(_message.Message):
    __slots__ = ("demand_id", "sale_order_id", "sale_order_number", "quantity")
    DEMAND_ID_FIELD_NUMBER: _ClassVar[int]
    SALE_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    SALE_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    demand_id: str
    sale_order_id: str
    sale_order_number: int
    quantity: float
    def __init__(self, demand_id: _Optional[str] = ..., sale_order_id: _Optional[str] = ..., sale_order_number: _Optional[int] = ..., quantity: _Optional[float] = ...) -> None: ...

class ExtraCost(_message.Message):
    __slots__ = ("id", "description", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    value: float
    def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...

class ProductionInput(_message.Message):
    __slots__ = ("id", "product_id", "product_name", "product_code", "unit", "required_quantity", "total_quantity", "consumed_quantity", "loss_percent", "unit_cost", "total_cost", "available_stock", "consumed_batches", "min_stock", "level", "parent_product_id", "parent_product_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CODE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LOSS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    UNIT_COST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_STOCK_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_BATCHES_FIELD_NUMBER: _ClassVar[int]
    MIN_STOCK_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    PARENT_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    product_id: str
    product_name: str
    product_code: str
    unit: str
    required_quantity: float
    total_quantity: float
    consumed_quantity: float
    loss_percent: float
    unit_cost: float
    total_cost: float
    available_stock: float
    consumed_batches: _containers.RepeatedCompositeFieldContainer[ConsumedBatch]
    min_stock: float
    level: int
    parent_product_id: str
    parent_product_name: str
    def __init__(self, id: _Optional[str] = ..., product_id: _Optional[str] = ..., product_name: _Optional[str] = ..., product_code: _Optional[str] = ..., unit: _Optional[str] = ..., required_quantity: _Optional[float] = ..., total_quantity: _Optional[float] = ..., consumed_quantity: _Optional[float] = ..., loss_percent: _Optional[float] = ..., unit_cost: _Optional[float] = ..., total_cost: _Optional[float] = ..., available_stock: _Optional[float] = ..., consumed_batches: _Optional[_Iterable[_Union[ConsumedBatch, _Mapping]]] = ..., min_stock: _Optional[float] = ..., level: _Optional[int] = ..., parent_product_id: _Optional[str] = ..., parent_product_name: _Optional[str] = ...) -> None: ...

class ConsumedBatch(_message.Message):
    __slots__ = ("batch_id", "batch_number", "quantity", "supplier_id", "supplier_name", "expiration_date")
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SUPPLIER_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLIER_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    batch_id: str
    batch_number: str
    quantity: float
    supplier_id: str
    supplier_name: str
    expiration_date: _timestamp_pb2.Timestamp
    def __init__(self, batch_id: _Optional[str] = ..., batch_number: _Optional[str] = ..., quantity: _Optional[float] = ..., supplier_id: _Optional[str] = ..., supplier_name: _Optional[str] = ..., expiration_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class InputAvailability(_message.Message):
    __slots__ = ("product_id", "product_name", "product_code", "unit", "available_stock", "quantity_per_unit", "producible_quantity", "limiting", "unit_cost", "min_stock")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CODE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_STOCK_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_PER_UNIT_FIELD_NUMBER: _ClassVar[int]
    PRODUCIBLE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LIMITING_FIELD_NUMBER: _ClassVar[int]
    UNIT_COST_FIELD_NUMBER: _ClassVar[int]
    MIN_STOCK_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    product_name: str
    product_code: str
    unit: str
    available_stock: float
    quantity_per_unit: float
    producible_quantity: float
    limiting: bool
    unit_cost: float
    min_stock: float
    def __init__(self, product_id: _Optional[str] = ..., product_name: _Optional[str] = ..., product_code: _Optional[str] = ..., unit: _Optional[str] = ..., available_stock: _Optional[float] = ..., quantity_per_unit: _Optional[float] = ..., producible_quantity: _Optional[float] = ..., limiting: _Optional[bool] = ..., unit_cost: _Optional[float] = ..., min_stock: _Optional[float] = ...) -> None: ...

class ProductionBatch(_message.Message):
    __slots__ = ("batch", "product_id", "product_name", "quantity", "manufacture_date", "expiration_date", "production_order_id", "production_order_number")
    BATCH_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURE_DATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    batch: str
    product_id: str
    product_name: str
    quantity: float
    manufacture_date: _timestamp_pb2.Timestamp
    expiration_date: _timestamp_pb2.Timestamp
    production_order_id: str
    production_order_number: int
    def __init__(self, batch: _Optional[str] = ..., product_id: _Optional[str] = ..., product_name: _Optional[str] = ..., quantity: _Optional[float] = ..., manufacture_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expiration_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., production_order_id: _Optional[str] = ..., production_order_number: _Optional[int] = ...) -> None: ...

class CreateProductionOrderRequest(_message.Message):
    __slots__ = ("production_order",)
    PRODUCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    production_order: ProductionOrder
    def __init__(self, production_order: _Optional[_Union[ProductionOrder, _Mapping]] = ...) -> None: ...

class CreateProductionOrderResponse(_message.Message):
    __slots__ = ("production_order",)
    PRODUCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    production_order: ProductionOrder
    def __init__(self, production_order: _Optional[_Union[ProductionOrder, _Mapping]] = ...) -> None: ...

class UpdateProductionOrderRequest(_message.Message):
    __slots__ = ("id", "production_order", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    production_order: ProductionOrder
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., production_order: _Optional[_Union[ProductionOrder, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateProductionOrderResponse(_message.Message):
    __slots__ = ("production_order",)
    PRODUCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    production_order: ProductionOrder
    def __init__(self, production_order: _Optional[_Union[ProductionOrder, _Mapping]] = ...) -> None: ...

class DeleteProductionOrderRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteProductionOrderResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetProductionOrderRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetProductionOrderResponse(_message.Message):
    __slots__ = ("production_order",)
    PRODUCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    production_order: ProductionOrder
    def __init__(self, production_order: _Optional[_Union[ProductionOrder, _Mapping]] = ...) -> None: ...

class ListProductionOrderRequest(_message.Message):
    __slots__ = ("ids", "status", "product_id", "product_name", "batch_code", "created_at_gte", "created_at_lte", "expected_date_gte", "expected_date_lte", "number", "sale_order_id", "only_late", "consumed_batch_number", "sale_order_ids", "with_fulfilled_demands", "sale_order_number", "tags", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    BATCH_CODE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DATE_GTE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DATE_LTE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    SALE_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    ONLY_LATE_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_BATCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SALE_ORDER_IDS_FIELD_NUMBER: _ClassVar[int]
    WITH_FULFILLED_DEMANDS_FIELD_NUMBER: _ClassVar[int]
    SALE_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    status: str
    product_id: str
    product_name: str
    batch_code: str
    created_at_gte: _timestamp_pb2.Timestamp
    created_at_lte: _timestamp_pb2.Timestamp
    expected_date_gte: _timestamp_pb2.Timestamp
    expected_date_lte: _timestamp_pb2.Timestamp
    number: int
    sale_order_id: str
    only_late: bool
    consumed_batch_number: str
    sale_order_ids: _containers.RepeatedScalarFieldContainer[str]
    with_fulfilled_demands: bool
    sale_order_number: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., status: _Optional[str] = ..., product_id: _Optional[str] = ..., product_name: _Optional[str] = ..., batch_code: _Optional[str] = ..., created_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expected_date_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expected_date_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., number: _Optional[int] = ..., sale_order_id: _Optional[str] = ..., only_late: _Optional[bool] = ..., consumed_batch_number: _Optional[str] = ..., sale_order_ids: _Optional[_Iterable[str]] = ..., with_fulfilled_demands: _Optional[bool] = ..., sale_order_number: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListProductionOrderResponse(_message.Message):
    __slots__ = ("production_order_list", "next_page_token")
    PRODUCTION_ORDER_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    production_order_list: _containers.RepeatedCompositeFieldContainer[ProductionOrder]
    next_page_token: str
    def __init__(self, production_order_list: _Optional[_Iterable[_Union[ProductionOrder, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class EstimateProductionRequest(_message.Message):
    __slots__ = ("product_id", "quantity", "explode_sub_assemblies")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    EXPLODE_SUB_ASSEMBLIES_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    quantity: float
    explode_sub_assemblies: bool
    def __init__(self, product_id: _Optional[str] = ..., quantity: _Optional[float] = ..., explode_sub_assemblies: _Optional[bool] = ...) -> None: ...

class EstimateProductionResponse(_message.Message):
    __slots__ = ("product_id", "product_name", "max_quantity", "can_produce", "inputs")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    CAN_PRODUCE_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    product_name: str
    max_quantity: float
    can_produce: bool
    inputs: _containers.RepeatedCompositeFieldContainer[InputAvailability]
    def __init__(self, product_id: _Optional[str] = ..., product_name: _Optional[str] = ..., max_quantity: _Optional[float] = ..., can_produce: _Optional[bool] = ..., inputs: _Optional[_Iterable[_Union[InputAvailability, _Mapping]]] = ...) -> None: ...

class CalculateCostRequest(_message.Message):
    __slots__ = ("id", "labor_cost", "other_cost")
    ID_FIELD_NUMBER: _ClassVar[int]
    LABOR_COST_FIELD_NUMBER: _ClassVar[int]
    OTHER_COST_FIELD_NUMBER: _ClassVar[int]
    id: str
    labor_cost: float
    other_cost: float
    def __init__(self, id: _Optional[str] = ..., labor_cost: _Optional[float] = ..., other_cost: _Optional[float] = ...) -> None: ...

class CalculateCostResponse(_message.Message):
    __slots__ = ("production_order",)
    PRODUCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    production_order: ProductionOrder
    def __init__(self, production_order: _Optional[_Union[ProductionOrder, _Mapping]] = ...) -> None: ...

class StartProductionRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class StartProductionResponse(_message.Message):
    __slots__ = ("production_order",)
    PRODUCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    production_order: ProductionOrder
    def __init__(self, production_order: _Optional[_Union[ProductionOrder, _Mapping]] = ...) -> None: ...

class FinishProductionRequest(_message.Message):
    __slots__ = ("id", "produced_quantity", "batch_code", "batch_manufacture_date", "batch_expiration_date", "notes", "lost_quantity")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    BATCH_CODE_FIELD_NUMBER: _ClassVar[int]
    BATCH_MANUFACTURE_DATE_FIELD_NUMBER: _ClassVar[int]
    BATCH_EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    LOST_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    produced_quantity: float
    batch_code: str
    batch_manufacture_date: _timestamp_pb2.Timestamp
    batch_expiration_date: _timestamp_pb2.Timestamp
    notes: str
    lost_quantity: float
    def __init__(self, id: _Optional[str] = ..., produced_quantity: _Optional[float] = ..., batch_code: _Optional[str] = ..., batch_manufacture_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., batch_expiration_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., lost_quantity: _Optional[float] = ...) -> None: ...

class FinishProductionResponse(_message.Message):
    __slots__ = ("production_order",)
    PRODUCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    production_order: ProductionOrder
    def __init__(self, production_order: _Optional[_Union[ProductionOrder, _Mapping]] = ...) -> None: ...

class CancelProductionRequest(_message.Message):
    __slots__ = ("id", "reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    reason: str
    def __init__(self, id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelProductionResponse(_message.Message):
    __slots__ = ("production_order",)
    PRODUCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    production_order: ProductionOrder
    def __init__(self, production_order: _Optional[_Union[ProductionOrder, _Mapping]] = ...) -> None: ...

class GetByBatchRequest(_message.Message):
    __slots__ = ("batch",)
    BATCH_FIELD_NUMBER: _ClassVar[int]
    batch: str
    def __init__(self, batch: _Optional[str] = ...) -> None: ...

class GetByBatchResponse(_message.Message):
    __slots__ = ("production_order_list",)
    PRODUCTION_ORDER_LIST_FIELD_NUMBER: _ClassVar[int]
    production_order_list: _containers.RepeatedCompositeFieldContainer[ProductionOrder]
    def __init__(self, production_order_list: _Optional[_Iterable[_Union[ProductionOrder, _Mapping]]] = ...) -> None: ...

class ListBatchesRequest(_message.Message):
    __slots__ = ("product_id", "manufacture_date_gte", "manufacture_date_lte", "expiration_date_gte", "expiration_date_lte", "filter")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURE_DATE_GTE_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURE_DATE_LTE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_GTE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_LTE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    manufacture_date_gte: _timestamp_pb2.Timestamp
    manufacture_date_lte: _timestamp_pb2.Timestamp
    expiration_date_gte: _timestamp_pb2.Timestamp
    expiration_date_lte: _timestamp_pb2.Timestamp
    filter: _filter_pb2.Filter
    def __init__(self, product_id: _Optional[str] = ..., manufacture_date_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., manufacture_date_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expiration_date_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expiration_date_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListBatchesResponse(_message.Message):
    __slots__ = ("batches",)
    BATCHES_FIELD_NUMBER: _ClassVar[int]
    batches: _containers.RepeatedCompositeFieldContainer[ProductionBatch]
    def __init__(self, batches: _Optional[_Iterable[_Union[ProductionBatch, _Mapping]]] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("report_type", "list_request")
    REPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    report_type: str
    list_request: ListProductionOrderRequest
    def __init__(self, report_type: _Optional[str] = ..., list_request: _Optional[_Union[ListProductionOrderRequest, _Mapping]] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class GetDefaultCostsRequest(_message.Message):
    __slots__ = ("product_id", "planned_quantity")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PLANNED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    planned_quantity: float
    def __init__(self, product_id: _Optional[str] = ..., planned_quantity: _Optional[float] = ...) -> None: ...

class GetDefaultCostsResponse(_message.Message):
    __slots__ = ("extra_costs",)
    EXTRA_COSTS_FIELD_NUMBER: _ClassVar[int]
    extra_costs: _containers.RepeatedCompositeFieldContainer[ExtraCost]
    def __init__(self, extra_costs: _Optional[_Iterable[_Union[ExtraCost, _Mapping]]] = ...) -> None: ...

class PrintRequest(_message.Message):
    __slots__ = ("id", "ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., ids: _Optional[_Iterable[str]] = ...) -> None: ...

class PrintResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class AddProductionEntryRequest(_message.Message):
    __slots__ = ("id", "good_quantity", "lost_quantity", "allocations", "prioritize_stock", "notes")
    ID_FIELD_NUMBER: _ClassVar[int]
    GOOD_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LOST_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
    PRIORITIZE_STOCK_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    good_quantity: float
    lost_quantity: float
    allocations: _containers.RepeatedCompositeFieldContainer[EntryAllocation]
    prioritize_stock: bool
    notes: str
    def __init__(self, id: _Optional[str] = ..., good_quantity: _Optional[float] = ..., lost_quantity: _Optional[float] = ..., allocations: _Optional[_Iterable[_Union[EntryAllocation, _Mapping]]] = ..., prioritize_stock: _Optional[bool] = ..., notes: _Optional[str] = ...) -> None: ...

class AddProductionEntryResponse(_message.Message):
    __slots__ = ("production_order", "entry")
    PRODUCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    production_order: ProductionOrder
    entry: ProductionEntry
    def __init__(self, production_order: _Optional[_Union[ProductionOrder, _Mapping]] = ..., entry: _Optional[_Union[ProductionEntry, _Mapping]] = ...) -> None: ...

class QuickProductionRequest(_message.Message):
    __slots__ = ("product_id", "quantity", "lost_quantity", "inputs", "batch_code", "batch_manufacture_date", "batch_expiration_date", "input_stock_name", "output_stock_name", "notes", "labor_cost", "extra_costs")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LOST_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    BATCH_CODE_FIELD_NUMBER: _ClassVar[int]
    BATCH_MANUFACTURE_DATE_FIELD_NUMBER: _ClassVar[int]
    BATCH_EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    INPUT_STOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_STOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    LABOR_COST_FIELD_NUMBER: _ClassVar[int]
    EXTRA_COSTS_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    quantity: float
    lost_quantity: float
    inputs: _containers.RepeatedCompositeFieldContainer[ProductionInput]
    batch_code: str
    batch_manufacture_date: _timestamp_pb2.Timestamp
    batch_expiration_date: _timestamp_pb2.Timestamp
    input_stock_name: str
    output_stock_name: str
    notes: str
    labor_cost: float
    extra_costs: _containers.RepeatedCompositeFieldContainer[ExtraCost]
    def __init__(self, product_id: _Optional[str] = ..., quantity: _Optional[float] = ..., lost_quantity: _Optional[float] = ..., inputs: _Optional[_Iterable[_Union[ProductionInput, _Mapping]]] = ..., batch_code: _Optional[str] = ..., batch_manufacture_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., batch_expiration_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., input_stock_name: _Optional[str] = ..., output_stock_name: _Optional[str] = ..., notes: _Optional[str] = ..., labor_cost: _Optional[float] = ..., extra_costs: _Optional[_Iterable[_Union[ExtraCost, _Mapping]]] = ...) -> None: ...

class QuickProductionResponse(_message.Message):
    __slots__ = ("production_order",)
    PRODUCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    production_order: ProductionOrder
    def __init__(self, production_order: _Optional[_Union[ProductionOrder, _Mapping]] = ...) -> None: ...

class GetPendingDemandsRequest(_message.Message):
    __slots__ = ("product_id",)
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class GetPendingDemandsResponse(_message.Message):
    __slots__ = ("products",)
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[PendingDemandProduct]
    def __init__(self, products: _Optional[_Iterable[_Union[PendingDemandProduct, _Mapping]]] = ...) -> None: ...

class PendingDemandProduct(_message.Message):
    __slots__ = ("product_id", "product_name", "product_code", "unit", "total_quantity", "items")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CODE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    product_name: str
    product_code: str
    unit: str
    total_quantity: float
    items: _containers.RepeatedCompositeFieldContainer[PendingDemandItem]
    def __init__(self, product_id: _Optional[str] = ..., product_name: _Optional[str] = ..., product_code: _Optional[str] = ..., unit: _Optional[str] = ..., total_quantity: _Optional[float] = ..., items: _Optional[_Iterable[_Union[PendingDemandItem, _Mapping]]] = ...) -> None: ...

class PendingDemandItem(_message.Message):
    __slots__ = ("sale_order_id", "sale_order_number", "sale_order_item_id", "customer_name", "order_date", "delivery_date", "quantity", "own_composition")
    SALE_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    SALE_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SALE_ORDER_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    ORDER_DATE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_DATE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    OWN_COMPOSITION_FIELD_NUMBER: _ClassVar[int]
    sale_order_id: str
    sale_order_number: int
    sale_order_item_id: str
    customer_name: str
    order_date: _timestamp_pb2.Timestamp
    delivery_date: _timestamp_pb2.Timestamp
    quantity: float
    own_composition: bool
    def __init__(self, sale_order_id: _Optional[str] = ..., sale_order_number: _Optional[int] = ..., sale_order_item_id: _Optional[str] = ..., customer_name: _Optional[str] = ..., order_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., delivery_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., quantity: _Optional[float] = ..., own_composition: _Optional[bool] = ...) -> None: ...

class GenerateFromSaleOrdersRequest(_message.Message):
    __slots__ = ("orders",)
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[GenerateOrderInput]
    def __init__(self, orders: _Optional[_Iterable[_Union[GenerateOrderInput, _Mapping]]] = ...) -> None: ...

class GenerateOrderInput(_message.Message):
    __slots__ = ("product_id", "extra_quantity", "demands", "expected_date", "input_stock_name", "output_stock_name")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DEMANDS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DATE_FIELD_NUMBER: _ClassVar[int]
    INPUT_STOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_STOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    extra_quantity: float
    demands: _containers.RepeatedCompositeFieldContainer[SaleOrderDemandInput]
    expected_date: _timestamp_pb2.Timestamp
    input_stock_name: str
    output_stock_name: str
    def __init__(self, product_id: _Optional[str] = ..., extra_quantity: _Optional[float] = ..., demands: _Optional[_Iterable[_Union[SaleOrderDemandInput, _Mapping]]] = ..., expected_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., input_stock_name: _Optional[str] = ..., output_stock_name: _Optional[str] = ...) -> None: ...

class SaleOrderDemandInput(_message.Message):
    __slots__ = ("sale_order_id", "sale_order_item_id", "quantity")
    SALE_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    SALE_ORDER_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    sale_order_id: str
    sale_order_item_id: str
    quantity: float
    def __init__(self, sale_order_id: _Optional[str] = ..., sale_order_item_id: _Optional[str] = ..., quantity: _Optional[float] = ...) -> None: ...

class GenerateFromSaleOrdersResponse(_message.Message):
    __slots__ = ("production_orders",)
    PRODUCTION_ORDERS_FIELD_NUMBER: _ClassVar[int]
    production_orders: _containers.RepeatedCompositeFieldContainer[ProductionOrder]
    def __init__(self, production_orders: _Optional[_Iterable[_Union[ProductionOrder, _Mapping]]] = ...) -> None: ...

class AddDemandsRequest(_message.Message):
    __slots__ = ("id", "demands", "increase_planned_quantity")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEMANDS_FIELD_NUMBER: _ClassVar[int]
    INCREASE_PLANNED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    demands: _containers.RepeatedCompositeFieldContainer[SaleOrderDemandInput]
    increase_planned_quantity: bool
    def __init__(self, id: _Optional[str] = ..., demands: _Optional[_Iterable[_Union[SaleOrderDemandInput, _Mapping]]] = ..., increase_planned_quantity: _Optional[bool] = ...) -> None: ...

class AddDemandsResponse(_message.Message):
    __slots__ = ("production_order",)
    PRODUCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    production_order: ProductionOrder
    def __init__(self, production_order: _Optional[_Union[ProductionOrder, _Mapping]] = ...) -> None: ...

class RemoveDemandRequest(_message.Message):
    __slots__ = ("id", "demand_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEMAND_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    demand_id: str
    def __init__(self, id: _Optional[str] = ..., demand_id: _Optional[str] = ...) -> None: ...

class RemoveDemandResponse(_message.Message):
    __slots__ = ("production_order",)
    PRODUCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    production_order: ProductionOrder
    def __init__(self, production_order: _Optional[_Union[ProductionOrder, _Mapping]] = ...) -> None: ...

class DashboardRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DashboardResponse(_message.Message):
    __slots__ = ("pending_demand_quantity", "pending_demand_orders", "in_production_count", "in_production_planned", "in_production_produced", "late_count", "ready_to_ship_quantity", "ready_to_ship_orders", "metrics")
    PENDING_DEMAND_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PENDING_DEMAND_ORDERS_FIELD_NUMBER: _ClassVar[int]
    IN_PRODUCTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    IN_PRODUCTION_PLANNED_FIELD_NUMBER: _ClassVar[int]
    IN_PRODUCTION_PRODUCED_FIELD_NUMBER: _ClassVar[int]
    LATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    READY_TO_SHIP_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    READY_TO_SHIP_ORDERS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    pending_demand_quantity: float
    pending_demand_orders: int
    in_production_count: int
    in_production_planned: float
    in_production_produced: float
    late_count: int
    ready_to_ship_quantity: float
    ready_to_ship_orders: int
    metrics: ProductionMetrics
    def __init__(self, pending_demand_quantity: _Optional[float] = ..., pending_demand_orders: _Optional[int] = ..., in_production_count: _Optional[int] = ..., in_production_planned: _Optional[float] = ..., in_production_produced: _Optional[float] = ..., late_count: _Optional[int] = ..., ready_to_ship_quantity: _Optional[float] = ..., ready_to_ship_orders: _Optional[int] = ..., metrics: _Optional[_Union[ProductionMetrics, _Mapping]] = ...) -> None: ...

class ProductionMetrics(_message.Message):
    __slots__ = ("produced_quantity", "lost_quantity", "loss_percentage", "total_cost", "input_cost", "labor_cost", "other_cost", "orders_completed", "planned_total_cost", "monthly", "top_products")
    PRODUCED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LOST_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LOSS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
    INPUT_COST_FIELD_NUMBER: _ClassVar[int]
    LABOR_COST_FIELD_NUMBER: _ClassVar[int]
    OTHER_COST_FIELD_NUMBER: _ClassVar[int]
    ORDERS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    PLANNED_TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_FIELD_NUMBER: _ClassVar[int]
    TOP_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    produced_quantity: float
    lost_quantity: float
    loss_percentage: float
    total_cost: float
    input_cost: float
    labor_cost: float
    other_cost: float
    orders_completed: int
    planned_total_cost: float
    monthly: _containers.RepeatedCompositeFieldContainer[MonthlyProduction]
    top_products: _containers.RepeatedCompositeFieldContainer[TopProduct]
    def __init__(self, produced_quantity: _Optional[float] = ..., lost_quantity: _Optional[float] = ..., loss_percentage: _Optional[float] = ..., total_cost: _Optional[float] = ..., input_cost: _Optional[float] = ..., labor_cost: _Optional[float] = ..., other_cost: _Optional[float] = ..., orders_completed: _Optional[int] = ..., planned_total_cost: _Optional[float] = ..., monthly: _Optional[_Iterable[_Union[MonthlyProduction, _Mapping]]] = ..., top_products: _Optional[_Iterable[_Union[TopProduct, _Mapping]]] = ...) -> None: ...

class MonthlyProduction(_message.Message):
    __slots__ = ("month", "quantity", "cost", "lost_quantity", "unit_cost")
    MONTH_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    LOST_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UNIT_COST_FIELD_NUMBER: _ClassVar[int]
    month: str
    quantity: float
    cost: float
    lost_quantity: float
    unit_cost: float
    def __init__(self, month: _Optional[str] = ..., quantity: _Optional[float] = ..., cost: _Optional[float] = ..., lost_quantity: _Optional[float] = ..., unit_cost: _Optional[float] = ...) -> None: ...

class TopProduct(_message.Message):
    __slots__ = ("product_id", "product_name", "unit", "quantity", "cost")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    product_name: str
    unit: str
    quantity: float
    cost: float
    def __init__(self, product_id: _Optional[str] = ..., product_name: _Optional[str] = ..., unit: _Optional[str] = ..., quantity: _Optional[float] = ..., cost: _Optional[float] = ...) -> None: ...
