from django.contrib.auth.models import User

from surveys.models import Answer
from surveys.models import Question
from surveys.models import Survey
from surveys.models import SurveyArea
from surveys.models import SurveyQuestion


# from surveys.models import SurveyQuestion


def create_user(login: str, password: str = "12345678", id: int = 1):
    user = User.objects.create_user(id=id, username=login, password=password)
    user.save()
    return user


def create_question(content: str, correct_answer_id: int, author_id: int, id: int = 1):
    # fmt: off
    question = Question(
        id=id,
        content=content,
        correct_answer_id=correct_answer_id,
        author_id=author_id
    )
    # fmt: on
    question.save()
    return question


def create_answer(content: str, question_id: int, id: int = 1):
    answer = Answer(id=id, content=content, question_id=question_id)
    answer.save()
    return answer


def create_survey_area(name: str, id: int = 1):
    survey_area = SurveyArea(id=id, name=name)
    survey_area.save()
    return survey_area


# fmt: off
def create_survey(name: str, author_id: int, area_id: int, type_survey: str = "Formal", id: int = 1):  # noqa: E501
    survey = Survey(id=id, name=name, author_id=author_id, area_id=area_id, type=type_survey)  # noqa: E501
    survey.save()
    return survey
# fmt: on


def create_survey_question(survey_id: int, question_id: int):
    survey_question = SurveyQuestion(  # fmt: off
        survey_id=survey_id, question_id=question_id
    )  # fmt: on
    survey_question.save()
    return survey_question
