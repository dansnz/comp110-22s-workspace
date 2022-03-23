"""Exercise 6: Dictionaries."""

__author__ = "730411941"


def invert(first_dictionary: dict[str, str] = {}) -> dict[str, str]:
    second_dictionary: dict[str, str]
    second_dictionary = {}
    for key in first_dictionary:
        for value in first_dictionary:
            second_dictionary = {value, key}
    return second_dictionary


def favorite_color(first_dictionary: dict[str, str] = {}) -> str:
    i: int = 0
    while i < len(first_dictionary):
        for key in first_dictionary:
            for value in key:
                if value in first_dictionary:


def count(start: list[str]) -> dict[str, int]:
    a_dictionary: dict[str, int]
    a_dictionary = {}
    i: int = 0
    while i < len(start):
    
