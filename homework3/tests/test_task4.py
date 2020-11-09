import pytest
from tasks_hw3.task4 import is_armstrong


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (153, True),
        (10, False),
        (9, True),
        (370, True),
        (371, True),
    ],
)
def test_is_armstrong(value, expected_result):
    actual_result = is_armstrong(value)
    assert actual_result == expected_result
