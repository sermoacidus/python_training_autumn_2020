import pytest
from tasks_hw6.task2_oop2 import DeadLineError, HomeworkResult, Student, Teacher

stud1 = Student("Lev", "Sokolov")
stud2 = Student("Leva", "Sokolova")
teac1 = Teacher("Aleksandr", "Smetanin")
hw = teac1.create_homework("Learn", 1)
hw_late = teac1.create_homework("Learn", 0)


def test_if_do_homework_method_returns_HomeworkResult():
    assert isinstance(stud1.do_homework(hw, "ive done"), HomeworkResult)


def test_if_raises_exc_if_hwresult_gets_not_a_hw_instance():
    with pytest.raises(TypeError, match=("You gave a not Homework object")):
        HomeworkResult(stud1, "ivedone", "sometask", "not a HomeworkType")


def test_if_do_homework_raises_exc_if_deadline_passed():
    with pytest.raises(DeadLineError, match=("You are late")):
        stud1.do_homework(hw_late, "_")


def test_if_homework_done_has_no_doubled_results():
    res1 = stud1.do_homework(hw, "my solution")
    res2 = stud2.do_homework(hw, "my solution")
    teac1.check_homework(res1)
    teac1.check_homework(res2)
    assert len(Teacher.homework_done[hw]) == 1


def test_if_short_solutions_are_not_accepted():
    res1 = stud1.do_homework(hw, "____")
    assert teac1.check_homework(res1) is False
