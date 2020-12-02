from tasks_hw7.task1 import find_occurrences

example_tree = {
    "first": ["RED", 4, {"fifth": 3}, 4, "BLUE", True, [4], {1, 2, 3}, (1, 2, 3)],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", False, "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
    "sixth": {1, 2, 3},
    "seventh": (1, 2, 3),
}


def test_counting_strings():
    assert find_occurrences(example_tree, "BLUE") == 2


def test_counting_ints():
    assert find_occurrences(example_tree, 3) == 5


def test_counting_nested_ints():
    assert find_occurrences(example_tree, 4) == 3


def test_counting_tuples():
    assert find_occurrences(example_tree, (1, 2, 3)) == 2


def test_counting_sets():
    assert find_occurrences(example_tree, {1, 2, 3}) == 2


def test_counting_dicts():
    assert find_occurrences(example_tree, {"fifth": 3}) == 1


def test_counting_bools():
    assert find_occurrences(example_tree, True) == 1
    assert find_occurrences(example_tree, False) == 1
