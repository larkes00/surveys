import json
from json.decoder import JSONDecodeError

from django.http.response import HttpResponseBadRequest
from surveys.serializers import QuestionSerializer

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from surveys.logic import allow_only
from surveys.logic import parse_questions
from surveys.models import Question
from surveys.settings import URL_LOGIN_REDIRECT


@allow_only("GET")
@login_required(login_url=URL_LOGIN_REDIRECT)
def question_list(request):
    questions = Question.objects.all()
    return JsonResponse({"data": parse_questions(questions)})


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
def new_question(request):
    try:
        request_body = json.loads(request.body)
    except (TypeError, JSONDecodeError):
        return HttpResponseBadRequest()

    serializer = QuestionSerializer(data=request_body)
    if not serializer.is_valid():
        return HttpResponseBadRequest(json.dumps(serializer.errors))
    body = serializer.validated_data
    question = Question(
        content=body["content"],
        correct_answer_id=body["correct_answer_id"],
    )
    question.save()
    return JsonResponse({"data": body})


# TODO: додумать
# @allow_only("POST")
# @login_required(login_url=URL_LOGIN_REDIRECT)
# def del_question(request):
#     body = json.loads(request.body)
#     question = get_question(body["question_id"])
#     if question is None:
#         return HttpResponseNotFound("No such question")
#     survey_question = get_survey_question(question.id)
#     if survey_question is not None:
#         return HttpResponseForbidden(  # fmt: off
#             "You cannot delete a question related to surveys"
#         )  # fmt: on
#     if session.user_id == question.author_id:
#         question.delete()
#         return JsonResponse({"data": question.id})
#     return HttpResponseForbidden("You are not the owner of the question")
