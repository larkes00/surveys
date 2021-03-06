# Generated by Django 3.1.1 on 2020-11-19 08:07
# pylint: disable=invalid-name

from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("surveys", "0005_auto_20201116_1803"),
    ]

    operations = [
        migrations.AddField(
            model_name="survey",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="surveys.user",
            ),
        ),
        migrations.AddField(
            model_name="survey",
            name="name",
            field=models.TextField(null=True),
        ),
    ]
