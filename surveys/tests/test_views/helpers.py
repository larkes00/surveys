from surveys.models import Answer
from surveys.models import Question
from surveys.models import Session
from surveys.models import Survey
from surveys.models import SurveyArea
from surveys.models import User


def make_user():
    User(id=1000, login="Bad12345", password="12345", name="Bruce").save()
    User(id=1001, login="Good12345", password="12345", name="Bob").save()


def make_session():
    Session(id="c101a895-f2c0-43a9-ac3e-a54f7f334d56", user_id=1000).save()
    Session(id="xd11a895-f2c0-43a9-ac3e-a54f7f334d56", user_id=1001).save()


def make_question():
    Question(id=1000, content="How are you?", correct_answer_id=1000).save()
    Question(id=1001, content="Where are you?", correct_answer_id=1001).save()


def make_answer():
    Answer(id=1000, content="Fine", question_id=1000).save()
    Answer(id=1001, content="I'm home", question_id=1001).save()


def make_survey_area():
    SurveyArea(id=1000, name="Something").save()


def make_survey():
    # fmt: off
    Survey(id=1000, name="Survey", author_id=1000, area_id=1000, type="Formal").save()  # noqa: E501
    # fmt: on


def make_survey_question():
    SurveyArea(survey_id=1001, question_id=1001).save()
