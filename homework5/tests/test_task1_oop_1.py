import datetime

from tasksk_hw5.task1_oop_1 import Homework, Teacher


def test_if_create_homework_meth_returns_Homework_obj():
    assert isinstance(Teacher("a", "b").create_homework("test", 6), Homework)


def test_if_isactve_meth_returns_false_if_the_task_is_expired():
    hw = Homework("_", 0)
    assert hw.is_active() is False


def test_if_isactve_meth_returns_true_if_the_task_isnt_expired():
    hw = Homework("_", 2)
    hw.created = datetime.datetime.now() - datetime.timedelta(days=1)
    assert hw.is_active() is True
