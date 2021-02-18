import json
import datetime

from django.http import HttpResponseNotAllowed
from django.http import JsonResponse

from surveys.models import CompleteSurvey


def new_complete_survey(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    complete_survey = CompleteSurvey(
        user_id=body["user_id"],
        survey_id=body["survey_id"],
        question_id=body["question_id"],
        answer_id=body["answer_id"],
        completed_at=datetime.datetime.utcnow()
    )
    complete_survey.save()
    return JsonResponse({"data": body})
