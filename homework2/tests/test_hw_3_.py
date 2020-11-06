import pytest
from tasks.hw3 import combinations


@pytest.mark.parametrize(
    ["args", "expected_result"],
    [
        (([1], [2]), [[1, 2]]),
        (
            ([1, 2], [3, 4], [2], [0, 5]),
            [
                [1, 3, 2, 0],
                [1, 3, 2, 5],
                [1, 4, 2, 0],
                [1, 4, 2, 5],
                [2, 3, 2, 0],
                [2, 3, 2, 5],
                [2, 4, 2, 0],
                [2, 4, 2, 5],
            ],
        ),
    ],
)
def test_custom_range(args, expected_result: list):
    actual_result = combinations(*args)

    assert actual_result == expected_result
