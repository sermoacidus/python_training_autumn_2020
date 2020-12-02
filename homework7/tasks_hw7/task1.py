"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Iterable

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    return (
        len([_ for _ in iter(recursive_search(tree, element)) if _ is element])
        if isinstance(element, bool)
        else len([_ for _ in iter(recursive_search(tree, element)) if _ == element])
    )


def recursive_search(data, element):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == element:
                yield key
            if value == element:
                yield value
                continue
            if isinstance(value, Iterable):
                yield from recursive_search(value, element)
    if isinstance(data, list) or isinstance(data, set) or isinstance(data, tuple):
        for value in data:
            if value == element:
                yield value
                continue
            if isinstance(value, Iterable):
                yield from recursive_search(value, element)
