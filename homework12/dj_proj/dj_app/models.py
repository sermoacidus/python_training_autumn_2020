from datetime import timedelta

from django.db import models

b = timedelta(days=1, hours=2, seconds=15)


class Person(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)


class Teacher(Person):
    pass


class Student(Person):
    pass


class Homework(models.Model):
    text = models.TextField(blank=True)
    deadline = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class HomeworkResult(models.Model):
    given_task = models.ForeignKey(Homework, on_delete=models.CASCADE)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    solution = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
