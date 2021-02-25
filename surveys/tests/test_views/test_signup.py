from django import urls
import pytest

from surveys.logic import get_user
from surveys.logic import parse_users
from surveys.tests.test_views.helpers import create_user


def get_singup_url():
    return urls.reverse("signup")


@pytest.mark.django_db
def test_singup_only_post(client):
    response = client.get(get_singup_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_successful_singup(client):
    response = client.post(
        get_singup_url(),
        {"login": "RedWhite", "password": "12345", "name": "Bob"},
        content_type="application/json",
    )
    assert response.status_code == 200
    user = parse_users(get_user(login="RedWhite"))
    assert user == {  # fmt: off
        "id": 1,
        "login": "RedWhite",
        "password": "12345",
        "name": "Bob",
    }  # fmt: on


@pytest.mark.django_db
def test_unsuccessful_singup(client):
    create_user(login="Bad12345", password="12345")
    response = client.post(  # fmt: off
        get_singup_url(),
        {"login": "Bad12345", "password": "12345", "name": "Bruce"},
        content_type="application/json",
    )  # fmt: on
    assert response.status_code == 400
    user = parse_users(get_user(login="Bad12345"))
    assert user == {  # fmt: off
        "login": "Bad12345",
        "password": "12345",
        "name": "John",
        "id": 1,
    }  # fmt: on
