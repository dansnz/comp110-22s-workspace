"""Testing list utility functions."""

__author__ = "730411941"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_edge() -> None:
    """Test for an empty string."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_single_item() -> None:
    """Test for a single integer in list."""
    xs: list[int] = [1]
    assert only_evens(xs) == []


def test_only_evens_many_items() -> None:
    """Test for several items in list."""
    xs: list[int] = [44, 65, 39, 34, 8, 66]
    assert only_evens(xs) == [44, 34, 8, 66]


def test_sub_edge_case() -> None:
    """Test for first and last integers in a list."""
    xs: list[int] = [5, 8, 4, 9, 2, 0]
    a: int = 0
    b: int = 6
    assert sub(xs, a, b) == [5, 8, 4, 9, 2, 0]


def test_sub_first_use_case() -> None:
    """Test for integers within the list input."""
    xs: list[int] = [5, 8, 4, 9, 2, 0]
    a: int = 1
    b: int = 2
    assert sub(xs, a, b) == [8]


def test_sub_second_use_case() -> None:
    """Test for other integers within the list input."""
    xs: list[int] = [5, 8, 4, 9, 2, 0]
    a: int = 2
    b: int = 5
    assert sub(xs, a, b) == [4, 9, 2]


def test_concat_edge_case() -> None:
    """Test for an empty list which acts like an edge use example."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_first_use_case() -> None:
    """Test for an irregular list."""
    xs: list[int] = [1, 2, 3, 4]
    ys: list[int] = [5, 6, 7, 7]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6, 7, 7]


def test_concat_second_use_case() -> None:
    """Test for a continuous list."""
    xs: list[int] = [10, 9, 8, 7, 6]
    ys: list[int] = [5, 4, 3, 2, 1]
    assert concat(xs, ys) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
