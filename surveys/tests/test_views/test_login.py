from django import urls
import pytest

from surveys.models import Session
from surveys.tests.test_views.helpers import create_user, make_user


def setup():
    make_user()


def get_login_url():
    return urls.reverse("login")


@pytest.mark.django_db
def test_login_only_post(client):
    response = client.get(get_login_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_succesful_login(client):
    user = create_user(login='john_doe', password="12345")
    response = client.post(
        get_login_url(),
        {"login": "john_doe", "password": "12345"},
        content_type="application/json",
    )
    assert response.status_code == 200

    user_session = Session.objects.get(user_id=user.id)
    assert user_session is not None


@pytest.mark.django_db
def test_wrong_login(client):
    response = client.post(
        get_login_url(),
        {"login": "-1", "password": "qq"},
        content_type="application/json",
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_login_wrong_password(client):
    response = client.post(
        get_login_url(),
        {"login": "Bad12345", "password": "zzzzzz"},
        content_type="application/json",
    )
    assert response.status_code == 403
