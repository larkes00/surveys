# Generated by Django 3.1.1 on 2021-03-12 07:19

from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("surveys", "0017_auto_20210311_1855"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="completesurvey",
            name="answer",
        ),
        migrations.RemoveField(
            model_name="completesurvey",
            name="question",
        ),
        migrations.CreateModel(
            name="CompleteSurveyQuestion",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="surveys.answer"
                    ),
                ),
                (
                    "complete_survey",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="surveys.completesurvey",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="surveys.question",
                    ),
                ),
            ],
        ),
    ]
