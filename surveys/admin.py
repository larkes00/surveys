from django.contrib import admin

from .models import Answer, QuestionAnswer
from .models import CompleteSurvey
from .models import Question
from .models import Survey
from .models import SurveyArea
from .models import SurveyQuestion


admin.site.register(CompleteSurvey)
admin.site.register(Survey)
admin.site.register(SurveyArea)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(SurveyQuestion)
admin.site.register(QuestionAnswer)
