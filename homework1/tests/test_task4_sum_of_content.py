import pytest
from task4.four_lists import check_sum_of_four


@pytest.mark.parametrize(
    ["value1", "value2", "value3", "value4", "expected_result"],
    [
        ([-1], [1], [-1], [1], 1),
        (
            [1, -3, -4, 2, -5, 5, 23],
            [-1, 3, 4, -2, 5, 5, -23],
            [1, -3, -4, 2, -5, 5, 23],
            [-1, 3, 4, -2, 5, 5, -23],
            117,
        ),
        ([], [], [], [], 0),
    ],
)
def test_max_and_min(
    value1: list, value2: list, value3: list, value4: list, expected_result: tuple
):
    actual_result = check_sum_of_four(value1, value2, value3, value4)

    assert actual_result == expected_result
