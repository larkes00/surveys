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
]
