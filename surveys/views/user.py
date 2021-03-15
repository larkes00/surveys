import io
import json
from json import JSONDecodeError

from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as DjangoUser
from django.http import HttpResponseBadRequest
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render

from surveys.logic import allow_only, validate

# from surveys.logic import get_user
# from surveys.logic import parse_users
from surveys.serializers import LoginSerializer, SignupSerializer
from surveys.settings import URL_LOGIN_REDIRECT


@allow_only("GET")
def view_login(request):
    return render(request, "surveys/login.html", {})


@allow_only("GET")
def view_signup(request):
    return render(request, "surveys/sign up.html", {})


# @allow_only("GET")
# @login_required(login_url=URL_LOGIN_REDIRECT)
# def user_list(request):
#     # if not request.user.is_authenticated:
#     #     return HttpResponse("User is not logged in", status=401)

#     users = User.objects.all()
#     return JsonResponse({"data": parse_users(users)})


# @allow_only("POST")
# def del_user(request):
#     body = json.loads(request.body)
#     user = get_user(body["user_id"])
#     if user is None:
#         return HttpResponseNotFound("No such user")
#     user.delete()
#     return JsonResponse({"data": user.id})


@allow_only("POST")
@validate(LoginSerializer)
def true_login(request):
    body = json.loads(request.body)
    user = authenticate(username=body["login"], password=body["password"])
    if user is None:
        return HttpResponseNotFound("No such user")
    django_login(request, user=user)
    return JsonResponse({})


@allow_only("POST")
@validate(SignupSerializer)
def true_signup(request):
    body = json.loads(request.body)
    user = DjangoUser.objects.create_user(
        username=body["login"], password=body["password"]
    )
    user.save()
    return JsonResponse({"data": body})


@allow_only("GET")
def logout(request):
    django_logout(request)
    return redirect("http://localhost:8000/view/surveys/")
