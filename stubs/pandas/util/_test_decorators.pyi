# Stubs for pandas.util._test_decorators (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,invalid-name
# pylint: disable=relative-beyond-top-level,arguments-differ
# pylint: disable=no-member,keyword-arg-before-vararg

from typing import Any, Optional

from _pytest.mark.structures import MarkDecorator


def safe_import(mod_name: Any, min_version: Optional[Any] = ...) -> Any:
    ...


def skip_if_installed(package: str) -> MarkDecorator:
    ...


def skip_if_no(
        package: str, min_version: Optional[str] = ...) -> MarkDecorator:
    ...


skip_if_no_mpl: Any
skip_if_mpl: Any
skip_if_32bit: Any
skip_if_windows: Any
skip_if_windows_python_3: Any
skip_if_has_locale: Any
skip_if_not_us_locale: Any
skip_if_no_scipy: Any
skip_if_no_ne: Any


def skip_if_np_lt(
        ver_str: Any, reason: Optional[Any] = ...,
        *args: Any, **kwds: Any) -> Any:
    ...


def parametrize_fixture_doc(*args: Any) -> Any:
    ...