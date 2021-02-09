from surveys.models import Answer
from surveys.models import Question
from surveys.models import Session
from surveys.models import Survey
from surveys.models import SurveyArea
from surveys.models import SurveyQuestion
from surveys.models import User


def create_user(login: str, password: str = "12345", name: str = "John"):
    user = User(login=login, password=password, name=name)
    user.save()
    return user


def create_session(session_id: str, user_id: int):
    session = Session(id=session_id, user_id=user_id)
    session.save()
    return session


def create_question(content: str, correct_answer_id: int, author_id: int):
    # fmt: off
    question = Question(
        content=content,
        correct_answer_id=correct_answer_id,
        author_id=author_id
    )
    # fmt: on
    question.save()
    return question


def create_answer(content: str, question_id: int):
    answer = Answer(content=content, question_id=question_id)
    answer.save()
    return answer


def create_survey_area(name: str):
    survey_area = SurveyArea(name=name)
    survey_area.save()
    return survey_area


def create_survey(name: str, author_id: int, area_id: int, type_survey: str = "Formal"):  # noqa: E501
    survey = Survey(name=name, author_id=author_id, area_id=area_id, type=type_survey)  # noqa: E501
    survey.save()
    return survey


def create_survey_question(survey_id: int, question_id: int):
    survey_question = SurveyQuestion(  # fmt: off
        survey_id=survey_id, question_id=question_id
    )  # fmt: on
    survey_question.save()
    return survey_question


def make_user():
    User(id=1000, login="Bad12345", password="12345", name="Bruce").save()
    User(id=1001, login="Good12345", password="12345", name="Bob").save()


def make_session():
    Session(id="c101a895-f2c0-43a9-ac3e-a54f7f334d56", user_id=1000).save()
    Session(id="xd11a895-f2c0-43a9-ac3e-a54f7f334d56", user_id=1001).save()


def make_question():
    Question(
        id=1000, content="How are you?", correct_answer_id=1000, author_id=1000
    ).save()
    Question(
        id=1001,
        content="Where are you?",
        correct_answer_id=1001,
        author_id=1001,  # noqa: E501
    ).save()


def make_answer():
    Answer(id=1000, content="Fine", question_id=1000).save()
    Answer(id=1001, content="I'm home", question_id=1001).save()


def make_survey_area():
    SurveyArea(id=1000, name="Something").save()
    SurveyArea(id=1001, name="Good").save()


def make_survey():
    # fmt: off
    Survey(id=1000, name="Survey", author_id=1000, area_id=1000, type="Formal").save()  # noqa: E501
    Survey(id=1001, name="Good", author_id=1001, area_id=1001, type="Test").save()  # noqa: E501
    # fmt: on


def make_survey_question():
    SurveyQuestion(id=1000, question_id=1001, survey_id=1001).save()
