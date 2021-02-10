from django import urls
import pytest


def get_answer_create_url():
    return urls.reverse("new_answer")


@pytest.mark.django_db
def test_answer_only_post(client):
    response = client.get(get_answer_create_url())
    assert response.status_code == 405
