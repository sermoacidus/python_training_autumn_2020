import pytest
from task5.subarray_sum import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value", "subarray_len", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([0, 1, 2], 1, 2),
        ([3, 1555, 24, 0], 1, 1555),
        ([4, 4, 4, 4, 0], 5, 16),
    ],
)
def test_max_and_min(value: list, subarray_len: int, expected_result: tuple):
    actual_result = find_maximal_subarray_sum(value, subarray_len)

    assert actual_result == expected_result
