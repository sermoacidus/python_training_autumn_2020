from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)


class Teacher(Person):
    pass


class Student(Person):
    pass


class Homework(models.Model):
    text = models.TextField().unique
    deadline = models.DurationField
    created = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class HomeworkResult(models.Model):
    given_task = models.ForeignKey(Homework, on_delete=models.CASCADE)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    solution = models.TextField
    created = models.DateField(auto_now_add=True)
