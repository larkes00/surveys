import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.http import JsonResponse

from surveys.models import CompleteSurvey


@login_required(login_url="/accounts/login/")
def new_complete_survey(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    complete_surveys = json.loads(request.body)
    for complete_survey in complete_surveys:
        CompleteSurvey(
            user_id=complete_survey["user_id"],
            survey_id=complete_survey["survey_id"],
            question_id=complete_survey["question_id"],
            answer_id=complete_survey["answer_id"],
            completed_at=datetime.datetime.utcnow(),
        ).save()
    return JsonResponse({"data": complete_surveys})
