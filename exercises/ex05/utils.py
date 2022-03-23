"""List utility functions."""

__author__ = "730411941"


def only_evens(xs: list[int]) -> list[int]:
    """Return a list with only the even elements."""
    xs_len: int = len(xs)
    i: int = 0
    evens: list[int] = []
    while i < xs_len:
        if xs[i] % 2 != 1:
            evens.append(xs[i])
        i += 1
    return evens


def sub(xs: list[int], a: int, b: int) -> list[int]:
    """Generate a list which is a subset of the given list."""
    subset: list[int] = []
    if a < 0:
        a = 0
    if b > len(xs):
        b = len(xs)
    while a < b:
        subset.append(xs[a])
        a += 1
    return subset


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Concatenates the second list after the first."""
    concatenation: list = []
    i: int = 0
    while i < len(xs):
        concatenation.append(xs[i])
        i += 1
    i = 0
    while i < len(ys):
        concatenation.append(ys[i])
        i += 1
    return concatenation