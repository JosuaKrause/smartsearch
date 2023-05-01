import time
from typing import Callable, Generic, TypeVar


KT = TypeVar('KT')
VT = TypeVar('VT')


MAX_RETRY = 10
RETRY_WAIT = 0.1


class LRU(Generic[KT, VT]):
    def __init__(
            self,
            max_items: int,
            soft_limit: int | None = None) -> None:
        self._values: dict[KT, VT] = {}
        self._times: dict[KT, float] = {}
        self._max_items = max_items
        self._soft_limit = (
            max(1, int(max_items * 0.9)) if soft_limit is None else soft_limit)
        assert self._max_items >= self._soft_limit

    def get(self, key: KT) -> VT | None:
        res = self._values.get(key)
        if res is not None:
            self._times[key] = time.monotonic()
        return res

    def set(self, key: KT, value: VT) -> None:
        self._values[key] = value
        self._times[key] = time.monotonic()
        self.gc()

    def clear_keys(self, prefix_match: Callable[[KT], bool]) -> None:
        for key in list(self._values.keys()):
            if prefix_match(key):
                # FIXME: mypy bug?
                self._values.pop(key, None)  # type: ignore
                self._times.pop(key, None)

    def gc(self) -> None:
        retry = 0
        while len(self._values) > self._max_items:
            try:
                to_remove = sorted(
                    self._times.copy().items(),
                    key=lambda item: item[1])[:-self._soft_limit]
                for rm_item in to_remove:
                    key = rm_item[0]
                    # FIXME: mypy bug?
                    self._values.pop(key, None)  # type: ignore
                    self._times.pop(key, None)
            except RuntimeError:
                # dictionary changed size during iteration: try again
                if retry >= MAX_RETRY:
                    raise
                retry += 1
                if RETRY_WAIT > 0:
                    time.sleep(RETRY_WAIT)
