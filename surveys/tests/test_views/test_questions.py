from django import urls
import pytest

from surveys.tests.test_views.helpers import make_answer
from surveys.tests.test_views.helpers import make_question
from surveys.tests.test_views.helpers import make_session
from surveys.tests.test_views.helpers import make_survey
from surveys.tests.test_views.helpers import make_survey_area
from surveys.tests.test_views.helpers import make_survey_question
from surveys.tests.test_views.helpers import make_user


def setup():
    make_answer()
    make_question()
    make_user()
    make_session()
    make_survey_area()
    make_survey()
    make_survey_question()


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
    respone = client.post(
        question_create_url(),
        {"content": "What is it?", "correct_answer_id": 1000},
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
    respone = client.post(
        question_delete_url(),
        {  # fmt: off
            "session_id": "c101a895-f2c0-43a9-ac3e-a54f7f334d56",
            "question_id": 0,
        },  # fmt: on
        content_type="application/json",
    )
    assert respone.status_code == 404


@pytest.mark.django_db
def test_delete_question_used(client):
    respone = client.post(
        question_delete_url(),
        {  # fmt: off
            "session_id": "c101a895-f2c0-43a9-ac3e-a54f7f334d56",
            "question_id": 1001,
        },  # fmt: on
        content_type="application/json",
    )
    assert respone.status_code == 403


@pytest.mark.django_db
def test_delete_question_is_author(client):
    respone = client.post(
        question_delete_url(),
        {  # fmt: off
            "session_id": "c101a895-f2c0-43a9-ac3e-a54f7f334d56",
            "question_id": 1000,
        },  # fmt: on
        content_type="application/json",
    )
    assert respone.status_code == 200


@pytest.mark.django_db
def test_delete_question_not_author(client):
    respone = client.post(
        question_delete_url(),
        {  # fmt: off
            "session_id": "c101a895-f2c0-43a9-ac3e-a54f7f334d56",
            "question_id": 1001,
        },  # fmt: on
        content_type="application/json",
    )
    assert respone.status_code == 403
