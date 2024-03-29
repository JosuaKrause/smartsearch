# Stubs for pandas.core.arrays.datetimes (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-import,unused-argument,invalid-name,redefined-builtin
# pylint: disable=too-few-public-methods,function-redefined
# pylint: disable=redefined-outer-name,too-many-ancestors,super-init-not-called
# pylint: disable=too-many-arguments,inconsistent-mro
from typing import Any, Optional

import numpy as np
from pandas.core.arrays import datetimelike as dtl
from pandas.core.dtypes.dtypes import DatetimeTZDtype


def tz_to_dtype(tz: Any) -> Any:
    ...


class DatetimeArray(
        dtl.DatetimeLikeArrayMixin,
        dtl.TimelikeOps,
        dtl.DatelikeOps):
    __array_priority__: int = ...

    def __init__(
            self, values: Any, dtype: Any = ...,
            freq: Optional[Any] = ...,
            copy: bool = ...) -> None:
        ...

    @property
    def tz(self) -> Any:
        ...

    @tz.setter
    def tz(self, value: Any) -> None:
        ...

    @property
    def tzinfo(self) -> Any:
        ...

    @property
    def is_normalized(self) -> Any:
        ...

    def __array__(self, dtype: Optional[Any] = ...) -> Any:
        ...

    def __iter__(self) -> None:
        ...

    def astype(self, dtype: Any, copy: bool = ...) -> Any:
        ...

    def tz_convert(self, tz: Any) -> Any:
        ...

    def tz_localize(
            self, tz: Any, ambiguous: str = ...,
            nonexistent: str = ...,
            errors: Optional[Any] = ...) -> Any:
        ...

    def to_pydatetime(self) -> Any:
        ...

    def normalize(self) -> Any:
        ...

    def to_period(self, freq: Optional[Any] = ...) -> Any:
        ...

    def to_perioddelta(self, freq: Any) -> Any:
        ...

    def month_name(self, locale: Optional[Any] = ...) -> Any:
        ...

    def day_name(self, locale: Optional[Any] = ...) -> Any:
        ...

    @property
    def time(self) -> Any:
        ...

    @property
    def timetz(self) -> Any:
        ...

    @property
    def date(self) -> Any:
        ...

    year: Any = ...
    month: Any = ...
    day: Any = ...
    hour: Any = ...
    minute: Any = ...
    second: Any = ...
    microsecond: Any = ...
    nanosecond: Any = ...
    weekofyear: Any = ...
    week: Any = ...
    dayofweek: Any = ...
    weekday: Any = ...
    weekday_name: Any = ...
    dayofyear: Any = ...
    quarter: Any = ...
    days_in_month: Any = ...
    daysinmonth: Any = ...
    is_month_start: Any = ...
    is_month_end: Any = ...
    is_quarter_start: Any = ...
    is_quarter_end: Any = ...
    is_year_start: Any = ...
    is_year_end: Any = ...
    is_leap_year: Any = ...

    def to_julian_date(self) -> Any:
        ...


def sequence_to_dt64ns(
        data: Any, dtype: Optional[Any] = ..., copy: bool = ...,
        tz: Optional[Any] = ..., dayfirst: bool = ..., yearfirst: bool = ...,
        ambiguous: str = ..., int_as_wall_time: bool = ...) -> Any:
    ...


def objects_to_datetime64ns(
        data: Any, dayfirst: Any, yearfirst: Any, utc: bool = ...,
        errors: str = ..., require_iso8601: bool = ...,
        allow_object: bool = ...) -> Any:
    ...


def maybe_convert_dtype(data: Any, copy: Any) -> Any:
    ...


def maybe_infer_tz(tz: Any, inferred_tz: Any) -> Any:
    ...


def validate_tz_from_dtype(dtype: Any, tz: Any) -> Any:
    ...
