import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.http import JsonResponse

from surveys.logic import allow_only
from surveys.logic import get_survey_area
from surveys.logic import parse_survey_areas
from surveys.logic import validate
from surveys.models import SurveyArea
from surveys.serializers import SurveyAreaDeleteSerializer
from surveys.serializers import SurveyAreaSerializer
from surveys.settings import URL_LOGIN_REDIRECT


@allow_only("GET")
def survey_areas_list(request):
    survey_areas = SurveyArea.objects.all()
    return JsonResponse({"data": parse_survey_areas(survey_areas)})


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
@validate(SurveyAreaSerializer)
def new_survey_area(request):
    body = json.loads(request.body)
    survey_area = SurveyArea(name=body["name"])
    survey_area.save()
    return JsonResponse({"data": body})


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
@validate(SurveyAreaDeleteSerializer)
def del_survey_area(request):
    body = json.loads(request.body)
    survey_area = get_survey_area(body["survey_area_id"])
    if survey_area is None:
        return HttpResponseNotFound("No such survey area")
    survey_area.delete()
    return JsonResponse({"data": survey_area.id})
