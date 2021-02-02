import pytest
from django import urls
from surveys.models import User


@pytest.mark.django_db
def test_succesful_login(client):
    url = urls.reverse("login")
    User.objects.create(login="Bad12345", password="12345")
    response = client.post(
        url, {"login": "Bad12345", "password": "12345"}, content_type="application/json"
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_wrong_login(client):
    url = urls.reverse("login")
    User.objects.create(login="Bad12345", password="12345")
    response = client.post(
        url, {"login": "-1", "password": "qq"}, content_type="application/json"
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_login_wrong_password(client):
    url = urls.reverse("login")
    User.objects.create(login="Bad12345", password="12345")
    response = client.post(
        url,
        {"login": "Bad12345", "password": "zzzzzz"},
        content_type="application/json",
    )
    assert response.status_code == 403
