import datetime

from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VehicleStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_UNSPECIFIED: _ClassVar[VehicleStatus]
    STATUS_AVAILABLE: _ClassVar[VehicleStatus]
    STATUS_RESERVED: _ClassVar[VehicleStatus]
    STATUS_RENTED: _ClassVar[VehicleStatus]
    STATUS_MAINTENANCE: _ClassVar[VehicleStatus]
    STATUS_INACTIVE: _ClassVar[VehicleStatus]

class VehicleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_UNSPECIFIED: _ClassVar[VehicleType]
    TYPE_COMPACT: _ClassVar[VehicleType]
    TYPE_SEDAN: _ClassVar[VehicleType]
    TYPE_SUV: _ClassVar[VehicleType]
    TYPE_LUXURY: _ClassVar[VehicleType]
    TYPE_VAN: _ClassVar[VehicleType]
    TYPE_TRUCK: _ClassVar[VehicleType]
    TYPE_CONVERTIBLE: _ClassVar[VehicleType]
    TYPE_SPORTS: _ClassVar[VehicleType]
    TYPE_ELECTRIC: _ClassVar[VehicleType]
    TYPE_HYBRID: _ClassVar[VehicleType]

class FuelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FUEL_TYPE_UNSPECIFIED: _ClassVar[FuelType]
    FUEL_TYPE_GASOLINE: _ClassVar[FuelType]
    FUEL_TYPE_DIESEL: _ClassVar[FuelType]
    FUEL_TYPE_ELECTRIC: _ClassVar[FuelType]
    FUEL_TYPE_HYBRID: _ClassVar[FuelType]
    FUEL_TYPE_ETHANOL: _ClassVar[FuelType]
    FUEL_TYPE_FLEX: _ClassVar[FuelType]
    FUEL_TYPE_CNG: _ClassVar[FuelType]

class MaintenanceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MAINTENANCE_TYPE_UNSPECIFIED: _ClassVar[MaintenanceType]
    MAINTENANCE_TYPE_REGULAR: _ClassVar[MaintenanceType]
    MAINTENANCE_TYPE_REPAIR: _ClassVar[MaintenanceType]
    MAINTENANCE_TYPE_INSPECTION: _ClassVar[MaintenanceType]
    MAINTENANCE_TYPE_CLEANING: _ClassVar[MaintenanceType]
    MAINTENANCE_TYPE_ACCIDENT: _ClassVar[MaintenanceType]
STATUS_UNSPECIFIED: VehicleStatus
STATUS_AVAILABLE: VehicleStatus
STATUS_RESERVED: VehicleStatus
STATUS_RENTED: VehicleStatus
STATUS_MAINTENANCE: VehicleStatus
STATUS_INACTIVE: VehicleStatus
TYPE_UNSPECIFIED: VehicleType
TYPE_COMPACT: VehicleType
TYPE_SEDAN: VehicleType
TYPE_SUV: VehicleType
TYPE_LUXURY: VehicleType
TYPE_VAN: VehicleType
TYPE_TRUCK: VehicleType
TYPE_CONVERTIBLE: VehicleType
TYPE_SPORTS: VehicleType
TYPE_ELECTRIC: VehicleType
TYPE_HYBRID: VehicleType
FUEL_TYPE_UNSPECIFIED: FuelType
FUEL_TYPE_GASOLINE: FuelType
FUEL_TYPE_DIESEL: FuelType
FUEL_TYPE_ELECTRIC: FuelType
FUEL_TYPE_HYBRID: FuelType
FUEL_TYPE_ETHANOL: FuelType
FUEL_TYPE_FLEX: FuelType
FUEL_TYPE_CNG: FuelType
MAINTENANCE_TYPE_UNSPECIFIED: MaintenanceType
MAINTENANCE_TYPE_REGULAR: MaintenanceType
MAINTENANCE_TYPE_REPAIR: MaintenanceType
MAINTENANCE_TYPE_INSPECTION: MaintenanceType
MAINTENANCE_TYPE_CLEANING: MaintenanceType
MAINTENANCE_TYPE_ACCIDENT: MaintenanceType

