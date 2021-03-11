from django.contrib import admin

from .models import Answer
from .models import CompleteSurvey
from .models import Question
from .models import Survey
from .models import SurveyArea


admin.site.register(CompleteSurvey)
admin.site.register(Survey)
admin.site.register(SurveyArea)
admin.site.register(Question)
admin.site.register(Answer)
