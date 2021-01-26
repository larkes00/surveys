from django.contrib import admin
from .models import User
from .models import CompleteSurvey
from .models import Survey
from .models import SurveyArea
from .models import Question
from .models import Answer

admin.site.register(User)
admin.site.register(CompleteSurvey)
admin.site.register(Survey)
admin.site.register(SurveyArea)
admin.site.register(Question)
admin.site.register(Answer)
