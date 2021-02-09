from django import urls
import pytest

from surveys.tests.test_views.helpers import create_session
from surveys.tests.test_views.helpers import create_user


def get_logout_url():
    return urls.reverse("logout")


@pytest.mark.django_db
def test_logout_only_post(client):
    response = client.get(get_logout_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_successful_logout(client):
    create_user(login="Bad12345", password="12345")
    create_session(session_id="test_session_id", user_id=1)
    response = client.post(
        get_logout_url(),
        {"session_id": "test_session_id"},
        content_type="application/json",
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_unsuccessful_logout(client):
    response = client.post(  # fmt: off
        get_logout_url(),
        {"session_id": "test_wrong_session_id"},
        content_type="application/json",
    )  # fmt: on
    assert response.status_code == 400
