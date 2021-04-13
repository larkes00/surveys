import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from surveys.logic import allow_only
from surveys.logic import parse_answer
from surveys.logic import parse_complete_survey
from surveys.logic import parse_complete_survey_question
from surveys.logic import parse_questions
from surveys.logic import parse_surveys
from surveys.logic import validate
from surveys.models import Answer
from surveys.models import CompleteSurvey
from surveys.models import CompleteSurveyQuestion
from surveys.models import Question
from surveys.models import Survey
from surveys.serializers import CompleteSurveySerializer
from surveys.settings import URL_LOGIN_REDIRECT


@allow_only("POST")
@login_required(login_url=URL_LOGIN_REDIRECT)
@validate(CompleteSurveySerializer)
def new_complete_survey(request):
    complete_surveys_json = json.loads(request.body)
    questions = []
    complete_survey = CompleteSurvey(
        user_id=complete_surveys_json["user_id"],
        survey_id=complete_surveys_json["survey_id"],
        completed_at=datetime.datetime.utcnow(),
    )
    complete_survey.save()
    for obj in complete_surveys_json["questions"]:
        questions.append(
            {
                "question_id": obj["question_id"],
                "answer_id": obj["answer_id"],
            }
        )
    for question in questions:
        CompleteSurveyQuestion(
            question_id=question["question_id"],
            answer_id=question["answer_id"],
            complete_survey_id=complete_survey.id,
        ).save()
    return JsonResponse({"data": complete_surveys_json})


def view_complete_survey(request, user_id):
    complete_surveys = parse_complete_survey(
        CompleteSurvey.objects.filter(user_id=user_id)
    )
    complete_survey_questions_obj = parse_complete_survey_question(CompleteSurveyQuestion.objects.all())
    complete_survey_question_list = []
    for complete_survey_question in complete_survey_questions_obj:
        for complete_survey in complete_surveys:
            if complete_survey["id"] == complete_survey_question["complete_survey_id"]:
                complete_survey_question_list.append(complete_survey_question)
        survey_list_obj = []
    for complete_survey in complete_surveys:
        survey_list_obj.append(
            Survey.objects.get(id=complete_survey["survey_id"])
        )  # Проблема
    answer_list_obj = []
    for complete_survey_question in complete_survey_question_list:
        answer_list_obj.append(
            Answer.objects.get(id=complete_survey_question["answer_id"])  # Проблема
        )
    question_list_obj = []
    for complete_survey_question in complete_survey_question_list:
        question_list_obj.append(
            Question.objects.get(id=complete_survey_question["question_id"])  # Проблема
        )
    return render(
        request,
        "surveys/complete_survey.html",
        {
            "complete_surveys": complete_surveys,
            "complete_survey_questions": complete_survey_question_list,
            "question_obj": parse_questions(question_list_obj),
            "answer_obj": parse_answer(answer_list_obj),
            "survey_obj": parse_surveys(survey_list_obj),
        },
    )
