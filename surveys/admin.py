from django.contrib import admin

from .models import Answer, CompleteSurvey, Question, Survey, SurveyArea, User

admin.site.register(User)
admin.site.register(CompleteSurvey)
admin.site.register(Survey)
admin.site.register(SurveyArea)
admin.site.register(Question)
admin.site.register(Answer)
