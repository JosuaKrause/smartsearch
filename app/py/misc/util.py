import contextlib
import hashlib
import inspect
import json
import os
import re
import string
import threading
import uuid
from typing import Any, Callable, IO, Iterable, Iterator, Type, TypeVar

import numpy as np
import pandas as pd
import torch
from py.misc.io import open_read


ET = TypeVar('ET')
CT = TypeVar('CT')
RT = TypeVar('RT')
VT = TypeVar('VT')
DT = TypeVar('DT', bound=pd.DataFrame | pd.Series)


NL = "\n"


TEST_SALT_LOCK = threading.RLock()
TEST_SALT: dict[str, str] = {}


def is_test() -> bool:
    test_id = os.getenv("PYTEST_CURRENT_TEST")
    return test_id is not None


def get_test_salt() -> str | None:
    test_id = os.getenv("PYTEST_CURRENT_TEST")
    if test_id is None:
        return None
    res = TEST_SALT.get(test_id)
    if res is None:
        with TEST_SALT_LOCK:
            res = TEST_SALT.get(test_id)
            if res is None:
                res = f"salt:{uuid.uuid4().hex}"
                TEST_SALT[test_id] = res
    return res


def get_text_hash(text: str) -> str:
    blake = hashlib.blake2b(digest_size=32)
    blake.update(text.encode("utf-8"))
    return blake.hexdigest()


def text_hash_size() -> int:
    return 64


def get_short_hash(text: str) -> str:
    blake = hashlib.blake2b(digest_size=4)
    blake.update(text.encode("utf-8"))
    return blake.hexdigest()


def short_hash_size() -> int:
    return 8


BUFF_SIZE = 65536  # 64KiB


def get_file_hash(fname: str) -> str:
    blake = hashlib.blake2b(digest_size=32)
    with open_read(fname, text=False) as fin:
        while True:
            buff = fin.read(BUFF_SIZE)
            if not buff:
                break
            blake.update(buff)
    return blake.hexdigest()


def file_hash_size() -> int:
    return 64


def is_hex(text: str) -> bool:
    hex_digits = set(string.hexdigits)
    return all(char in hex_digits for char in text)


def as_df(series: pd.Series) -> pd.DataFrame:
    return series.to_frame().T


def fillnonnum(df: DT, val: float) -> DT:
    return df.replace([-np.inf, np.inf], np.nan).fillna(val)


def only(arr: list[RT]) -> RT:
    if len(arr) != 1:
        raise ValueError(f"array must have exactly one element: {arr}")
    return arr[0]


# time units for logging request durations
ELAPSED_UNITS: list[tuple[int, str]] = [
    (1, "s"),
    (60, "m"),
    (60*60, "h"),
    (60*60*24, "d"),
]


def elapsed_time_string(elapsed: float) -> str:
    """Convert elapsed time into a readable string."""
    cur = ""
    for (conv, unit) in ELAPSED_UNITS:
        if elapsed / conv >= 1 or not cur:
            cur = f"{elapsed / conv:8.3f}{unit}"
        else:
            break
    return cur


def to_bool(value: bool | float | int | str) -> bool:
    value = f"{value}".lower()
    if value == "true":
        return True
    if value == "false":
        return False
    try:
        return bool(int(float(value)))
    except ValueError:
        pass
    raise ValueError(f"{value} cannot be interpreted as bool")


def to_list(value: Any) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{value} is not a list")
    return value


def is_int(value: Any) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_float(value: Any) -> bool:
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def is_json(value: str) -> bool:
    try:
        json.loads(value)
    except json.JSONDecodeError:
        return False
    return True


def report_json_error(err: json.JSONDecodeError) -> None:
    raise ValueError(
        f"JSON parse error ({err.lineno}:{err.colno}): "
        f"{repr(err.doc)}") from err


def json_maybe_read(data: str) -> Any | None:
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return None


def json_load(fin: IO[str]) -> Any:
    try:
        return json.load(fin)
    except json.JSONDecodeError as e:
        report_json_error(e)
        raise e


def json_dump(obj: Any, fout: IO[str]) -> None:
    print(json_pretty(obj), file=fout)


def json_pretty(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, indent=2)


def json_compact(obj: Any) -> bytes:
    return json.dumps(
        obj,
        sort_keys=True,
        indent=None,
        separators=(',', ':')).encode("utf-8")


def json_read(data: bytes) -> Any:
    try:
        return json.loads(data.decode("utf-8"))
    except json.JSONDecodeError as e:
        report_json_error(e)
        raise e


def read_jsonl(fin: IO[str]) -> Iterable[Any]:
    for line in fin:
        line = line.rstrip()
        if not line:
            continue
        try:
            yield json.loads(line)
        except json.JSONDecodeError as e:
            report_json_error(e)
            raise e


UNIX_EPOCH = pd.Timestamp("1970-01-01", tz="UTC")


def from_timestamp(timestamp: float) -> pd.Timestamp:
    return pd.to_datetime(timestamp, unit="s", utc=True)


def to_timestamp(time: pd.Timestamp) -> float:
    return (time - UNIX_EPOCH) / pd.Timedelta("1s")


def now_ts() -> pd.Timestamp:
    return pd.Timestamp("now", tz="UTC")


def get_function_info(*, clazz: Type) -> tuple[str, int, str]:
    stack = inspect.stack()

    def get_method(cur_clazz: Type) -> tuple[str, int, str] | None:
        class_filename = inspect.getfile(cur_clazz)
        for level in stack:
            if os.path.samefile(level.filename, class_filename):
                return level.filename, level.lineno, level.function
        return None

    queue = [clazz]
    while queue:
        cur = queue.pop(0)
        res = get_method(cur)
        if res is not None:
            return res
        queue.extend(cur.__bases__)
    frame = stack[1]
    return frame.filename, frame.lineno, frame.function


