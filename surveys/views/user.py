import json

from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as DjangoUser
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render

from surveys.logic import get_user
from surveys.logic import parse_users
from surveys.models import User


def view_login(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    return render(request, "surveys/login.html", {})


def view_signup(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    return render(request, "surveys/sign up.html", {})


@login_required(login_url="/accounts/login/")
def user_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    # if not request.user.is_authenticated:
    #     return HttpResponse("User is not logged in", status=401)

    users = User.objects.all()
    return JsonResponse({"data": parse_users(users)})


# def new_user(request):
#     if request.method != "POST":
#         return HttpResponseNotAllowed(["POST"])
#     body = json.loads(request.body)
#     user = User(  # fmt: off
#         name=body["name"], login=body["login"], password=body["password"]
#     )  # fmt: on
#     user.save()
#     return JsonResponse({"data": body})


def del_user(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    user = get_user(body["user_id"])
    if user is None:
        return HttpResponseNotFound("No such user")
    user.delete()
    return JsonResponse({"data": user.id})


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


def true_login(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    user = authenticate(username=body["login"], password=body["password"])
    if user is None:
        return HttpResponseNotFound("No such user")
    django_login(request, user=user)
    return JsonResponse({})


# def singup(request):
#     if request.method != "POST":
#         return HttpResponseNotAllowed(["POST"])
#     body = json.loads(request.body)
#     user = get_user(body["login"])
#     if user is None:
#         user = User(
#             name=body["name"],
#             login=body["login"],
#             password=body["password"],
#         )
#         user.save()
#         return JsonResponse({"data": body})
#     return HttpResponseBadRequest("Such user exists")


def true_signup(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    body = json.loads(request.body)
    user = DjangoUser.objects.create_user(
        username=body["login"], password=body["password"]
    )
    user.save()
    return JsonResponse({"data": body})


def logout(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    # body = json.loads(request.body)
    # session = get_session(body["session_id"])
    # if session is None:
    #     return HttpResponseBadRequest("User already logout")
    # session.delete()
    django_logout(request)
    return redirect("http://localhost:8000/view/surveys/")
