# Stubs for pandas.core.sparse.frame (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,super-init-not-called
from typing import Any, Optional

from pandas.core.frame import DataFrame


depr_msg: str


class SparseDataFrame(DataFrame):
    def __init__(
            self, data: Optional[Any] = ..., index: Optional[Any] = ...,
            columns: Optional[Any] = ...,
            default_kind: Optional[Any] = ...,
            default_fill_value: Optional[Any] = ...,
            dtype: Optional[Any] = ..., copy: bool = ...) -> None:
        ...

    def to_coo(self) -> Any:
        ...

    def to_dense(self) -> Any:
        ...

    @property
    def default_fill_value(self) -> Any:
        ...

    @property
    def default_kind(self) -> Any:
        ...

    @property
    def density(self) -> Any:
        ...

    def get_value(self, index: Any, col: Any, takeable: bool = ...) -> Any:
        ...

    def set_value(
            self, index: Any, col: Any, value: Any,
            takeable: bool = ...) -> Any:
        ...

    def transpose(self, *args: Any, **kwargs: Any) -> Any:
        ...

    T: Any = ...

    def isna(self) -> Any:
        ...

    isnull: Any = ...

    def notna(self) -> Any:
        ...

    notnull: Any = ...


def to_manager(sdf: Any, columns: Any, index: Any) -> Any:
    ...


def stack_sparse_frame(frame: Any) -> Any:
    ...


def homogenize(series_dict: Any) -> Any:
    ...
