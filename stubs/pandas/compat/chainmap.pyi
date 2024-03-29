# Stubs for pandas.compat.chainmap (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,invalid-name
# pylint: disable=relative-beyond-top-level,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin
# pylint: disable=too-many-ancestors
from collections import ChainMap
from typing import Any, Optional


class DeepChainMap(ChainMap):
    def __setitem__(self, key: Any, value: Any) -> None:
        ...

    def __delitem__(self, key: Any) -> None:
        ...

    def new_child(self, m: Optional[Any] = ...) -> Any:
        ...
