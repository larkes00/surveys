from django import urls
import pytest

from surveys.tests.test_views.helpers import create_user


def get_logout_url():
    return urls.reverse("logout")


@pytest.mark.django_db
def test_logout_only_get(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    response = client.post(get_logout_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_successful_logout(client):
    create_user(login="TestUser")
    client.login(username="TestUser", password="12345678")
    response = client.get(get_logout_url())
    assert response.status_code == 302


@pytest.mark.django_db
def test_unsuccessful_logout(client):
    response = client.get(get_logout_url())
    assert response.status_code == 302
