import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.http.response import HttpResponseForbidden
from django.shortcuts import render

from surveys.logic import allow_only
from surveys.logic import get_survey
from surveys.logic import parse_survey
from surveys.logic import validate
from surveys.models import QuestionAnswer
from surveys.models import Survey
from surveys.models import SurveyQuestion
from surveys.serializers import SurveyDeleteSerializer
from surveys.serializers import SurveySerializer
from surveys.settings import URL_LOGIN_REDIRECT


@allow_only("GET")
def view_surveys_list(request):
    surveys = Survey.objects.all()
    return render(request, "surveys/surveys_list.html", {"surveys": surveys})


@allow_only("GET")
@login_required(login_url=URL_LOGIN_REDIRECT)
def view_survey(request, survey_id):
    survey_obj = get_survey(survey_id)
    if survey_obj is None:
        return HttpResponseNotFound("No such survey")
    question_answers = []
    for survey_question in SurveyQuestion.objects.filter(survey_id=survey_id):
        question_answers.append(
            QuestionAnswer.objects.filter(question_id=survey_question.question_id)
        )
    return render(
        request,
        "surveys/survey.html",
        {"question_answers": question_answers, "survey": survey_obj},
    )


@allow_only("GET")
@login_required(login_url=URL_LOGIN_REDIRECT)
def survey(request, survey_id):
    survey_obj = get_survey(survey_id)
    if survey_obj is None:
        return HttpResponseNotFound("No such survey")
    return JsonResponse({"data": parse_survey(survey_obj)})


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
@validate(SurveySerializer)
def new_survey(request):
    body = json.loads(request.body)
    survey_obj = Survey(
        author_id=body["author_id"],
        area_id=body["area_id"],
        name=body["name"],
        type=body["type"],
    )
    survey_obj.save()
    return JsonResponse({"data": body})


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
@validate(SurveyDeleteSerializer)
def del_survey(request):
    body = json.loads(request.body)
    survey_obj = get_survey(body["survey_id"])
    if survey_obj is None:
        return HttpResponseNotFound("No such survey")
    if survey_obj.author_id == request.user.id:
        survey_obj.delete()
        return JsonResponse({"data": survey_obj.id})
    return HttpResponseForbidden("You cannot delete someone else's survey")
