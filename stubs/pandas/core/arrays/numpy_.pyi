# Stubs for pandas.core.arrays.numpy_ (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-import,unused-argument,invalid-name,redefined-builtin
# pylint: disable=too-few-public-methods,function-redefined
# pylint: disable=redefined-outer-name,too-many-ancestors,super-init-not-called
# pylint: disable=too-many-arguments

from typing import Any, Optional

from numpy.lib.mixins import NDArrayOperatorsMixin
from pandas.core.arrays.base import ExtensionArray, ExtensionOpsMixin
from pandas.core.dtypes.dtypes import ExtensionDtype


class PandasDtype(ExtensionDtype):
    def __init__(self, dtype: Any) -> None:
        ...

    @property
    def numpy_dtype(self) -> Any:
        ...

    @property
    def name(self) -> Any:
        ...

    @property
    def type(self) -> Any:
        ...

    @classmethod
    def construct_from_string(cls, string: Any) -> Any:
        ...

    @classmethod
    def construct_array_type(cls) -> Any:
        ...

    @property
    def kind(self) -> Any:
        ...

    @property
    def itemsize(self) -> Any:
        ...


class PandasArray(ExtensionArray, ExtensionOpsMixin, NDArrayOperatorsMixin):
    __array_priority__: int = ...

    def __init__(self, values: Any, copy: bool = ...) -> None:
        ...

    @property
    def dtype(self) -> Any:
        ...

    def __array__(self, dtype: Optional[Any] = ...) -> Any:
        ...

    def __array_ufunc__(
            self, ufunc: Any, method: Any, *inputs: Any,
            **kwargs: Any) -> Any:
        ...

    def __getitem__(self, item: Any) -> Any:
        ...

    def __setitem__(self, key: Any, value: Any) -> None:
        ...

    def __len__(self) -> Any:
        ...

    @property
    def nbytes(self) -> Any:
        ...

    def isna(self) -> Any:
        ...

    def fillna(
            self, value: Optional[Any] = ..., method: Optional[Any] = ...,
            limit: Optional[Any] = ...) -> Any:
        ...

    def copy(self) -> Any:
        ...

    def unique(self) -> Any:
        ...

    def any(
            self, axis: Optional[Any] = ..., out: Optional[Any] = ...,
            keepdims: bool = ..., skipna: bool = ...) -> Any:
        ...

    def all(
            self, axis: Optional[Any] = ..., out: Optional[Any] = ...,
            keepdims: bool = ..., skipna: bool = ...) -> Any:
        ...

    def min(
            self, axis: Optional[Any] = ..., out: Optional[Any] = ...,
            keepdims: bool = ..., skipna: bool = ...) -> Any:
        ...

    def max(
            self, axis: Optional[Any] = ..., out: Optional[Any] = ...,
            keepdims: bool = ..., skipna: bool = ...) -> Any:
        ...

    def sum(
            self, axis: Optional[Any] = ..., dtype: Optional[Any] = ...,
            out: Optional[Any] = ..., keepdims: bool = ...,
            initial: Optional[Any] = ..., skipna: bool = ...,
            min_count: int = ...) -> Any:
        ...

    def prod(
            self, axis: Optional[Any] = ..., dtype: Optional[Any] = ...,
            out: Optional[Any] = ..., keepdims: bool = ...,
            initial: Optional[Any] = ..., skipna: bool = ...,
            min_count: int = ...) -> Any:
        ...

    def mean(
            self, axis: Optional[Any] = ..., dtype: Optional[Any] = ...,
            out: Optional[Any] = ..., keepdims: bool = ...,
            skipna: bool = ...) -> Any:
        ...

    def median(
            self, axis: Optional[Any] = ..., out: Optional[Any] = ...,
            overwrite_input: bool = ..., keepdims: bool = ...,
            skipna: bool = ...) -> Any:
        ...

    def std(
            self, axis: Optional[Any] = ..., dtype: Optional[Any] = ...,
            out: Optional[Any] = ..., ddof: int = ..., keepdims: bool = ...,
            skipna: bool = ...) -> Any:
        ...

    def var(
            self, axis: Optional[Any] = ..., dtype: Optional[Any] = ...,
            out: Optional[Any] = ..., ddof: int = ..., keepdims: bool = ...,
            skipna: bool = ...) -> Any:
        ...

    def sem(
            self, axis: Optional[Any] = ..., dtype: Optional[Any] = ...,
            out: Optional[Any] = ..., ddof: int = ..., keepdims: bool = ...,
            skipna: bool = ...) -> Any:
        ...

    def kurt(
            self, axis: Optional[Any] = ..., dtype: Optional[Any] = ...,
            out: Optional[Any] = ..., keepdims: bool = ...,
            skipna: bool = ...) -> Any:
        ...

    def skew(
            self, axis: Optional[Any] = ..., dtype: Optional[Any] = ...,
            out: Optional[Any] = ..., keepdims: bool = ...,
            skipna: bool = ...) -> Any:
        ...

    def searchsorted(
            self, value: Any, side: str = ...,
            sorter: Optional[Any] = ...) -> Any:
        ...

    def __invert__(self) -> Any:
        ...
