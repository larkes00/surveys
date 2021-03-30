import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from surveys.logic import allow_only, parse_answer, parse_questions, parse_surveys
from surveys.logic import validate
from surveys.models import Answer, CompleteSurvey, Question, Survey
from surveys.models import CompleteSurveyQuestion
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


def complete_survey_view(request, user_id):
    complete_surveys = CompleteSurvey.objects.filter(user_id=user_id)
    complete_survey_list = []
    for complete_survey in complete_surveys:
        complete_survey_list.append(
            {
                "id": complete_survey.id,
                "survey_id": complete_survey.survey_id,
                "user_id": complete_survey.user_id,
                "completed_at": complete_survey.completed_at,
            }
        )
    complete_survey_questions = CompleteSurveyQuestion.objects.filter(
        complete_survey_id=complete_survey_list[0]["id"]
    )
    complete_survey_question_list = []
    for complete_survey_question in complete_survey_questions:
        complete_survey_question_list.append(
            {
                "id": complete_survey_question.id,
                "answer_id": complete_survey_question.answer_id,
                "complete_survey_id": complete_survey_question.complete_survey_id,
                "question_id": complete_survey_question.question_id,
            }
        )
    survey_obj = Survey.objects.filter(id=complete_survey_list[0]["survey_id"])
    question_obj = Question.objects.filter(
        id=complete_survey_question_list[0]["question_id"]
    )
    answer_obj = Answer.objects.filter(id=complete_survey_question_list[0]["answer_id"])
    return render(
        request,
        "surveys/complete_survey.html",
        {
            "complete_survey_question": complete_survey_question_list,
            "question_obj": parse_questions(question_obj),
            "answer_obj": parse_answer(answer_obj),
            "survey_obj": parse_surveys(survey_obj)
        },
    )
