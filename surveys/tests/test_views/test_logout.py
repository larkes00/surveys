from surveys.tests.test_views.helpers import make_session, make_user
import pytest
from django import urls


def setup():
    make_user()
    make_session()


@pytest.mark.django_db
def test_successful_logout(client):
    url = urls.reverse("logout")
    response = client.post(
        url,
        {"session_id": "c101a895-f2c0-43a9-ac3e-a54f7f334d56"},
        content_type="application/json",
    )  # fmt: on
    assert response.status_code == 200


@pytest.mark.django_db
def test_unsuccessful_logout(client):
    url = urls.reverse("logout")
    response = client.post(
        url, {"session_id": "21daxz"}, content_type="application/json"
    )
    assert response.status_code == 400
