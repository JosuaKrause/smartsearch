from typing import Any

from app.misc.util import escape, retain_some, unescape


def test_retain_some() -> None:

    def test_rs(
            input_arr: list[int],
            count: int,
            output_arr: list[int],
            delete_arr: set[int],
            **kwargs: Any) -> None:
        res, to_delete = retain_some(
            input_arr, count, key=lambda v: v, **kwargs)
        assert res == output_arr
        assert set(to_delete) == delete_arr

    test_rs(
        [5, 3, 2, 1, 9, 3, 0, 6],
        4,
        [3, 3, 5, 6, 9],
        {0, 1, 2})
    test_rs(
        [5, 3, 2, 1, 9, 3, 0, 6],
        4,
        [3, 5, 6, 9],
        {0, 1, 2, 3},
        keep_last=False)
    test_rs(
        [5, 3, 2, 1, 9, 3, 0, 6],
        4,
        [6, 3, 2, 1, 0],
        {3, 5, 9},
        reverse=True)
    test_rs(
        [5, 3, 2, 1, 9, 3, 0, 6],
        4,
        [3, 2, 1, 0],
        {3, 5, 6, 9},
        reverse=True,
        keep_last=False)
    test_rs(
        [5, 3, 2, 1, 9, 3, 0, 6],
        5,
        [2, 3, 3, 5, 6, 9],
        {0, 1})
    test_rs(
        [5, 3, 2, 1, 9, 3, 0, 6],
        5,
        [3, 3, 5, 6, 9],
        {0, 1, 2},
        keep_last=False)
    test_rs(
        [5, 3, 2, 1, 9, 3, 0, 6],
        5,
        [6, 3, 3, 2, 1, 0],
        {5, 9},
        reverse=True)
    test_rs(
        [5, 3, 2, 1, 9, 3, 0, 6],
        5,
        [3, 3, 2, 1, 0],
        {5, 6, 9},
        reverse=True,
        keep_last=False)
    test_rs(
        [5, 3, 2, 1, 9, 3],
        5,
        [1, 2, 3, 3, 5, 9],
        set())
    test_rs(
        [5, 3, 2, 1, 9, 3],
        6,
        [1, 2, 3, 3, 5, 9],
        set(),
        keep_last=False)
    test_rs(
        [5, 3, 2],
        6,
        [2, 3, 5],
        set())
    test_rs(
        [5, 3, 2],
        6,
        [2, 3, 5],
        set(),
        keep_last=False)


def test_escape() -> None:

    def test(text: str, subs: dict[str, str]) -> None:
        rsubs = {
            repl: key
            for key, repl in subs.items()
        }
        assert text == unescape(escape(text, subs), rsubs)

    test("abc", {"\n": "n"})
    test("abc\0\n", {"\n": "n"})
    test("\\n\n", {"\n": "n"})
    test("\\n0\\0\0\n", {"\n": "n"})

    test("abc", {"\0": "0"})
    test("abc\0\n", {"\0": "0"})
    test("\\n\n", {"\0": "0"})
    test("\\n0\\0\0\n", {"\0": "0"})

    test("abc", {"\n": "n", "\0": "0"})
    test("abc\0\n", {"\n": "n", "\0": "0"})
    test("\\n\n", {"\n": "n", "\0": "0"})
    test("\\n0\\0\0\n", {"\n": "n", "\0": "0"})
