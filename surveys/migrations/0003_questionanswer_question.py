# Generated by Django 3.1.1 on 2020-11-16 17:37
# pylint: disable=invalid-name

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("surveys", "0002_auto_20201116_1734"),
    ]

    operations = [
        migrations.AddField(
            model_name="questionanswer",
            name="question",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="surveys.question",
            ),
        ),
    ]
