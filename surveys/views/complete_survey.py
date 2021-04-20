import datetime
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

from surveys.logic import allow_only
from surveys.logic import parse_answer
from surveys.logic import parse_complete_survey
from surveys.logic import parse_complete_survey_question
from surveys.logic import parse_questions
from surveys.logic import parse_surveys
from surveys.logic import parse_users
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
    survey_list_obj = []
    complete_survey_question_list = []
    for complete_survey in complete_surveys:
        survey = parse_surveys(Survey.objects.get(id=complete_survey["survey_id"]))
        complete_survey_questions = parse_complete_survey_question(
            CompleteSurveyQuestion.objects.filter(
                complete_survey_id=complete_survey["id"]
            )
        )
        complete_survey_question_list = []
        for complete_survey_question in complete_survey_questions:
            complete_survey_question_list.append(
                {
                    "questions": parse_questions(
                        Question.objects.get(id=complete_survey_question["question_id"])
                    ),
                    "answers": parse_answer(
                        Answer.objects.get(id=complete_survey_question["answer_id"])
                    ),
                }
            )

        survey_list_obj.append(
            {
                "complete_survey": complete_survey,
                "survey": survey,
                "questions": complete_survey_question_list,
            }
        )
    return render(
        request,
        "surveys/complete_survey.html",
        {
            "survey_obj": survey_list_obj,
        },
    )


def view_leaderboard(request):
    complete_survey_list = []
    complete_surveys = parse_complete_survey(CompleteSurvey.objects.all())
    for complete_survey in complete_surveys:
        user = parse_users(User.objects.get(id=complete_survey["user_id"]))
        found = False
        for i in range(0, len(complete_survey_list)):
            if complete_survey_list[i]["user"] == user:
                complete_survey_list[i]["count"] += 1
                found = True
            else:
                found = False
        if len(complete_survey_list) == 0 or not found:
            complete_survey_list.append({"user": user, "count": 1})
    new_list = sorted(complete_survey_list, key=lambda k: k['count'], reverse=True)
    return render(
        request, "surveys/leaderboard.html", {"complete_surveys": new_list}
    )
