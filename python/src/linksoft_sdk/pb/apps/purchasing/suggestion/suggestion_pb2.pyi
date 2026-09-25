from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SuggestionMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUGGESTION_METHOD_UNSPECIFIED: _ClassVar[SuggestionMethod]
    SUGGESTION_METHOD_MIN_MAX: _ClassVar[SuggestionMethod]
    SUGGESTION_METHOD_REORDER_POINT: _ClassVar[SuggestionMethod]
    SUGGESTION_METHOD_DEMAND_FORECAST: _ClassVar[SuggestionMethod]

class AbcClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ABC_CLASS_UNSPECIFIED: _ClassVar[AbcClass]
    ABC_CLASS_A: _ClassVar[AbcClass]
    ABC_CLASS_B: _ClassVar[AbcClass]
    ABC_CLASS_C: _ClassVar[AbcClass]
SUGGESTION_METHOD_UNSPECIFIED: SuggestionMethod
SUGGESTION_METHOD_MIN_MAX: SuggestionMethod
SUGGESTION_METHOD_REORDER_POINT: SuggestionMethod
SUGGESTION_METHOD_DEMAND_FORECAST: SuggestionMethod
ABC_CLASS_UNSPECIFIED: AbcClass
ABC_CLASS_A: AbcClass
ABC_CLASS_B: AbcClass
ABC_CLASS_C: AbcClass

class AnalisarRequest(_message.Message):
    __slots__ = ("method", "category_ids", "product_ids", "lead_time_days", "coverage_days", "analysis_window_days", "only_to_buy", "explode_composition")
    METHOD_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_IDS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_IDS_FIELD_NUMBER: _ClassVar[int]
    LEAD_TIME_DAYS_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_DAYS_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_WINDOW_DAYS_FIELD_NUMBER: _ClassVar[int]
    ONLY_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    EXPLODE_COMPOSITION_FIELD_NUMBER: _ClassVar[int]
    method: SuggestionMethod
    category_ids: _containers.RepeatedScalarFieldContainer[str]
    product_ids: _containers.RepeatedScalarFieldContainer[str]
    lead_time_days: int
    coverage_days: int
    analysis_window_days: int
    only_to_buy: bool
    explode_composition: bool
    def __init__(self, method: _Optional[_Union[SuggestionMethod, str]] = ..., category_ids: _Optional[_Iterable[str]] = ..., product_ids: _Optional[_Iterable[str]] = ..., lead_time_days: _Optional[int] = ..., coverage_days: _Optional[int] = ..., analysis_window_days: _Optional[int] = ..., only_to_buy: _Optional[bool] = ..., explode_composition: _Optional[bool] = ...) -> None: ...

class AnalisarResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SuggestionItem]
    def __init__(self, items: _Optional[_Iterable[_Union[SuggestionItem, _Mapping]]] = ...) -> None: ...

class SuggestionItem(_message.Message):
    __slots__ = ("product_id", "product_code", "product_name", "unit", "category_name", "current_stock", "minimum_stock", "maximum_stock", "average_daily_consumption", "reorder_point", "suggested_quantity", "abc_class", "last_purchase_price", "estimated_cost", "vendor_id", "vendor_name", "source_product_id", "source_product_name")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CODE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STOCK_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_STOCK_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_STOCK_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_DAILY_CONSUMPTION_FIELD_NUMBER: _ClassVar[int]
    REORDER_POINT_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ABC_CLASS_FIELD_NUMBER: _ClassVar[int]
    LAST_PURCHASE_PRICE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_COST_FIELD_NUMBER: _ClassVar[int]
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    product_code: str
    product_name: str
    unit: str
    category_name: str
    current_stock: float
    minimum_stock: float
    maximum_stock: float
    average_daily_consumption: float
    reorder_point: float
    suggested_quantity: float
    abc_class: AbcClass
    last_purchase_price: float
    estimated_cost: float
    vendor_id: str
    vendor_name: str
    source_product_id: str
    source_product_name: str
    def __init__(self, product_id: _Optional[str] = ..., product_code: _Optional[str] = ..., product_name: _Optional[str] = ..., unit: _Optional[str] = ..., category_name: _Optional[str] = ..., current_stock: _Optional[float] = ..., minimum_stock: _Optional[float] = ..., maximum_stock: _Optional[float] = ..., average_daily_consumption: _Optional[float] = ..., reorder_point: _Optional[float] = ..., suggested_quantity: _Optional[float] = ..., abc_class: _Optional[_Union[AbcClass, str]] = ..., last_purchase_price: _Optional[float] = ..., estimated_cost: _Optional[float] = ..., vendor_id: _Optional[str] = ..., vendor_name: _Optional[str] = ..., source_product_id: _Optional[str] = ..., source_product_name: _Optional[str] = ...) -> None: ...

class GerarPedidosRequest(_message.Message):
    __slots__ = ("items", "group_by_vendor")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_VENDOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[GerarPedidoItem]
    group_by_vendor: bool
    def __init__(self, items: _Optional[_Iterable[_Union[GerarPedidoItem, _Mapping]]] = ..., group_by_vendor: _Optional[bool] = ...) -> None: ...

class GerarPedidoItem(_message.Message):
    __slots__ = ("product_id", "product_code", "product_name", "unit", "quantity", "unit_price", "vendor_id", "vendor_name")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CODE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UNIT_PRICE_FIELD_NUMBER: _ClassVar[int]
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_NAME_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    product_code: str
    product_name: str
    unit: str
    quantity: float
    unit_price: float
    vendor_id: str
    vendor_name: str
    def __init__(self, product_id: _Optional[str] = ..., product_code: _Optional[str] = ..., product_name: _Optional[str] = ..., unit: _Optional[str] = ..., quantity: _Optional[float] = ..., unit_price: _Optional[float] = ..., vendor_id: _Optional[str] = ..., vendor_name: _Optional[str] = ...) -> None: ...

class GerarPedidosResponse(_message.Message):
    __slots__ = ("purchase_order_ids", "total_orders")
    PURCHASE_ORDER_IDS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ORDERS_FIELD_NUMBER: _ClassVar[int]
    purchase_order_ids: _containers.RepeatedScalarFieldContainer[str]
    total_orders: int
    def __init__(self, purchase_order_ids: _Optional[_Iterable[str]] = ..., total_orders: _Optional[int] = ...) -> None: ...

class GerarCotacaoRequest(_message.Message):
    __slots__ = ("items", "title")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[GerarPedidoItem]
    title: str
    def __init__(self, items: _Optional[_Iterable[_Union[GerarPedidoItem, _Mapping]]] = ..., title: _Optional[str] = ...) -> None: ...

class GerarCotacaoResponse(_message.Message):
    __slots__ = ("quotation_id", "quotation_number")
    QUOTATION_ID_FIELD_NUMBER: _ClassVar[int]
    QUOTATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    quotation_id: str
    quotation_number: int
    def __init__(self, quotation_id: _Optional[str] = ..., quotation_number: _Optional[int] = ...) -> None: ...
