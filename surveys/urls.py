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
from surveys import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('surveys/', views.surveys_list, name='surveys'),
    path('surveys/<int:survey_id>/', views.survey, name='survey'),
    path('users/', views.user_list, name='users'),
    path('surveyareas/', views.survey_areas_list, name='users'),
    path('questions/', views.question_list, name='questions'),
    path('surveys/create/', views.new_survey, name='create_survey'),
    path('user/create/', views.new_user, name='create_user'),
    path('answer/create', views.new_answer, name='new_answer'),
    path('question/create/', views.new_question, name='new_question'),
    path('survey_area/create/', views.new_survey_area, name='new_survey_area'),
    path('surveys/delete/', views.del_survey, name='del_survey')
]
