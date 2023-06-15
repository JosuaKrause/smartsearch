import re


CONTEXT_SIZE = 20
CONTEXT_MAX_EXPAND = 10
CONTEXT_END = re.compile(r"\b")
CONTEXT_START = re.compile(r"\b")
ELLIPSIS = "…"


def get_context(text: str, start: int, stop: int) -> str:
    orig_start = start
    orig_stop = stop
    start = max(start - CONTEXT_SIZE, 0)
    stop += CONTEXT_SIZE
    end = CONTEXT_END.search(f"w{text[stop:stop + CONTEXT_MAX_EXPAND]}", 1)
    if end is not None:
        stop += end.start() - 1
    from_start = max(start - CONTEXT_MAX_EXPAND, 0)
    rev = text[from_start:start][::-1]
    front = CONTEXT_START.search(f"w{rev}", 1)
    if front is not None:
        start -= front.start() - 1
    if start == 1:
        start = 0
    if stop == len(text) - 1:
        stop = len(text)
    pre = ELLIPSIS if start > 0 else ""
    post = ELLIPSIS if stop < len(text) else ""
    return (
        f"{pre}{text[start:orig_start]}"
        f"*{text[orig_start:orig_stop]}*"
        f"{text[orig_stop:stop]}{post}")
