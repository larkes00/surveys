from django.contrib.auth.models import User
from django.db import models


class CompleteSurveyQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
    )
    answer = models.ForeignKey(
        "Answer",
        on_delete=models.CASCADE,
    )
    complete_survey = models.ForeignKey("CompleteSurvey", on_delete=models.CASCADE)


class CompleteSurvey(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey("Survey", on_delete=models.CASCADE)
    completed_at = models.DateTimeField(null=True)


class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    area = models.ForeignKey("SurveyArea", on_delete=models.CASCADE)
    type = models.TextField(null=True)


class SurveyArea(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    correct_answer = models.ForeignKey(
        "Answer",  # fmt: off
        on_delete=models.CASCADE,
        null=True,
        related_name="correct_answer_id",  # fmt: on
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
    )


class SurveyQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    survey = models.ForeignKey("Survey", on_delete=models.CASCADE)
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
