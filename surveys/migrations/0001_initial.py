# Generated by Django 3.1.1 on 2020-11-12 07:24

from django.db import migrations, models
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
                        on_delete=django.db.models.deletion.CASCADE,
                        to="surveys.question",
                    ),
                ),
                (
                    "survey",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="surveys.survey"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="survey",
            name="area",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="surveys.surveyarea"
            ),
        ),
        migrations.CreateModel(
            name="QuestionAnswer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="surveys.answer"
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
                        on_delete=django.db.models.deletion.CASCADE, to="surveys.survey"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="surveys.user"
                    ),
                ),
            ],
        ),
    ]
