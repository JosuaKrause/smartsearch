# Stubs for pandas.plotting._matplotlib.hist (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,invalid-name
# pylint: disable=relative-beyond-top-level,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin
# pylint: disable=unused-import,useless-import-alias,signature-differs
# pylint: disable=blacklisted-name,c-extension-no-member,import-error
from typing import Any, Optional

from pandas.plotting._matplotlib.core import LinePlot


class HistPlot(LinePlot):
    bins: Any = ...
    bottom: Any = ...

    def __init__(
            self, data: Any, bins: int = ...,
            bottom: int = ..., **kwargs: Any) -> None:
        ...

    @property
    def orientation(self) -> Any:
        ...


class KdePlot(HistPlot):
    orientation: str = ...
    bw_method: Any = ...
    ind: Any = ...

    def __init__(
            self, data: Any, bw_method: Optional[Any] = ...,
            ind: Optional[Any] = ..., **kwargs: Any) -> None:
        ...


def hist_series(
        self: Any, by: Optional[Any] = ..., ax: Optional[Any] = ...,
        grid: bool = ..., xlabelsize: Optional[Any] = ...,
        xrot: Optional[Any] = ..., ylabelsize: Optional[Any] = ...,
        yrot: Optional[Any] = ..., figsize: Optional[Any] = ...,
        bins: int = ..., **kwds: Any) -> Any:
    ...


def hist_frame(
        data: Any, column: Optional[Any] = ..., by: Optional[Any] = ...,
        grid: bool = ..., xlabelsize: Optional[Any] = ...,
        xrot: Optional[Any] = ..., ylabelsize: Optional[Any] = ...,
        yrot: Optional[Any] = ..., ax: Optional[Any] = ...,
        sharex: bool = ..., sharey: bool = ..., figsize: Optional[Any] = ...,
        layout: Optional[Any] = ..., bins: int = ..., **kwds: Any) -> Any:
    ...