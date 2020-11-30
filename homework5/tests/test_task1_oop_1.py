import datetime

from tasksk_hw5.task1_oop_1 import Homework, Student, Teacher


def test_if_create_homework_meth_returns_Homework_obj():
    assert isinstance(Teacher("a", "b").create_homework("test", 6), Homework)


def test_if_isactve_meth_returns_false_if_the_task_is_expired():
    hw = Homework("_", 0)
    assert hw.is_active() is False


def test_if_isactve_meth_returns_true_if_the_task_isnt_expired():
    hw = Homework("_", 2)
    hw.created = datetime.datetime.now() - datetime.timedelta(days=1)
    assert hw.is_active() is True


def test_do_homework_return_homework_if_the_task_isnt_expired():
    a = Student("a", "b")
    hw = Homework("_", 1)
    assert a.do_homework(hw) == hw


def test_do_homework_return_message_if_the_task_is_expired(capsys):
    a = Student("a", "b")
    hw = Homework("_", 0)
    a.do_homework(hw)
    captured = capsys.readouterr()
    assert captured.out == "You are late\n"
