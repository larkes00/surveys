# Generated by Django 3.1.1 on 2021-02-01 06:30
# pylint: disable=invalid-name

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("surveys", "0014_auto_20210131_2109"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="question",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="survey",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="surveyarea",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
