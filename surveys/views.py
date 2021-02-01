import json

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseForbidden
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.shortcuts import render

from logic import create_session_code
from logic import get_answer
from logic import get_question
from logic import get_session
from logic import get_survey
from logic import get_survey_area
from logic import get_survey_question
from logic import get_user
from logic import parce_questions
from logic import parce_survey_area
from logic import parce_surveys
from logic import parce_users
from surveys.models import Answer
from surveys.models import Question
from surveys.models import Session
from surveys.models import Survey
from surveys.models import SurveyArea
from surveys.models import User


def surveys_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    surveys = Survey.objects.all()
    return render(request, "surveys/surveys_list.html", {"surveys": surveys})


def survey(request, survey_id):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    survey_obj = get_survey(survey_id)
    if survey_obj is None:
        return HttpResponseNotFound("No such survey")
    return JsonResponse({"date": parce_surveys(survey_obj)})


def user_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    users = User.objects.all()
    return JsonResponse({"data": parce_users(users)})


def question_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    questions = Question.objects.all()
    return JsonResponse({"date": parce_questions(questions)})


def survey_areas_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    survey_areas = SurveyArea.objects.all()
    return JsonResponse({"date": parce_survey_area(survey_areas)})


def new_survey(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    survey_obj = Survey(
        id=body["id"],
        author_id=body["author_id"],
        area_id=body["area_id"],
        name=body["name"],
        type=body["type"],
    )
    survey_obj.save()
    return JsonResponse({"date": body})


def new_user(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    user = User(id=body["id"], name=body["name"])
    user.save()
    return JsonResponse({"date": body})


def new_question(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    question = Question(
        id=body["id"],
        content=body["content"],
        correct_answer_id=body["correct_answer_id"],
    )
    question.save()
    return JsonResponse({"date": body})


def new_answer(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    answer = Answer(
        id=body["id"], content=body["content"], question_id=body["question_id"]
    )
    answer.save()
    return JsonResponse({"date": body})


def new_survey_area(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    survey_area = SurveyArea(id=body["id"], name=body["name"])
    survey_area.save()
    return JsonResponse({"date": body})


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
        return JsonResponse({"date": survey_obj.id})
    return HttpResponseForbidden("You cannot delete someone else''s survey")


def del_question(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    session = get_session(body["sesion_id"])
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
            return JsonResponse({"date": question.id})
        return HttpResponseForbidden("You are not the owner of the question")
    return HttpResponseForbidden(  # fmt: off
        "You cannot delete a question related to surveys"
    )  # fmt: on


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
        return JsonResponse({"date": answer.id})
    return HttpResponseForbidden(  # fmt: off
        "You cannot delete a reply used by other people"
    )  # fmt: on


def del_survey_area(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    survey_area = get_survey_area(body["survey_area_id"])
    if survey_area is None:
        return HttpResponseNotFound("No such survey area")
    survey_area.delete()
    return JsonResponse({"date": survey_area.id})


def del_user(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    user = get_user(body["user_id"])
    if user is None:
        return HttpResponseNotFound("No such user")
    user.delete()
    return JsonResponse({"date": user.id})


# def login(request):
#     if request.method != "POST":
#         return HttpResponseNotAllowed(["POST"])
#     body = json.loads(request.body)
#     user = get_user(body["login"])
#     if user is None:
#         return HttpResponseNotFound("No such user")
#     if user.password == body["password"]:
#         session = get_session(user_id=user.id)
#         if session is None:
#             session_code = create_session_code()
#             session_list = Session(id=session_code, user_id=user.id)
#             session_list.save()
#             return JsonResponse({"session_id": session_list.id})
#         return JsonResponse({"session_id": session.id})
#     return HttpResponseForbidden("Wrong password")


def login(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    user = get_user(request.POST["login"])
    if user is None:
        return HttpResponseNotFound("No such user")
    if user.password == request.POST["password"]:
        session = get_session(user_id=user.id)
        if session is None:
            session_code = create_session_code()
            session_list = Session(id=session_code, user_id=user.id)
            session_list.save()
            return JsonResponse({"session_id": session_list.id})
        return JsonResponse({"session_id": session.id})
    return HttpResponseForbidden("Wrong password")


# def singup(request):
#     if request.method != "POST":
#         return HttpResponseNotAllowed(["POST"])
#     body = json.loads(request.body)
#     user = get_user(body["login"])
#     if user is None:
#         user = User(
#             id=body["id"],
#             name=body["name"],
#             login=body["login"],
#             password=body["password"],
#         )
#         user.save()
#         return JsonResponse({"date": body})
#     return HttpResponseBadRequest("Such user exists")


def singup(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    user = get_user(request.POST["login"])
    if user is None:
        user = User(
            name=request.POST["name"],
            login=request.POST["login"],
            password=request.POST["password"],
        )
        user.save()
        return JsonResponse({"date": request.POST})
    return HttpResponseBadRequest("Such user exists")


# def logout(request):
#     if request.method != "POST":
#         return HttpResponseNotAllowed(["POST"])
#     body = json.loads(request.body)
#     session = get_session(body["session_id"])
#     if session is None:
#         return HttpResponseBadRequest("User already logout")
#     session.delete()
#     return JsonResponse({"data": "d"})


def logout(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    session = get_session(request.POST["session_id"])
    if session is None:
        return HttpResponseBadRequest("User already logout")
    session.delete()
    return JsonResponse({"data": "d"})


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
        return JsonResponse({"date": survey})
    return HttpResponseForbidden("")
