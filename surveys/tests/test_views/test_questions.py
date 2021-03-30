from django import urls
import pytest

from surveys.logic import get_question
from surveys.logic import parse_questions
from surveys.tests.test_views.helpers import create_answer
from surveys.tests.test_views.helpers import create_question
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
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    response = client.get(question_list_url())
    assert response.status_code == 200


@pytest.mark.django_db
def test_question_create(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    create_answer(content="Nothing", question_id=1)
    respone = client.post(
        question_create_url(),
        {"content": "TestQuestion2", "correct_answer_id": 1},
        content_type="application/json",
    )
    assert respone.status_code == 200


@pytest.mark.django_db
def test_question_delete_not_auth(client):
    respone = client.post(
        question_delete_url(),
        {},
        content_type="application/json",
    )
    assert respone.status_code == 302


@pytest.mark.django_db
def test_delete_question_not_exist(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    respone = client.post(
        question_delete_url(),
        {  # fmt: off
            "question_id": 0,
        },  # fmt: on
        content_type="application/json",
    )
    assert respone.status_code == 404


@pytest.mark.django_db
def test_delete_question_used(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    create_answer(content="TestAnswer", question_id=1)
    question = create_question(  # fmt: off
        content="TestQuestion?", author_id=1, correct_answer_id=1
    )  # fmt: on
    create_survey_area(name="Anything")
    create_survey(name="Survey", author_id=1, area_id=1)
    create_survey_question(survey_id=1, question_id=1)
    respone = client.post(
        question_delete_url(),
        {  # fmt: off
            "question_id": 1,
        },  # fmt: on
        content_type="application/json",
    )
    assert respone.status_code == 403
    question_obj = parse_questions(get_question(question_id=question.id))
    assert question_obj == {  # fmt: off
        "id": 1,
        "content": "TestQuestion?",
        "author_id": 1,
    }  # fmt: on


@pytest.mark.django_db
def test_delete_question_is_author(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    create_answer(content="Fine", question_id=1)
    question = create_question(  # fmt: off
        content="How are you?", author_id=1, correct_answer_id=1
    )  # fmt: on
    respone = client.post(
        question_delete_url(),
        {  # fmt: off
            "question_id": 1,
        },  # fmt: on
        content_type="application/json",
    )
    assert respone.status_code == 200
    question_obj = get_question(question_id=question.id)
    assert question_obj is None


@pytest.mark.django_db
def test_delete_question_not_author(client):
    create_user(id=1, login="TestUser1")
    create_user(id=2, login="TestUser2")
    client.login(username="TestUser1", password="12345678")
    create_answer(content="Fine", question_id=1)
    question = create_question(  # fmt: off
        content="How are you?", author_id=2, correct_answer_id=1
    )  # fmt: on
    respone = client.post(
        question_delete_url(),
        {  # fmt: off
            "question_id": 1,
        },  # fmt: on
        content_type="application/json",
    )
    assert respone.status_code == 403
    question_obj = parse_questions(get_question(question_id=question.id))
    assert question_obj == {  # fmt: off
        "id": 1,
        "content": "How are you?",
        "author_id": 2,
    }  # fmt: on
