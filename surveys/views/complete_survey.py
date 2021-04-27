import datetime
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

from surveys.logic import allow_only
from surveys.logic import parse_answer
from surveys.logic import parse_complete_survey_questions
from surveys.logic import parse_complete_surveys
from surveys.logic import parse_question
from surveys.logic import parse_survey
from surveys.logic import parse_user
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
    complete_surveys = parse_complete_surveys(
        CompleteSurvey.objects.filter(user_id=user_id)
    )
    survey_list_obj = []
    complete_survey_question_list = []
    for complete_survey in complete_surveys:
        survey = parse_survey(Survey.objects.get(id=complete_survey["survey_id"]))
        complete_survey_questions = parse_complete_survey_questions(
            CompleteSurveyQuestion.objects.filter(
                complete_survey_id=complete_survey["id"]
            )
        )
        for complete_survey_question in complete_survey_questions:
            complete_survey_question_list.append(
                {
                    "questions": parse_question(
                        Question.objects.get(id=complete_survey_question["question_id"])
                    ),
                    "answers": parse_answer(
                        Answer.objects.get(id=complete_survey_question["answer_id"])
                    ),
                }
            )
        survey_list_obj.append(
            {
                "complete_survey": {
                    "completed_at": complete_survey["completed_at"],
                    "data": complete_survey_question_list,
                },
                "survey": survey,
                # "questions": complete_survey_question_list,
            }
        )
    return render(
        request,
        "surveys/complete_survey.html",
        {
            "data": survey_list_obj,
        },
    )


def view_leaderboard(request):
    complete_surveys = (
        CompleteSurvey.objects.all()
        .values("user_id")
        .annotate(total=Count("user_id"))
        .order_by("-total")
    )
    response_list = []
    for complete_survey in complete_surveys:
        response_list.append(
            {
                "user": parse_user(User.objects.get(id=complete_survey["user_id"])),
                "total": complete_survey["total"],
            }
        )
    return render(
        request, "surveys/leaderboard.html", {"complete_surveys": response_list}
    )
