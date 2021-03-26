from django import urls
import pytest

from surveys.tests.test_views.helpers import create_user


def get_login_url():
    return urls.reverse("user_login")


@pytest.mark.django_db
def test_login_only_post(client):
    response = client.get(get_login_url())
    print(response.content)
    assert response.status_code == 405


@pytest.mark.django_db
def test_successful_login(client):
    create_user(login="TestUser", password="12345678")
    response = client.post(
        get_login_url(),
        {"login": "TestUser", "password": "12345678"},
        content_type="application/json",
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_wrong_login(client):
    create_user(login="TestUser")
    response = client.post(
        get_login_url(),
        {"login": "WrongTestUser", "password": "12345678"},
        content_type="application/json",
    )
    print(response.content)
    assert response.status_code == 404
