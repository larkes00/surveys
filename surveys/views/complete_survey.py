import datetime
import json
from json import JSONDecodeError

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http.response import HttpResponseBadRequest

from surveys.logic import allow_only, validate
from surveys.models import CompleteSurvey, CompleteSurveyQuestion
from surveys.serializers import CompleteSurveySerializer
from surveys.settings import URL_LOGIN_REDIRECT


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
# @validate(CompleteSurveySerializer)
def new_complete_survey(request):
    complete_surveys = json.loads(request.body)
    questions = []
    for obj in complete_surveys["questions"]:
        questions.append(
            {
                "question_id": obj["question_id"],
                "answer_id": obj["answer_id"],
                "complete_survey": obj["complete_survey"],
            }
        )
    for question in questions:
        CompleteSurveyQuestion(
            question_id=question["question_id"],
            answer_id=question["answer_id"],
            complete_survey_id=question["complete_survey"],
        ).save()
    CompleteSurvey(
        user_id=complete_surveys["user_id"],
        survey_id=complete_surveys["survey_id"],
        completed_at=datetime.datetime.utcnow(),
    ).save()
    return JsonResponse({"data": complete_surveys})
