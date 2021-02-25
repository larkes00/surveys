import json

from django.http import HttpResponseBadRequest
from django.http import HttpResponseForbidden
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.shortcuts import render

from surveys.logic import create_session_code
from surveys.logic import get_session
from surveys.logic import get_user
from surveys.logic import parse_users
from surveys.models import Session
from surveys.models import User


def view_login(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    return render(request, "surveys/login.html", {})


def view_signup(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    return render(request, "surveys/sign up.html", {})


def user_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    users = User.objects.all()
    return JsonResponse({"data": parse_users(users)})


def new_user(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    user = User(  # fmt: off
        name=body["name"], login=body["login"], password=body["password"]
    )  # fmt: on
    user.save()
    return JsonResponse({"data": body})


def del_user(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    user = get_user(body["user_id"])
    if user is None:
        return HttpResponseNotFound("No such user")
    user.delete()
    return JsonResponse({"data": user.id})


def login(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    user = get_user(body["login"])
    if user is None:
        return HttpResponseNotFound("No such user")
    if user.password == body["password"]:
        session = get_session(user_id=user.id)
        if session is None:
            session_code = create_session_code()
            session_list = Session(id=session_code, user_id=user.id)
            session_list.save()
            return JsonResponse({"session_id": session_list.id})
        return JsonResponse({"session_id": session.id})
    return HttpResponseForbidden("Wrong password")


def singup(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    user = get_user(body["login"])
    if user is None:
        user = User(
            name=body["name"],
            login=body["login"],
            password=body["password"],
        )
        user.save()
        return JsonResponse({"data": body})
    return HttpResponseBadRequest("Such user exists")


def logout(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    session = get_session(body["session_id"])
    if session is None:
        return HttpResponseBadRequest("User already logout")
    session.delete()
    return JsonResponse({"data": "d"})
