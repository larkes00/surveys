import json

from django.http import HttpResponseForbidden
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseNotFound
from django.http import JsonResponse

from surveys.logic import get_answer
from surveys.logic import get_question
from surveys.logic import get_session
from surveys.logic import get_survey
from surveys.logic import get_survey_question
from surveys.models import Answer


def new_answer(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    answer = Answer(
        id=body["id"], content=body["content"], question_id=body["question_id"]
    )
    answer.save()
    return JsonResponse({"data": body})


def del_answer(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    session = get_session(body["session_id"])
    if session is None:
        return HttpResponseNotFound("User is not logged in")
    answer = get_answer(body["answer_id"])
    if answer is None:
        return HttpResponseNotFound("No such answer")
    question = get_question(answer.question_id)
    survey_obj = get_survey(body["survey_id"])
    survey_question = get_survey_question(question.id, survey_obj.id)
    if survey_question is None:
        answer.delete()
        return JsonResponse({"data": answer.id})
    return HttpResponseForbidden(  # fmt: off
        "You cannot delete a reply used by other people"
    )  # fmt: on
