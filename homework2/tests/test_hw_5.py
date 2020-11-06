import string

import pytest
from tasks.hw5 import custom_range


@pytest.mark.parametrize(
    ["iter_input", "args", "expected_result"],
    [
        (string.ascii_lowercase, ("g", "p", 3), ["g", "j", "m"]),
        (
            string.ascii_lowercase,
            ("g", "p"),
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        (string.ascii_lowercase, ("p", "g", -2), ["p", "n", "l", "j", "h"]),
        (
            [1, 3, 5, 4, 13, 7, 6, 10.1, "hello", "again", 0.2],
            (0.2, 1, -2),
            [0.2, "hello", 6, 13, 5],
        ),
    ],
)
def test_custom_range(iter_input, args, expected_result: list):
    actual_result = custom_range(iter_input, *args)

    assert actual_result == expected_result
