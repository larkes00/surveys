import uuid

from surveys.models import Answer
from surveys.models import Question
from surveys.models import Session
from surveys.models import Survey
from surveys.models import SurveyArea
from surveys.models import SurveyQuestion
from surveys.models import User


def create_session_code():
    return str(uuid.uuid4())


def get_survey(survey_id):
    try:
        survey = Survey.objects.get(id=survey_id)
    except Survey.DoesNotExist:
        return None
    else:
        return survey


def get_session(session_id=None, user_id=None):
    try:
        if session_id is not None:
            session = Session.objects.get(id=session_id)
        else:
            session = Session.objects.get(user_id=user_id)
    except Session.DoesNotExist:
        return None
    else:
        return session


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
            survey_question = SurveyQuestion.objects.get(question_id=question_id)
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


def get_user(login):
    try:
        user = User.objects.get(login=login)
    except User.DoesNotExist:
        return None
    else:
        return user


def parse_surveys(surveys):
    return {
        "id": surveys.id,
        "author_id": surveys.author_id,
        "survey name": surveys.name,
        "type": surveys.type,
    }


def parse_users(users):
    response_list = []
    for user in users:
        response_list.append(
            {
                "id": user.id,
                "user name": user.name,
                "login": user.login,
                "password": user.password,
            }
        )
    return response_list


def parse_questions(questions):
    response_list = []
    for question in questions:
        response_list.append(
            {
                "id": question.id,
                "question name": question.content,
                "author_id": question.author_id,
            }
        )
    return response_list


def parse_survey_area(survey_areas):
    response_list = []
    for survey_area in survey_areas:
        response_list.append(  # fmt: off
            {"id": survey_area.id, "question name": survey_area.name}
        )  # fmt: on
    return response_list
