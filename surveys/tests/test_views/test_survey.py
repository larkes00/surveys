from django import urls
import pytest

from surveys.logic import get_survey
from surveys.logic import parse_survey
from surveys.tests.test_views.helpers import create_survey
from surveys.tests.test_views.helpers import create_survey_area
from surveys.tests.test_views.helpers import create_user


def get_survey_list_url():
    return urls.reverse("view_surveys")


def get_survey_get_one_url(survey_id):
    return urls.reverse("survey", args=[survey_id])


def get_survey_create_url():
    return urls.reverse("create_survey")


def get_survey_delete_url():
    return urls.reverse("del_survey")


@pytest.mark.django_db
def test_survey_list_only_get(client):
    response = client.post(  # fmt off
        get_survey_list_url(), {}, content_type="application/json"
    )  # fmt on
    assert response.status_code == 405


@pytest.mark.django_db
def test_survey_get_one_only_get(client):
    response = client.post(
        get_survey_get_one_url(2000), {}, content_type="application/json"
    )
    assert response.status_code == 405


@pytest.mark.django_db
def test_survey_create_only_post(client):
    response = client.get(get_survey_create_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_survey_delete_only_post(client):
    response = client.get(get_survey_delete_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_survey_list(client):
    response = client.get(get_survey_list_url())
    assert response.status_code == 200


@pytest.mark.django_db
def test_successful_get_one_survey(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    create_survey_area("Anything")
    create_survey(name="Survey", author_id=1, area_id=1)
    response = client.get(get_survey_get_one_url(1))
    assert response.status_code == 200
    survey = parse_survey(get_survey(survey_id=1))
    assert survey == {
        "id": 1,
        "name": "Survey",
        "author_id": 1,
        "area_id": 1,
        "type": "Formal",
    }


@pytest.mark.django_db
def test_unsuccessful_get_one_survey(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    response = client.get(get_survey_get_one_url(10000))
    assert response.status_code == 404


@pytest.mark.django_db
def test_create_survey(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    create_survey_area("Anything")
    response = client.post(
        get_survey_create_url(),
        {  # fmt off
            "author_id": 1,
            "area_id": 1,
            "name": "I don't know",
            "type": "Formal",
        },  # fmt on
        content_type="application/json",
    )
    assert response.status_code == 200
    survey_obj = parse_survey(get_survey(survey_id=1))
    assert survey_obj == {
        "id": 1,
        "author_id": 1,
        "area_id": 1,
        "name": "I don't know",
        "type": "Formal",
    }


@pytest.mark.django_db
def test_delete_survey_no_accees(client):
    response = client.post(  # fmt off
        get_survey_delete_url(),
        {},
        content_type="application/json",
    )  # fmt on
    assert response.status_code == 302


@pytest.mark.django_db
def test_delete_survey_no_such_survey(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    create_survey_area("TestSurveyArea")
    create_survey(name="TestSurvey", author_id=1, area_id=1)
    response = client.post(
        get_survey_delete_url(),
        {"session_id": "test_session_id", "survey_id": 0},
        content_type="application/json",
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_successful_delete_survey(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    create_survey_area("TestSurveyArea")
    survey = create_survey(name="TestSurvey", author_id=1, area_id=1)
    response = client.post(
        get_survey_delete_url(),
        {  # fmt off
            "survey_id": 1,
        },  # fmt on
        content_type="application/json",
    )
    assert response.status_code == 200
    survey_obj = get_survey(survey_id=survey.id)
    assert survey_obj is None


@pytest.mark.django_db
def test_not_author_delete_survey(client):
    create_user(login="TestUser1", id=1)
    create_user(login="TestUser2", id=2)
    client.login(username="TestUser2", password="12345678")
    create_survey_area("TestSurveyArea")
    create_survey(name="TestSurvey", author_id=1, area_id=1)
    response = client.post(
        get_survey_delete_url(),
        {"survey_id": 1},  # fmt off  # fmt on
        content_type="application/json",
    )
    assert response.status_code == 403
