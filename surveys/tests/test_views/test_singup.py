from django import urls
import pytest

from surveys.logic import parse_users
from surveys.models import User
from surveys.tests.test_views.helpers import create_user


def get_singup_url():
    return urls.reverse("singup")


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
    print(parse_users(User.objects.all()))


@pytest.mark.django_db
def test_unsuccessful_singup(client):
    create_user(login="Bad12345", password="12345")
    response = client.post(  # fmt: off
        get_singup_url(),
        {"login": "Bad12345", "password": "12345", "name": "Bruce"},
        content_type="application/json",
    )  # fmt: on
    assert response.status_code == 400
