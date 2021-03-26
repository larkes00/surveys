import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from surveys.logic import allow_only
from surveys.logic import validate
from surveys.models import CompleteSurvey
from surveys.models import CompleteSurveyQuestion
from surveys.serializers import CompleteSurveySerializer
from surveys.settings import URL_LOGIN_REDIRECT


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
@validate(CompleteSurveySerializer)
def new_complete_survey(request):
    complete_surveys_json = json.loads(request.body)
    questions = []
    complete_survey = CompleteSurvey(
        user_id=complete_surveys_json["user_id"],
        survey_id=complete_surveys_json["survey_id"],
        completed_at=datetime.datetime.utcnow(),
    )
    complete_survey.save()
    for obj in complete_surveys_json["questions"]:
        questions.append(
            {
                "question_id": obj["question_id"],
                "answer_id": obj["answer_id"],
            }
        )
    for question in questions:
        CompleteSurveyQuestion(
            question_id=question["question_id"],
            answer_id=question["answer_id"],
            complete_survey_id=complete_survey.id,
        ).save()
    return JsonResponse({"data": complete_surveys_json})
