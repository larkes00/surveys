import datetime
import json
from json import JSONDecodeError

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http.response import HttpResponseBadRequest

from surveys.logic import allow_only
from surveys.models import CompleteSurvey
from surveys.serializers import CompleteSurveySerializer
from surveys.settings import URL_LOGIN_REDIRECT


@allow_only("POST")
# @login_required(login_url=URL_LOGIN_REDIRECT)
def new_complete_survey(request):
    # complete_surveys = json.loads(request.body)
    try:
        request_body = json.loads(request.body)
    except (TypeError, JSONDecodeError):
        return HttpResponseBadRequest()

    serializer = CompleteSurveySerializer(data=request_body, many=True)
    if not serializer.is_valid():
        return HttpResponseBadRequest(json.dumps(serializer.errors))
    complete_surveys = serializer.validated_data
    for complete_survey in complete_surveys:
        CompleteSurvey(
            user_id=complete_survey["user_id"],
            survey_id=complete_survey["survey_id"],
            question_id=complete_survey["question_id"],
            answer_id=complete_survey["answer_id"],
            completed_at=datetime.datetime.utcnow(),
        ).save()
    return JsonResponse({"data": complete_surveys})
