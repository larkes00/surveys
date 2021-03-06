# Generated by Django 3.1.1 on 2020-11-25 21:12
# pylint: disable=invalid-name

from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("surveys", "0006_auto_20201119_0807"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,  # noqa: E501 fmt: off
                to="surveys.question",  # fmt: on
            ),
        ),
        migrations.AlterField(
            model_name="completesurvey",
            name="answer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,  # noqa: E501 fmt: off
                to="surveys.answer",  # fmt: on
            ),
        ),
        migrations.AlterField(
            model_name="completesurvey",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,  # noqa: E501 fmt: off
                to="surveys.question",  # fmt: on
            ),
        ),
        migrations.AlterField(
            model_name="survey",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="surveys.user"
            ),
        ),
        migrations.AlterField(
            model_name="survey",
            name="name",
            field=models.TextField(),
        ),
    ]
