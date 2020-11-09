import pytest
from tasks_hw3.task2 import mproc_sum, runtime_timer, slow_calculate


@pytest.mark.parametrize(
    ["func", "value", "expected_result"],
    [
        (slow_calculate, 500, 1024259),
        (slow_calculate, 10, 21846),
    ],
)
def test_slow_calc(func, value, expected_result):
    mproc_sum_w_timer = runtime_timer(mproc_sum)
    actual_result, runtime = mproc_sum_w_timer(func, value)
    assert actual_result == expected_result
    assert float(runtime) < 60
