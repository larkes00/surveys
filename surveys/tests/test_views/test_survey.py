from django import urls
import pytest

from surveys.tests.test_views.helpers import make_session
from surveys.tests.test_views.helpers import make_survey
from surveys.tests.test_views.helpers import make_survey_area
from surveys.tests.test_views.helpers import make_user


def setup():
    make_survey_area()
    make_user()
    make_survey()
    make_session()


def get_survey_list_url():
    return urls.reverse("surveys")


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
    response = client.get(get_survey_get_one_url(1000))
    assert response.status_code == 200


@pytest.mark.django_db
def test_unsuccessful_get_one_survey(client):
    response = client.get(get_survey_get_one_url(10000))
    assert response.status_code == 404


@pytest.mark.django_db
def test_create_survey(client):
    response = client.post(
        get_survey_create_url(),
        {  # fmt off
            "author_id": 1000,
            "area_id": 1000,
            "name": "I don't know",
            "type": "Formal",
        },  # fmt on
        content_type="application/json",
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_survey_wrong_session_code(client):
    response = client.post(  # fmt off
        get_survey_delete_url(),
        {"session_id": "1"},
        content_type="application/json",
    )  # fmt on
    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_survey_no_such_survey(client):
    response = client.post(
        get_survey_delete_url(),
        {"session_id": "c101a895-f2c0-43a9-ac3e-a54f7f334d56", "survey_id": 0},
        content_type="application/json",
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_successful_delete_survey(client):
    response = client.post(
        get_survey_delete_url(),
        {  # fmt off
            "session_id": "c101a895-f2c0-43a9-ac3e-a54f7f334d56",
            "survey_id": 1000,
        },  # fmt on
        content_type="application/json",
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_no_accees_delete_survey(client):
    response = client.post(
        get_survey_delete_url(),
        {  # fmt off
            "session_id": "xd11a895-f2c0-43a9-ac3e-a54f7f334d56",
            "survey_id": 1000,
        },  # fmt on
        content_type="application/json",
    )
    assert response.status_code == 403
