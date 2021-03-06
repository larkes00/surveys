# Generated by Django 3.1.1 on 2020-11-12 07:24
# pylint: disable=invalid-name

from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("content", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("content", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Survey",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="SurveyArea",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="SurveyQuestion",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,  # noqa: E501 fmt: off
                        to="surveys.question",  # fmt: on
                    ),
                ),
                (
                    "survey",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,  # fmt: off # noqa: E501
                        to="surveys.survey",  # fmt: on
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="survey",
            name="area",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,  # fmt: off
                to="surveys.surveyarea",  # fmt: on
            ),
        ),
        migrations.CreateModel(
            name="QuestionAnswer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,  # noqa: E501 fmt: off
                        to="surveys.answer",  # fmt: on
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CompleteSurvey",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "survey",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,  # noqa: E501 fmt: off
                        to="surveys.survey",  # fmt: on
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,  # noqa: E501 fmt: off
                        to="surveys.user",  # fmt: on
                    ),
                ),
            ],
        ),
    ]
