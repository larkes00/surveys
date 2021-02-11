from django import urls
import pytest

from surveys.tests.test_views.helpers import create_answer
from surveys.tests.test_views.helpers import create_question
from surveys.tests.test_views.helpers import create_session
from surveys.tests.test_views.helpers import create_survey
from surveys.tests.test_views.helpers import create_survey_area
from surveys.tests.test_views.helpers import create_survey_question
from surveys.tests.test_views.helpers import create_user


def question_list_url():
    return urls.reverse("questions")


def question_create_url():
    return urls.reverse("new_question")


def question_delete_url():
    return urls.reverse("del_question")


@pytest.mark.django_db
def test_question_list_only_get(client):
    respone = client.post(question_list_url())
    assert respone.status_code == 405


@pytest.mark.django_db
def test_questions_list(client):
    response = client.get(question_list_url())
    assert response.status_code == 200


@pytest.mark.django_db
def test_question_create(client):
    create_answer(content="Nothing", question_id=1)
    respone = client.post(
        question_create_url(),
        {"content": "What is it?", "correct_answer_id": 1},
        content_type="application/json",
    )
    assert respone.status_code == 200


@pytest.mark.django_db
def test_question_delete_session_error(client):
    respone = client.post(
        question_delete_url(),
        {"session_id": "1"},
        content_type="application/json",
    )
    assert respone.status_code == 401


@pytest.mark.django_db
def test_delete_question_not_exist(client):
    create_user(login="Bad12345", password="12345")
    create_session(session_id="test_session_id", user_id=1)
    respone = client.post(
        question_delete_url(),
        {  # fmt: off
            "session_id": "test_session_id",
            "question_id": 0,
        },  # fmt: on
        content_type="application/json",
    )
    assert respone.status_code == 404


@pytest.mark.django_db
def test_delete_question_used(client):
    create_answer(content="Fine", question_id=1)
    create_question(content="How are you?", author_id=1, correct_answer_id=1)
    create_user(login="Bad12345", password="12345")
    create_session(session_id="test_session_id", user_id=1)
    create_survey_area(name="Anything")
    create_survey(name="Survey", author_id=1, area_id=1)
    create_survey_question(survey_id=1, question_id=1)
    respone = client.post(
        question_delete_url(),
        {  # fmt: off
            "session_id": "test_session_id",
            "question_id": 1,
        },  # fmt: on
        content_type="application/json",
    )
    assert respone.status_code == 403


@pytest.mark.django_db
def test_delete_question_is_author(client):
    create_user(login="Bad12345", password="12345")
    create_session(session_id="test_session_id", user_id=1)
    create_answer(content="Fine", question_id=1)
    create_question(content="How are you?", author_id=1, correct_answer_id=1)
    respone = client.post(
        question_delete_url(),
        {  # fmt: off
            "session_id": "test_session_id",
            "question_id": 1,
        },  # fmt: on
        content_type="application/json",
    )
    assert respone.status_code == 200


@pytest.mark.django_db
def test_delete_question_not_author(client):
    create_user(id=1, login="Bad12345")
    create_user(id=2, login="Good12345")
    create_session(session_id="test_session_id", user_id=1)
    create_answer(content="Fine", question_id=1)
    create_question(content="How are you?", author_id=2, correct_answer_id=1)
    respone = client.post(
        question_delete_url(),
        {  # fmt: off
            "session_id": "test_session_id",
            "question_id": 1,
        },  # fmt: on
        content_type="application/json",
    )
    assert respone.status_code == 403
