import json

from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseNotFound
from django.http import JsonResponse

from surveys.logic import get_question
from surveys.logic import get_session
from surveys.logic import get_survey
from surveys.logic import get_survey_question
from surveys.logic import parse_questions
from surveys.models import Question


def question_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    questions = Question.objects.all()
    return JsonResponse({"data": parse_questions(questions)})


def new_question(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    question = Question(
        content=body["content"],
        correct_answer_id=body["correct_answer_id"],
    )
    question.save()
    return JsonResponse({"data": body})


def del_question(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    session = get_session(body["session_id"])
    if session is None:
        return HttpResponse("User is not logged in", status=401)
    question = get_question(body["question_id"])
    if question is None:
        return HttpResponseNotFound("No such question")
    survey_obj = get_survey(body["survey_id"])
    survey_question = get_survey_question(question.id, survey_obj.id)
    if survey_question is None:
        if session.user_id == question.author_id:
            question.delete()
            return JsonResponse({"data": question.id})
        return HttpResponseForbidden("You are not the owner of the question")
    return HttpResponseForbidden(  # fmt: off
        "You cannot delete a question related to surveys"
    )  # fmt: on