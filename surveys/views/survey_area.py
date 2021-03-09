import json
from json.decoder import JSONDecodeError

from django.http.response import HttpResponseBadRequest
from surveys.serializers import SurveyAreaSerializer

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.http import JsonResponse

from surveys.logic import allow_only
from surveys.logic import get_survey_area
from surveys.logic import parse_survey_area
from surveys.models import SurveyArea
from surveys.settings import URL_LOGIN_REDIRECT


@allow_only("GET")
def survey_areas_list(request):
    survey_areas = SurveyArea.objects.all()
    return JsonResponse({"data": parse_survey_area(survey_areas)})


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
def new_survey_area(request):
    try:
        request_body = json.loads(request.body)
    except (TypeError, JSONDecodeError):
        return HttpResponseBadRequest()

    serializer = SurveyAreaSerializer(data=request_body)
    if not serializer.is_valid():
        return HttpResponseBadRequest(json.dumps(serializer.errors))
    body = serializer.validated_data
    body = json.loads(request.body)
    survey_area = SurveyArea(name=body["name"])
    survey_area.save()
    return JsonResponse({"data": body})


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
def del_survey_area(request):
    body = json.loads(request.body)
    survey_area = get_survey_area(body["survey_area_id"])
    if survey_area is None:
        return HttpResponseNotFound("No such survey area")
    survey_area.delete()
    return JsonResponse({"data": survey_area.id})
