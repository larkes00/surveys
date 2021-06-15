import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.response import HttpResponseBadRequest
from django.http.response import HttpResponseForbidden
from django.http.response import HttpResponseNotFound

from surveys.logic import allow_only
from surveys.logic import get_question
from surveys.logic import get_survey_question
from surveys.logic import parse_question
from surveys.logic import parse_questions
from surveys.logic import parse_survey
from surveys.logic import validate
from surveys.models import Question
from surveys.models import Survey
from surveys.models import SurveyQuestion
from surveys.serializers import QuestionDeleteSerializer
from surveys.serializers import QuestionSerializer
from surveys.settings import URL_LOGIN_REDIRECT


@allow_only("GET")
@login_required(login_url=URL_LOGIN_REDIRECT)
def question_list(request):
    questions = Question.objects.all()
    return JsonResponse({"data": parse_questions(questions)})


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
@validate(QuestionSerializer)
def new_question(request):
    body = json.loads(request.body)
    if "correct_answer_id" in body:
        question = Question(
            content=body["content"], correct_answer_id=body["correct_answer_id"]
        )
    else:
        question = Question(content=body["content"])
    question.save()
    return JsonResponse({"data": body})


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
# Добавить валидатор
def new_survey_question(request):
    body = json.loads(request.body)
    survey = parse_survey(Survey.objects.get(id=body["survey_id"]))
    question = parse_question(Question.objects.get(id=body["question_id"]))
    if survey["type"] == "Formal" and question["correct_answer_id"] is not None:
        return HttpResponseBadRequest("Formal survey didn't have correct answer")

    if survey["type"] == "Test" and question["correct_answer_id"] is None:
        return HttpResponseBadRequest("Question without correct_answer")

    survey_question = SurveyQuestion(question_id=question["id"], survey_id=survey["id"])
    survey_question.save()
    return JsonResponse({"data": survey_question})


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
@validate(QuestionDeleteSerializer)
def del_question(request):
    body = json.loads(request.body)
    question = get_question(body["question_id"])
    if question is None:
        return HttpResponseNotFound("No such question")
    survey_question = get_survey_question(question.id)
    if survey_question is not None:
        return HttpResponseForbidden(  # fmt: off
            "You cannot delete a question related to surveys"
        )  # fmt: on
    if request.user.id == question.author_id:
        question.delete()
        return JsonResponse({"data": question.id})
    return HttpResponseForbidden("You are not the owner of the question")
