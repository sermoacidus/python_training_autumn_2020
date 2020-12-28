import pytest
from tasks_hw11.task1_hw11 import ColorsEnum, SizesEnum


def test_if_keys_are_reachable():
    a = ColorsEnum()
    assert a.RED == "RED"
    b = SizesEnum()
    assert b.XL == "XL"
    with pytest.raises(AttributeError):
        a.GREEN
