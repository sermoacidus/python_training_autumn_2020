import pytest
from tasks_hw9.hw9_task2_ import Supressor, supressor_func


def test_if_Supressor_class_supresses_error():
    with Supressor(IndexError):
        print([][2])


def test_if_supressor_func_supresses_error():
    with supressor_func(IndexError):
        print([][2])


def test_if_other_exceptions_raise_under_Supressor_class():
    a = {}
    with pytest.raises(KeyError):
        with Supressor(IndexError):
            _ = a["k"]


def test_if_other_exceptions_raise_under_supressor_func():
    a = {}
    with pytest.raises(KeyError):
        with supressor_func(IndexError):
            _ = a["k"]