def get_relative_function_info(
        depth: int) -> tuple[str, int, str, dict[str, Any]]:
    depth += 1
    stack = inspect.stack()
    if depth >= len(stack):
        return "unknown", -1, "unknown", {}
    frame = stack[depth]
    return frame.filename, frame.lineno, frame.function, frame.frame.f_locals


def identity(obj: RT) -> RT:
    return obj


def sigmoid(x: Any) -> Any:
    return np.exp(-np.logaddexp(0, -x))


NUMBER_PATTERN = re.compile(r"\d+")


def extract_list(
        arr: Iterable[str],
        prefix: str | None = None,
        postfix: str | None = None) -> Iterable[tuple[str, str]]:
    if not arr:
        yield from []
        return

    for elem in arr:
        text = elem
        if prefix is not None:
            if not text.startswith(prefix):
                continue
            text = text[len(prefix):]
        if postfix is not None:
            if not text.endswith(postfix):
                continue
            text = text[:-len(postfix)]
        yield (elem, text)


def extract_number(
        arr: Iterable[str],
        prefix: str | None = None,
        postfix: str | None = None) -> Iterable[tuple[str, int]]:

    def get_num(text: str) -> int | None:
        match = re.search(NUMBER_PATTERN, text)
        if match is None:
            return None
        try:
            return int(match.group())
        except ValueError:
            return None

    for elem, text in extract_list(arr, prefix=prefix, postfix=postfix):
        num = get_num(text)
        if num is None:
            continue
        yield elem, num


def highest_number(
        arr: Iterable[str],
        prefix: str | None = None,
        postfix: str | None = None) -> tuple[str, int] | None:
    res = None
    res_num = 0
    for elem, num in extract_number(arr, prefix=prefix, postfix=postfix):
        if res is None or num > res_num:
            res = elem
            res_num = num
    return None if res is None else (res, res_num)


def retain_some(
        arr: Iterable[VT],
        count: int,
        *,
        key: Callable[[VT], Any],
        reverse: bool = False,
        keep_last: bool = True) -> tuple[list[VT], list[VT]]:
    res: list[VT] = []
    to_delete: list[VT] = []
    if keep_last:
        for elem in arr:
            if len(res) <= count:
                res.append(elem)
                continue
            res.sort(key=key, reverse=reverse)
            to_delete.extend(res[:-count])
            res = res[-count:]
            res.append(elem)
    else:
        for elem in arr:
            res.append(elem)
            if len(res) < count:
                continue
            res.sort(key=key, reverse=reverse)
            to_delete.extend(res[:-count])
            res = res[-count:]
    res.sort(key=key, reverse=reverse)
    return res, to_delete


def safe_ravel(x: torch.Tensor) -> torch.Tensor:
    if len(x.shape) == 1:
        return x
    shape = torch.Tensor(list(x.shape)).int()
    if torch.max(shape).item() != torch.prod(shape).item():
        raise ValueError(f"not safe to ravel shape {shape.tolist()}")
    return x.ravel()


def python_module() -> str:
    stack = inspect.stack()
    module = inspect.getmodule(stack[1][0])
    if module is None:
        raise ValueError("module not found")
    res = module.__name__
    if res != "__main__":
        return res
    package = module.__package__
    if package is None:
        package = ""
    mfname = module.__file__
    if mfname is None:
        return package
    fname = os.path.basename(mfname)
    fname = fname.removesuffix(".py")
    if fname in ("__init__", "__main__"):
        return package
    return f"{package}.{fname}"


def parent_python_module(p_module: str) -> str:
    dot_ix = p_module.rfind(".")
    if dot_ix < 0:
        return ""
    return p_module[:dot_ix]


def check_pid_exists(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def ideal_thread_count() -> int:
    res = os.cpu_count()
    if res is None:
        return 4
    return res


def escape(text: str, subs: dict[str, str]) -> str:
    text = text.replace("\\", "\\\\")
    for key, repl in subs.items():
        text = text.replace(key, f"\\{repl}")
    return text


def unescape(text: str, subs: dict[str, str]) -> str:
    res: list[str] = []
    in_escape = False
    for c in text:
        if in_escape:
            in_escape = False
            if c == "\\":
                res.append("\\")
                continue
            done = False
            for key, repl in subs.items():
                if c == key:
                    res.append(repl)
                    done = True
                    break
            if done:
                continue
        if c == "\\":
            in_escape = True
            continue
        res.append(c)
    return "".join(res)


def nbest(
        array: list[ET],
        key: Callable[[ET], float],
        *,
        count: int,
        is_bigger_better: bool) -> list[ET]:
    arr = np.array([
        key(elem) if is_bigger_better else -key(elem)
        for elem in array
    ], dtype=np.float64)
    ind = np.argpartition(arr, -count)[-count:]
    return [
        array[ix]
        for ix in ind[np.argsort(arr[ind])[::-1]]
    ]


@contextlib.contextmanager
def progress(
        *,
        desc: str,
        total: int,
        show: bool) -> Iterator[Callable[[int], None]]:
    if not show:
        yield lambda _: None
        return
    # FIXME: add stubs
    from tqdm.auto import tqdm  # type: ignore

    with tqdm(desc=desc, total=total) as pbar:
        yield pbar.update
