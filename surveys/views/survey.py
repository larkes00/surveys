import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.shortcuts import render

from surveys.logic import allow_only
from surveys.logic import get_survey
from surveys.logic import parse_surveys
from surveys.logic import parse_users
from surveys.logic import validate
from surveys.models import Answer
from surveys.models import Survey
from surveys.models import SurveyQuestion
from surveys.serializers import GetOneSurveySerializer
from surveys.serializers import SurveySerializer
from surveys.settings import URL_LOGIN_REDIRECT


@allow_only("GET")
def view_surveys_list(request):
    surveys = Survey.objects.all()
    return render(request, "surveys/surveys_list.html", {"surveys": surveys})


# TODO: починить
# @allow_only("GET")
@login_required(login_url=URL_LOGIN_REDIRECT)
def view_survey(request, survey_id):
    survey_obj = get_survey(survey_id)
    if survey_obj is None:
        return HttpResponseNotFound("No such survey")
    questions = []
    answers = []
    for survey_question in SurveyQuestion.objects.filter(survey_id=survey_id):
        questions.append(survey_question.question)
    for answer in Answer.objects.all():
        answers.append(answer)
    user = parse_users(request.user)
    return render(
        request,
        "surveys/survey.html",
        {
            "survey": survey_obj,
            "questions": questions,
            "answers": answers,
            "user": user,
        },
    )


@allow_only("GET")
@login_required(login_url=URL_LOGIN_REDIRECT)
@validate(GetOneSurveySerializer)
def survey(request, survey_id):
    survey_obj = get_survey(survey_id)
    if survey_obj is None:
        return HttpResponseNotFound("No such survey")
    return JsonResponse({"data": parse_surveys(survey_obj)})


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


# TODO: додумать
# @allow_only("POST")
# @login_required(login_url=URL_LOGIN_REDIRECT)
# def del_survey(request):
#     body = json.loads(request.body)
#     survey_obj = get_survey(body["survey_id"])
#     if survey_obj is None:
#         return HttpResponseNotFound("No such survey")
#     if survey_obj.author_id == session.user_id:
#         survey_obj.delete()
#         return JsonResponse({"data": survey_obj.id})
#     return HttpResponseForbidden("You cannot delete someone else's survey")
