import json

from django.http import HttpResponseNotAllowed
from django.http import HttpResponseNotFound
from django.http import JsonResponse

from surveys.logic import get_survey_area
from surveys.logic import parse_survey_area
from surveys.models import SurveyArea


def survey_areas_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    survey_areas = SurveyArea.objects.all()
    return JsonResponse({"data": parse_survey_area(survey_areas)})


def new_survey_area(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    survey_area = SurveyArea(name=body["name"])
    survey_area.save()
    return JsonResponse({"data": body})


def del_survey_area(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    survey_area = get_survey_area(body["survey_area_id"])
    if survey_area is None:
        return HttpResponseNotFound("No such survey area")
    survey_area.delete()
    return JsonResponse({"data": survey_area.id})
