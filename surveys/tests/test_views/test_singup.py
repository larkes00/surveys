import pytest
from django import urls
from surveys.models import User


@pytest.mark.django_db
def test_successful_singup(client):
    url = urls.reverse("singup")
    response = client.post(
        url,
        {"login": "RedWhite", "password": "1111", "name": "Bob"},
        content_type="application/json",
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_unsuccessful_singup(client):
    url = urls.reverse("singup")
    User.objects.create(login="GG", password="12345", name="Bruce")
    response = client.post(  # fmt: off
        url,
        {"login": "GG", "password": "12345", "name": "Bruce"},
        content_type="application/json",
    )  # fmt: on
    assert response.status_code == 400
