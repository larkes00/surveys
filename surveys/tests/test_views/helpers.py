from surveys.models import Answer
from surveys.models import Question
from surveys.models import Session
from surveys.models import Survey
from surveys.models import SurveyQuestion
from surveys.models import User


def make_user():
    user = User(id=1000, login="Bad12345", password="12345", name="Bruce")
    user.save()


def make_session():
    session = Session(id="c101a895-f2c0-43a9-ac3e-a54f7f334d56", user_id=1000)
    session.save()
