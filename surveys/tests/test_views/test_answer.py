from django import urls
import pytest

from surveys.logic import get_answer
from surveys.logic import parse_answer
from surveys.tests.test_views.helpers import create_question
from surveys.tests.test_views.helpers import create_user


def get_answer_create_url():
    return urls.reverse("new_answer")


@pytest.mark.django_db
def test_answer_only_post(client):
    response = client.get(get_answer_create_url())
    assert response.status_code == 405


@pytest.mark.django_db
def test_answer_create(client):
    create_user(login="Good12345")
    create_question(content="How are you?", author_id=1, correct_answer_id=1)
    response = client.post(
        get_answer_create_url(),
        {"content": "Bad", "question_id": 1},
        content_type="application/json",
    )
    assert response.status_code == 200
    answer = parse_answer(get_answer(answer_id=1))
    assert answer == {"id": 1, "content": "Bad", "question_id": 1}
