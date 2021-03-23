import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.http import HttpResponseNotFound
from django.http import JsonResponse

from surveys.logic import allow_only
from surveys.logic import get_answer
from surveys.logic import get_question
from surveys.logic import get_survey
from surveys.logic import get_survey_question
from surveys.logic import validate
from surveys.models import Answer
from surveys.serializers import AnswerDeleteSerializer
from surveys.serializers import AnswerSerializer
from surveys.settings import URL_LOGIN_REDIRECT


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
@validate(AnswerSerializer)
def new_answer(request):
    body = json.loads(request.body)
    answer = Answer(content=body["content"], question_id=body["question_id"])
    answer.save()
    return JsonResponse({"data": body})


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
@validate(AnswerDeleteSerializer)
def del_answer(request):
    body = json.loads(request.body)
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
