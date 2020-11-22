"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истело ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from dataclasses import dataclass


@dataclass()
class Student:
    last_name: str
    first_name: str

    def do_homework(self, homework: "Homework"):
        """Returns homework obj if it's still active otherwise returns None"""
        if homework.is_active():
            return homework
        else:
            print("You are late")


@dataclass()
class Teacher:
    last_name: str
    first_name: str

    @staticmethod
    def create_homework(task: str, days_to_complete: int) -> "Homework":
        return Homework(task, days_to_complete)


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """If period isn't expired yet - returns True, otherwise - False"""
        return (
            True if (datetime.datetime.now() - self.deadline) < self.created else False
        )
