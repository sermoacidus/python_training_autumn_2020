# Generated by Django 3.1.4 on 2020-12-30 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Homework",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(blank=True)),
                ("deadline", models.IntegerField(default=0)),
                ("created", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=75)),
                ("last_name", models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="dj_app.person",
                    ),
                ),
            ],
            bases=("dj_app.person",),
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="dj_app.person",
                    ),
                ),
            ],
            bases=("dj_app.person",),
        ),
        migrations.CreateModel(
            name="HomeworkResult",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("solution", models.TextField(blank=True)),
                ("created", models.DateField(auto_now_add=True)),
                (
                    "given_task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dj_app.homework",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="dj_app.student"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="homework",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dj_app.teacher"
            ),
        ),
    ]