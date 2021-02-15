from django import urls
import pytest

from surveys.logic import get_session
from surveys.tests.test_views.helpers import create_user


def get_login_url():
    return urls.reverse("login")


@pytest.mark.django_db
def test_login_only_post(client):
    response = client.get(get_login_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_successful_login(client):
    user = create_user(login="Bad12345", password="12345")
    response = client.post(
        get_login_url(),
        {"login": "Bad12345", "password": "12345"},
        content_type="application/json",
    )
    assert response.status_code == 200

    user_session = get_session(user_id=user.id)
    assert user_session is not None


@pytest.mark.django_db
def test_login_wrong_login(client):
    user = create_user(login="Bad12345", password="12345")
    response = client.post(
        get_login_url(),
        {"login": "-1", "password": "12345"},
        content_type="application/json",
    )
    assert response.status_code == 404
    session = get_session(user_id=user.id)
    assert session is None


@pytest.mark.django_db
def test_login_wrong_password(client):
    user = create_user(login="Bad12345", password="12345")
    response = client.post(
        get_login_url(),
        {"login": "Bad12345", "password": "wrong_password"},
        content_type="application/json",
    )
    assert response.status_code == 403
    session = get_session(user_id=user.id)
    assert session is None
