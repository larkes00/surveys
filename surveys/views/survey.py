import json

from django.http import HttpResponseForbidden
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.shortcuts import render

from surveys.logic import get_session
from surveys.logic import get_survey
from surveys.logic import parse_surveys
from surveys.models import Answer
from surveys.models import Survey
from surveys.models import SurveyQuestion


def view_surveys_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    surveys = Survey.objects.all()
    return render(request, "surveys/surveys_list.html", {"surveys": surveys})


def view_survey(request, survey_id):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    survey_obj = get_survey(survey_id)
    if survey_obj is None:
        return HttpResponseNotFound("No such survey")
    questions = []
    answers = []
    for survey_question in SurveyQuestion.objects.filter(survey_id=survey_id):
        questions.append(survey_question.question)
    for answer in Answer.objects.all():
        answers.append(answer)
    return render(
        request,
        "surveys/survey.html",
        {"survey": survey_obj, "questions": questions, "answers": answers},
    )


def survey(request, survey_id):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    survey_obj = get_survey(survey_id)
    if survey_obj is None:
        return HttpResponseNotFound("No such survey")
    return JsonResponse({"data": parse_surveys(survey_obj)})


def new_survey(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    survey_obj = Survey(
        author_id=body["author_id"],
        area_id=body["area_id"],
        name=body["name"],
        type=body["type"],
    )
    survey_obj.save()
    return JsonResponse({"data": body})


def del_survey(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    session = get_session(body["session_id"])
    if session is None:
        return HttpResponseNotFound("No such session")
    survey_obj = get_survey(body["survey_id"])
    if survey_obj is None:
        return HttpResponseNotFound("No such survey")
    if survey_obj.author_id == session.user_id:
        survey_obj.delete()
        return JsonResponse({"data": survey_obj.id})
    return HttpResponseForbidden("You cannot delete someone else's survey")


def edit_survey(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    session = get_session(body["session_id"])
    if session is None:
        return HttpResponseNotFound("No such session")
    survey_obj = get_survey(body["survey_id"])
    if survey_obj is None:
        return HttpResponseNotFound("No such survey")
    if survey_obj.author_id == session.user_id:
        # fmt: off
        survey_obj = Survey.objects.filter(id=body["survey_id"]).update(
            name=body["name"]
        )
        survey_obj = Survey.objects.filter(id=body["survey_id"]).update(
            type=body["type"]
        )
        # fmt: on
        return JsonResponse({"data": survey_obj})
    return HttpResponseForbidden("")
