from django import urls
import pytest

from surveys.logic import get_answer
from surveys.logic import parse_answer
from surveys.tests.test_views.helpers import create_answer
from surveys.tests.test_views.helpers import create_question
from surveys.tests.test_views.helpers import create_survey
from surveys.tests.test_views.helpers import create_survey_area
from surveys.tests.test_views.helpers import create_survey_question
from surveys.tests.test_views.helpers import create_user


def get_answer_create_url():
    return urls.reverse("new_answer")


def get_answer_delete_url():
    return urls.reverse("del_answer")


@pytest.mark.django_db
def test_create_answer_only_post(client):
    response = client.get(get_answer_create_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_delete_answer_only_post(client):
    response = client.get(get_answer_delete_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_answer_create(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    create_question(content="How are you?", author_id=1)
    response = client.post(
        get_answer_create_url(),
        {"content": "Bad", "question_id": 1},
        content_type="application/json",
    )
    assert response.status_code == 200
    answer = parse_answer(get_answer(answer_id=1))
    assert answer == {"id": 1, "content": "Bad"}


@pytest.mark.django_db
def test_del_answer_not_exists(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    response = client.post(
        get_answer_delete_url(),
        {"answer_id": 1, "survey_id": 1},
        content_type="application/json",
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_del_answer_not_successful(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    create_question(content="TestQuestion", author_id=1)
    create_answer(content="TestAnswer")
    create_survey_area(name="TestSurveyArea")
    create_survey_question(question_id=1, survey_id=1)
    create_survey(name="TestSurvey", author_id=1, area_id=1)
    response = client.post(
        get_answer_delete_url(),
        {"answer_id": 1, "survey_id": 1},
        content_type="application/json",
    )
    assert response.status_code == 403


@pytest.mark.django_db
def test_del_answer_successful(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    create_question(content="TestQuestion", author_id=1)
    create_answer(content="TestAnswer")
    create_survey_area(name="TestSurveyArea")
    create_survey(name="TestSurvey", author_id=1, area_id=1)
    response = client.post(
        get_answer_delete_url(),
        {"answer_id": 1, "survey_id": 1},
        content_type="application/json",
    )
    assert response.status_code == 200
