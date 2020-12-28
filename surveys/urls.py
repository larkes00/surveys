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
    path('surveys/<int:survey_id>/', views.survey, name='surveys'),
    path('users/', views.user_list, name='users'),
    path('surveyareas/', views.survey_areas_list, name='users'),
    path('questions/', views.question_list, name='questions'),
    # path('new_survey/', views.new_survey, name='new_survey'),
    # path('new_user/', views.new_user, name='new_user'),
    # path('new_question/', views.new_question, name='new_question'),
    # path('new_answer/', views.new_answer, name='new_answer'),
    path('surveys/create/', views.new_survey, name='create_survey'),
    path('surveys/delete/', views.del_survey, name='del_survey'),
    path('new_survey_area/', views.new_survey_area, name='new_survey_area')
]
