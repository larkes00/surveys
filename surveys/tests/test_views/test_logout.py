from django import urls
import pytest

from surveys.tests.test_views.helpers import make_session
from surveys.tests.test_views.helpers import make_user


def setup():
    make_user()
    make_session()


def get_logout_url():
    return urls.reverse("logout")


@pytest.mark.django_db
def test_logout_only_post(client):
    response = client.get(get_logout_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_successful_logout(client):
    response = client.post(
        get_logout_url(),
        {"session_id": "c101a895-f2c0-43a9-ac3e-a54f7f334d56"},
        content_type="application/json",
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_unsuccessful_logout(client):
    response = client.post(  # fmt off
        get_logout_url(),
        {"session_id": "21daxz"},
        content_type="application/json",
    )  # fmt on
    assert response.status_code == 400
