import json
from json import JSONDecodeError

from django.http.response import HttpResponseBadRequest
from django.http.response import HttpResponseNotAllowed

from surveys.models import Answer
from surveys.models import Question
from surveys.models import Survey
from surveys.models import SurveyArea
from surveys.models import SurveyQuestion


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


# def get_user(login):
#     try:
#         user = User.objects.get(login=login)
#     except User.DoesNotExist:
#         return None
#     else:
#         return user


def parse_surveys(surveys):
    return {
        "id": surveys.id,
        "author_id": surveys.author_id,
        "area_id": surveys.area_id,
        "name": surveys.name,
        "type": surveys.type,
    }


def parse_users(users):
    response_list = []
    try:
        for user in users:
            response_list.append(
                {
                    "id": user.id,
                    "username": user.username,
                }
            )
    except TypeError:
        return {
            "id": users.id,
            "username": users.username,
        }
    return response_list


def parse_questions(questions):
    response_list = []
    try:
        for question in questions:
            response_list.append(
                {
                    "id": question.id,
                    "question name": question.content,
                    "author_id": question.author_id,
                }
            )
    except TypeError:
        return {
            "id": questions.id,
            "question name": questions.content,
            "author_id": questions.author_id,
        }
    return response_list


def parse_survey_area(survey_areas):
    response_list = []
    try:
        for survey_area in survey_areas:
            response_list.append(  # fmt: off
                {"id": survey_area.id, "name": survey_area.name}
            )  # fmt: on
    except TypeError:
        return {"id": survey_areas.id, "name": survey_areas.name}
    return response_list


def parse_answer(answer):
    return {
        "id": answer.id,
        "content": answer.content,
        "question_id": answer.question_id,
    }


def allow_only(methods):
    def decorator(handler):
        def new_handler(request):
            if request.method not in methods:
                return HttpResponseNotAllowed(methods)
            return handler(request)

        return new_handler

    return decorator


def validate(serializer_cls):
    def decorator(handler):
        def new_handler(request):
            try:
                request_body = json.loads(request.body)
            except (TypeError, JSONDecodeError):
                return HttpResponseBadRequest()
            serializer = serializer_cls(data=request_body)
            if not serializer.is_valid():
                return HttpResponseBadRequest(json.dumps(serializer.errors))
            return handler(request)

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
