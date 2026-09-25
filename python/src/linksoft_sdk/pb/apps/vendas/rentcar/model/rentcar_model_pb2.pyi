import datetime

from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Reservation(_message.Message):
    __slots__ = ("reservation_number", "reference", "start_date", "end_date", "pickup_time", "return_time", "pickup_location", "return_location", "customer_license_num", "customer_license_exp", "customer_date_of_birth", "vehicle_id", "vehicle_make", "vehicle_model", "vehicle_year", "vehicle_type", "vehicle_license_plate", "vehicle_vin", "vehicle_odometer", "vehicle_fuel_level", "extras", "charges", "hq_rental_id", "last_sync_at")
    RESERVATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    PICKUP_TIME_FIELD_NUMBER: _ClassVar[int]
    RETURN_TIME_FIELD_NUMBER: _ClassVar[int]
    PICKUP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    RETURN_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_LICENSE_NUM_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_LICENSE_EXP_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_DATE_OF_BIRTH_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_MAKE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_MODEL_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_YEAR_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_LICENSE_PLATE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_VIN_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ODOMETER_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_FUEL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXTRAS_FIELD_NUMBER: _ClassVar[int]
    CHARGES_FIELD_NUMBER: _ClassVar[int]
    HQ_RENTAL_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_SYNC_AT_FIELD_NUMBER: _ClassVar[int]
    reservation_number: str
    reference: str
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp
    pickup_time: str
    return_time: str
    pickup_location: str
    return_location: str
    customer_license_num: str
    customer_license_exp: _timestamp_pb2.Timestamp
    customer_date_of_birth: _timestamp_pb2.Timestamp
    vehicle_id: str
    vehicle_make: str
    vehicle_model: str
    vehicle_year: int
    vehicle_type: str
    vehicle_license_plate: str
    vehicle_vin: str
    vehicle_odometer: int
    vehicle_fuel_level: str
    extras: _containers.RepeatedCompositeFieldContainer[Extra]
    charges: _containers.RepeatedCompositeFieldContainer[Charge]
    hq_rental_id: str
    last_sync_at: _timestamp_pb2.Timestamp
    def __init__(self, reservation_number: _Optional[str] = ..., reference: _Optional[str] = ..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., pickup_time: _Optional[str] = ..., return_time: _Optional[str] = ..., pickup_location: _Optional[str] = ..., return_location: _Optional[str] = ..., customer_license_num: _Optional[str] = ..., customer_license_exp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., customer_date_of_birth: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., vehicle_id: _Optional[str] = ..., vehicle_make: _Optional[str] = ..., vehicle_model: _Optional[str] = ..., vehicle_year: _Optional[int] = ..., vehicle_type: _Optional[str] = ..., vehicle_license_plate: _Optional[str] = ..., vehicle_vin: _Optional[str] = ..., vehicle_odometer: _Optional[int] = ..., vehicle_fuel_level: _Optional[str] = ..., extras: _Optional[_Iterable[_Union[Extra, _Mapping]]] = ..., charges: _Optional[_Iterable[_Union[Charge, _Mapping]]] = ..., hq_rental_id: _Optional[str] = ..., last_sync_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Extra(_message.Message):
    __slots__ = ("id", "name", "description", "price", "quantity", "total_amount")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    price: float
    quantity: int
    total_amount: float
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ..., total_amount: _Optional[float] = ...) -> None: ...

class Charge(_message.Message):
    __slots__ = ("id", "name", "description", "amount", "type", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    amount: float
    type: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., amount: _Optional[float] = ..., type: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
