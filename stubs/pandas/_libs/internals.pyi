# Stubs for pandas.core.indexing (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument

from typing import Any


class BlockPlacement:
    def __init__(self, val: Any) -> None:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def __len__(self) -> int:
        ...

    def __iter__(self) -> Any:
        ...

    @property
    def as_slice(self) -> Any:
        ...

    @property
    def indexer(self) -> Any:
        ...

    def isin(self, arr: Any) -> Any:
        ...

    @property
    def as_array(self) -> Any:
        ...

    @property
    def is_slice_like(self) -> bool:
        ...

    def __getitem__(self, loc: Any) -> Any:
        ...

    def delete(self, loc: Any) -> Any:
        ...

    def append(self, others: Any) -> Any:
        ...

    def add(self, other: Any) -> Any:
        ...

    def sub(self, other: Any) -> Any:
        ...