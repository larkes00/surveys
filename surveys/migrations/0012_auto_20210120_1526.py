# Generated by Django 3.1.1 on 2021-01-20 15:26
# pylint: disable=invalid-name

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("surveys", "0011_auto_20210108_1946"),
    ]

    operations = [
        migrations.AlterField(
            model_name="session",
            name="id",
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
