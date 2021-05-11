import datetime
import json

from django.contrib.auth.decorators import login_required
from django.db import connection
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


def complete_survey_sql(user_id):
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT survey.name, auth_user.username, compl_survey.completed_at, answer.content as answer, question.content as question
            FROM surveys_completesurvey as compl_survey
            JOIN surveys_survey survey on compl_survey.survey_id = survey.id
            JOIN surveys_completesurveyquestion compl_survey_question on compl_survey.id = compl_survey_question.complete_survey_id
            JOIN surveys_question question on compl_survey_question.question_id = question.id
            JOIN surveys_answer answer on compl_survey_question.answer_id = answer.id
            JOIN auth_user on compl_survey.user_id = auth_user.id
            WHERE compl_survey.user_id = {user_id}
            ORDER BY compl_survey.completed_at;
        """
    )
    return dictfetchall(cursor)


def view_complete_survey(request, user_id):
    complete_survey = complete_survey_sql(user_id=user_id)
    # complete_surveys = parse_complete_surveys(
    #     CompleteSurvey.objects.filter(user_id=user_id)
    # )
    # survey_list_obj = []
    # for complete_survey in complete_surveys:
    #     complete_survey_question_list = []
    #     survey = parse_survey(Survey.objects.get(id=complete_survey["survey_id"]))
    #     complete_survey_questions = parse_complete_survey_questions(
    #         CompleteSurveyQuestion.objects.filter(
    #             complete_survey_id=complete_survey["id"]
    #         )
    #     )
    #     for complete_survey_question in complete_survey_questions:
    #         complete_survey_question_list.append(
    #             {
    #                 "question": parse_question(
    #                     Question.objects.get(id=complete_survey_question["question_id"])
    #                 ),
    #                 "answer": parse_answer(
    #                     Answer.objects.get(id=complete_survey_question["answer_id"])
    #                 ),
    #             }
    #         )
    #     survey_list_obj.append(
    #         {
    #             "survey": survey,
    #             "complete_survey": {
    #                 "completed_at": complete_survey["completed_at"],
    #                 "data": complete_survey_question_list,
    #             },
    #         }
    #     )
    # return render(
    #     request,
    #     "surveys/complete_survey.html",
    #     {
    #         "data": survey_list_obj,
    #     },
    # )
    return render(request, "surveys/complete_survey.html", {"data": complete_survey})


def dictfetchall(cursor):
    """Returns all rows from a cursor as a dict"""
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]


def leaderboard_sql():
    cursor = connection.cursor()
    cursor.execute(
        """SELECT username, COUNT(user_id) as total
            FROM surveys_completesurvey
            JOIN auth_user ON auth_user.id = surveys_completesurvey.user_id
            GROUP BY user_id, username
            ORDER BY total DESC
            LIMIT 10;"""
    )
    return dictfetchall(cursor)


def view_leaderboard(request):
    rows = leaderboard_sql()
    # complete_surveys = (
    #     CompleteSurvey.objects.all()
    #     .values("user_id")
    #     .annotate(total=Count("user_id"))
    #     .order_by("-total")
    # )
    # response_list = []
    # for complete_survey in complete_surveys:
    #     response_list.append(
    #         {
    #             "user": parse_user(User.objects.get(id=complete_survey["user_id"])),
    #             "total": complete_survey["total"],
    #         }
    #     )
    return render(request, "surveys/leaderboard.html", {"complete_surveys": rows})


def leaderboard(request):
    rows = leaderboard_sql()
    return JsonResponse({"data": rows})
