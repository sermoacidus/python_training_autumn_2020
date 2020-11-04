from pathlib import Path

import pytest
from task3.max_and_min import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (Path("tests/testfile_for_task3_1.txt"), (0, 551515)),
        (Path("tests/testfile_for_task3_2.txt"), (-6465166, 7984098)),
        (Path("tests/testfile_for_task3_3.txt"), (1, 1)),
    ],
)
def test_max_and_min(value: str, expected_result: tuple):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
