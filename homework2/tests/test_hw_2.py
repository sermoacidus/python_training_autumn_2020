import pytest
from tasks.hw2 import major_and_minor_elem


@pytest.mark.parametrize(
    ["input_", "expected_result"],
    [
        ([2, 2, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0], (0, 1)),
        ([11, 11, 2], (11, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
    ],
)
def test_major_and_minor_elem(input_, expected_result):
    actual_result = major_and_minor_elem(input_)
    assert actual_result == expected_result
