"""surveys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include  # noqa: F401 pylint: disable=W0611

from surveys import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("view/surveys/", views.view_surveys_list, name="view_surveys"),
    path("view/surveys/<int:survey_id>/", views.view_survey, name="view_survey"),
    path(
        "complete_survey/create/",
        views.new_complete_survey,
        name="new_complete_survey",
    ),
    path("view/login/", views.view_login, name="view_login"),
    path("view/signup/", views.view_signup, name="view_signup"),
    path("surveys/<int:survey_id>/", views.survey, name="survey"),
    path("users/", views.user_list, name="users"),
    path("surveyareas/", views.survey_areas_list, name="survey_areas"),
    path("questions/", views.question_list, name="questions"),
    path("question/<int:question_id>/", views.survey, name="question"),
    path("surveys/create/", views.new_survey, name="create_survey"),
    path("answer/create/", views.new_answer, name="new_answer"),
    path("question/create/", views.new_question, name="new_question"),
    path("survey_area/create/", views.new_survey_area, name="new_survey_area"),
    path("surveys/delete/", views.del_survey, name="del_survey"),
    path("question/delete/", views.del_question, name="del_question"),
    path("answer/delete/", views.del_answer, name="del_answer"),
    path("surveyarea/delete/", views.del_survey_area, name="del_survey_area"),
    # path("user/delete/", views.del_user, name="del_user"),
    path("login/", views.true_login, name="login"),
    path("signup/", views.true_signup, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/", views.logout, name="logout"),
]
