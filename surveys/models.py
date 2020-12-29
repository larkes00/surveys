from django.db import models

class CompleteSurvey(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        'User',
        on_delete = models.CASCADE
    )
    survey = models.ForeignKey(
        'Survey',
        on_delete = models.CASCADE
    )
    question = models.ForeignKey(
        'Question',
        on_delete = models.CASCADE,
    )
    answer = models.ForeignKey(
        'Answer',
        on_delete = models.CASCADE,
    )
    completed_at = models.DateField(
        null=True
    )

class Survey(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(
    )
    author = models.ForeignKey(
        'User',
        on_delete = models.CASCADE,
    )
    area = models.ForeignKey(
        'SurveyArea',
        on_delete = models.CASCADE
    )
    type = models.TextField(
        null = True
    )

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

class SurveyArea(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.TextField()
    correct_answer = models.ForeignKey(
        'Answer',
        on_delete = models.CASCADE,
        null = True,
        related_name = 'correct_answer_id'
    )    

class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.TextField()
    question = models.ForeignKey(
        'Question',
        on_delete= models.CASCADE,
    )

class SurveyQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    survey = models.ForeignKey(
        'Survey',
        on_delete = models.CASCADE
    )
    question = models.ForeignKey(
        'Question',
        on_delete = models.CASCADE
    )

class Session(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        'User',
        on_delete = models.CASCADE
    )