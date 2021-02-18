from django import urls
import pytest

from surveys.logic import get_survey_area
from surveys.logic import parse_survey_area
from surveys.tests.test_views.helpers import create_survey_area


def get_survey_area_list_url():
    return urls.reverse("survey_areas")


def get_survey_area_create_url():
    return urls.reverse("new_survey_area")


def get_survey_area_delete_url():
    return urls.reverse("del_survey_area")


@pytest.mark.django_db
def test_survey_area_list_get_only(client):
    response = client.post(
        get_survey_area_list_url(), {}, content_type="application/json"
    )
    assert response.status_code == 405


@pytest.mark.django_db
def test_survey_area_create_post_only(client):
    response = client.get(get_survey_area_create_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_survey_area_delete_post_only(client):
    response = client.get(get_survey_area_delete_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_survey_area_get_list(client):
    create_survey_area(id=1, name="Anything")
    create_survey_area(id=2, name="Nothing")
    response = client.get(get_survey_area_list_url())
    assert response.status_code == 200
    assert response.json()["data"] == [
        {"id": 1, "name": "Anything"},
        {"id": 2, "name": "Nothing"},
    ]


@pytest.mark.django_db
def test_survey_area_create_successful(client):
    response = client.post(
        get_survey_area_create_url(),
        {"name": "Something"},
        content_type="application/json",
    )
    assert response.status_code == 200
    survey_area = parse_survey_area(get_survey_area(survey_area_id=1))
    assert survey_area == {"id": 1, "name": "Something"}


@pytest.mark.django_db
def test_survey_area_delete_successful(client):
    survey_area = create_survey_area(name="Anything")
    response = client.post(
        get_survey_area_delete_url(),
        {"survey_area_id": 1},
        content_type="application/json",
    )
    assert response.status_code == 200
    survey_area_obj = get_survey_area(survey_area_id=survey_area.id)
    assert survey_area_obj is None


@pytest.mark.django_db
def test_survey_area_delete_unsuccessful(client):
    response = client.post(
        get_survey_area_delete_url(),
        {"survey_area_id": 1},
        content_type="application/json",
    )
    assert response.status_code == 404
