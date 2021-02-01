import pytest
from django import urls
from surveys.models import User
from surveys.models import Session


@pytest.mark.django_db
def test_successful_singup(client):
    url = urls.reverse("singup")
    response = client.post(
        url, {"login": "RedWhite", "password": "1111", "name": "Bob"}
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_unsuccessful_singup(client):
    url = urls.reverse("singup")
    User.objects.create(login="GG", password="12345", name="Bruce")
    response = client.post(  # fmt: off
        url, {"login": "GG", "password": "12345", "name": "Bruce"}
    )  # fmt: on
    assert response.status_code == 400


@pytest.mark.django_db
def test_succesful_login(client):
    url = urls.reverse("login")
    User.objects.create(login="Bad12345", password="12345")
    response = client.post(url, {"login": "Bad12345", "password": "12345"})
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_wrong_login(client):
    url = urls.reverse("login")
    User.objects.create(login="Bad12345", password="12345")
    response = client.post(url, {"login": "-1", "password": "qq"})
    assert response.status_code == 404


@pytest.mark.django_db
def test_login_wrong_password(client):
    url = urls.reverse("login")
    User.objects.create(login="Bad12345", password="12345")
    response = client.post(url, {"login": "Bad12345", "password": "zzzzzz"})
    assert response.status_code == 403


@pytest.mark.django_db
def test_successful_logout(client):
    url = urls.reverse("logout")
    Session.objects.create(
        id="c101a895-f2c0-43a9-ac3e-a54f7f3s4d56", user_id=1
    )  # fmt: off
    response = client.post(
        url, {"session_id": "c101a895-f2c0-43a9-ac3e-a54f7f334d56"}
    )  # fmt: on
    assert response.status_code == 200


@pytest.mark.django_db
def test_unsuccessful_logout(client):
    url = urls.reverse("logout")
    Session.objects.create(  # fmt: off
        id="c101a895-f2c0-43a9-ac3e-a54f7f3s4d56", user_id=1
    )  # fmt: on
    response = client.post(url, {"session_id": "21daxz"})
    assert response.status_code == 400
