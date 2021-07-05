import json
from json import JSONDecodeError

from django.contrib.auth.models import User
from django.http.response import HttpResponseBadRequest
from django.http.response import HttpResponseNotAllowed

from surveys.models import Answer
from surveys.models import Question
from surveys.models import Survey
from surveys.models import SurveyArea
from surveys.models import SurveyQuestion


def dictfetchall(cursor):
    """Returns all rows from a cursor as a dict"""
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]


def get_survey(survey_id):
    try:
        survey = Survey.objects.get(id=survey_id)
    except Survey.DoesNotExist:
        return None
    else:
        return survey


def get_answer(answer_id):
    try:
        answer = Answer.objects.get(id=answer_id)
    except Answer.DoesNotExist:
        return None
    else:
        return answer


def get_question(question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return None
    else:
        return question


def get_survey_question(question_id, survey_id=None):
    try:
        if survey_id is not None:
            survey_question = SurveyQuestion.objects.get(
                survey_id=survey_id, question_id=question_id
            )
        else:
            survey_question = SurveyQuestion.objects.get(  # fmt: off
                question_id=question_id
            )  # fmt: on
    except SurveyQuestion.DoesNotExist:
        return None
    else:
        return survey_question


def get_survey_area(survey_area_id):
    try:
        survey_area = SurveyArea.objects.get(id=survey_area_id)
    except SurveyArea.DoesNotExist:
        return None
    else:
        return survey_area


def get_user(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    else:
        return user


def parse_survey(survey):
    return {
        "id": survey.id,
        "author_id": survey.author_id,
        "area_id": survey.area_id,
        "name": survey.name,
        "type": survey.type,
    }


def parse_surveys(surveys):
    response_list = []
    for survey in surveys:
        response_list.append(parse_survey(survey))
    return response_list


def parse_user(user):
    return {
        "id": user.id,
        "username": user.username,
    }


def parse_users(users):
    response_list = []
    for user in users:
        response_list.append(parse_user(user))
    return response_list


def parse_question(question):
    return {
        "id": question.id,
        "content": question.content,
        "author_id": question.author_id,
    }


def parse_questions(questions):
    response_list = []
    for question in questions:
        response_list.append(parse_question(question))
    return response_list


def parse_survey_area(survey_area):
    return {"id": survey_area.id, "name": survey_area.name}


def parse_survey_areas(survey_areas):
    response_list = []
    for survey_area in survey_areas:
        response_list.append(parse_survey_area(survey_area))
    return response_list


def parse_answer(answer):
    return {
        "id": answer.id,
        "content": answer.content,
    }


def parse_answers(answers):
    response_list = []
    for answer in answers:
        response_list.append(parse_answer(answer))
    return response_list


def parse_complete_survey(complete_survey):
    return {
        "id": complete_survey.id,
        "survey_id": complete_survey.survey_id,
        "user_id": complete_survey.user_id,
        "completed_at": complete_survey.completed_at,
    }


def parse_complete_surveys(complete_surveys):
    response_list = []
    for complete_survey in complete_surveys:
        response_list.append(parse_complete_survey(complete_survey))
    return response_list


def parse_complete_survey_question(complete_survey_question):
    return {
        "id": complete_survey_question.id,
        "answer_id": complete_survey_question.answer_id,
        "complete_survey_id": complete_survey_question.complete_survey_id,
        "question_id": complete_survey_question.question_id,
    }


def parse_complete_survey_questions(complete_survey_questions):
    response_list = []
    for complete_survey_question in complete_survey_questions:
        response_list.append(parse_complete_survey_question(complete_survey_question))
    return response_list


def allow_only(methods):
    def decorator(handler):
        def new_handler(request, *args, **kwargs):
            if request.method not in methods:
                return HttpResponseNotAllowed(methods)
            return handler(request, *args, **kwargs)

        return new_handler

    return decorator


def validate(serializer_cls):
    def decorator(handler):
        def new_handler(request, *args, **kwargs):
            try:
                request_body = json.loads(request.body)
            except (TypeError, JSONDecodeError) as e:
                return HttpResponseBadRequest(f"Error while parsing response body: {e}")
            serializer = serializer_cls(data=request_body)
            if not serializer.is_valid():
                return HttpResponseBadRequest(json.dumps(serializer.errors))
            return handler(request, *args, **kwargs)

        return new_handler

    return decorator


def ensure_json():
    def decorator(handler):
        def new_handler(request):
            try:
                json.loads(request.body)
            except ValueError:
                return HttpResponseBadRequest()
            return handler(request)

        return new_handler

    return decorator
