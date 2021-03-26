from django import urls
import pytest

from surveys.tests.test_views.helpers import create_user


def get_user_list_url():
    return urls.reverse("users")


@pytest.mark.django_db
def test_user_list_only_get(client):
    response = client.post(  # fmt: off
        get_user_list_url(), {}, content_type="application/json"
    )  # fmt: on
    assert response.status_code == 405


@pytest.mark.django_db
def test_user_list_successful(client):
    create_user(id=1, login="TestUser1")
    client.login(username="TestUser1", password="12345678")
    create_user(id=2, login="TestUser2")
    response = client.get(get_user_list_url())
    assert response.status_code == 200
