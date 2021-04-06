from django import urls
import pytest

from surveys.models import CompleteSurvey
from surveys.tests.test_views.helpers import create_answer
from surveys.tests.test_views.helpers import create_question
from surveys.tests.test_views.helpers import create_survey
from surveys.tests.test_views.helpers import create_survey_area
from surveys.tests.test_views.helpers import create_user


def get_login_url():
    return urls.reverse("new_complete_survey")


@pytest.mark.django_db
def test_complete_survey_post_only(client):
    response = client.get(get_login_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_complete_survey_not_auth(client):
    response = client.post(get_login_url(), {}, content_type="application/json")
    assert response.status_code == 302


@pytest.mark.django_db
def test_complete_survey_successful(client):
    create_user(login="TestUser")
    create_survey_area(name="TestSurveyArea")
    create_survey(name="TestSurvey", author_id=1, area_id=1)
    create_answer(content="TestAnswer1", question_id=1, id=1)
    create_question(content="TestQuestion1", correct_answer_id=1, author_id=1, id=1)
    create_answer(content="TestAnswer2", question_id=2, id=2)
    create_question(content="TestQuestion2", correct_answer_id=2, author_id=1, id=2)
    client.login(username="TestUser", password="12345678")
    test_data = {
        "questions": [
            {"question_id": 1, "answer_id": 1, "complete_survey": 1},
            {"question_id": 2, "answer_id": 2, "complete_survey": 1},
        ],
        "user_id": 1,
        "survey_id": 1,
    }
    response = client.post(
        get_login_url(),
        test_data,
        content_type="application/json",
    )
    assert response.status_code == 200
