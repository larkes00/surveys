from django import urls
import pytest

from surveys.logic import get_user
from surveys.logic import parse_users
from surveys.tests.test_views.helpers import create_user


def get_singup_url():
    return urls.reverse("user_signup")


@pytest.mark.django_db
def test_singup_only_post(client):
    response = client.get(get_singup_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_successful_singup(client):
    response = client.post(
        get_singup_url(),
        {"login": "TestUser", "password": "12345678"},
        content_type="application/json",
    )
    assert response.status_code == 200
    user = parse_users(get_user(username="TestUser"))
    assert user == {  # fmt: off
        "id": 1,
        "username": "TestUser",
    }  # fmt: on


# TODO: доделать
@pytest.mark.django_db
def test_unsuccessful_singup(client):
    create_user(login="TestUser", password="12345678")
    response = client.post(  # fmt: off
        get_singup_url(),
        {"login": "TestUser", "password": "12345678"},
        content_type="application/json",
    )  # fmt: on
    assert response.status_code == 400
    user = parse_users(get_user(username="TestUser"))
    assert user == {  # fmt: off
        "id": 1,
        "username": "TestUser",
    }  # fmt: on