class VehicleData(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "fields", "make", "model", "year", "type", "color", "license_plate", "vin", "odometer", "fuel_type", "fuel_level", "seats", "doors", "has_air_conditioning", "has_gps", "has_bluetooth", "has_automatic_transmission", "status", "location", "daily_rate", "weekly_rate", "monthly_rate", "currency", "features", "image_url", "notes", "maintenance_history", "hq_rental_id", "last_sync_at")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    MAKE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    LICENSE_PLATE_FIELD_NUMBER: _ClassVar[int]
    VIN_FIELD_NUMBER: _ClassVar[int]
    ODOMETER_FIELD_NUMBER: _ClassVar[int]
    FUEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    FUEL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SEATS_FIELD_NUMBER: _ClassVar[int]
    DOORS_FIELD_NUMBER: _ClassVar[int]
    HAS_AIR_CONDITIONING_FIELD_NUMBER: _ClassVar[int]
    HAS_GPS_FIELD_NUMBER: _ClassVar[int]
    HAS_BLUETOOTH_FIELD_NUMBER: _ClassVar[int]
    HAS_AUTOMATIC_TRANSMISSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DAILY_RATE_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_RATE_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_RATE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    HQ_RENTAL_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_SYNC_AT_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    fields: _metadata_pb2.BasicFields
    make: str
    model: str
    year: int
    type: VehicleType
    color: str
    license_plate: str
    vin: str
    odometer: int
    fuel_type: FuelType
    fuel_level: str
    seats: int
    doors: int
    has_air_conditioning: bool
    has_gps: bool
    has_bluetooth: bool
    has_automatic_transmission: bool
    status: VehicleStatus
    location: str
    daily_rate: float
    weekly_rate: float
    monthly_rate: float
    currency: str
    features: _containers.RepeatedScalarFieldContainer[str]
    image_url: str
    notes: str
    maintenance_history: _containers.RepeatedCompositeFieldContainer[Maintenance]
    hq_rental_id: str
    last_sync_at: _timestamp_pb2.Timestamp
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., make: _Optional[str] = ..., model: _Optional[str] = ..., year: _Optional[int] = ..., type: _Optional[_Union[VehicleType, str]] = ..., color: _Optional[str] = ..., license_plate: _Optional[str] = ..., vin: _Optional[str] = ..., odometer: _Optional[int] = ..., fuel_type: _Optional[_Union[FuelType, str]] = ..., fuel_level: _Optional[str] = ..., seats: _Optional[int] = ..., doors: _Optional[int] = ..., has_air_conditioning: _Optional[bool] = ..., has_gps: _Optional[bool] = ..., has_bluetooth: _Optional[bool] = ..., has_automatic_transmission: _Optional[bool] = ..., status: _Optional[_Union[VehicleStatus, str]] = ..., location: _Optional[str] = ..., daily_rate: _Optional[float] = ..., weekly_rate: _Optional[float] = ..., monthly_rate: _Optional[float] = ..., currency: _Optional[str] = ..., features: _Optional[_Iterable[str]] = ..., image_url: _Optional[str] = ..., notes: _Optional[str] = ..., maintenance_history: _Optional[_Iterable[_Union[Maintenance, _Mapping]]] = ..., hq_rental_id: _Optional[str] = ..., last_sync_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Maintenance(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "type", "description", "start_date", "end_date", "completed", "cost", "notes", "odometer")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    ODOMETER_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    type: MaintenanceType
    description: str
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp
    completed: bool
    cost: float
    notes: str
    odometer: int
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., type: _Optional[_Union[MaintenanceType, str]] = ..., description: _Optional[str] = ..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completed: _Optional[bool] = ..., cost: _Optional[float] = ..., notes: _Optional[str] = ..., odometer: _Optional[int] = ...) -> None: ...
