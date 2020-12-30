import datetime

from dj_app.models import Homework, HomeworkResult, Student, Teacher


def run():
    oop_teacher = Teacher(first_name="Daniil", last_name="Shadrin")
    oop_teacher.save()
    advanced_python_teacher = Teacher(first_name="Aleksandr", last_name="Smetanin")
    advanced_python_teacher.save()
    lazy_student = Student(first_name="Roman", last_name="Petrov")
    lazy_student.save()
    good_student = Student(first_name="Lev", last_name="Sokolov")
    good_student.save()

    oop_hw = Homework(text="Learn OOP", deadline=1, created_by=oop_teacher)
    oop_hw.save()
    result_1 = HomeworkResult(
        given_task=oop_hw, author=lazy_student, solution="I have done this hw "
    )
    result_1.save()
