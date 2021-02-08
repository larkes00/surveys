from django import urls
import pytest

from surveys.tests.test_views.helpers import make_survey_area


def setup():
    make_survey_area()


def get_survey_area_list_url():
    return urls.reverse("survey_areas")


def get_survey_area_create_url():
    return urls.reverse("new_survey_area")


def get_survey_area_delete_url():
    return urls.reverse("del_survey_area")


@pytest.mark.django_db
def test_survey_area_list_get_only(client):
    respone = client.post(
        get_survey_area_list_url(), {}, content_type="appication/json"
    )
    assert respone.status_code == 405


@pytest.mark.django_db
def test_survey_area_create_post_only(client):
    respone = client.get(get_survey_area_create_url())
    assert respone.status_code == 405


@pytest.mark.django_db
def test_survey_area_delete_post_only(client):
    respone = client.get(get_survey_area_delete_url())
    assert respone.status_code == 405


@pytest.mark.django_db
def test_survey_area_get_list(client):
    respone = client.get(get_survey_area_list_url())
    assert respone.status_code == 200


@pytest.mark.django_db
def test_survey_area_create_successful(client):
    respone = client.post(
        get_survey_area_create_url(),
        {"id": 1004, "name": "Something"},
        content_type="application/json",
    )
    assert respone.status_code == 200


@pytest.mark.django_db
def test_survey_area_delete_successful(client):
    respone = client.post(
        get_survey_area_delete_url(),
        {"survey_area_id": 1000},
        content_type="application/json",
    )
    assert respone.status_code == 200


@pytest.mark.django_db
def test_survey_area_delete_unsuccessful(client):
    respone = client.post(
        get_survey_area_delete_url(),
        {"survey_area_id": 1002},
        content_type="application/json",
    )
    assert respone.status_code == 404
